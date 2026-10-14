a=input("enter list of word").split(',')
long_len=0

for word in a:
    word=word.strip()
    curr_len=len(word)

    if curr_len > long_len:
        long_len = curr_len
        long_word = word

print(f"Longest word: '{long_word}' with length{long_len}")
