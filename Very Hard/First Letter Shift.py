def shift_sentence(text):
    words = text.split(' ')
    out = []
    for word in words:
        word_list = list(word)
        word_list[0] = list(words[(words.index(word)-1)%len(words)])[0]
        out.append(''.join(word_list))
    return ' '.join(out)
    
    
print(shift_sentence("create a function"))