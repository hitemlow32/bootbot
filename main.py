

def _main_():
    with open("/home/bdoyle/Code/boot.dev/bootbot/books/frankenstein.txt", 'r') as file:
        book = file.read()

    lowercased_words = book.lower()

    num_split = lowercased_words.split()
    num_words = len(num_split)

    letter_dict = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0,'f': 0, 'g': 0,'h': 0, 'i': 0, 'j': 0,'k': 0, 'l': 0,'m': 0, 'n': 0, 'o': 0, 'p': 0,'q': 0,'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0,'x': 0,'y': 0,'z': 0,}

    for i in list(lowercased_words):

        if i == 'a':
            letter_dict['a'] += 1
        elif i == 'b':
            letter_dict['b'] += 1
        elif i == 'c':
            letter_dict['c'] += 1
        elif i == 'd':
            letter_dict['d'] += 1
        elif i == 'e':
            letter_dict['e'] += 1
        elif i == 'f':
            letter_dict['f'] += 1
        elif i == 'g':
            letter_dict['g'] += 1
        elif i == 'h':
            letter_dict['h'] += 1
        elif i == 'i':
            letter_dict['i'] += 1
        elif i == 'j':
            letter_dict['j'] += 1
        elif i == 'k':
            letter_dict['k'] += 1
        elif i == 'l':
            letter_dict['l'] += 1
        elif i == 'm':
            letter_dict['m'] += 1
        elif i == 'n':
            letter_dict['n'] += 1
        elif i == 'o':
            letter_dict['o'] += 1
        elif i == 'p':
            letter_dict['p'] += 1
        elif i == 'q':
            letter_dict['q'] += 1
        elif i == 'r':
            letter_dict['r'] += 1
        elif i == 's':
            letter_dict['s'] += 1
        elif i == 't':
            letter_dict['t'] += 1
        elif i == 'u':
            letter_dict['u'] += 1
        elif i == 'v':
            letter_dict['v'] += 1
        elif i == 'w':
            letter_dict['w'] += 1
        elif i == 'x':
            letter_dict['x'] += 1
        elif i == 'y':
            letter_dict['y'] += 1
        elif i == 'z':
            letter_dict['z'] += 1


    print("--- Begin report of books/frankenstein.txt ---")
    print(num_words, " words found in the document")
    print("")

    for i in letter_dict:
        print("The ", i, "character was found", letter_dict[i], "times")

    print("--- End report ---")

_main_()