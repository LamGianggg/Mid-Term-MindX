def find_word(frequency, inp_str):
    inp_str = inp_str.lower()
    
    new_str = ''
    for string in inp_str:
        if string.isalpha() or string.isspace() == True:
            new_str += string

    list = new_str.split()

    a = {}
    for i in list:
        if i in a:
            a[i] += 1
        else:
            a[i] = 1
    
    c = []
    for key,value in a.items():
        if value == frequency:
            c.append(key)
    
    a = ' '.join(c)
    return a

print(find_word(2,"The cat is chasing the rat. The dog is also chasing the rat."))