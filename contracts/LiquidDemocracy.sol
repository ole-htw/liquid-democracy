// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

enum Vote{ FOR, AGAINST, NEUTRAL }
enum Domain{EDUCATION, ECOLOGY, ECONOMY }

struct SubmittedVote {
    address voter;
    uint proposalID;
    Vote vote;
}

struct Proposal {
    uint id; 
    Domain domain;
    string description; 
}

contract LiquidDemocracy {
    Proposal[] proposals;
    mapping(uint => mapping(address => Vote)) submittedVotes;
    mapping(address => mapping(Domain => address)) delegations;

    function propose(Domain domain, string memory description) public payable {
        proposals.push(Proposal(
            proposals.length,
            domain,
            description
        ));
    }

    function vote(uint proposalID, Vote value) public payable {
        submittedVotes[proposalID][msg.sender] = value;
    }

    function delegate(Domain domain, address to) public payable {
        delegations[msg.sender][domain] = to;
    }
}