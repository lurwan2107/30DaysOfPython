import re

def count_lines(text):
    with open(text) as f:
        new_txt = f.read().splitlines()
        return f'We have {len(new_txt)} of lines'
    
speech = ["./data/Obama's_speech.txt", "./data/Michelle's_speech.txt", "./data/Trump's_speech", "./data/Melina's_speech"] 
for j in speech:
    print(count_lines(j))


def count_words(words):
    with open(words) as k:
        txt = k.read()
        wd = re.sub(r'[.,;"-]', '', txt)
        word = re.split(' ', wd)
        return f'number of words e hwva are {word}'
speechs = ["./data/Obama's_speech.txt", "./data/Michelle's_speech.txt", "./data/Trump's_speech", "./data/Melina's_speech"] 
for l in speechs:
    print(count_words(l))