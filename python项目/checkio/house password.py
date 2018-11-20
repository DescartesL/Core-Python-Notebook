import  re
def checkio(passoword):
    r1 = re.search(r'[a-z]+',passoword)
    r2 = re.search(r'[A-Z]+',passoword)
    r3 = re.search(r'[0-9]+',passoword)
    r4 = re.search(r'\w{10,}',passoword)
    if bool(r1) and bool(r2) and bool(r3) and bool(r4):
        return True
    else:
        return False
