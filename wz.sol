

contract wahlorga {
    struct Gesetzesvorschlag {
        string beschreibung;
        string name;
        uint32 id;
        time time;
        adress urne_ja;
        adress urne_nein;
    }

    adress[] waehlerverzeichnis;

    uint32 letzte_gesetzes_id = 1;
    Gesetzesvorschlag[] aktuelle_gvs; \\ nach Zeit geordnet



    function registieren() {
        waehlerverzeichnis.push(msg.sender);
    }

    function neuerGesetzesvorschlag(string same, 
                                    string beschreibung,
                                    ) {
        if msg.sender not in waehlerverzeichnis {
            break;
        }

        Gesetzesvorschlag neuerGV = {
            name = name,
            beschreibung = beschreibung,
            id = letzte_gesetzes_id,
            time = jetzt
        };

        aktuelle_gvs.push(neuerGV);
        letzte_gesetzes_id = letzte_gesetzes_id + 1;

        \\ token erstellt werden
        \\ zwei urnen erstellen


    }

}




