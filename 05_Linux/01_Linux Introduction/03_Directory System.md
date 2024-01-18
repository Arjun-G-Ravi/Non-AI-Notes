# Linux Directory system

![Alt text](<Screenshot from 2023-10-31 12-47-40.png>)

- Root: The root is at the top of the file system heirarchy. It is generally represented by forward-slash(\).
  - **root**: There is a directory called root inside root. That sucks.
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

# Directory representation in Linux

    .    Refers to the current directory
    ..   Refers to the prev directory
    ~    Refers to home
    /    Refers to the root

# Disk Partitions

Partitions are subdivisions of the whole disk. On Linux, they’re denoted with a number after the whole block device, and therefore have device names such as /dev/sda1 and /dev/sdb3. The kernel presents each partition as a block device, just as it would an entire disk. Partitions are defined on a small area of the disk called a partition table.

Use `sudo parted -l` to see all the partitions in disk.

# Swap space

It’s also possible to augment the RAM on a machine with disk space. If you run out of real memory, the Linux virtual memory system can automatically move pieces of memory to and from a disk storage. This is called swapping because pieces of idle programs are swapped to the disk in exchange for active pieces residing on the disk. The disk area used to store memory pages is called swap space (or just swap for short).
