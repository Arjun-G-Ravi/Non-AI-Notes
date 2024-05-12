# TMUX - terminal multiplexer
tmux is a program which runs in a terminal and allows multiple other terminal programs to be run inside it. It allows multiple sessions with windows, panes, and more.

## Primary uses
- Protect running programs on a remote server from connection drops by running them inside tmux.
- Allow programs running on a remote server to be accessed from multiple different local computers.
- Work with multiple programs and shells together in one terminal, a bit like a window manager.
![alt text](tmux-server.png)

## TMUX concepts
- tmux keeps all its state in a single main process, called the tmux server.
- `Panes` are the individual sections within a window that can be split and used for different tasks.
- `Windows` are the separate environments within which these panes exist. A window is made up of one or more panes which together cover its entire area. They are tabs in sessions.
- `Sessions` allow you to group related windows together and provide a convenient way to manage and switch between them. 

## Tmux status line
![alt text](image.png)

# Tmux terminal commands

1. Create new tmux session
   1. tmux new -s < SessionName >: Creates a new session with the SessionName
2. tmux ls: Lists all sessions
3. Attach
   1. tmux a: Attach to the most recent tmux session
   2. tmux a -t < SessionName >: Attach to the index (get index from tmux ls)
4. Kill a session: tmux kill-session -t < SessionName >
5. Kill the whole server: tmux kill-server

# Shortcuts

### General
1.  C-b ?: Open help
2.  C-b d: Detach from a session

### Panes
1.  C-b %: Split pane vertically
2.  C-b ": Split pane horizontally
3.  C-b < arrows >: Move around tmux panes
4.  C-b q < Index >: Move around tmux panes fast 
5.  C-b C-< arrows >: Adjust size of panes
6.  C-b Alt-< arrows >: Adjust size of panes fast
7.  C-b Alt-< 1 to 5>: Choose pre-selected layouts for panes
8.  C-b X: To kill a pane 

### Window
10. C-b c: Create a new window
11. C-b n: Move through the windows
12. C-b ,: Rename the current window
13. C-b &: Kill the window(and all the panes in it)
14. C-b w: Move through windows

https://github.com/tmux/tmux/wiki/Getting-Started