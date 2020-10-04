'''
Used resourches:
1) https://cryptography.io/en/latest/fernet/
2) https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/
3) https://devqa.io/encrypt-decrypt-data-python/
4) https://nitratine.net/blog/post/asymmetric-encryption-and-decryption-in-python/
'''

import os
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet


def keyGenerator(): #generates private and public key
    privateKey = rsa.generate_private_key(public_exponent=65537, key_size=2048,backend=default_backend())
    publicKey = privateKey.public_key()
    return {"privateKey": privateKey, "publicKey": publicKey} #storing keys as pairs


def encryption(pubKey, textToEncrypt): #encrypts text with public key
    cipheredText = pubKey.encrypt(textToEncrypt, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                              algorithm=hashes.SHA256(), label=None))
    return cipheredText

def decryption(privKey, cipheredText): #decrypts encrypted text with private key
    noCipheredText = privKey.decrypt(cipheredText, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                                algorithm=hashes.SHA256(), label=None))
    return noCipheredText

def sym_Encryption(symKey, msgToEncrypt): #encrypts message with symmetric key
    cipher = Fernet(symKey)
    return cipher.encrypt(msgToEncrypt)

def sym_Decryption(symKey, msgToDecrypt): #decrypts encrypted message with symmetric key
    cipher = Fernet(symKey)
    return cipher.decrypt(msgToDecrypt)


#Process betweeen Bob and Alice
secretMsg = b"Hello there!" #message will be ciphered
key_Bob = {}
key_Bob = keyGenerator() #generates key for bob

key_Alice = {}
key_Alice['pubKey_Bob'] = key_Bob['publicKey'] #takes bobs key
key_Alice['symKey_Alice'] = Fernet.generate_key() #alice creates symmetric key

#alice encrypts taken key with her symmetric key
encryptionProcess = encryption(key_Alice['pubKey_Bob'], key_Alice['symKey_Alice'])

#bob decrypts taken back key with his private key
decryptionProcess = decryption(key_Bob["privateKey"], encryptionProcess)

#and encrypts secret message with his symmetric key and sends back to alice
decryptedMessage = sym_Decryption(decryptionProcess, sym_Encryption(decryptionProcess, secretMsg))

#now alice can see the secret message
print(f'Secret Message: {decryptedMessage.decode()}')

