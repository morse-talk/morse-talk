import morse_talk as mtalk


def mutual():
    flag = 0
    print('\n')
    x = input("input>>> ")
    if x == 'quit':
        print("Program Exited")
    else:
        q = ""
        try:
            q = mtalk.decode(x)
        except:
            q = mtalk.encode(x)

        print("output: "+q+'\n')
        mutual()


def main():
    import doctest
    doctest.testmod()
    mutual()


if __name__ == '__main__':
    main()
