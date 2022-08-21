# Fund Me Solidity Contract using Brownie
 A solidity contract where users can fund an address and that address can withdraw those funds and it keeps a track of all the funders.
 
 This project is compiled and deployed using a python. A python frameworks based on web3.py called **Brownie** is used to deploy and test this contract.
 The contract is deployed to different networks to test its working. The networks I used include
 - Local Ganache Instance
 - Rinkeby Testnet
 - Mainnet Fork

# Folders
The repo consists of the following folders:
- contracts
  - This folder consists of the FundMe.sol smart contract and a MockAggregator.sol file that is used in testing.
- scripts 
  - All of the python scripts including the deploy script and interaction scripts are contained in this folder.
- test
  - The scripts that are used to test the contract on Local RPC Client are contained in this folder. Theses test files make sure the contract is behaving the way its supposed to and doesn't run into any problems.
 
 # Files 
 ### FundMe.sol
Here are the details of this contract and how it works.
The contracts has following public variables.
- ``` address payable public owner ```
  - The address that calls and deploys this contract is stored as the owner is stored as the Owner in this address variable. This is a payable address that can receive funds from other addresses.
- ``` address[] public funders ```
  - This is a list of all the address that have funded this contract.
- ``` mapping(address => uint256) public address_to_balance ```
  - This map stores the funder address and the amount of ether they have funded.
- ``` AggregatorV3Interface public price_feed ```
  - This contract uses real price feeds to return the current market value of ethereum in USD. The contract imports the ```AggregatorV3Interface.sol``` from the **Chainlink-Mix** repository and stores the conversion address in this variable. _Note that Mainnet ETH/USD price feed address will be different from the rinkeby ETH/USD price feed address_. This variable stores one of these addresses so that they can be passed as a parameter to a function.

#### Here's how this contract works:
The contructor gets a Price Feed address as a parameter and initializes the ``` address payable public owner ``` variable to the deployer of this contract.
- The ``fund`` function check for a minimum price condition and adds the funder to the ```address[] public funders``` variable and the ``withdraw`` functions withdraws the fund to the owner and initializes the funders to a new address (removing all the previous funders). There's also a Owner modifier that makes sure that only the owner can withdraw all of the funds.
- In order to get the ETH/USD Price Feeds, ``getPrice()`` is used that returns the current price of ethereum in WEI and ``ETH_to_USD_conversion(uint256 ETH)`` is used to convert that price in USD.

