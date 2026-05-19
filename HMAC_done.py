# Miles Byrnes
# CMPT436
# 4/24/26
# But you must have the HMAC class with at least the indicated methods, and a main routine.

from hashlib import sha512
import base64

def HMAC_suffix(k, x):
# Input: a secret key k, message x
# Output: HMAC cfor the message (secret suffix MAC: h(x||k))
    x_k = x + k
    # append the key to the message 
    # secret suffix MAC: h(x||k)
    hmac_suffix = sha512(x_k.encode()).digest()
    return hmac_suffix


def HMAC_suffix_verify(k, x, t):
# Input: a secret key k, received message x, received HMAC t (secret suffix MAC: t= h(x||k))
# Output: true if received HMAC t matches the received message x 
    #We do the same as above, like we are receiving the key, message, and MAC 
    #so to verify it must be recomputed
    x_k = x + k
    hmac_suffix = sha512(x_k.encode()).digest()

    #then we need to check that the recieved MAC is the same as what we just computed
    if t == hmac_suffix:
      print("The message is successfully verfied.")
    else:
      print("The message is corrupted. ")


def HMAC_prefix(k, x):
# Input: a secret key k, message x
# Output: HMAC cfor the message (secret prefix MAC: h(k||x))
    k_x = k + x
    # append the key to the message 
    # secret suffix MAC: h(k||x)
    hmac_prefix = sha512(k_x.encode()).digest()
    return hmac_prefix



def HMAC_prefix_verify(k, x, t):
# Input: a secret key k, received message x, received HMAC t (secret prefix MAC: t= h(k||x))
# Output: true if received HMAC t matches the received message x 
    #like other verification, we must recompute
    k_x = k + x
    hmac_prefix = sha512(k_x.encode()).digest()

    #then we need to check that the recieved MAC is the same as what we just computed
    if t == hmac_prefix:
      print("The message is successfully verfied.")
    else:
      print("The message is corrupted. ")




# test case 1
# this a test for suffix HMAC
# Assume Alice and Bob have established a shared secret key, i.e., through DHKE. 
# Assume this secrety key is "secret key", :)
secret_key = "secret key"
# Alice wants to send a message to Bob. 
# Alice adds a HMAC (suffix) to the message. 
m = "This is a test message"
hmac_a_suffix = HMAC_suffix(secret_key, m)
print("Alice sends message: ", m, " with hmac: ", hmac_a_suffix, " to Bob.")
# Bob receives and validates the HMAC
verification_suffix = HMAC_suffix_verify(secret_key, m, hmac_a_suffix)


  
# test case 2
# add a test case for prefix HMAC
secret_key2 = "wowie"
# Alice wants to send a message to Bob. 
# Alice adds a HMAC (suffix) to the message. 
mes = "Sure is a good message"
hmac_a_prefix = HMAC_prefix(secret_key2, mes)
print("Alice sends message: ", mes, " with hmac: ", hmac_a_prefix, " to Bob.")
# Bob receives and validates the HMAC
verification_prefix = HMAC_prefix_verify(secret_key2, mes, hmac_a_prefix)
  


# test case 3
# add a test case for prefix HMAC with wrong message check
secret_key2 = "wowie"
# Alice wants to send a message to Bob. 
# Alice adds a HMAC (suffix) to the message. 
mes = "Sure is a good message"
bad_mess = "this isnt a good message"
hmac_a_prefix = HMAC_prefix(secret_key2, mes)
print("Alice sends message: ", mes, " with hmac: ", hmac_a_prefix, " to Bob.")
# Bob receives and validates the HMAC
verification_prefix = HMAC_prefix_verify(secret_key2, bad_mess, hmac_a_prefix)
   

#test case 4, suffix bad message
secret_key = "secret key"
# Alice wants to send a message to Bob. 
# Alice adds a HMAC (suffix) to the message. 
m = "This is a test message"
m2 = "this message is corrupted"
hmac_a_suffix = HMAC_suffix(secret_key, m)
print("Alice sends message: ", m, " with hmac: ", hmac_a_suffix, " to Bob.")
# Bob receives and validates the HMAC
verification_suffix = HMAC_suffix_verify(secret_key, m2, hmac_a_suffix)