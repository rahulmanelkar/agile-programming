# simple word encrypt/decrypt program
word = "This"
index = 3
encr =""
decr = ""

print ("Original = ",word)
for x in word:
    #print (x, ord(x), ord(x)+index, chr(ord(x)+index))
    encr = encr+chr(ord(x)+index)
print ("Encrypted = ", encr)
for x in encr:
    #print (chr((ord(chr(ord(x)-index)))))
    decr = decr + chr((ord(chr(ord(x)-index))))
print ("Decrypted = ", decr)
