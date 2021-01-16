for i in range(97, 123):
    with open(chr(i) + '.txt', 'w') as file:
        file.write(chr(i))
