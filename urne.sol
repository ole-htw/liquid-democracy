pragma solidity ^0.8.0;




contract urne {
    string gesetz_name;
    string gesetz_beschreibung;
    bool ist_ja_urne;
    uint32 gesetz_id;

    constructor(string memory _gesetz_name, string memory _gesetz_beschreibung, bool _ist_ja_urne, uint32 _gesetz_id) public {
        gesetz_name = _gesetz_name;
        gesetz_beschreibung = _gesetz_beschreibung;
        ist_ja_urne = _ist_ja_urne;
        gesetz_id = _gesetz_id;
    }

}