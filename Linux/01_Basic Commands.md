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
19. less: It can be used to read a file in a very user friendly way
20. echo: Repeats what was followed by echo
    1.  Eg: echo "COW" > cow.txt  # Creates a file cow.txt and puts COW into it.
    2.  echo *.txt returns all txt files in the directory
21. wc: Counts lines, words and bytes in a file
22. Piping: Using the output of a command as the input of another
    1.  Eg: ls | wc : This takes the ls, and put it as input to word count
    2.  Eg: cat file1 file2 | wc -l > file3: Counts the number of lines in the appended version of file1 and file2, and appends them to file 3
23. sort: Sorts the file, but doesn't store them
    1.  -u: To remove unique values
24. uniq: Reports or omits adjacent repeated lines
    1.  -d: Only prints duplicates
    2.  -u: Prints only non-duplicates
    3.  -c: Gives count
        1.  Eg: ls | sort | uniq -c : Gives the count of all the files and directories present in the working dir
25. Expansions
    1. *: Matches all any character
        1.  Eg: *.pdf refers to all the pdf files (in the dir)
    2. ?: Matches one character 
       1. Eg: *.?? will match all files with 2 character extensions like .py, .md, etc
       2. Eg: rm *.??? -i: Will interactively remove all 3 character extensions in the directory 
    3. {}: Uses distributive property
       1. {a,b,c}.txt is equivalent to a.txt b.txt c.txt
       2. {1..99} : This extends to all natural numbers [1,99]
26. diff: Find the difference between two files
     1.  -y: Side by side comparison
     2.  -u: For more context. Git uses somthing similar
27. find: Lets us find files and directories recursively based on a lot of things like name, mod time, etc.
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
28. grep: Helps us find text inside of files
    1.  grep #string# #file_loc#: Prints the matching string lines in file_loc
    2.  -n: Gives line numbers
    3.  -C: gives context. More lines before and after the matching word    
    4.  -r: To recursively check a directory
    5.  We can use regex to make the search more general
29. du: Shows disk usage of every directory
30. df: Information about mounted file systems
31. history: Shows terminal history
    1.  history | grep 'install'
32. Task managing commands
    1.  ps: Display all process started by the user
        1.  ps ax: Display all process
        2.  ps axww:  Display all processes with word wrapping
    2. top: Opens up processes based on their cpu load
       1. top -o mem: Sort by memory
    3. htop: A better top
    4. btop: A better htop
33. Killing process
    - Find process id using ps axww|grep 'Visual Studio Code'
    - Now we use the kill command to kill the process
      - kill #Pid#: This is the gentle way to kill
      - kill -9 #Pid#: This is a brutal way to kill a process
      - killall #Pname#: Kills all the processes with the Pname
      - killall -9 #Pname#: Kills all the processes with the Pname violently
34. job, fg, bg: Create processes in foreground and bg
35. gzip -k filename: Create a zip of the file. -k keeps the unzipped file. If used on multiple files, it zips them separately.
36. gunzip -k filename: Unzip the file 
37. tar -cf #EndFileName.tar# file1 file2 file3: Creates archives of multiple files. Now we can use gzip to compress the archive.
    1. tar -xf #EndFileName.tar# file1 file2 file3: To extract the archive
    2. tar -tf #ArchiveName#: To view contents of the archive
    3. tar -czf #EndFileName.tar# file1 file2 file3: To create and compress the archive all in one
 38. nano: It is an in-built text editor in linux
 39. alias: We can rename different keywords to be custom commands
    











