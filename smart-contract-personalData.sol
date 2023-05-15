pragma solidity ^0.8.0;

contract PersonalData {

    struct UserData {
        uint dataID;
        string name;
        string email;
        string phone;
        uint paymentAmount;
        bool isApproved;
    }

    mapping(uint => UserData) private userData;

    uint public dataCount = 0;

    function addUserData(string memory _name, string memory _email, string memory _phone) public payable {
        require(msg.value >= 1 ether, "Insufficient payment amount");
        dataCount++;
        userData[dataCount] = UserData(dataCount, _name, _email, _phone, msg.value, false);
    }

    function approveUserData(uint _dataID) public {
        require(msg.sender == owner, "Only owner can approve user data");
        userData[_dataID].isApproved = true;
    }

    function getUserData(uint _dataID) public view returns (string memory, string memory, string memory, uint, bool) {
        UserData memory user = userData[_dataID];
        return (user.name, user.email, user.phone, user.paymentAmount, user.isApproved);
    }

}
