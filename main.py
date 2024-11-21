text = ''
while True:
	entered = input('enter or paste your text, one paragraph at a time please or it won't work! when you\'re done, just enter a single backslash!\n')
	if entered == '\':
		break
	else:
		text = text + '\n' + entered

text_corrected_for_words = text.replace('—', ' ')
