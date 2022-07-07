# Client

Wallet erstellen

```bash
export PRIVATE_KEY=0x`openssl rand -hex 32`
```

Lokale Node ins Testnetzwerk starten:

```bash
geth --http --http.corsdomain="https://remix.ethereum.org" --http.api web3,eth,debug,personal,net --vmdebug --datadir data --dev console
```

Deploy

```bash
truffle migrate --network ganache
```
