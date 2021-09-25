from brownie import Gehirn, accounts

def test_deploy():
    account = accounts.load("freeaccount")

    gehirn = Gehirn.deploy({"from": account})
    ini_iq = gehirn.retrieve()

    expected = 0

    assert ini_iq == expected

def test_update():
    account = accounts.load("freeaccount")

    gehirn = Gehirn.deploy({"from": account})
    
    expected = 15
    ini_iq = gehirn.store(expected, {"from": account})

    assert expected == gehirn.retrieve()