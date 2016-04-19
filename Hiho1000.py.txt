while True:
    try:
        values = raw_input()
        (a, b) = ( int(x) for x in values.split())
        print a+b
    except EOFError:
        break
