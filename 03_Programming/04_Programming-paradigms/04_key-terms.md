- Delaying decisions about program implementation
until run time is known as late binding
- The compiler relies on a separate program, known as a linker, to
merge the appropriate library routines into the final program
- Many compilers generate assembly language instead of machine language.
- Occasionally one would hear the C++ compiler referred to as a preproces-
sor, presumably because it generated high-level output that was in turn com-
piled. I consider this a misuse of the term: compilers attempt to “understand”
their source; preprocessors do not.
- Many compilers are self-hosting: they are written in the language they
compile—Ada compilers in Ada, C compilers in C.(using a technique known as bootstrapping)
- a compiler does not necessarily translate from a high-level programming language into machine language. Eg: latex