# Git

Git is a distributed version control system (DVCS) that is commonly used for tracking changes in source code during software development. It allows multiple developers to collaborate on a project, tracking changes to the codebase, and managing different versions of the software.
It was created by Linus Torvalds and is open source. Platforms like GitHub, GitLab, and Bitbucket provide additional tools and features built on top of Git to facilitate collaboration and project management.

# Key concepts related to Git

- Repository (Repo): A repository is a collection of files and the history of changes made to those files. It can be local (on your computer) or remote (on a server).

- Branch: A version of the repository that diverges from the main working project. Branches can be a new version of a repository, experimental changes, or personal forks of a repository for users to alter and test changes. You can create a new branch to work on a specific feature or bug fix without affecting the main codebase. Once your changes are complete, you can merge the branch back into the main branch.
  
- Git Checkout: The git checkout command is used to switch branches in a repository. git checkout testing-el would take you to the testing-el branch whereas git checkout master would drop you back into master. Be careful with your staged files and commits when switching between branches.
  
- Clone: A clone is a copy of a repository or the action of copying a repository. When cloning a repository into another branch, the new branch becomes a remote-tracking branch that can talk upstream to its origin branch (via pushes, pulls, and fetches).

- Commit: A commit is a snapshot of the changes made to the code at a specific point in time. Each commit has a unique identifier, and it includes a message that describes the changes made.

- Push: Pushing is the act of sending your committed changes to a remote repository. This makes your changes available to others who can then pull those changes into their own local copies.

- Fetch: Fetching retrieves the latest changes from the remote repository but does not automatically merge them into your local branch. It updates your remote-tracking branches, such as origin/master but does not modify your working directory or current branch. It allows you to see what changes are available on the remote repository before deciding to integrate them into your local branch.

- Pull: Pulling, on the other hand, is a combination of two operations: fetching changes from the remote repository and merging them into your local branch. It automatically updates your working directory and merges the changes into your current branch. It is a more convenient way to update your local branch with the latest changes from the remote repository, but it may result in automatic merges that could lead to conflicts.

- Index: The working, or staging, area of Git. Files that have been changed, added and deleted will be staged within the index until you are ready to commit the files. To see what is set in your Git index, run git status within your repository. 

- Master/ main: The primary branch of all repositories. All committed and accepted changes should be on the master branch. You can work directly from the master branch, or create other branches

- Merge: Merging is the process of combining changes from one branch into another. This is typically done to incorporate the changes made in a feature branch back into the main branch.

- Pull Request (PR): In Git platforms like GitHub or GitLab, a pull request is a way to propose changes to a codebase. It allows others to review the changes before they are merged into the main branch. Pull requests ask the repo maintainers to review the commits made, and then, if acceptable, merge the changes upstream. A pull happens when adding the changes to the master branch.

- Fork: Forking is the process of creating a personal copy of someone else's project. This copy is independent of the original project and allows you to make changes without affecting the original codebase. 

- Rebase: Rebase is a Git operation that allows you to move or combine a sequence of commits to a new base commit. It's an alternative to merging and can help create a cleaner, linear history. However, it should be used with caution, especially on shared branches.

- Origin: The conventional name for the primary version of a repository. Git also uses origin as a system alias for pushing and fetching data to and from the primary branch. For example, git push origin master, when run on a remote, will push the changes to the master branch of the primary repository database.



Stash: A stash is a way to temporarily save changes that are not ready to be committed. This is useful when you need to switch to a different branch or address an urgent issue before completing your current changes.

Conflict: A conflict occurs when Git is unable to automatically merge changes from different branches. Developers need to manually resolve conflicts by choosing which changes to keep.

- HEAD: HEAD is a reference variable used to denote the most current commit of the repository in which you are working. When you add a new commit, HEAD will then become that new commit.

# Github

GitHub is a web-based platform that provides hosting for software development and version control using Git. It serves as a collaborative platform for developers to work on projects together, track changes to the codebase, and manage the development workflow. 


# Credits

 - https://www.pluralsight.com/resources/blog/cloud/git-terms-explained
 - https://www.youtube.com/watch?v=RGOj5yH7evk&t=1900s&ab_channel=freeCodeCamp.org
 - https://www.youtube.com/watch?v=DVRQoVRzMIY&t=1793s&pp=ygUPZ2l0aHViIHR1dG9yaWFs