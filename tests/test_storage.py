from brownie import Storage, accounts


def test_deploy():
    account = accounts[0]
    storage = Storage.deploy({"from": account})
    transaction = storage.addPerson('wangwu', 32, {"from": account})
    transaction.wait(1)
    # call people function to get data from people array
    result = storage.people(0)
    assert result == ('wangwu', 32)