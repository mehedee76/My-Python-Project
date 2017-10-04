def bio(fname,address,pcode):
    ur_bio = str (fname), str (address), int (pcode)
    return ur_bio

fname = input ("Enter your name: ")
address = input("Enter your address: ")
pcode = input("Enter your postcode:")
print(bio(fname,address,pcode))

def portname(finame):
    nfiname = str(finame)
    return nfiname
def portadd(add):
    nadd = str(add)
    return nadd
def portcode(code):
    ncode = int(code)
    return ncode

finame = input("Enter your name: ")
print(portname(finame),"Fakir")
add = input("Enter your village: ")
print(portadd(add),"kahalu, Bogra")
code = input("Enter your post code: ")
print(portcode(code),"Bogra")
