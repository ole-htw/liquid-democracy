from web3 import Web3
from web3.contract import ContractConstructor
import os
from eth_account.signers.local import LocalAccount
from .enums import Domain, Vote

class ContractInterface:
    def __init__(self, w3: Web3, account: LocalAccount, abi):
        self.w3 = w3
        self.account = account
        self.abi = abi
        self.contract = w3.eth.contract(address=os.getenv('CONTRACT_ADDR'), abi=self.abi)

    def __build_sign_and_send(self, tx: ContractConstructor):
        tx = tx.buildTransaction({
            'from': self.account.address,
            'nonce': self.w3.eth.get_transaction_count(self.account.address),
            'gasPrice': self.w3.eth.gas_price,
        })
        tx_create = self.w3.eth.account.sign_transaction(tx, self.account.privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(tx_create.rawTransaction)
        tx_receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
        return tx_receipt

    def propose(self, domain: Domain, description: str):
        return self.__build_sign_and_send(self.contract.functions.propose(domain.value, description))
    
    def vote(self, proposalID: int, vote: Vote):
        return self.__build_sign_and_send(self.contract.functions.vote(proposalID, vote.value))

    def delegate(self, domain: Domain, address: str):
        return self.__build_sign_and_send(self.contract.functions.delegate(domain.value, address))

    def votes(self, billID: int):
        return self.contract.functions.votes(billID).call()

    def getDelegation(self, domain: Domain):
        return self.contract.functions.getDelegation(domain.value).call()

    def getBills(self):
        return self.contract.functions.getBills().call()
