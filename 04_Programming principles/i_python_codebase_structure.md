# Structure of a Python Program

https://docs.python-guide.org/writing/structure/

```
Project1                    # The root directory
├── README.md               # Basic overview
├── LICENSE                 # Open Source licence
├── Makefile                # An easy way to install and run tests
├── setup.py                # To setup env and install requirements
├── requirements.txt        # To install requirements (not necessary if setup exists)
├── Utils                   # Helper functions that is to be used for every class [2]
│   ├── util1
│   ├── util2
│   └── util2 
├── Project1                # The same name as the repo. Contains the important code
│   ├── p1                  # Subsection
│   │   ├── __init__.py     # Makes this directory callable as a module [1]
│   │   ├── p1.py           # main code for this subsection
│   │   ├── helpers.py      # Additional functions to be called by p1.py
│   │   ├── config.py       # config files and constants
│   └── p2
│       ├── __init__.py
│       ├── p2.py
│       └── helpers.py
|
├── Docs                    # Documentation for the project
│   ├── doc1
│   └── doc2
|
└── tests                   # Files for testing
    ├── unit_tests
    |   └── test_1.py       
    |   └── test_2.py
    |   └── test_3.py
    └── integration_tests
        └── test_1.py
        └── test_2.py
        └── test_3.py
```

[1] Use relative import to import p1, to make future importing easier
[2] and hence, cannot be put into any single sub-directory