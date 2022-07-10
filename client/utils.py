import os
from eth_account import Account
from eth_account.signers.local import LocalAccount

def get_account() -> LocalAccount:
    private_key = os.environ.get("PRIVATE_KEY")
    assert private_key is not None, "You must set PRIVATE_KEY environment variable"
    assert private_key.startswith("0x"), "Private key must start with 0x hex prefix"
    account: LocalAccount = Account.from_key(private_key)
    return account
