// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

enum Vote{ FOR, AGAINST, NEUTRAL }
enum Domain{ EDUCATION, ECOLOGY, ECONOMY }

struct SubmittedVote {
    address voter;
    uint billID;
    Vote vote;
}

struct Bill {
    uint id;
    Domain domain;
    string description; 
}

contract LiquidDemocracy {
    Bill[] bills;
    mapping(uint => Vote[]) billVotes; // billID => votes
    mapping(uint => mapping(address => Vote)) submittedVotes; // billID => voter => value
    mapping(address => mapping(Domain => address)) delegations; // who delegates what to who
    mapping(address => mapping(Domain => address[])) delegators;  // who was delegated for what by whom

    function propose(Domain domain, string memory description) public payable {
        bills.push(Bill(
            bills.length,
            domain,
            description
        ));
    }

    function vote(uint billID, Vote value) public payable {
        require(billID < bills.length, "Bill ID does not exist.");
        Domain domain = bills[billID].domain;
        require(
            delegations[msg.sender][domain] == address(0), 
            "You have delegated votes in this domain."
        );

        submittedVotes[billID][msg.sender] = value;
        billVotes[billID].push(value);

        // add delegated votes as well
        for (uint i = 0; i < delegators[msg.sender][domain].length; i++) {
            address voter = delegators[msg.sender][domain][i];
            submittedVotes[billID][voter] = value;
            billVotes[billID].push(value);
        }
    }

    function delegate(Domain domain, address to) public payable {
        delegations[msg.sender][domain] = to;
        delegators[to][domain].push(msg.sender);
    }

    function votes(uint billID) public view returns(int result) {
        Vote[] memory v = billVotes[billID];
        for (uint i = 0; i < v.length; i++) {
            if (v[i] == Vote.FOR) {
                result++;
            }
            if (v[i] == Vote.AGAINST) {
                result--;
            }
        }
        return result;
    }

    function getDelegation(Domain domain) public view returns (address) {
        return delegations[msg.sender][domain];
    }

    function getBills() public view returns (Bill[] memory) {
        return bills;
    }
}