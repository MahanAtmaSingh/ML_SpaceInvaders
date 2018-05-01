
import sys, getopt, os

if( __name__ == '__main__'):
    print("Invoke was:", sys.argv)
    generalInformation = False
    if("--version" in sys.argv or "-v" in sys.argv):
        print("Here should be the SHA1 or the last tag...")
        generalInformation = True
    if("--help" in sys.argv or "-h" in sys.argv):
        print("This software shall show some machine learning example by Space Invaders")
        generalInformation = True

    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    print("The execution path:", abspath, "... and: ", dname)

    newExecutionPath = dname+"/Space_Invaders"
    os.chdir(newExecutionPath)
    print("Changed execution path to", newExecutionPath)
    
    from spaceinvaders import *

    applicationMode = input("When you want to do machine learning enter 'm':")
    if( applicationMode == "M" or applicationMode == "m"):
        showBumpers = False
        goalStayAlive = True
        game.setMachineLearning( showBumpers, goalStayAlive )

    game.main()
