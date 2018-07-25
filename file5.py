var=int(input("Enter a integer:"))
print("variable holds:",var)

def check_odd(num):
    if num%2==0:
        return False
    else :
        return True


print("the number is Odd :",check_odd(var))
