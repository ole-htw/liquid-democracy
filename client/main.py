from web3 import Web3, EthereumTesterProvider
import os
from eth_account import Account
from eth_account.signers.local import LocalAccount
from web3.auto import w3
from web3.middleware import construct_sign_and_send_raw_middleware
import json

abi = None
with open('../build/contracts/WahlOrga.json', 'r') as f:
    abi = json.loads(f.read())

private_key = os.environ.get("PRIVATE_KEY")
assert private_key is not None, "You must set PRIVATE_KEY environment variable"
assert private_key.startswith("0x"), "Private key must start with 0x hex prefix"

account: LocalAccount = Account.from_key(private_key)
w3.middleware_onion.add(construct_sign_and_send_raw_middleware(account))

print(f"Your hot wallet address is {account.address}")

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))
if not w3.isConnected():
    print("connection failed")
    raise SystemExit

contract = w3.eth.contract(address='0x9403c262441f5D675BAd652d5aEc51506e6B8138', abi=abi['abi'])
tx = contract.functions.registrieren().buildTransaction(
    {
        'from': account.address,
        'nonce': w3.eth.get_transaction_count(account.address),
        'gasPrice': w3.eth.gas_price
    }
)
tx_create = w3.eth.account.sign_transaction(tx, private_key)
tx_hash = w3.eth.send_raw_transaction(tx_create.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

print(f'Tx successful with hash: { tx_receipt.transactionHash.hex() }')

balance = w3.eth.get_balance(account.address)
print(balance)
