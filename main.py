import os.path
import commands


def run(command):
    """Run command and return output:
        None: error
        Other: success (done or suggestion)
    """
    exitCode, output = commands.getstatusoutput(command)
    if (exitCode != 0):
        if (output == None):
            return None
    return output

#test run function
# print run("ps -au $(whoami)")

# test split()
# print os.path.split(run("pwd")) #return tuple
# print os.path.basename(run("pwd")) #file name
# print os.path.dirname(run("pwd"))   #parent path

