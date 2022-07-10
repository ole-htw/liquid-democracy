// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

enum Vote{ FOR, AGAINST, NEUTRAL }
enum Domain{ EDUCATION, ECOLOGY, ECONOMY }

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
    mapping(uint => Vote[]) proposalVotes; // proposalID => votes
    mapping(uint => mapping(address => Vote)) submittedVotes; // proposalID => voter => value
    mapping(address => mapping(Domain => address)) delegations; // who delegates what to who
    mapping(address => mapping(Domain => address[])) delegators;  // who was delegated for what by whom

    function propose(Domain domain, string memory description) public payable {
        proposals.push(Proposal(
            proposals.length,
            domain,
            description
        ));
    }

    function vote(uint proposalID, Vote value) public payable {
        require(proposalID < proposals.length, "Proposal ID does not exist.");
        Domain domain = proposals[proposalID].domain;
        require(
            delegations[msg.sender][domain] == address(0), 
            "You have delegated votes in this domain."
        );

        submittedVotes[proposalID][msg.sender] = value;
        proposalVotes[proposalID].push(value);

        // add delegated votes as well
        for (uint i = 0; i < delegators[msg.sender][domain].length; i++) {
            address voter = delegators[msg.sender][domain][i];
            submittedVotes[proposalID][voter] = value;
            proposalVotes[proposalID].push(value);
        }
    }

    function delegate(Domain domain, address to) public payable {
        delegations[msg.sender][domain] = to;
        delegators[to][domain].push(msg.sender);
    }

    function status(uint proposalID) public payable returns(int) {
        int result = 0;
        Vote[] memory votes = proposalVotes[proposalID];
        for (uint i = 0; i < votes.length; i++) {
            if (votes[i] == Vote.FOR) {
                result++;
            }
            if (votes[i] == Vote.AGAINST) {
                result--;
            }
        }
        return result;
    }
}