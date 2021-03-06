import os.path
import commands
import time
import glob
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
# print __file__  # path for this file
# print time.ctime(os.path.getatime(__file__))    #access time
# print time.ctime(os.path.getmtime(__file__))    #modify time
# print time.ctime(os.path.getctime(__file__))    #change time
# print os.path.getsize(__file__)    #size

#file testing
# filenames = [__file__, '/usr/local/bin']
# for file in filenames:
#     if os.path.exists(file):
#         print 'File: ', 'is file ', os.path.isfile(file), 'is dir: ', os.path.isdir(file)

#traversing a dir

# def traverseDir(arg, dir, names):
#     if os.path.exists(dir):
#         for name in names:
#             subname = os.path.join(dir, name)
#             if os.path.isdir(subname):
#                 print ' %s/' % name
#             else:
#                 print ' %s' % name
# os.path.walk(os.path.pardir, traverseDir, 'haint test')                

def traverseDir(path, inVisibleDir):
    result = []
    if inVisibleDir == True:
        pathSearch = ( (path + '/*'), (path + '/.*') )
    else:
        pathSearch = ( (path + '/*'), (path + '/.*') )
    for myPath in pathSearch:
        print myPath
        for path in glob.glob(myPath):
            print '\t', path
            result.append(path)
    return result
print traverseDir(os.path.dirname(__file__), True)




