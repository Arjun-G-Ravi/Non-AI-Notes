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

We can change the permission using `chmod` command.
