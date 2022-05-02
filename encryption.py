
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
class encrpython():
  keyPair = RSA.generate(8192)
  
  def pubKey(keyPair):
    
    pubKey = keyPair.publickey()
    print(f"Public key:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
     pubKeyPEM = pubKey.exportKey()

    print(pubKeyPEM.decode('ascii'))
    return  pubKeyPEM
  
  #print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")
  def privKey(KeyPair):
    
    privKeyPEM = keyPair.exportKey()
    print(privKeyPEM.decode('ascii'))
    return privKeyPEM
  def encryption(msg,pubKey):
    encryptor = PKCS1_OAEP.new(pubKey)
    encrypted = encryptor.encrypt(msg)
    print("Encrypted:", binascii.hexlify(encrypted))
    return encrypted
  
