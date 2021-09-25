from brownie import accounts, config, Gehirn

def read_iq():
    gehirn = Gehirn[-1]
    print("Der Gehirn IQ auf der Blockchain ist " , gehirn.retrieve())

def main():
    read_iq()