pragma solidity ^0.8.0;

contract PersonalDataProtection {
    mapping (address => bool) private approved;

    function requestApproval() public {
        approved[msg.sender] = true;
    }

    function getApprovalStatus(address user) public view returns (bool) {
        return approved[user];
    }
}
