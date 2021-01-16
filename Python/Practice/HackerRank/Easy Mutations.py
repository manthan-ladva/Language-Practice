def mutate_string(string, position, character):
    new = string[:position] + character + string[position+1:]
    return new

s = input()
i, c = input().split()      #Keep a space between so that error does not occur during run time
s_new = mutate_string(s, int(i), c)
print(s_new)