contents = open("../data/dinos.txt").read().lower()
# print(contents)
chars = list(contents)
# print(chars)
uniqChars = set(chars)
data_size = len(chars)
vocab_size = len(uniqChars)
print("there are {}chars,and {}unique chars".format(data_size,vocab_size))

char_to_ix = { ch:i for i,ch in enumerate(sorted(uniqChars)) }
ix_to_char = { i:ch for i,ch in enumerate(sorted(uniqChars)) }
print(char_to_ix)
# print(ix_to_char)