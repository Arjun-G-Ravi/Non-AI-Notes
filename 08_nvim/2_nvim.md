# NVIM

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
