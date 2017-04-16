from collections import Counter
from string import punctuation

text = "WE all love to eat lots of the bananas, don't we. we. we."
text_lowercase = text.lower()
text_lowercase_without_punctuation =



words = text_lowercase_without_punctuation.split()

counter = Counter(words)
top_three = counter.most_common(3)
print(top_three)





