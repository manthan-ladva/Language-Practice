while True:
    psw = input("Enter new Password: ")
    if any(i.isdigit() for i in psw) and any(i.isupper() for i in psw) and len(psw) >= 5:
        print("Password is generated")
        break
    else:
        print("Dosen't match conditions")
