# Credits
https://www.youtube.com/watch?v=ZtqBQ68cfJc&t=1s&ab_channel=freeCodeCamp.org

# Super Basic Terminal Commands

1. whoami: returns username
2. Manuals and helps
   1. man: return manual pages
   2. help: a worse, but more general man page
   3. tldr: a better man page
3. which: Returns the full path of the executable in the file system
4. clear: clear screen
   1. clear -x: (Shortcut is Ctrl+L). It clears the terminal, by maintaining scroll history.
5. pwd: print working directory
6. ls: lists files and folders in the working directory 
   1. ls {path}: Perform ls on the path
   2. ls -l: Lists more details along with listing  
   3. ls -a: Lists hidden files also
7. cd: Change directory
   1. cd ..: To go back
   2. cd ~: Go to home
   3. cd \: Go to root
8. mkdir: Make directory
   1. mkdir dir1 dir2 dir3: Make multiple directories at once
   2. mkdir -p dir1/dir2/dir3: Creates all the directories to make this path. i.e, creates nested directory
9.  rmdir: Remove empty directories (kinda inferior to rm)
10. touch: Create files. Just changes the modification time if the file aldready exists.
    1.  touch file1 file2 file3: To create multiple files
11. rm: Remove files and directories. Have to use -r for directories
12. trash: Does the same as rm, but redirects them to trash.
13. open/ xdg-open: Opens file/ folder in UI in default application
14. mv: Move files and folders around. Can also be used for renaming.
15. cp: To copy files and folders. Have to use -r for directories
16. head/ tail: Lets us print out the first 10 line from the first and last part, respectively of a file. 
    1.  You can change the length with -n flag.
    2.  You can monitor for more data with only tail if you add -f. 
17. Redirect: Greater-than(>) is used to redirect std output into a file. Creates files if it doesn't exist.
    1. date > test.txt : The current date is written (over-written) in the file 
    2. date >> test.txt: The current date is appended to the contents of the file 
18. cat: Primarily used for displaying the contents of one or more files to the terminal. 
    1.  cat file1 file2 file3: Concatnates all three and prints them as stdout
19. bat: cat with wings. 
20. less: It can be used to read a file in a very user friendly way
21. echo: Repeats what was followed by echo
    1.  Eg: echo "COW" > cow.txt  # Creates a file cow.txt and puts COW into it.
    2.  echo *.txt returns all txt files in the directory
22. wc: Counts lines, words and bytes in a file
23. Piping: Using the output of a command as the input of another
    1.  Eg: ls | wc : This takes the ls, and put it as input to word count
    2.  Eg: cat file1 file2 | wc -l > file3: Counts the number of lines in the appended version of file1 and file2, and appends them to file 3
24. sort: Sorts the file, but doesn't store them
    1.  -u: To remove unique values
25. uniq: Reports or omits adjacent repeated lines
    1.  -d: Only prints duplicates
    2.  -u: Prints only non-duplicates
    3.  -c: Gives count
        1.  Eg: ls | sort | uniq -c : Gives the count of all the files and directories present in the working dir
26. Expansions
    1. *: Matches all any character
        1.  Eg: *.pdf refers to all the pdf files (in the dir)
    2. ?: Matches one character 
       1. Eg: *.?? will match all files with 2 character extensions like .py, .md, etc
       2. Eg: rm *.??? -i: Will interactively remove all 3 character extensions in the directory 
    3. {}: Uses distributive property
       1. {a,b,c}.txt is equivalent to a.txt b.txt c.txt
       2. {1..99} : This extends to all natural numbers [1,99]
27. diff: Find the difference between two files
     1.  -y: Side by side comparison
     2.  -u: For more context. Git uses somthing similar
28. find: Lets us find files and directories recursively based on a lot of things like name, mod time, etc.
     1. find . : Finds all the files nested anywhere in the directory
     2. find #location# -name '*cow*.png' : Find all png files in the #location# directory with the word cow as the name 
     3. find /home -type d : finds all the directories in home
     4. find /home/arjun/Desktop -type f -name '*E*.jpg' : Finds all jpg files in desktop with E in it 
     5. find . -type f -size +100k: Files greater than 100 Kb
     6. There are also 
        1. find files by size
        2. logical operators like -not -or 
        3. -mtime for modified time
        4. We can even use -exec to execute another operation to the found out files.
29. grep: Helps us find text inside of files
    1.  grep #string# #file_loc#: Prints the matching string lines in file_loc
    2.  -n: Gives line numbers
    3.  -C: gives context. More lines before and after the matching word    
    4.  -r: To recursively check a directory
    5.  We can use regex to make the search more general
30. du: Shows disk usage of every directory
31. df: Information about mounted file systems
32. history: Shows terminal history
    1.  history | grep 'install'
33. Task managing commands
    1.  ps: Display all process started by the user
        1.  ps ax: Display all process
        2.  ps axww:  Display all processes with word wrapping
    2. top: Opens up processes based on their cpu load
       1. top -o mem: Sort by memory
    3. htop: A better top
    4. btop: A better htop
34. Killing process
    - Find process id using ps axww|grep 'Visual Studio Code'
    - Now we use the kill command to kill the process
      - kill #Pid#: This is the gentle way to kill
      - kill -9 #Pid#: This is a brutal way to kill a process
      - killall #Pname#: Kills all the processes with the Pname
      - killall -9 #Pname#: Kills all the processes with the Pname violently
35. job, fg, bg: Create processes in foreground and bg
36. gzip -k filename: Create a zip of the file. -k keeps the unzipped file. If used on multiple files, it zips them separately.
37. gunzip -k filename: Unzip the file 
38. tar -cf #EndFileName.tar# file1 file2 file3: Creates archives of multiple files. Now we can use gzip to compress the archive.
    1. tar -xf #EndFileName.tar# file1 file2 file3: To extract the archive
    2. tar -tf #ArchiveName#: To view contents of the archive
    3. tar -czf #EndFileName.tar# file1 file2 file3: To create and compress the archive all in one
39. nano: It is an in-built text editor in linux
40. alias: We can rename different keywords to be custom commands. This has to be put on config file for fish, bashrc for bash in home directory.
41. xargs: Some commands expect arguments for its functioning. xargs lets us pipe the output of another command (stdout) as the arguments of the command.
    - cat file1|xargs touch: Creates all the filenames present in file1
    - find . -size +1G | xargs rm: Remove all files in the current directory that is larger than 1 GB.
42. ln: Links
    1. Hardlink: A hardlink to a file is like a copy of that file, but if any change in one will be reflected in the other. If you delete one, the other WILL persist, as it is pointing to the same thing in memory.
        - ln #original# #link#
    2. Softlink/ Symbolic link: A softlink to a file is like a copy of that file, but if any change in one will be reflected in the other(same as hard link). If you delete one, the other WILL NOT persist, as the link is pointing to the file itself, not the memory location
        - ln -s #original# #link#
43. su: Lets you switch users to a different terminal just for that terminal instance.
44. sudo: Super user do - Lets you run commands as the root user, with elevated permissions if you have administrative permissions. This is generally required if you are making changes that affects multiple users.
45. passwd: To change, expire, delete, etc. our or other user's (if you have root access) passwords.
46. chown: Lets us change ownership of files and directories.
47. chmod (Change mode): To Changing Permissions
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
48. ranger: Open ranger - a terminal file system manager
49. source: To activate virtual environment
    - source "/home/arjun/AI_ENV/bin/activate.fish"
    - source "/home/arjun/AI_ENV/bin/activate"
50. Open terminal
    - bash: Open bash
    - fish: Open fish
51. nvidia-smi: Details about NVIDIA graphics card
52. env: Environmental variables 
53. apropos <words>: Identifies commands related to the words
54. Networking:
    1. uname -a: Tells a lot about the user and the system you are using
    2. id, ip, netstat, ss: A lot of network stuff
    3. nslookup: To get the Domain Name Address(DNS) of a domain name
    4. ping: To check the ping of an IP address or domain name
    5. tracepath: To trace the path from the current computer to a domain. It shows all the intermediate nodes.
    6. ifconfig: To get the network details of our device.
    7. iwconfig: To see wifi related network details
    8. nmap: To see a lot of information about the router and the connected devices
    9. sudo cat /etc/NetworkManager/system-connections/<WiFi-SSID>: To retrieve wifi password from your device
55. 

https://www.youtube.com/watch?v=vX3krP6JmOY&list=PLIhvC56v63IJIujb5cyE13oLuyORZpdkL&index=5&ab_channel=NetworkChuck``

### Add and remove window buttons
gsettings set org.gnome.desktop.wm.preferences button-layout :

gsettings reset org.gnome.desktop.wm.preferences button-layout