# GIT COMMANDS

1. git init: Initialise a repository to be maintained by git
2. git clone #Repo SSH#: Clone the repo into your local machine. It also init the repo.
3. git status: Checks the current status of the repo
4. git add .: Adds every change in the current working directory to git. The dot can be replaced with file name.
5. git commit -m 'Commit msg': Commits the current repo
   - git commit -am 'comm msg': Adds and commits. Works only if the file is aldready added. ie, for modified files.
6. git push origin master: This pushes the repo remotely. 
    - git push: If you have done git push -u origin master one time, you just have to git push in the future
7. git remote add origin #SSH github#: To link a local repo to our new github repo
8. git branch: Lets you see all the branches.
9.  git checkout -b #branchName#: Create a new branch
10. git checkout #branchName#: Switch to another branch
11. git diff #branchName# : Shows differecce between main and #branchName#
12. git push --set-upstream origin #branchName#
13. git branch -d #branchName#: Delete the branch
14. git merge #branchName#: Merges #branchName# to current branch
15. git log: To see log of the commit
16. git reset: Undo add .
17. git reset HEAD~1: Undo last commit. HEAD is the pointer to the last commit. This asks git to point HEAD to one commit before.
18. git reset #commitVal#: Resets to that commit val. The commit cal can be seen in git log
19. git reset --hard #CommitVal#: This not just undos the commit but also deletes the changes they have made
20. 


# Local Git Workflow
1. pull?
2. git add .
3. git commit -m 'msg'
4. git push
5. make pull request