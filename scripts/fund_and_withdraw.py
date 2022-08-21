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


def main():
    fund()
    withdraw()
