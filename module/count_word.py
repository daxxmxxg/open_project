import sys
import re

input_data = sys.argv[1]
data = open("input_data",'w+')
document = data.read().lower()
match_pattern = re.search(r'\b[a-z]{3,15}\b', documnet)
for word in match_pattern:
  count = frequency.get(word,0)
  frequency[word] = count + 1
for words in frequency_list:
    print words, frequency[words]
