class IO_versions():
  Ecrypt=encrpython()
  def load(Ecrypt):
    keys=[]
    keys.append(Ecrypt.Pubkey(Ecrypt.KeyPair))
    keys.append(Ecrypt.PrivKey(Ecrypt.KeyPair))
    return keys
