// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./Urne.sol";
import "./WahlToken.sol";


contract WahlOrga {
    struct Gesetzesvorschlag {
        string name;
        string beschreibung;
        uint32 id;
        uint time;
        address urne_ja;
        address urne_nein;
    }


    mapping(address => bool) public map_waehlerverzeichnis;
    address[] list_waehlerverzeichnis;

    uint32 public letzte_gesetzes_id = 1;
    Gesetzesvorschlag[] public aktuelle_gvs; // nach Zeit geordnet

    WahlToken public wahltokens = new WahlToken();
    mapping (uint256 => uint32) public token_2_gesetz_id;
    mapping (uint256 => bool) public ist_token_noch_aktiv;
    
    
    struct _owner_gesetz {
        address owner;
        uint32 gesetz_id;
    }
    
    
    mapping (address => mapping(uint32 => uint256)) public owner_gesetz_2_token_id;


    function registieren() public {
        map_waehlerverzeichnis[msg.sender] = true;
        list_waehlerverzeichnis.push(msg.sender);
    }

    function neuerGesetzesvorschlag(string memory name, string memory beschreibung) public payable{
        require(map_waehlerverzeichnis[msg.sender]);

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

        // token erstellt werden

        uint arrayLength = list_waehlerverzeichnis.length;
        for (uint i=0; i<arrayLength; i++) {
            uint256 token_id = wahltokens.safeMint(list_waehlerverzeichnis[i]);
            //uint256 token_id = uint256(uint160(list_waehlerverzeichnis[i]));
            token_2_gesetz_id[token_id] = letzte_gesetzes_id;
            ist_token_noch_aktiv[token_id] = true;

            //_owner_gesetz owner_gesetz = _owner_gesetz(list_waehlerverzeichnis[i], letzte_gesetzes_id);
            owner_gesetz_2_token_id[list_waehlerverzeichnis[i]][letzte_gesetzes_id] = token_id;
        }

        letzte_gesetzes_id++;

    }


    function deactivate_old_wahltoken (uint32 gesetz_id) public {
        //_owner_gesetz alte_owner_gesetz = _owner_gesetz(msg.sender, gesetz_id);
        uint256 alte_token_id = owner_gesetz_2_token_id[msg.sender][gesetz_id];

        ist_token_noch_aktiv[alte_token_id] = false;

        uint256 token_id = wahltokens.safeMint(msg.sender);
        token_2_gesetz_id[token_id] = gesetz_id;
        ist_token_noch_aktiv[token_id] = true;

        //_owner_gesetz neue_owner_gesetz = _owner_gesetz(msg.sender, gesetz_id);
        owner_gesetz_2_token_id[msg.sender][gesetz_id] = token_id;
    }

    function Wahltokens_ownerOf(uint256 tokenId) public returns (address owner){
        return wahltokens.ownerOf(tokenId);
    }

    function Wahltokens_transferFrom(address from, address to, uint256 tokenId) public {
        wahltokens.safeTransferFrom(from, to, tokenId);
    }



}