import sys

# The first element in sys.argv is the script name itself
script_name = sys.argv[0]

# The following elements are the command-line arguments passed to the script
arguments = sys.argv[1:]

print("Script name:", script_name)
print("Arguments:", arguments)
