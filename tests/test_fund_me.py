from scripts.helpful_scripts import LOCAL_BLOCKCHAINS, get_acc, get_priceFeed_address
from scripts.deploy import deploy_fundME
from brownie import FundMe, accounts, exceptions, network
import pytest


def test_canWithdraw():
    acc = get_acc()
    fund_me = deploy_fundME()
    entrance_fee = fund_me.getEntranceFee()
    trx = fund_me.fund({"from": acc, "value": entrance_fee})
    trx.wait(1)
    assert fund_me.address_to_balance(acc.address) == entrance_fee
    trx2 = fund_me.withdraw({"from": acc})
    assert fund_me.address_to_balance(acc.address) == 0


def test_only_owner():
    if network.show_active() not in LOCAL_BLOCKCHAINS:
        pytest.skip("This test is only for Local Networks")
    fund_me = deploy_fundME()
    acc = get_acc()
    entrance_fee = fund_me.getEntranceFee()
    trx = fund_me.fund({"from": acc, "value": entrance_fee})
    trx.wait(1)
    not_owner = accounts.add()
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from": not_owner})


# def test_funders():
#     acc = get_acc()
#     fund_me = deploy_fundME()
#     entrance_fee = fund_me.getEntranceFee()
#     funders = []
#     funders.append(acc)
#     for i in range(1, 5):
#         acc = accounts[i]
#         funders.append(acc)
#         trx = fund_me.fund({"from": acc, "value": entrance_fee})
#         trx.wait(1)
#     for i in range(5):
#         assert fund_me.funders(i) == funders[i]
