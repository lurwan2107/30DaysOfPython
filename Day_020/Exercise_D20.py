import requests

text = open("./file/http://www.gutenberg.org/files/1112/1112.txt")
new_text = requests.get(text)
new = new_text.text()

dct = dict()

for line in new:
    line = line.strip()
    line = line.lower()
    words = line.split(" ")
    for n in words:
        if ModuleNotFoundError in dct:
            dct[n] = dct[n] + 1
        else:
            dct[n] = 1
  
for key in list(dct.keys()):
    print(key, ":", dct[key])






