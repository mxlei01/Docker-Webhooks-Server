import json
import tornado.web
from tornado import gen
from docker_settings import docker_commands, whitelist
from executor import executors
from linux_command import linux_command_execute
from loggers import logger
from slack import slack_messages, slack_settings, slack_http_client

# docker_webhook_handler.py contains all the handlers that tornado application uses

# This class is used to handle the main of the webpage
# according to router.py, this handlers is mapped to /
# which means the localhost:8888/
class WebHook(tornado.web.RequestHandler):
    @gen.coroutine
    def post(self):
        # Usage:
        #       Reads a POST request, which will be sent from docker webhook. Then reads the json file from the
        #       request body, and gets the repository name, then populates a list of commands that we need to
        #       execute. Then stops the containers, remove old images and containers to save space, and repull,
        #       then reruns.
        # Arguments:
        #       None
        # Return:
        #       None

        # Log the json file
        logger.logger.info(self.request.body)

        # Get the repository name
        repositoryName = json.loads(self.request.body)["repository"]["repo_name"]

        # Populates a list of commands that we need to run
        #   1. Stop the current container
        #   2. Remove the containers
        #   3. Removes the images
        #   4. Pull the repo
        #   5. Run the repo
        commands = [
            docker_commands.stopRepoContainer % repositoryName,
            docker_commands.deleteRepoContainers % repositoryName,
            docker_commands.deleteRepoImages % repositoryName,
            docker_commands.pullRepo % repositoryName,
            docker_commands.runRepo % (repositoryName.replace("/", "-"), repositoryName)
        ]

        # Run the commands only if the repository name is inside the whitelist
        if repositoryName.split("/")[0] in whitelist.whitelist:
            # Execute the commands using an executor
            future = executors.executor.submit(linux_command_execute.executeLinuxCommands, commands, repositoryName)

            # After the execution is done, it will call a callback that will send a slack message
            future.add_done_callback(self.sendSlackMessage)

    @gen.coroutine
    def sendSlackMessage(self, futureResult):
        # Usage:
        #       Sends a message to slack channels defined in the slack_Settings.py
        # Arguments:
        #       None
        # Return:
        #       None

        # Send messages to webhooks in slack using coroutines
        logger.logger.info("Sending Webhooks to Slack")
        for url in slack_settings.webhook_urls:
            response = yield slack_http_client.post_slack_coroutine(url, slack_messages.docker_update % futureResult.result())
            logger.logger.info("Response from Slack:%s" % response)