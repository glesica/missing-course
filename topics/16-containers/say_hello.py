import os, sys

PREAMBLE = "SAY_HELLO_PREAMBLE"

# A message will be printed, addressed to a human, by the computer. The first
# parameter is the name of the human, the second is the name of the computer.
# Both parameters are optional.

human = "kindly user"
if len(sys.argv) > 1:
    human = sys.argv[1]

computer = "your helpful computer"
if len(sys.argv) > 2:
    computer = sys.argv[2]

# The preamble will be printed before the rest of the message and can be
# specified either directly through an environment variable or by pointing at a
# file, which will be read and its contents printed.

if PREAMBLE in os.environ:
    preamble = os.environ[PREAMBLE]
else:
    preamble = ""

if preamble:
    try:
        pre_file = open(preamble, "r")
        pre_content = pre_file.read().strip()
        pre_file.close()
    except FileNotFoundError:
        pre_content = preamble

    print(pre_content)

print(f"Hello, {human}, I am {computer}!")

