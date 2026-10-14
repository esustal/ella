# Git is a local platform and Github is online and hosts Git platforms
# The terminal is the window where the command line is. Yout type your commands in the command line
# The local repository is from a personal computer and remote repository is hosted online somewhere like Github
# Version control is how you manage and save changes made to your code, like the repo, commits, and branching
# The staging area is where you can make changes to your files before committing them
# git add moves the python file into the staging area
# git commit saves changes
# git push uploads the code to github
# git status checks the state of the staging area, like which changes are staged for the next commit
# git pull downloads python code from a remote repo
# pwd is print working directory, which shows what directory you're in
# ls is list and lists what's inside your directory
# cd is change directory and navigates you from directory to directory
# nano is a text editor in the terminal
# touch creates a file
# mv moves files or directories to new locations
# rm removes files or directories
# cat prints files contents in terminal

# to check which of judy's directories i'm in, i'd call pwd
# ls
# cd ~/python_decal/brianna, git pull
# cp homework.py ~/python_decal/judy_decal/homework/
# cd ~/python_decal/brianna
# cat homework.py
# cd ~/python_decal/judy_decal, git add ., git commit -m "homework done", git push
# git pull origin main, git push origin main
# cd /Users/judy/Recents

# def checkDataType(object):
#     return type(object)
# print(checkDataType(3.14))
# print(checkDataType(True))

def evenOrOdd(num):
    if num % 2 == 0:
      return "Even"
    else:
       return "Odd"
print(evenOrOdd(7))
print(evenOrOdd(10))

numbers = [1, 2, 3, 4, 5]

def sumWithLoop(numbers):
   total = 0
   for num in numbers:
      total += num
    
   return total
print(sumWithLoop(numbers))

list = ["a", "b", "c"]

def duplicateList(list):
   return list*2
print(duplicateList(list))

def square(num):
   return num * num
print(square(2))

#fav code