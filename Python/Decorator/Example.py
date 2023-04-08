def divideandsum(divfun):
    print("hello!")
    def checkeraddedfun(a,b,c):
        print("I am going to divide", a, "and", b)
        if b==0:
            print("You cannot divide with 0")
            return
        print(divfun(a,b) + c)
    print("return!")
    return checkeraddedfun

@divideandsum
def divide(a,b):
    return a/b

divide(2,5,3)
divide(2,0,3)