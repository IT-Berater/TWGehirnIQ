# TWGehirnIQ

See http://blog.wenzlaff.de/?p=17484

Setzen in einer neuen Datei: .env
<pre>
# Projekt ID aus dem Settings Reiter von infura.io
# Endpoint: https://rinkeby.infura.io/v3/...
export WEB3_INFURA_PROJECT_ID='TODO'

# aus Metamask Testnet
export PRIVATE_KEY='0x TODO'

### Token von https://etherscan.io/myapikey
export ETHERSCAN_TOKEN='TODO'
</pre>

Start mit:

brownie run scripts/deploy.py --network rinkeby
