# Linux Terminal Commands

1. whoami: returns username
2. pwd: print working directory
3. Manuals and helps
   1. man: return manual pages
   2. help: a worse, but more general man page
   3. tldr: a shorter and readable man page
4. which: Returns the full path of the executable in the file system
5. clear: clear screen
   1. clear -x: (Shortcut is Ctrl+L). It clears the terminal, by maintaining scroll history.
6. tree: To print the whole directorier down recursively in tree format
7. ls: lists files and folders in the working directory
   1. ls {path}: Perform ls on the path
   2. ls -l: Lists more details along with listing
   3. ls -a: Lists hidden files also
8. cd: Change directory
   1. cd ..: To go back
   2. cd ~: Go to home
   3. cd \: Go to root
   4. cd -: Go to the last used directory
9. mkdir: Make directory
   1. mkdir dir1 dir2 dir3: Make multiple directories at once
   2. mkdir -p dir1/dir2/dir3: Creates all the directories to make this path. i.e, creates nested directory
10. rmdir: Remove empty directories (kinda inferior to rm)
11. touch: Create files. Just changes the modification time if the file aldready exists.
    1. touch file1 file2 file3: To create multiple files
12. rm: Remove files and directories. Have to use -r for directories
13. trash: Does the same as rm, but redirects them to trash.
14. open/ xdg-open: Opens file/ folder in UI in default application
15. mv: Move files and folders around. Can also be used for renaming.
16. cp: To copy files and folders. Have to use -r for directories
17. neofetch: Fetch details of the OS and hardware.
18. head/ tail: Lets us print out the first 10 line from the first and last part, respectively of a file.
    1. You can change the length with -n flag.
    2. You can monitor for more data with only tail if you add -f.
19. `Redirect`: Greater-than(>) is used to redirect std output into a file. Creates files if it doesn't exist.
    1. date > test.txt : The current date is written (over-written) in the file
    2. date >> test.txt: The current date is appended to the contents of the file
20. cat: Primarily used for displaying the contents of one or more files to the terminal.
    1. cat file1 file2 file3: Concatnates all three and prints them as stdout
21. less: It can be used to read a file in a very user friendly way
22. echo: Repeats what was followed by echo
    1. Eg: echo "COW" > cow.txt # Creates a file cow.txt and puts COW into it.
    2. echo \*.txt returns all txt files in the directory
23. wc: Counts lines, words and bytes in a file
24. `Piping`: Using the output of a command as the input of another
    1. Eg: ls | wc : This takes the ls, and put it as input to word count
    2. Eg: cat file1 file2 | wc -l > file3: Counts the number of lines in the appended version of file1 and file2, and appends them to file 3
25. sort: Sorts the file, but doesn't store them
    1. -u: To remove unique values
26. uniq: Reports or omits adjacent repeated lines
    1. -d: Only prints duplicates
    2. -u: Prints only non-duplicates
    3. -c: Gives count
       1. Eg: ls | sort | uniq -c : Gives the count of all the files and directories present in the working dir
27. `Regex representations in terminal` - can be used with grep, touch, etc.
    1. \*: Matches all any character
       1. Eg: \*.pdf refers to all the pdf files (in the dir)
    2. ?: Matches one character
       1. Eg: \*.?? will match all files with 2 character extensions like .py, .md, etc
       2. Eg: rm \*.??? -i: Will interactively remove all 3 character extensions in the directory
    3. {}: Uses distributive property
       1. {a,b,c}.txt is equivalent to a.txt b.txt c.txt
       2. {1..99} : This extends to all natural numbers [1,99]
28. diff: Find the difference between two files
    1. -y: Side by side comparison
    2. -u: For more context. Git uses somthing similar
29. find: Lets us find files and directories recursively based on a lot of things like name, mod time, etc.
    1. find . : Finds all the files nested anywhere in the directory
    2. find #location# -name '_cow_.png' : Find all png files in the #location# directory with the word cow as the name
    3. find /home -type d : finds all the directories in home
    4. find /home/arjun/Desktop -type f -name '_E_.jpg' : Finds all jpg files in desktop with E in it
    5. find . -type f -size +100k: Files greater than 100 Kb
    6. There are also
       1. find files by size
       2. logical operators like -not -or
       3. -mtime for modified time
       4. We can even use -exec to execute another operation to the found out files.
30. grep: Helps us find text inside of files. It stands for global regular expression print.
    1. grep #string# #file_loc#: Prints the matching string lines in file_loc
    2. -n: Gives line numbers
    3. -C: gives context. More lines before and after the matching word
    4. -r: To recursively check a directory
    5. We can use regex to make the search more general
31. du: Shows disk usage of every directory
32. df: Information about mounted file systems
33. history: Shows terminal history
    1. history | grep 'install'
34. `Process managing commands`
    1. ps: Display all process started by the user
       1. ps ax: Display all process
       2. ps axww: Display all processes with word wrapping
    2. top: Opens up processes based on their cpu load
       1. top -o mem: Sort by memory
    3. htop: A better top
    4. btop: A better htop
    5. nvidia-smi: Details about NVIDIA graphics card, and the process that run in it.
35. `Killing processes`
    - Find process id using ps axww|grep 'Visual Studio Code'
    - Now we use the kill command to kill the process
      - kill #Pid#: This is the gentle way to kill. This is the same as `kill -15 <Pid>`
      - kill -9 #Pid#: This is a brutal way to kill a process
      - killall #Pname#: Kills all the processes with the Pname
      - killall -9 #Pname#: Kills all the processes with the Pname brutally.
      - pkill -9 #part of Pname#: Kills process brutally, but if the pname is a part of the real process name, it is killed. So use carefully as it may kill unwanted processes.
36. fg, bg: Create processes in foreground and background
37. jobs: See all the sleeping and background processes
38. gzip -k filename: Create a zip of the file. -k keeps the unzipped file. If used on multiple files, it zips them separately.
39. gunzip -k filename: Unzip the file
40. tar -cf #EndFileName.tar# file1 file2 file3: Creates archives of multiple files. Now we can use gzip to compress the archive.
    1. tar -xf #EndFileName.tar# file1 file2 file3: To extract the archive
    2. tar -tf #ArchiveName#: To view contents of the archive
    3. tar -czf #EndFileName.tar# file1 file2 file3: To create and compress the archive all in one
41. `Editors`:
    1. nano: Built-in, light weight, super easy text editor in linux
    2. gedit: Open in notepad
    3. vi: Open in vim. Built in most linux systems
    4. code: Open in vscode
    5. nvim: Open in nvim
42. `alias`: We can rename different keywords to be custom commands. This has to be put on config file for fish, bashrc for bash in home directory.
43. `xargs`: Some commands expect arguments for its functioning. xargs lets us pipe the output of another command (stdout) as the arguments of the command.
    - cat file1|xargs touch: Creates all the filenames present in file1
    - find . -size +1G | xargs rm: Remove all files in the current directory that is larger than 1 GB.
44. `ln: Links`
    1. Hardlink: A hardlink to a file is like a copy of that file, but if any change in one will be reflected in the other. If you delete one, the other WILL persist, as it is pointing to the same thing in memory.
       - ln #original# #link#
    2. Softlink/ Symbolic link: A softlink to a file is like a copy of that file, but if any change in one will be reflected in the other(same as hard link). If you delete one, the other WILL NOT persist, as the link is pointing to the file itself, not the memory location
       - ln -s #original# #link#
45. `Managing Users`
    1. su: Lets you switch users to a different terminal just for that terminal instance.
    2. sudo: Super user do - Lets you run commands as the root user, with elevated permissions if you have administrative permissions. This is generally required if you are making changes that affects multiple users. This is primarily for debian type Linux like ubuntu, parrotOS and mint.
    3. passwd: To change, expire, delete, etc. our or other user's (if you have root access) passwords.
    4. chown: Lets us change ownership of files and directories.
    5. chmod (Change mode): To Changing Permissions
    - Format: chmod #mode# #file#
      ```
      Mode includes the following
      - who
          - u: User (owner)
          - g: Group
          - o: Others
          - a: all of this
      - What
          - minus sign(-): Removes permission
          - plus sign(+): Adds permission
          - equal to sign(=): Set a permission and removes others
      - Which
          - r
          - w
          - x
      ```
      Eg: chmod ug+rw file1.txt : This add read and write permission to the user and group for file1.txt
46. ranger: Open ranger - a terminal file system manager
47. `source`: To activate virtual environment
    - source "/home/arjun/AI_ENV/bin/activate.fish"
    - source "/home/arjun/AI_ENV/bin/activate"
48. `Open shell`
    - bash: Open bash
    - fish: Open fish
49. env: Environmental variables
50. apropos <words>: Identifies commands related to the words
51. `Networking`:
    1. uname -a: Tells a lot about the user and the system you are using
    2. id, ip, netstat, ss: A lot of network stuff
    3. nslookup: To get the Domain Name Address(DNS) of a domain name
    4. ping: To check the ping of an IP address or domain name
    5. tracepath: To trace the path from the current computer to a domain. It shows all the intermediate nodes.
    6. ifconfig: To get the network details of our device.
    7. iwconfig: To see wifi related network details
    8. nmap: To see a lot of information about the router and the connected devices
    9. sudo cat /etc/NetworkManager/system-connections/<WiFi-SSID>: To retrieve wifi password from your device
52. `Package managers`:
    1. dpkg: Low level package manager for debian. We have to download the .deb file for the installation ourself and perform `sudo dpkg -i <path to pkg>`. Another issue with this is that you have to manually download all the requirements for the installed package.
    2. apt: High level.
       1. To install a package: `sudo apt install <pkg name>`.
       2. To remove a package: `sudo apt remove <pkg name>` # This removes the package, but preserves user data and modification done to that package. This will let us continue from
       3. where we left off, by reinstalling the package again.
       4. To completely remove a package: `sudo apt purge <pkg name>`
       5. To update and upgrade all apps: `sudo apt update && sudo apt upgrade`
    3. snap: Kind of like a store, where developers can put their packages in a snap.
    4. pip: Python's package manager. `pip install <package name>`
       1. `pip install -r <file name>`: To install all the things mentioned in the file. Generally used for installing requirements.txt
    5. git: We can use `git clone <url>` to clone a repo

# Shortcuts for the terminal

Ctrl + A: Go to the very first of the line
Ctrl + E: Go to the very end of the line
Ctrl + U: Cut(delete) to the left of cursor
Ctrl + K: Cut(delete) to the right of cursor
Ctrl + Y: Paste
Alt + E: Opens that line in selected editor(for fish. Ctrl+X+E for bash)
Ctrl + C: Kills a process in the terminal. Kill signal 2
Ctrl + Z: Sleeps a process. Kill signal 19
& at the end of a process: Sends the proecess straight to background

# Credits

- https://www.youtube.com/watch?v=ZtqBQ68cfJc&t=1s&ab_channel=freeCodeCamp.org
- https://www.youtube.com/watch?v=vX3krP6JmOY&list=PLIhvC56v63IJIujb5cyE13oLuyORZpdkL&index=5&ab_channel=NetworkChuck``
