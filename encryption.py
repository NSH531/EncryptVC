import rsa
import binascii
class encrpython():
  def generateKeys():
    (publicKey, privateKey) = rsa.newkeys(8192)
    with open('keys/publcKey.pem', 'wb') as p:
        p.write(publicKey.save_pkcs1('PEM'))
     with open('keys/privateKey.pem', 'wb') as p:
        p.write(privateKey.save_pkcs1('PEM'))
        
