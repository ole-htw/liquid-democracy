from calendar import c
from web3 import Web3, EthereumTesterProvider
import os
from eth_account import Account
from eth_account.signers.local import LocalAccount
import json

def propose(w3, account: LocalAccount, description: str):
    abi = None
    with open('../build/contracts/LiquidDemocracy.json', 'r') as f:
        abi = json.loads(f.read())

    contract = w3.eth.contract(address='0x77088CE7A28b8c412c6fDD97865E7F54e8412053', abi=abi['abi'])
    tx = contract.functions.register().buildTransaction({
        'from': account.address,
        'nonce': w3.eth.get_transaction_count(account.address),
        'gasPrice': w3.eth.gas_price,
    })
    tx_create = w3.eth.account.sign_transaction(tx, account.privateKey)
    tx_hash = w3.eth.send_raw_transaction(tx_create.rawTransaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return tx_receipt