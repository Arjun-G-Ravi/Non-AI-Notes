# 1. VIM MOTIONS

`GENERAL FORMAT: Command Count Motion`

# Change modes

    1. Enter insert mode (small letter is for character, capital is for line)
        i -> before the character
        I -> at the start of the line
        a -> after the character
        A -> at the end of the line
        s -> replacing that letter
        S -> replaces entire line
        r -> replace one letter
        R -> starts replacing characters (like getting into insert mode)
        o -> creates line after
        O -> creates line before
        (not using now)c -> Just like 'd',  but also enter insert mode after deletion

    2. : -> command mode
        :! command -> Lets us type bash command
    3. v -> visual mode
        Shift+v -> Visual mode and select that line
    4. Esc/ Ctrl+c -> normal mode

## 1. Normal mode

### Horizontal Motions

    1. h, l: Move around character
    2. w, b: Move around words, where words are string separated by special characters
    3. $: Move to end of line
    4. _: Move to start of line
    5. 0: Move to begining character
    6. #: Move to last place (skip)
    7. f +`<char>`: (find) Move to the next `<char>` that appears in the line (F for backward motion)
    8. t + `<char>`: (to) Move to one `<char>` before that appears in the line(T for backward motion)

### Vertical Motions

    1. j, k: Move up and down
    2. { and }(rare): Moves around through paragraphs
    3. Ctrl D and Ctrl u: Move half a page down and up
    4. GG, gg (rare): Move to last, first line

### Commands for Normal mode

    1.Delete/ Cut (d,c)
        1. d -> Delete selected part
        2. D -> Deletes rest of the line, from the cursor
        3. c -> Delete selected part and enter insert mode
        4. r -> Replace a character (like s), but stays in normal mode.
        5. bw -> Deletes next word
        6. db -> Delete prev word
        7. dd -> deletes a line
        8. cc -> deletes a line and enter insert mode
        9. de -> Delete till end of the word
    2. Inner(i)
        1.  diw -> Delete inner word. Deletes the word(if cursor is on middle)
        2. ciw -> Change inner word
        3. yi" -> Selects inside "   "
        4. 'ci(' or 'ci)' -> Deletes inner () and puts you to insert mode
    3. % -> Goes to the next pattern for brackets (not quotes)
        1. d% -> If done at a '(', it deletes everything till a ')'
    4. Copy/ Yank (y)
       1. yy: Copy the line
    5. Paste
       1. p -> After cursor
       2. P -> Before cursor
    6. u: Undo
    7. Ctrl+r: Redo
    8. zz: Centres your view
    9. /: To search through the text. Press N, n to move through searches
    10. * (at any word): Searches that word in the text. Press n, N to traverse through
    11. 'line_no' + G: Move to that line

    ### Intendation
    << To intend to left
    >> To intend to right

## 2. Command mode

    w: saves (writes)
    q: Quit
        :q! - Quit without saving
        :wq - Save and quit
    line_no: To move to that line

## 3. Visual mode

Selects the way through. We can move around using normal mode motion. Then the selected text can be deleted, copied, etc.
    v -> Visual mode
    V -> Visual line mode
    Ctlr + v -> Lets you access the visual block mode (may cause problems with paste)

## 4. Insert mode

The normal typing experience.

---

# 2. NVIM

nvim is a popular text editor that is a modern, improved version of the classic vim editor. It stands for "Neovim" and is a fork of the original vim project, with the goal of providing a more extensible and maintainable codebase.

### Telescope

Telescope is a powerful and highly customizable fuzzy finder plugin for Neovim (nvim). It provides a user-friendly interface for quickly searching and navigating through various types of content within your Neovim environment.

## LSP

LSP stands for "Language Server Protocol", and it is a protocol that allows software development tools, such as code editors and IDEs, to communicate with language-specific servers to provide advanced code editing features.

The main purpose of LSP is to enable a consistent and standardized way for code editors to interact with language-specific tools, such as compilers, linters, and code completion engines, to provide a rich and seamless coding experience. It includes code completion, syntax highlighting, refactoring, go-to definitions, etc.

## Mason

The default installer in nvim.

# Commands

`Space is the leader key.   `

- Tutor in nvim is a good way to start with the commands
- Lua vim.opt: To change settings from nvim command
- Lazy: To install new plugins and stuff
- q: To quit overlapping windows

# Shortcuts

- Leader s h: Help
- Leader s n: To search for a nvim related file
- Leader /: Search for a word or similar word in a file
- Leader d s: Opens document symbols - a list of all classes, variables, etc in the given file
- Leader w s: Opens workspace symbol, the above but for an entire workspace
- [ d: Go to next error message line
- g d: Go to definition
- g r: Go to references
- K over a word: Shows its documentation

## Nvim(kickstart) specific vim motions

- va)  - [V]isually select [A]round [)]paren
- yinq - [Y]ank [I]nside [N]ext [']quote
- ci'  - [C]hange [I]nside [']quote
- saiw) - [S]urround [A]dd [I]nner [W]ord [)]Paren
- sd'   - [S]urround [D]elete [']quotes
- sr)'  - [S]urround [R]eplace [)] [']
