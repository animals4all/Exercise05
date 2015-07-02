from sys import argv

LETTERS = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def main():
	script, filename = argv
	fileObj = open(filename)
	fileContents = fileObj.read()
	fileContents = fileContents.lower()
	fileContents.replace(" ", "")

	for letter in LETTERS:
		occurences = 0
		for line in fileContents:
			for char in line:
				if char == letter:
					occurences += 1
		print str(occurences)

if __name__ == "__main__":
	main()