pragma solidity ^0.8.15;

contract Logic {
    bool[40] public boolArray; // Storage slot 0x0 (collides with Proxy's visits)
    address public admin; // Storage slot 0x0 (collides with Proxy's visits)
    uint[] artworkIDs; // Storage slot 0x1
    mapping(uint => address) artworkHolders; // Storage slot 0x2


    address testAddr = 0xB989a9F9E42be50dF74afe4687dA5FfdbC1f3d63;


    event Log(string message, uint value);
    event Log2(string message, string value);
    event Log3(string message, bool value);
    event Log4(string message, address value);



    function initialize() public {
        boolArray[0] = true;
        boolArray[1] = true;
        boolArray[4] = true;
        boolArray[20] = true;
        
    }
    

    function withdraw() external {
        require(msg.sender == admin, "Not authorized");
        payable(admin).transfer(address(this).balance);
    }

    function get_admin() public {
        emit Log4("ini++ ", admin);
        emit Log4("ini++ ", testAddr);
    }

    function check_access() public {
        emit Log4("address ", testAddr);
        for (uint i = 0; i < 40; i++) {
            if (boolArray[i] == true) {
                emit Log2("check passed ", " ");
            } else {
                emit Log2("check failed ", " ");
            }
        }
    }

     function getStorageSlot() public view returns (uint256) {
        bytes32 slot;
        assembly {
            slot := sload(boolArray.slot)
        }
        return uint256(slot);
    }
}


