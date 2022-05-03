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
        return         rsa.newkeys(8192)

      def generateKeys():
        (publicKey, privateKey) = encrpython.gk()

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

MyCrypt=encrpython()
@app.route("/crypt",methods=["POST"])
def myload():
    name = request.args.get("name")
    file= request.args.get('file')
    keys=MyCrypt.gk()
    c1.append({name:keys})

    with open('keys', 'w') as c:
      c.write(c1)
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
     app.run()
