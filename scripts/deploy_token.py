from brownie import FLMToken, network, config
from scripts.helpful_scripts import get_account

INITIAL_SUPPLY = 1000000000000000

def deploy_token():
    account = get_account()
    flames = FLMToken.deploy(INITIAL_SUPPLY, {"from": account}, publish_source = config["networks"][network.show_active()].get("verify"))
    print (f"contract deployed to {flames.address}")
    print (f"total tokens in account = {flames.balanceOf(account.address)}")


def main():
    print("deploy ERC20 Token contract!")
    deploy_token()