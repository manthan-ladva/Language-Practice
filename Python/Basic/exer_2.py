def string_length(mystring):
    if type(mystring) == int:
        return 'Sorry due to integer'
    elif type(mystring) == float:
        return 'Sorry due to float'
    else:
        return len(mystring)
print(string_length(20.0))
