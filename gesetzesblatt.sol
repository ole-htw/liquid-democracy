pragma solidity ^0.8.0;


// hier Überprüfung für Wahlverzeichnis einbauen


    contract gesetzesblatt {
        struct Gesetz {
            string name;
            string beschreibung;
        }

        Gesetz[] public gueltige_gesetze;

        function add_gesetz (string memory neues_gesetz_name, string memory neues_gesetz_beschreibung) public {
            Gesetz memory neues_gesetz = Gesetz(neues_gesetz_name, neues_gesetz_beschreibung);
            gueltige_gesetze.push(neues_gesetz);
        }
    }
