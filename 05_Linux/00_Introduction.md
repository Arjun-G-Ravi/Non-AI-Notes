# Terminal commands
There is a whole bunch of OS that spawned from UNIX. They all use similar directory system, and hence similar terminal commands. 
It includes Linux based OS like ubuntu, fedora and kali, MacOS, Android, etc.
Windows doesn't fall in this class, and has a separate terminal.
https://eylenburg.github.io/os_familytree.htm

# Linux Origin Story
- Richard Stallman and a group of people aimed to create an open-source UNIX based operating system. It was named GNU.
    Linus Torvalds was working to create his own kernel known as Linux.
- At that time, GNU lacked a kernel. So, Linux combined his kernel with the existing operating system to create a full operating system.
- Thus linux is the name of the kernel used in the operating system. Its just a piece of the OS that connects the software to the hardware. Many people call the operating system itself as Linux. It should be called GNU/Linux.

# True UNIX and UNIX-like
True UNIX refers to operating systems that are certified as compliant with the Single UNIX Specification, which is a set of standards for operating systems that conform to the original UNIX design principles. It costs money, and effort for this certification.
Eg: Solaris (Oracle), AIX (IBM)

UNIX-like operating systems, also known as Unix-like or Unix-compatible, are not certified as true UNIX but share many of the same design principles and features. They generally don't go True because either of money or effort reasons. Some don't certify as it defeats the purpose of being open source.
Eg: Linux, macOS

# GNU/ Linux
GNU/Linux(commonly reffered to as linux) is a popular open source UNIX-like operating system that used Linux kernel and GNU tools.


# Linux Distributions
A linux distribution is a Linux kernel, some GNU tools, documentation, desktop manager, and whole lot of other things. There are 1000s of linux distros.
Eg: 
- Ubuntu: Most popular, user friendly
- Fedora: Cutting edge of open-source technologies
- Debian: Robust and stable Linux distribution, Serves as the basis other distributions, including Ubuntu.
- Arch Linux: Rolling-release distribution favored by advanced users, minimal base installation, and users build their systems from the ground up.
- Linux Mint: Out-of-the-box usability, comes with the Cinnamon desktop environment, Great choice for newcomers to Linux.
- Kali Linux: Specialized distribution designed for penetration testing and ethical hacking. 
- Slackware: Oldest Linux distributions and is known for its simplicity and minimalism.
  

# Linux Directory system
![Alt text](<Screenshot from 2023-10-31 12-47-40.png>)
- Root: The root is at the top of the file system heirarchy. It is generally represented by forward-slash(\).
    - **root**: There is a directory called root also. That sucks.
    - **bin**: Contains binaries/executables essential for the entire OS. These files can be run through terminal at any time. Eg:ls, touch, curl
    - **sbin**: Contains system binaries, which can be accessed only by root user. Eg: mount, deluser
    - **lib**: This directory contain files which are common for bin and sbin
    - **usr**: These contains non-essential binaries
      - bin, sbin: The usr directory also has a separate bin and sbin directories. These directories contains binaries are non-essential for the OS, and is for the use of the end user.
      - local: This contains binaries compiled by the user itself. It provides a safe place for binaries, to not conflict with system binaries.
    - **etc**: Editable text config files
    - **home**: It will contain a folder for each user registered in the system. It is represented by squiggle(~). 
      - user1: For each user, it will contain many folders like:
        - Desktop: Files and folders to be shown in the desktop
        - Documents, Downloads, etc.
      - user2: similar
    - **boot**: Contains files needed to boot the system
    - **dev**: Device files for hardware and drivers
    - **var**: Contain variable files and caches
    - **tmp**: Contains temperory files
    - **proc**: Illusionary file system that does't exist on the disk. It is created by the linux kernel on the memory, to keep track of running processes.

# Terminal and Shell
The terminal, also known as a command-line interface (CLI) or console, is a text-based interface that allows users to interact with the shell(and thus the OS) by typing commands. It serves as a user interface for entering and executing commands. 

The shell is a command interpreter, which is a program that takes the commands entered by the user via the terminal and interprets them for the operating system. It is called shell as it hides the kernel.
Eg:
- **Bash (Bourne-Again Shell)**: Default shell on many Linux distributions. Bash is known for its scripting capabilities and is highly customizable. It provides a robust set of features for both interactive use and scripting.
- **Fish (Friendly Interactive Shell)**: Fish is designed to be user-friendly and interactive. It offers features like syntax highlighting, autosuggestions, and a helpful web-based configuration interface.
- **Zsh (Z Shell)**: Zsh is an extended shell that offers many interactive features and advanced scripting capabilities. It includes features like advanced auto-completion, themes, and plugins. Macs these days use Z Shell.

![Alt text](<Screenshot from 2023-10-31 10-37-49.png>)


# Permissions

![Alt text](<Screenshot from 2023-11-09 20-01-30.png>)

The permission will be a 10 character string:
 - 1 st character
    - d: It is a directory
    - -: It is a file
    - l: Symbolic links
 - Next 3 characters: Permissions for the Owner
 - Next 3 characters: Permissions for the Group Owner
 - Next 3 characters: Permissions for the World (everybody except the above two)
    - rwx: Stands for read, write, executable permission for the corresponding user.

![Alt text](<Screenshot from 2023-11-09 20-02-20.png>)
