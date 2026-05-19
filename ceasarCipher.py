
  

# A global constant defining the alphabet. 
alphabet = "abcdefghijklmnopqrstuvwxyz"


def encrypt(message, key):
    # encryption function
    ciphertext = ""
    # make the message case insensitive
    # all letters are converted to lowercase.
    message = message.lower()
    for c in message:
        if c in alphabet:
            index = alphabet.find(c)
            # caesar encryption is just a simple shift of characters according to the key use modular arithmetic to transform the values within the range [0,num_of_letters_in_alphabet]
            index = (index + key) % len(alphabet)
            ciphertext += alphabet[index]
        else:
        # if this char does not appear in alphabet
        # just append the original char to the cipher
            ciphertext += c
            
    return ciphertext
            


def decrypt(ciphertext, key):
    # decryption function
    # input: ciphertext, key
    # output: decrypted plaintext
    #take the plaintext
    plaintext = ""
    #for all letters in text that are in the defined alphabet
    for c in ciphertext:
        if c in alphabet:
            #take each letter and just go back from the originial key with - instead of +
            index = alphabet.find(c)
            index = (index - key) % len(alphabet)
            plaintext += alphabet[index]
        else:
            #if not in defined alphabet, just move forward
            plaintext += c
    return plaintext
  



def bruteforce(ciphertext):
    # bruteforce cracker function
    # input: ciphertext
    # output: print the decrypted plaintext for each possible key
    print("Given ciphertext: ", ciphertext)
    #for all keys in the alphabet range
    for key in range(26):
        #run the decryption algorithm for each key and print the result
        decrypt_msg = decrypt(ciphertext, key)
        print(f"Key: {key:2}: {decrypt_msg} ")

    
    
    
    
    
# test case 1  
key = 1
print(key)
# encryption key
message = "you are awesome"
# plaintext
cipher = encrypt(message, key)
# encryption
print(cipher)
# ciphertext
message = decrypt(cipher, key)
# decryption
print(message)
# decrypted message

# A brute-force attack
bruteforce(cipher)


# test case 2   
key = -11
print(key)
# encryption key
message = "You ARE S00 Cool"
# plaintext
cipher = encrypt(message, key)
# encryption
print(cipher)
# ciphertext
message = decrypt(cipher, key)
# decryption
print(message)
# decrypted message

# A brute-force attack
bruteforce(cipher)


# test case 3  
key = 20
print(key)
# encryption key
message = "LALA Land, I've never seen that movie OMG, Shutup @*#&$&#"
# plaintext
cipher = encrypt(message, key)
# encryption
print(cipher)
# ciphertext
message = decrypt(cipher, key)
# decryption
print(message)
# decrypted message

# A brute-force attack
bruteforce(cipher)