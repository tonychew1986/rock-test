from eth_account import Account
import requests
from web3 import Web3, HTTPProvider

w3 = Web3(HTTPProvider("https://ropsten.infura.io/v3/7028773b635f4c7bbbdf53d529f64c4c"))

# blockNum = w3.eth.blockNumber
# print("blockNum", blockNum)

def generateAddressAndKeys():
    acct = Account.create('')

    return acct

def sendCoins(addressFrom, addressTo, amount, privateKeyFrom):
    gas_limit = 250000
    gas_price = 60

    transaction = {
        'to': addressTo,
        'from': addressFrom,
        'value': w3.toWei(amount,'ether'),
        'gas': gas_limit,
        'gasPrice': int(gas_price*(10**9)),
        'nonce': w3.eth.getTransactionCount(addressFrom)
    }

    signed_transaction = w3.eth.account.signTransaction(transaction, privateKeyFrom)
    transaction_id = w3.eth.sendRawTransaction(signed_transaction.rawTransaction)

    print ('\nhttps://etherscan.io/tx/{0}'.format(transaction_id.hex()))

def getAccountBalance(address):
    url = "https://api-ropsten.etherscan.io/api?module=account&action=balance&address=" + str(address) + "&tag=latest&apikey=YourApiKeyToken"

    r = requests.get(url)
    r = r.json()

    return r

acct1 = generateAddressAndKeys()
print("acct1 key", acct1.privateKey)
print("acct1 address", acct1.address)

acct2 = generateAddressAndKeys()
print("acct2 key", acct2.privateKey)
print("acct2 address", acct2.address)

hardcodedAddress1 = "0xf5a84671Ec697d43e760A92ffD777071103Ae32B"
hardcodedKey1 = b'aC\x8dC\xa1#8\t\xd8\x9a\x00G\xd6e\xbcr\xfd\xbd\x80\xc2\xcd/\x81f\x82r\xb5\xc0\xd8u\xf4q'

hardcodedAddress2 = "0x0A79B282B7fB14931986bD955201e542b989d8F7"
hardcodedKey2 = b'\xb8\xf5\xef#Xz\x07\xb6fCW|\xc2P\xa3Z\x9a\xf7H\x8aN\xed\xdb\x1a\xd9\xe8\x8c\xdf\xfe\xb8\xfb\x17'

acct1Balance = getAccountBalance(hardcodedAddress1)
acct2Balance = getAccountBalance(hardcodedAddress2)

print("acct1Balance", acct1Balance)
print("acct2Balance", acct2Balance)


# uncomment to send coins
# sendCoins(hardcodedAddress1)

# res = sendCoins(hardcodedAddress1, hardcodedAddress2, 0.1, hardcodedKey1)
# print("res", res)
