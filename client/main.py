from web3 import Web3, EthereumTesterProvider
import os
from eth_account import Account
from eth_account.signers.local import LocalAccount
from web3.auto import w3
from web3.middleware import construct_sign_and_send_raw_middleware
import json
import argparse
from vote import vote
from status import status
from propose import propose
from utils import get_account
from register import register

def main(args):
    w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))
    account: LocalAccount = get_account()
    print(f"Is connected? {w3.isConnected()}")
    print(f"Your hot wallet address is {account.address}")
    w3.middleware_onion.add(construct_sign_and_send_raw_middleware(account))
    if not w3.isConnected():
        print("connection failed")
        raise SystemExit

    if args.action == 'register':
        try:
            erg = register(w3, account)
            print("Sie haben sich erfoglreich registriert.")
            print(erg)
        except:
            print("Die Registrierung ist leider fehlgeschlagen.")
    elif args.action == 'propose':
        try:
            erg = propose(w3, account, args.description)
            print("Ihr Gesetzesvorschlag wurde eingereicht. Vielen Dank.")
            print(erg)
        except:
            print("Leider gab es einen Fehler. Ihr Gesetzesvorschlag wurde nicht eingereicht. Bitte versuchen Sie es erneut.")
    elif args.action == 'status':
        try:
            erg = status(w3, account)
            print(erg)
        except:
            print("Leider gab es einen Fehler. Der Status kann derzeit nicht angezeigt werden.")
    elif args.action == 'vote':
        try:
            erg = vote(w3, account)
            print("Ihre Stimmabgabe war erfolgreich.")
            print(erg)
        except:
            print('Leider ist die Stimmabgabe fehlgeschlagen. Bitte überprüfen Sie ihre Eingabe.')
    elif args.action == 'delegate':
        pass
    else:
        print('Kommando nicht erkannt.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Client CLI to interact with the Liquid Democracy system.')

    sub_parsers = parser.add_subparsers(help='Aktionen', dest='action')

    parser_register = sub_parsers.add_parser('register', help='Registriere dich ins Wählerverzeichnis')
    
    parser_delegate = sub_parsers.add_parser('propose', help='Reiche einen neuen Gesetzesvorschlag ein')
    parser_delegate.add_argument('--description', type=str, help='Beschreibung des Gesetzes')
    
    parser_delegate = sub_parsers.add_parser('status', help='Statusabfrage')
    
    parser_delegate = sub_parsers.add_parser('vote', help='Stimme für oder gegen einen Gesetzesvorschlag')
    parser_delegate.add_argument('--id', type=int, help='Gesetzesvorschlag ID')
    parser_delegate.add_argument('--value', type=bool, help='True = Stimme dafür; False = Stimme dagegen')
    
    parser_delegate = sub_parsers.add_parser('delegate', help='Delegiere dein Stimmrecht an eine andere Entität')
    parser_delegate.add_argument('--address', type=str, help='Adresse des Delegierten')

    args = parser.parse_args()

    main(args)
