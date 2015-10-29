import tornado.web
import json
import docker_commands
import logger
import whitelist
import synchronous
import executors

# handlers.py contains all the handlers that tornado application uses

# This class is used to handle the main of the webpage
# according to url.py, this handler is mapped to /
# which means the localhost:8888/
class WebHook(tornado.web.RequestHandler):
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
            docker_commands.runRepo % repositoryName
        ]

        # Run the commands only if the repository name is inside the whitelist
        if repositoryName.split("/")[0] in whitelist.whitelist:
            # Execute the commands using an executor
            executors.executor.submit(synchronous.executeLinuxCommands, commands)
