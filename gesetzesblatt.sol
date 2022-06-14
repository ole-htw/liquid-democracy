pragma solidity ^0.8.0;


// hier Überprüfung für Wahlverzeichnis einbauen


    contract gesetzesblatt {
        string[] public gueltige_gesetze;

        function add_gesetz (string memory neues_gesetz) public {
            gueltige_gesetze.push(neues_gesetz);
        }
    }
