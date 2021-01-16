while True:
    notes = []
    psw = input("Enter new Password: ")

    if not any(i.isdigit() for i in psw):
        notes.append("Atleast 1 digit is required")
    if not any(i.isupper() for i in psw):
        notes.append("Atleast 1 Upper-case letter is required")
    if len(psw) < 5:
        notes.append("Atleast 5 character is required")

    if len(notes) == 0:
        print("Password is fine")
        break
    else:
        print('Please check the following')
        for i in notes:
            print(i)
