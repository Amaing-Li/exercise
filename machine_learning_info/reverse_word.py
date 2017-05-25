def reverse_word(sentence):
    reverse_list = []
    words = sentence.split()
    for word in words:
        word = word[::-1]
        reverse_list.append(word)
    result = " ".join(reverse_list)
    return result
