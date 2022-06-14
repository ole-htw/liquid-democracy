pragma solidity ^0.8;


// hier Überprüfung für Wahlverzeichnis einbauen


contract gesetzesblatt {
    string[] gueltige_gesetze;

    function add_gesetz (string neues_gesetz) {
        gueltige_gesetze.push(neues_gesetz);
    }
}
