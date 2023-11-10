# GIT COMMANDS

1. git init: Initialise a repository to be maintained by git
2. git clone #Repo SSH#: Clone the repo into your local machine. It also init the repo.
3. git status: Checks the current status of the repo
4. git add .: Adds every change in the current working directory to git. The dot can be replaced with file name.
5. git commit -m 'Commit msg': Commits the current repo
6. git push origin master: This pushes the repo remotely. 
    - git push: If you have done git push -u origin master one time, you just have to git push in the future
8. git remote add origin #SSH github#: To link a local repo to our new github repo
9. git branch: Lets you see all the branches.
10. git checkout -b #branchName#: Create a new branch
11. git checkout #branchName#: Switch to another branch
12. git diff #branchName# : Shows differecce between main and #branchName#
13. git push --set-upstream origin #branchName#
14. git branch -d #branchName#: Delete the branch



# Local Git Workflow
1. pull?
2. git add .
3. git commit -m 'msg'
4. git push
5. make pull request