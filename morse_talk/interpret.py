import morse_talk as mtalk


def char_frequency(s):
    d = {}
    for n in s:
        if n in d.keys():
            d[n] += 1
        else:
            d[n] = 1
    return d


def ismorse(r):
    MORSE_CHARS = [".", "-", " "]
    d = char_frequency(r)
    for c in d.keys():
        if c not in MORSE_CHARS:
            return False
    return True


def interpret(q):
    if ismorse(q):
        return mtalk.decode(q)
    else:
        return mtalk.encode(q)


def main():
    print('\n')
    x = input("input>>> ")
    if x == "quit":
        print("program exited")
    else:
        y = interpret(x)
        print("output: "+y+'\n')
        main()


if __name__ == '__main__':
    main()
