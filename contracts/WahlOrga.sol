// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./Urne.sol";

contract WahlOrga {
    struct Gesetzesvorschlag {
        string name;
        string beschreibung;
        uint32 id;
        uint time;
        address urne_ja;
        address urne_nein;
    }

    /**
    DISKUSSION: Ich schlage vor daraus ein address[] zu machen. Ich verstehe die Vorteile einer Hashtable, aber wir brauchen ein Iterable.
    Eventuell können wir auch eine zweite State Variable machen, siehe  https://medium.com/@blockchain101/looping-in-solidity-32c621e05c22.
     */
    mapping(address => bool) public waehlerverzeichnis;

    uint32 public letzte_gesetzes_id = 1;
    Gesetzesvorschlag[] public aktuelle_gvs; // nach Zeit geordnet


    function registieren() public {
        waehlerverzeichnis[msg.sender] = true;
    }

    function neuerGesetzesvorschlag(string memory name, string memory beschreibung) public {
        require(waehlerverzeichnis[msg.sender]);

        // urne erstellen
        Urne ja_urne = new Urne(name, beschreibung, true, letzte_gesetzes_id);
        Urne nein_urne = new Urne(name, beschreibung, false, letzte_gesetzes_id);

        Gesetzesvorschlag memory neuerGV = Gesetzesvorschlag(name, 
                                                    beschreibung, 
                                                    letzte_gesetzes_id, 
                                                    block.timestamp, 
                                                    address(ja_urne), 
                                                    address(nein_urne));

        aktuelle_gvs.push(neuerGV);
        letzte_gesetzes_id++;

        // token erstellt werden

    }

}