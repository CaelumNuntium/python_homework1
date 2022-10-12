def check_password(pw):
    haslower, hasupper, hasdigit, hasspecial = False, False, False, False
    if len(pw) < 8:
        return False
    for c in pw:
        if c.isdigit():
            hasdigit = True
        elif c.islower():
            haslower = True
        elif c.isupper():
            hasupper = True
        elif not c.isalnum() and not c.isspace():
            hasspecial = True
    return hasdigit and haslower and hasupper and hasspecial


#test
print(check_password("rdfcvyuvDFFtbo74755$77y"))
print(check_password("vubuyvbsd376254FFf"))
print(check_password("DGSDGSRG5446$::"))
print(check_password("difugufauiFEG&&RWEDFF"))
