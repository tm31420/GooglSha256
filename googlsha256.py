
import binascii, hashlib, base58, sys, ecdsa, codecs
ra = open('sha256ofaddr.txt', 'w')


def convert(aa):
    string = aa
    aa = hashlib.sha256(string).hexdigest()
    ra.write("%s \n" % aa)    
    print aa
    
with open("addrs.txt") as file:
    for line in file:

        ss = str.strip(line)
        print "__________________________________________________\n"
        print "Converting pvk: " + ss
        
        convert(ss)

