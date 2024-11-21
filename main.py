text = ''

print('enter or paste your text, one paragraph at a time please or it won\'t work! when you\'re done, just enter a single backslash! also, values will probably (?) not be accurate if you put spaces around your em dashes, so uh. yeah.')
while True:
	entered = input('enter text below:\n')
	if entered == '\\':
		break
	else:
		text = text + '\n' + entered

character_count = len(text)

text_corrected = text.replace('—', ' ') #because you are NOT supposed to put spaces around your em dashes!!! i WILL make the assumption that people know how to use punctuation correctly!!
text_corrected = text_corrected.replace('!', '.')
text_corrected = text_corrected.replace('?', '.')
text_corrected = text_corrected.replace('. . .', '')
text_corrected = text_corrected.replace(' .', '.')

words = text_corrected.split()
sentences = text_corrected.split('. ')

longest_sentence = ''
shortest_sentence = ''
max_words = 0
min_words = float('inf')
for sentence in sentences:
	if len(sentence.split()) > max_words:
		longest_sentence = sentence
		max_words = len(sentence.split())
	if len(sentence.split()) < min_words:
		shortest_sentence = sentence
		min_words = len(sentence.split())

word_count = len(words)
sentence_count = len(sentences)
words_per_sentence = word_count/sentence_count

print('Character count (includes spaces and newlines):', character_count)
print('Word count:', word_count)
