pragma solidity ^0.8.0;


import "./urne.sol";

contract wahlorga {
    struct Gesetzesvorschlag {
        string name;
        string beschreibung;
        uint32 id;
        uint time;
        address urne_ja;
        address urne_nein;
    }

    mapping(address => bool) public waehlerverzeichnis;

    uint32 public letzte_gesetzes_id = 1;
    //Gesetzesvorschlag[] aktuelle_gvs; // nach Zeit geordnet


    function registieren() public {
        waehlerverzeichnis[msg.sender] = true;
    }

    function neuerGesetzesvorschlag(string memory name, string memory beschreibung) public {
        require(waehlerverzeichnis[msg.sender]);

        // urne erstellen
        Urne ja_urne = new Urne(name, beschreibung, true, letzte_gesetzes_id);
        Urne nein_urne = new Urne(name, beschreibung, false, letzte_gesetzes_id);


        // Gesetzesvorschlag neuerGV = Gesetzesvorschlag(name, beschreibung, letzte_gesetzes_id, now, ja_urne.get_address(), nein_urne.get_address());

        //aktuelle_gvs.push(neuerGV);
        letzte_gesetzes_id++;// = letzte_gesetzes_id + 1;

        // token erstellt werden
        // zwei urnen erstellen


    }

}