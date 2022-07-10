from web3 import Web3
from web3.middleware import construct_sign_and_send_raw_middleware
import json
import os
import argparse
from .enums import Domain, Vote
from .contract import ContractInterface
from .utils import get_account

def main(args):
    abi = None
    with open('./build/contracts/LiquidDemocracy.json', 'r') as f: abi = json.loads(f.read())['abi']
    w3 = Web3(Web3.HTTPProvider(os.getenv('ENDPOINT')))
    account = get_account()
    w3.middleware_onion.add(construct_sign_and_send_raw_middleware(account))
    if not w3.isConnected():
        print("Verbindung fehlgeschlagen.")
        raise SystemExit

    ci = ContractInterface(w3, account, abi)

    res = ""
    try:
        if args.action == 'propose':
            res = ci.propose(Domain.from_string(args.domain), args.description)
            print("Ihr Gesetzesvorschlag wurde eingereicht. Vielen Dank.")
            if args.debug: print(res)
        elif args.action == 'vote':
            res = ci.vote(args.id, Vote.from_string(args.value))
            print("Ihre Stimmabgabe war erfolgreich.")
            if args.debug: print(res)
        elif args.action == 'delegate':
            res = ci.delegate(Domain.from_string(args.domain), args.address)
            print("Ihre Stimme wurde delegiert.")
        elif args.action == 'reset-delegate':
            res = ci.delegate(Domain.from_string(args.domain), '0x0000000000000000000000000000000000000000')
            print("Ihre Stimme ist fortan nicht mehr delegiert.")
            if args.debug: print(res)
        elif args.action == 'status':
            print("Gesetze\n======================")
            for id, domain, description in ci.getBills():
                votes = ci.votes(id)
                print(f'ID: {id} | {Domain(domain).to_string()} | {description} | {votes}')
            print("\nDelegierungen\n======================")
            for domain in Domain.all():
                res = ci.getDelegation(domain)
                print(domain.to_string(), res)
        else:
            print('Kommando nicht erkannt.')
    except Exception as e:
        print('Es ist ein Fehler aufgetreten.')
        print(res, e)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Client CLI to interact with the Liquid Democracy system.')
    parser.add_argument('--debug', type=bool, help='Aktivieren für mehr Logging')
    sub_parsers = parser.add_subparsers(help='Aktionen', dest='action')
    # propose
    p = sub_parsers.add_parser('propose', help='Reiche einen neuen Gesetzesvorschlag ein')
    p.add_argument('--description', type=str, help='Beschreibung des Gesetzes')
    p.add_argument('--domain', choices=Domain.choices())
    # status
    sub_parsers.add_parser('status', help='Statusabfrage')
    # vote
    p = sub_parsers.add_parser('vote', help='Stimme für bzw. gegen einen Gesetzesvorschlag')
    p.add_argument('--id', type=int, help='Gesetzesvorschlag ID')
    p.add_argument('--value', choices=Vote.choices())
    # delegate
    p = sub_parsers.add_parser('delegate', help='Delegiere dein Stimmrecht an eine andere Entität')
    p.add_argument('--domain', choices=Domain.choices(), help='Politische Domäne für die delegiert werden soll')
    p.add_argument('--address', type=str, help='Adresse des Delegierten')
    # reset-delegate
    p = sub_parsers.add_parser('reset-delegate', help='Setze eine Delegation zurück')
    p.add_argument('--domain', choices=Domain.choices(), help='Domäne für welche die Delegation zurückgesetzt werden soll')

    args = parser.parse_args()
    main(args)
