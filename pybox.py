#
#       simple wrapper for virtualbox
#       by thewatcher/ikbenlike
#

import subprocess

def getVMList(optLong, printOutput):
    if optLong == True:
        p = subprocess.check_output(["VBoxManage", "list", "vms", "-l"], universal_newlines=True)
    else:
        p = subprocess.check_output(["VBoxManage", "list", "vms"], universal_newlines=True)
    if printOutput == True:
        print(p)



def createNewVM(newVMName, registerVM, printOutput):
    if registerVM == True:
        p = subprocess.check_output(["VBoxManage", ])
    if printOutput == True:
        print(p)



def startVM(VMName, startType, printOutput):
    p = subprocess.check_output(["VBoxManage", "startvm", VMName, "--type", startType],universal_newlines=True)



def showVMInfo(VMName, printOutput):
    p = subprocess.check_output(["VBoxManage", "showvminfo", VMName], universal_newlines=True)
    print(p)

showVMInfo("win10")
