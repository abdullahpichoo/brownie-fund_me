from brownie import FundMe, MockV3Aggregator, accounts, network, config
import os
from scripts.helpful_scripts import get_acc, get_priceFeed_address
from web3 import Web3

# right now we can only verify contracts deployed on the rinkeby testnet and this process will fail if I dont pass the network flag in brownie run command.
# this is due to our FundMe contract has a hardcoded rinkeby priceFeed address and we can only verify our contract only if we use rinkeby testnet
# to fix this we edit our FundMe contract and send a address parameter of any chain and this way we can verify the chain that we're using


# logic here: If selected network is of testnet then the original AggregatorV3 is deployed though the FundMe contract
# else the network must be a development network and the MockV3Aggregator contract will be deployed that will return a mock price feed


def deploy_fundME():
    acc = get_acc()
    priceFeed_address = get_priceFeed_address()
    contract = FundMe.deploy(
        priceFeed_address,
        {"from": acc},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract Deployed to Address: {contract}")
    return contract


def main():
    deploy_fundME()


# 5.33.06
