from typing import TYPE_CHECKING, Type


lyrics_all = []
with open('lyrics.txt', encoding = 'utf8') as f:
    lyrics = f.read()
    lyrics_all.append(lyrics)
lyrics_list = []
banned = [' ','.',',','!']
lyrics_word = ''
for w in lyrics:
    w = w.lower()
    if w =='\n': 
        if lyrics_word:
            lyrics_list.append(lyrics_word)
            lyrics_word = ''
    elif w not in banned:
        lyrics_word += w
    else:
        if lyrics_word:
            lyrics_list.append(lyrics_word)
        lyrics_word = ''
if lyrics_word:
    lyrics_list.append(lyrics_word)
    lyrics_word = ''
check_dupes = {}
for w in lyrics_list:
    w = w.lower()
    if w not in check_dupes:
        check_dupes[w] = 1
    else: check_dupes[w] += 1

number = ('w',1)
for word in check_dupes.items():
    if word [1] >= number [1]:
        number = word
print(number)

