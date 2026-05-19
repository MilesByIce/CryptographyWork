
#were assuming RSA has already been computed, which is why there are no
#checks for primality for e and tot(n) (plus there is no p and q to check tot(n))

def sign(message, d, n):
# Input: the message Alice wants to send, and Alice's priv key
# Output: signature
# signature equation
  signature = pow(message, d) % n
  return signature
  
  
def verify(message,sig, e, n):
# Input: the message and the signature Bob recieves, and Alice's pub key
# Output: true if the message is from Alice, false otherwise
# verification equation
  ver = pow(sig, e) % n
  #establish result
  result = False
  #check if the verifcation is equal to the original message
  #if yes, set bool to true and print verification message
  #if no, keep bool as false and print message
  if ver == message % n:
    result = True
    print("The message is successfully verfied.")
    return result
  else:
    print("The message does NOT match the signature. The message is corrupted. ")
    return result
     
  


# Test case 1 we have already executed RSA:
# Alice Public key (e, n): 5, 170171
# Alice Secret key (d) 9677
n = 170171
e = 5
d = 9677

# This is the message that Alice wants to sign and send to Bob
message = 20

# Step 1: create signature (use Alice's private key)
sig = sign(message, d, n)

# Step 2: send message with signature to Alice
print("Alice sends message: ", message, " with signature: ", sig, " to Bob.")


# Bob verifies the signature
# Step 1: Verify the signature (use Alice's public key)
verification = verify(message, sig, e, n)
print("Verification value from the signature", verification)


# This is Eve being evil and modifies the message
m_modified = 10
print("Modified message: ",m_modified)

# Assume Bob receives the modified message
# Step 1: Verify the signature (use Alice's public key)
verification = verify(m_modified, sig, e, n)
print("Verification value", verification)

'''#Test case 2, message larger than keys
n = 33
d = 7 
e = 3

message = 208

#sign
sig = sign(message, d, n)
print("Alice sends message: ", message, " with signature: ", sig, " to Bob.")
#verify
verification = verify(message, sig, e, n)
print("Verification value from the signature", verification)
# This is Eve being evil and modifies the message
m_modified = 102
print("Modified message: ",m_modified)
#Verify the signature (use Alice's public key)
verification = verify(m_modified, sig, e, n)
print("Verification value", verification)'''
