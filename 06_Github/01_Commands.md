# GIT COMMANDS

1. git init: Initialise a repository to be maintained by git
2. git clone #Repo SSH#: Clone the repo into your local machine. It also init the repo.
3. git status: Checks the current status of the repo
4. git remote add origin #SSH github#: To link a local repo to our new github repo
5. git add .: Adds every change in the current working directory to git. The dot can be replaced with file name.
6. git log: To see log of the commit
7. COMMIT
   - git commit -m 'Commit msg': Commits the current repo
   - git commit -am 'comm msg': Adds and commits. Works only if the file is aldready added. ie, for modified files.
8. PUSH
    - git push origin master: This pushes the repo remotely. 
    - git push: If you have done git push -u origin master one time, you just have to git push in the future
    - git push --set-upstream origin #branchName#
9. BRANCHING
   1.  git branch: Lets you see all the branches.
   2.  git checkout -b #branchName#: Create a new branch
   3.  git checkout #branchName#: Switch to another branch
   4.  git diff #branchName# : Shows differecce between main and #branchName#
   5.  git branch -d #branchName#: Delete the branch
   6.  git merge #branchName#: Merges #branchName# to current branch
10. RESET
    1.  git reset: Undo add .
    2.  git reset HEAD~1: Undo last commit. HEAD is the pointer to the last commit. This asks git to point HEAD to one commit before.
    3.  git reset #commitVal#: Resets to that commit val. The commit cal can be seen in git log
    4.  git reset --hard #CommitVal#: This not just undos the commit but also deletes the changes they have made
11. CONFIGURATION
    - git config pull.rebase false: You are calling for manual merge conflict


# Local Git Workflow
1. pull?
2. git add .
3. git commit -m 'msg'
4. git push
5. make pull request