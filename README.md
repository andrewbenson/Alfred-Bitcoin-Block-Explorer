# Alfred Bitcoin Block Explorer

- Version 0.0.1
- Created by Andrew Benson
- Follow me on [Twitter](https://twitter.com/AndrewBenson) or [GitHub](https://github.com/andrewbenson)

## About 

This Alfred Workflow provides quick access to the leading Bitcoin blockchain explorers. 

### Supported Queries

The workflow currently supports the following functions: 

- Search Addresses
- Search Blocks
- Search Transactions (by txid)

### Supported Block Explorers

By default, the workflow uses the Mempool.space block explorer. This is configurable in the workflow settings. 

The following Bitcoin block explorers are currently supported: 

- Mempool.space (default)
- Blockstream.info
- Blockchain.com


### Blockchain Instance Support

By default, the workflow uses Bitcoin's mainnet. This is configurable in teh workflow settings. 

The workflow currently supports the following instances of the Bitcoin blockchain: 

- Mainnet (detfault)
- Testnet 
- Signet

*Note: Blockchain.com does not support Signet queries. If Blockchain.com and Signet are selected, the workflow falls back to Mempool.space.*


# Requirements 

- Python 3.10 or later