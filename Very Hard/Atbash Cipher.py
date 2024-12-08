def atbash(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet = alphabet + alphabet.upper()
    out_list = []
    for i in list(text):
        if i in alphabet:
            out_list.append(alphabet[int(len(alphabet)/2-alphabet.index(i)-1)])
        else:
            out_list.append(i)
    return ''.join(out_list)


print(atbash("Hello World!"))