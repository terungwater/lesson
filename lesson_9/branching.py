# CensorWord
"""
Implement censor_words(text, banned_word). 
Return a new string where every occurrence of banned_word is replaced with "***". 
The match is case-sensitive. Do not use import or regular expressions.
"""

def censor_words(text, banned_word):
    split_text = text.split()
    words = []
    i = 0
    while i < len(split_text):
        cha = split_text[i]
        if cha == banned_word:
            words.append("***")
        else:
            words.append(cha)
        i+= 1
    return " ".join(words)
print(censor_words("this code is bad", "bad"))