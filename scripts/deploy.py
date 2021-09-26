from brownie import accounts, config, Gehirn, network	

def deploy_gehirn():

	account = get_account()
	print("Verwende Account...", account)
	gehirn = Gehirn.deploy({"from": account}, publish_source=True)
	iq = gehirn.getIQ()
	print("Der IQ=", iq)
	transaktion = gehirn.setIQ(120, {"from": account})
	transaktion.wait(1)
	neuer_iq = gehirn.getIQ()
	print("Der neue IQ=", neuer_iq)

def get_account():
	if network.show_active() == "development":
		return accounts[0]
	else:
		return accounts.add(config["wallets"]["from_key"])
		
def main():
	print("Start ...")
	deploy_gehirn()
