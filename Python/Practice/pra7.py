def mutate_string(string, position, character):
    st = str(string)
    l = list(string)
    l[position] = character
    st = "".join(l)
    st = str(st)
    return st

print(mutate_string("monili", 3, "a"))
