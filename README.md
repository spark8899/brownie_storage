# brownie_storage
tech brownie contract develop

# request
get infura token

go to https://infura.io/

get Rinkeby eth

go to https://faucets.chain.link/

# start ganache-cli test
```shell
ganache-cli
```

# install python3 venv
```shell
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

# compile
```shell
brownie compile
```

# deploy on local
```shell
brownie run ./scripts/deploy.py
```

# deploy on rinkeby
```shell
brownie run .\scripts\deploy.py --network rinkeby 
```

# test
```shell
brownie test
```

# brownie console
```shell

>>> from brownie import network
>>> network.show_active()
'development'
>>> from brownie import accounts
>>> account = accounts[0]
>>> from brownie import Storage
>>> storage = Storage.deploy({"from": account})
Transaction sent: 0x33656826beb46a90963c3c4f3681936cfa44511c3766e57394fe313ee531c763
  Gas price: 0.0 gwei   Gas limit: 6721975   Nonce: 2
  Storage.constructor confirmed   Block: 3   Gas used: 243860 (3.63%)
  Storage deployed at: 0x5f7b8e2ebceA5f0e484a8618B4981f134873868c
>>> transaction = storage.addPerson('wangwu', 32, {"from": account})
>>> transaction.wait(1)
```