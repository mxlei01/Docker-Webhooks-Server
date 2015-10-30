# slack_messages.py contains all the messages that will get sent to slack

# docker_update is a string to notify a slack channel that a repo is updated
docker_update = '{"channel": "#server", "username": "webhookbot", "text": "Repo:%s, is updated on the server", "icon_emoji": ":sheep:"}'
