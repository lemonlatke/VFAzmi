# File: homework2.py

# Your file path should look like:
# python_decal_fa25/VFAzmi/homework2/homework2.py

# Questions (Answer these in the homework2.py file as comments):

# 1) What’s the difference between Git, GitHub, and Git Bash?
# Git is a software that helps track files that are being edited by multiple users, GitHub is a remote server where you can share the files you have worked on, and Git Bash is a terminal where you can edit code and maneuver through your computer.

# 2) What’s the difference between the terminal and the command line?
# The terminal is a  way to talk to your computer. You can input commands to make your computer do things for you. The command line is the actual text interface that allows you to input said commands.

# 3) How does Windows PowerShell differ from Git Bash?
#Windows Powershell and Git Bash are both terminals but they use different languages to communicate with the computer.

# 4) What’s the difference between Anaconda, conda, and Python?
#Anaconda is a software bundle that includes many notebooks and packages for Python. Conda is a package manager for Anaconda and apparently its baby, Miniconda. Python is the coding language we are using in this class.

# 5) What is VS Code?
#VS Code is a code editor.

# 6) What is a Jupyter Notebook? How is it different from Jupyter Lab?
#Jupyter Notebook helps the user create Jupyter notebook documents. JupyterLab includes Jupyter notebooks and generally has more advanced features.

# 7) What does ~/ mean?
#This is the home, or root, directory.

# 8) What’s the difference between an absolute path and a relative path?
#An absolute path involves writing the proper file path to navigate to the desired directory, while a relative path involves relating the desired directory to the current one.

# 9) Imagine you're in your "yourname" repo. Write the absolute and relative paths to "course_assignments/homework2".
#absolute path: cd ~/python_decal_fa25/course_assignments/homework2/
#relative path: cd ../course_assignments/homework2/

# 10) What command lets you move from "course_assignments/homework2/" to "course_assignments/"?
#cd ../

# 11) What would rm ./ do in your current directory? (Don’t try it!)
#it would delete the directory (self destruct button!)

# 12) What do the following commands do?
# git add: adds all mentioned files to a staging area to be tracked
# git commit: saves files in staging area locally
# git push: pushes files to remote repository

# 13) What's the difference between "git add ." and "git add <file>"?
#"git add ." adds all files and directories within the current directory to the staging area, whereas "git add <file>" only adds the specific file you have mentioned.

# 14) What do "git status" and "git log -1" do?
#"git status" relays information about the current state of your staging area, and includes information about which files are being tracked and which are not. "git log -1" shows you the most recent commit you made.

# 15) What’s the difference between cloning a repository and pulling from it?
#Cloning provides you your own copy of a directory or file that you can edit separately from the master copy. Pulling from a repository will allow you to make changes on the master copy.

# 16) What has been your most frustrating bug or error in this class so far? How did you troubleshoot or fix it?
#I had no idea why my datatypes.py script refused to run, as whenever I called it in the terminal it would return nothing. I realized...everything had been commented out.

# 17) What’s a question you still have? What’s something you’re confused about?
#I wonder when we get to start learning more in depth code.

# 18) Tell me a fun fact!
#I have a cat named Mu'ezza who is my actual son that I birthed, I am his real parent.

# 19) Print your favorite math expression you've learned in Python so far.
# (Hint: Use print() and add a comment explaining what it does.)

print(23 % 17)
#modulus function, prints remainder in division process.
