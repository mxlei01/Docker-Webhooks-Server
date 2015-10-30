import subprocess
import logger

# synchronous.py will include all the functions that are synchronous

def executeLinuxCommands(commands, repositoryName):
    # Usage:
    #       This function will execute linux commands serially in the commands list
    # Arguments:
    #       commands       : a list of linux commands to be executed
    #       repositoryName : the repository name
    # Return:
    #       None

    # Loop through commands, and use subprocess to execute the commands and pipe the stderr to stdout
    # then record the result in a logger
    for command in commands:
        pipe = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        pipe.wait()
        logger.logger.info("Executed:%s, Result:%s" % (command, pipe.stdout.read()))

    # Returns the repository name to send to a slack channel
    return repositoryName