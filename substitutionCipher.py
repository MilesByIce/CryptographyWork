
import random

# A global constant defining the alphabet. 
LETTERS = "abcdefghijklmnopqrstuvwxyz"


def makeRandomKeyDic():
    # A legal random key is a permutation of LETTERS.
    lst = list( LETTERS )    # Turn string into list of letters
    random.shuffle( lst )    # Shuffle the list randomly
    ''.join( lst )    # Assemble them back into a string     
    
    encryptdic = {}
    for c in LETTERS:      # create a letter-key mapping dictionary for encryption    
        index = LETTERS.find(c)
        encryptdic[c] = lst[index]
    return encryptdic

def makeRandomKeyDic_Decrypt(encryptdic):
    # input: encryptdic, a letter-key mapping dictionary for encryption
    # output: a key-letter mapping dictionary for decryption
    decryptdic = {v:k for k, v in encryptdic.items()}
    return decryptdic
    
    
    
def encrypt(encryptdic, plaintext):
    # encryption function
    ciphertext = ""
    # to simplify, all letters are converted to lowercase.
    plaintext = plaintext.lower()
    for c in plaintext:
        if c in LETTERS:
            ciphertext += encryptdic[c]
        else:
        # if this char is not a letter, 
        # just append the original char to the cipher
            ciphertext += c
    return ciphertext



def decrypt(dencryptdic, ciphertext):
    # decryption function
    # input: ciphertext, encryptdic
    # output: decrypted plaintext
    plaintext = ""
    for c in ciphertext:
        if c in LETTERS:
            plaintext += dencryptdic[c]
        else:
            plaintext += c
    return plaintext
    


#test 1
encryptdic = makeRandomKeyDic()
dencryptdic = makeRandomKeyDic_Decrypt(encryptdic)
# encryption key
print(encryptdic)
# test case
message = "YOU ARE AWESOME"
# plaintext
ciphertext = encrypt(encryptdic, message)
# encryption
print(ciphertext)
# ciphertext
print(dencryptdic)
dmessage = decrypt(dencryptdic, ciphertext)
# decryption
print(dmessage)
# decrypted message


#test 2
encryptdic = makeRandomKeyDic()
dencryptdic = makeRandomKeyDic_Decrypt(encryptdic)
# encryption key
print(encryptdic)
# test case
message = "You Are 109 years old? Thats very old! Wow, I want to live that long :)"
# plaintext
ciphertext = encrypt(encryptdic, message)
# encryption
print(ciphertext)
# ciphertext
print(dencryptdic)
dmessage = decrypt(dencryptdic, ciphertext)
# decryption
print(dmessage)
# decrypted message

#test 3
encryptdic = makeRandomKeyDic()
dencryptdic = makeRandomKeyDic_Decrypt(encryptdic)
# encryption key
print(encryptdic)
# test case
message = "***3243429panda__lol"
# plaintext
ciphertext = encrypt(encryptdic, message)
# encryption
print(ciphertext)
# ciphertext
print(dencryptdic)
dmessage = decrypt(dencryptdic, ciphertext)
# decryption
print(dmessage)
# decrypted message