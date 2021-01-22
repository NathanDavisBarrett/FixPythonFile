# Copyright 2021: Nathan Barrett, All Rights Reserved                          #
# fixPythonFile.py is distributed in the hope that it will be useful,          #
# but WITHOUT ANY WARRANTY; without even the implied warranty of               #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                #
# GNU General Public License for more details.                                 #
# Version: 2021.1.0 (01/22/2021)                                               #

"""
Sometimes when you switch between text editors, there is a mismatch in spacing for python indentation.
This file fill will fix that by replacing any instances of "    " (i.e. 4 spaces) style of indentation with
a single "tab" character.

To operate, either
	1) pass in the path to the file you'd like to fix as the first command line argument.
	or 2) specify the path to the file you'd like to fix in the "file" variable below.

"""

import sys

if len(sys.argv) == 2:
	file = sys.argv[1]
elif len(sys.argv) > 2:
	raise Exception("Please do not specify any more command line arguments that the file path of the file you'd like to fix.")
else:
	file = "hrz-orient.py"

indent = "\t"

newFile = []



print("WARNING! If somthing goes wrong, this code could significantly damage the textual configuration of \"" + file + "\"")
print("With that in mind, it is STRONGLY recommended that you create a backup of the file before proceeding.")
while True:
	print("Would you like to continue? (y/n)")
	response = input()

	if response == "n":
		sys.exit(0)
	elif response == "y":
		break
	else:
		print("Input not recognized.  Please type \"y\" or \"n\"")

with open(file) as inFile:
	for line in inFile:
		newLine = str()
		spaceBuffer = 0
		tabbed = False
		for char in line:
			if char == " " and tabbed == False:
				spaceBuffer += 1
			else:
				numTabs = spaceBuffer / 4
				#print(spaceBuffer,numTabs)
				for i in range(int(numTabs)):
					newLine += "\t"
				tabbed = True

				newLine += char
				spaceBuffer = 0
		newFile.append(newLine)

with open(file,"w") as outFile:
	for line in newFile:
		outFile.write(line)
