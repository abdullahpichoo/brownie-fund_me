from scripts.helpful_scripts import get_acc, get_priceFeed_address
from brownie import FundMe, accounts


def fund():
    fund_me = FundMe[-1]
    acc = get_acc()
    entrance_fee = fund_me.getEntranceFee()
    print(f"entry fee:{entrance_fee}")
    trx = fund_me.fund({"from": acc, "value": entrance_fee})


def withdraw():
    fund_me = FundMe[-1]
    acc = get_acc()
    fund_me.withdraw({"from": acc})


def test_funders():
    acc = get_acc()
    fund_me = FundMe[-1]
    entrance_fee = fund_me.getEntranceFee()
    funders = []
    funders.append(acc)
    print(f"{fund_me.funders(0)} || {funders[0]}")
    trx = fund_me.fund({"from": acc, "value": entrance_fee})
    print(f"{fund_me.funders(1)} || {funders[0]}")
    # for i in range(1, 5):
    #     acc = accounts[i]
    #     funders.append(acc)
    #     trx = fund_me.fund({"from": acc, "value": entrance_fee})
    #     trx.wait(1)
    # for i in range(5):
    #     print(f"{fund_me.funders(i)} || {funders[i]}")


def main():
    test_funders()
