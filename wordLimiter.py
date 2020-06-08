def wordLimiter(textToPrint, numberOfWordsPerLine):

	lines = textToPrint.split()
	charLimit = numberOfWordsPerLine
	currentLine = 0
	printedWords = 0
	printableLine = []

	while printedWords < len(lines):
		while currentLine < charLimit and printedWords < len(lines):
			printableLine.append(lines[printedWords])
			currentLine += 1
			printedWords += 1

		print(*printableLine)
		currentLine = 0
		printableLine = []