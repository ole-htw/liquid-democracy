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


## Smart Contract Logik

Die Wahlberechtigten werden mit ihrer Adresse in einem Array, dem Wählerverzeichnis, gespeichert. Falls ein Gesetzesvorschlag auftaucht, bekommt jede Adresse aus dem Wählerverzeichnis
einen Coin oder Token, der spezifisch für den Gesetzesvorschlag ist. Um zu verhindern, dass man
aus früheren Gesetzesvorschlägen Tokens oder Coins sammelt, haben wir mehrere Lösungen diskutiert: Eine Lösung ist es, dass mit dem Gesetzesvorschlag eine Coin generiert wird, die nur für den
speziellen Gesetzesvorschlag gültig ist. Oder wir erstellen immer ein NFT mit einer ID, die auf
den speziellen Gesetzesvorschlag verweist.

Der Gesetzesvorschlag zählt nur nach einer Deadline, wieviel Coins oder Tokens zu zwei Adressen
verschickt worden sind (”Ja-Adresse” und ”Nein-Adresse”).

Wenn es mehr Tokens oder Coins auf der ”Ja-Adresse” gibt, gilt der Gesetzesvorschlag als
angenommen, sonst abgelehnt. Er landet auf einer Liste an angenommenen Gesetzesvorschlägen
(sogenanntes ”Bundesgesetzblatt”).

Der Vorteil dieser Lösung ist es, dass implizit die Liquid Democracy gegeben ist. Ein Wähler
kann seine Stimme delegieren, indem er seine Stimme an eine andere Adresse sendet.


## Steuerung durch Client

Der Client kann den Wahl-spezifischen Token ausgeben und damit entweder
- seine Stimme für den Gesetzesvorschlag abgeben,
- seine Stimme gegen den Gesetzesvorschlag abgeben oder
- seine Stimme an eine andere Adresse (Person oder Organisation) delegieren.
Durch client-seitige Automatisierung kann erreicht werden, dass Wählerstimmen, etwa auch zu
bestimmten Wahlbereichen, an andere Entitäten delegiert werden.
Aufgrund der offenen Ethereum-API können individuelle Clients verwendet werden. Dies
ermöglicht Nicht-Blockchain-Experten die Benutzung durch selbstgewählte Clients. Diese Clients
können auch intelligent agieren, indem sie z.B. Gesetze aus bestimmten Themengebieten automatisch an andere Adressen weiterleiten.

<hr>

## Installation

```bash
npm install truffle -g
npm install
```
