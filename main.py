text = ''

print('enter or paste your text, one paragraph at a time please or it won\'t work! when you\'re done, just enter a single backslash! also, values will probably (?) not be accurate if you put spaces around your em dashes, so uh. yeah.')
while True:
	entered = input('enter text below:\n')
	if entered == '\\':
		break
	else:
		text = text + '\n' + entered

character_count = len(text)
print('Character count (includes spaces and newlines):', character_count)

text_corrected = text.replace('—', ' ') #because you are NOT supposed to put spaces around your em dashes!!! i WILL make the assumption that people know how to use punctuation correctly!!
word_count = len(text_corrected.split())
print('Word count:', word_count)

text_corrected = text_corrected.replace('!', '.')
text_corrected = text_corrected.replace('?', '.')
sentences = text_corrected.split('. ')
words_per_sentence = word_count/len(sentences)

