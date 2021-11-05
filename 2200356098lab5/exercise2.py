intp =input("please enter a email:\n")
def email(email):
    a=0
    b=0
    for x in email:
        if x== "@":
            a+=1
        elif x == ".":
            b+=1
    if a>=1 and b>=1:
        return True
    else:
        return False
print(email(intp))