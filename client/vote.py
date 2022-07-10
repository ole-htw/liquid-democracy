from calendar import c
from web3 import Web3, EthereumTesterProvider
import os
from eth_account import Account
from eth_account.signers.local import LocalAccount
from web3.auto import w3
from web3.middleware import construct_sign_and_send_raw_middleware
import json

def vote(w3: w3, account: LocalAccount):
    abi = None
    with open('../build/contracts/WahlToken.json', 'r') as f:
        abi = json.loads(f.read())

    contract = w3.eth.contract(address='0x6E25D2c91742aC37D8a50531B4aEAC98De85f70b',  abi=abi['abi'])
    mint_txn = contract.functions.transferFrom(account.address, '0x4EbCC2D57bbB944672BfF034498Fed618CBd0535', 1).buildTransaction({
        'from': account.address,
        'nonce': w3.eth.get_transaction_count(account.address),
        'gasPrice': w3.eth.gas_price
    })
    signed_txn = w3.eth.account.sign_transaction(mint_txn, 
    private_key=account.privateKey)
    return w3.eth.send_raw_transaction(signed_txn.rawTransaction)
