#! python3
# bulletPointerAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard

import pyperclip
text = pyperclip.paste()

# TODO : Separate lines and add star

pyperclip.copy(text)

# Separate lines and star

lines = text.split('\n')
for i in range(len(lines)): #loop through all indexes in the 'lines' list
    line[i] = '* ' + lines[i] # add star to each string in 'lines' list

text = '\n'.join(lines)
pyperclip.copy(text)
