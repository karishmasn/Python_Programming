fhand=open("/etc/resolv.conf")
data=fhand.read()
if data:
    print("the file Exists")
else :
    print("The file doesnot Exist")
