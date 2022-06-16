// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// hier Überprüfung für Wahlverzeichnis einbauen


contract Gesetzblatt {
    struct Gesetz {
        string name;
        string beschreibung;
    }

    // Gültige, beschlossene Gesetze
    Gesetz[] public gesetze;

    function add_gesetz (string memory neues_gesetz_name, string memory neues_gesetz_beschreibung) public {
        Gesetz memory neues_gesetz = Gesetz(neues_gesetz_name, neues_gesetz_beschreibung);
        gesetze.push(neues_gesetz);
    }
}
