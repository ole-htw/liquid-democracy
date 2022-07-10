# Liquid Democracy

Dies ist ein Studentenprojekt, welches im Rahmen der Vorlesung _"Blockchain Technologies"_ entstanden ist.


## Einleitung

In einer Demokratie hat jede\*r Wahlberechtigte\*r eine Stimme pro Abstimmung. Oft ist es jedoch
so, dass Wahlberechtigte nicht über genug Zeit, Energie oder Know-How verfügen, um guten
Gewissens an einer Abstimmung teilnehmen zu können. Daher konnte sich die repräsentative
Demokratie durchsetzen, in der die Wahlberechtigten ihre Stimme an eine Person abgeben, die sich
ausschließlich mit Abstimmen beschäftigt. Dieses System löst viele Probleme, bringt jedoch auch
eine gewisse Starrheit mit sich, da die Stimme über den gesamten Zeitraum nicht zurückgeholt
oder anderweitig verwendet werden kann. Mit den Möglichkeiten moderner Datenverarbeitung
bieten sich hier flexiblere Modelle an. Liquid Democracy beschreibt einen Demokratieprozess, in
dem der/die Wahlberechtigte für jede Abstimmung neu entscheiden kann, ob die eigene Stimme
selbst abgegeben oder weiter delegiert werden soll.


## Implementierungsstrategie

Eine Alternative zum Token-Modell, die wir diskutiert haben,
ist es die logischen Funktionen und Delegationen durch Methodenaufrufe und State innerhalb des Smart Contracts zu lösen.

Hierzu könnten Gesetzesentwürfe durch eine Funktion `propose(Domain domain, string description) public returns (Proposal)`
eingereicht werden und damit zu einem Array hinzugefügt werden.

Nutzer könnten über eine Methode
`vote(uint proposalID, Vote vote)}`
für oder gegen einen Gesetzesentwurf abstimmen. Die Votes aller Adressen auf ein Proposal würden in einer Datenstruktur festgehalten.

Weiterhin könnten Nutzer ihre Stimme (auch Wahlbereich-spezifisch) an andere Adressen delegieren bzw. wieder abziehen.
Sie wären dann nicht mehr selbst dazu in der Lage für Gesetzesentwürfe in dem jeweiligen Bereich abzustimmen.
Die Delegationen könnten in einer Datenstruktur der Form `mapping(address => mapping(Domain => address))` festgehalten werden.

Abschließend, z.B. zu einer Deadline hin,
würde ein Algorithmus die Stimmen, die ein Gesetzesentwurf erhalten hat, zählen.
Hierbei würde rekursiv ein Lookup auf die Datenstruktur der Delegierungen erfolgen um die akkumulierte Gewichtung einer Stimme zu berechnen.

<hr>

## Installation

1. Abhängigkeiten installieren

```bash
npm install truffle -g
npm install
pip3 install -r client/requirements.txt
```

2. Smart Contract deployen

Netzwerke können in der [truffle-config.js](./truffle-config.js) konfiguriert werden.
Der folgende Befehle wählt beispielhaft Ganache.

```bash
truffle migrate --network ganache
```

3. Umgebungsvariablen setzen

Die Ausgabe des vorherigen Befehls enthält eine _Contract Address_. Diese muss als `CONTRACT_ADDR` gesetzt werden.

```bash
export CONTRACT_ADDR=0x.....
```

Außerdem braucht der Client ein Wallet, d.h. einen Private Key.
Der folgende Befehl generiert einen neuen und exportiert ihn gleichzeitig in die Umgebungsvariablen.

```bash
export PRIVATE_KEY=0x`openssl rand -hex 32`
```

Jetzt muss noch der Endpunkt zu einer laufenden Node gesetzt werden. Für eine Verbindung mit Ganache kann es wie folgt aussehen:

```bash
export ENDPOINT=http://127.0.0.1:7545
```

4. Bedienung

```bash
python3 -m client --help
```

### Beispielhafte Bedienung

Die folgende Befehlreihe macht einen Gesetzesvorschlag _"Hauptschule abschaffen"_ in der Domäne _"EDUCATION"_.
Anschließend stimmt er für diesen Vorschlag und delegiert Abstimmungen im Bereich _"ECOLOGY"_ an ein externes Wallet.
Schließlich wird der Status abgerufen, wo sich gesetzte Daten widerspiegeln.

```bash
python3 -m client propose --domain EDUCATION --description "Hauptschule abschaffen"
python3 -m client vote --id 0 --value FOR
python3 -m client delegate --domain ECOLOGY --address=0x3b2b3C2e2E7C93db335E69D827F3CC4bC2A2A2cB
python3 -m client status
```

**Status-Ausgabe**

```
Gesetze
======================
ID: 0 | ECONOMY | Anarchie | -1
ID: 1 | EDUCATION | Hauptschule abschaffen | 1

Delegierungen
======================
ECOLOGY 0x0000000000000000000000000000000000000000
ECONOMY 0x0000000000000000000000000000000000000000
EDUCATION 0x0000000000000000000000000000000000000000
```