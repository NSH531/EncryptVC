#from hashlib import _Hash
import hashlib
import rsa
import binascii
from flask import Flask, render_template, request
app = Flask(__name__)
class encrpython():
      
      def verify(message, signature, key):
        try:
            return rsa.verify(message.encode('ascii'), signature, key,) == 'SHA-1'
        except:
            return False

      def sign(message, key):
        return rsa.sign(message.encode('ascii'), key, 'SHA-1')

      def encrypt(message, key):
        return rsa.encrypt(message.encode('ascii'), key)
      def decrypt(ciphertext, key):
        try:
            return rsa.decrypt(ciphertext, key).decode('ascii')
        except:
            return False
      def gk():
            x=rsa.newkeys(4608)
            pubkey=x[0]
            privkey=x[1]
            return        [pubkey,privkey] 

      def generateKeys():
        [publicKey, privateKey] = encrpython.gk()

        with open('keys/publcKey.pem', 'wb') as p:
            p.write(publicKey.save_pkcs1('PEM'))
        with open('keys/privateKey.pem', 'wb') as p:
            p.write(privateKey.save_pkcs1('PEM'))
      def loadKeys():
        with open('keys/publicKey.pem', 'rb') as p:
            publicKey = rsa.PublicKey.load_pkcs1(p.read())
        with open('keys/privateKey.pem', 'rb') as p:
            privateKey = rsa.PrivateKey.load_pkcs1(p.read())
        return privateKey, publicKey

            
c1=[]
V1=[]
MyCrypt=encrpython()
@app.route("/crypt",methods=["POST"])
def myload():
    name = request.args.get("name")
    for i in c1:
          if(i==name):
                return c1
    file= request.args.get('file')
    keys= rsa.newkeys(4608)
    if(name):
              n=hashlib.sha1(bytes(name),usedforsecurity=True).hexdigest()
    else:
              n=hashlib.sha1(bytes("נתנאל שטרן"),usedforsecurity=True).hexdigest()
    
    c1.append([n,keys])

    with open('keys', 'a') as c:
      c.write(c1)
    with open('DATA', 'ab') as V:
      k=[]
      for i in c1:
            if i[0]==n:
                  k=i[1]
                  print(k)
                  
      V1=MyCrypt.encrypt()
      V.write(V1)
    return keys
@app.route("/")
def index():
    return """<div>
  <form method="post" action="/crypt">
    <input id="name"></input>
    <input type="file" id="data"></input>
  <input type="submit">
  </form>
</div>
"""
if __name__ == "__main__":
     app.run('0.0.0.0',8531)
