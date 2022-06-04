#COMMAND LINE ARGUMENTS:
#these are the values passed to the python program at the command prompt
#they are passed to the program from outside the program
#arguments entered via keyboard , seperated by SPACE.

#these arguments are stored in the form of strings ...by default
#stored in a list with the name 'argv' , which is available in sys-module.
#argv[0] represents the name of the program.
#argv[1] represents the first value ..and so on...
#to find number of command line arguments entered at command prompt ..use function - len() , as len(argv)

#program to display command line arguments
import sys
n=len(sys.argv)
args=sys.argv
print("no. of command line arguments=",n)
print("the args are",args)
for a in args:
    print(a)