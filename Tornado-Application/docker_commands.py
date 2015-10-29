# docker_commands.py contains all the linux commands to control docker

# stopTargetContainer will stop all the containers associated with a docker repo name
stopRepoContainer = "sudo docker kill $(sudo docker ps | grep '%s' | awk '{print $1}')"

# deleteRepoContainers will remove all docker containers associated with a docker repo name
deleteRepoContainers = "sudo docker rm $(sudo docker ps -a | grep '%s' | awk '{print $1}')"

# deleteRepoImages will remove all the docker images associated with a docker repo name
deleteRepoImages = "sudo docker rmi $(sudo docker images | grep '%s' | awk '{print $3}')"

# pullRepo will pull the repo using a docker repo name
pullRepo = "sudo docker pull %s"

# runRepo will run the repo using a docker repo name
runRepo = "sudo docker run -d --net='host' %s"