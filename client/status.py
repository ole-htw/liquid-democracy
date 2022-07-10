from calendar import c
from web3 import Web3, EthereumTesterProvider
import os
from eth_account import Account
from eth_account.signers.local import LocalAccount
from web3.auto import w3
from web3.middleware import construct_sign_and_send_raw_middleware
import json

def status(w3: w3, account: LocalAccount):
    abi = None
    with open('../build/contracts/WahlToken.json', 'r') as f:
        abi = json.loads(f.read())

    contract = w3.eth.contract(address='0x6E25D2c91742aC37D8a50531B4aEAC98De85f70b',  abi=abi['abi'])
    token_balance = contract.functions.ownerOf(2).call()
    return token_balance