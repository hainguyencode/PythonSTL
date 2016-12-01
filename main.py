import os.path
import commands
import time
from matplotlib.font_manager import path


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

path = "ls -la"
cmd = 'pwd'

# test split()
# print os.path.split(run(cmd)) #return tuple: dirname + basename
# print os.path.basename(run("pwd")) #file name
# print os.path.dirname(run("pwd"))   #parent path

#test splittext
# print os.path.splitext("/usr/local/test.txt") # --> ('/usr/local/test', '.txt')

#test join: to buid path
# for parts in [ ('/', 'usr', 'local') ]:
#     print os.path.join(*parts)
# cmd = path + ' ' + os.path.join(*parts) 
# print run(cmd)

#test expanduser(): auto expand variable in a path
# print os.path.expanduser('~'+run('whoami')) # '~' is a variable and it's expanded to /Users

#test normpath()
# cmd = path + ' ' + os.path.normpath('/usr//local//')
# print cmd
# print run(cmd)

#file info
print __file__  # path for this file
print time.ctime(os.path.getatime(__file__))    #access time
print time.ctime(os.path.getmtime(__file__))    #modify time
print time.ctime(os.path.getctime(__file__))    #change time
print os.path.getsize(__file__)    #size



