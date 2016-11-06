from msvcrt import getch, putch


def putstr(str):
    for c in str:
        putch(c)


def adinput(prompt, default=None):
    putstr(prompt)
    if default is None:
        data = []
    else:
        data = list(default)
        putstr(data)
    while True:
        c = getch()
        if c in '\r\n':
            break
        elif c == '\003':  # Ctrl-C
            putstr('\r\n')
            raise KeyboardInterrupt
        elif c == '\b':  # Backspace
            if data:
                putstr('\b \b')  # Backspace and wipe the character cell
                data.pop()
        elif c in '\0\xe0':  # Special keys
            getch()
        else:
            putch(c)
            data.append(c)
    putstr('\r\n')
    return ''.join(data)


if __name__ == '__main__':
    p = adinput("enter name", "noortheen\nraja")
    print "%r" % p
