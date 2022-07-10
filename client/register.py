from calendar import c
from web3 import Web3, EthereumTesterProvider
import os
from eth_account import Account
from eth_account.signers.local import LocalAccount
from web3.middleware import construct_sign_and_send_raw_middleware
import json

def register(w3, account: LocalAccount):
    abi = None
    with open('../build/contracts/WahlOrga.json', 'r') as f:
        abi = json.loads(f.read())

    contract = w3.eth.contract(address=os.getenv('WAHLORGA_ADDR'), abi=abi['abi'])
    print(w3.eth.gas_price)
    tx = contract.functions.registrieren().buildTransaction({
        'from': account.address,
        'nonce': w3.eth.get_transaction_count(account.address),
        'gasPrice': 20908031321
    })
    tx_create = w3.eth.account.sign_transaction(tx, account.privateKey)
    tx_hash = w3.eth.send_raw_transaction(tx_create.rawTransaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return tx_receipt