from brownie import network, accounts
import os


def get_acc():
    if network.show_active == "development":
        return accounts[0]
    else:
        return accounts.add(os.getenv("priv_key"))
