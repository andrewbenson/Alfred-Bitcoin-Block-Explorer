import os
import sys

# determine the serach time (address, txid, or block)
search_type = os.environ["search_type"]

query = os.environ["search_query"]

# get the user-specified block explorer, fall back to Mempool.Space if unspecified
try: 
   os.environ["Block_Explorer"]
except NameError: 
    block_explorer = "mempool"
else: 
    block_explorer = os.environ["Block_Explorer"]


# get the user-specified blockchain, fall back to mainnet if unspecified
try: 
    os.environ["Blockchain"]
except NameError: 
    blockchain = "mainnet"
else: 
    blockchain = os.environ["Blockchain"]


## build URL

def urlBuild(search_type, query, block_explorer, blockchain): 

    match block_explorer:
        case "mempool":
            match blockchain: 
                case "mainnet":
                    url_base = "https://mempool.space/"

                case "testnet":
                    url_base = "https://mempool.space/testnet/"

                case "signet":
                    url_base = "https://mempool.space/signet/"

            match search_type: 
                case "address": 
                    url_path = "address/" + query

                case "block":
                    url_path = "block/" + query

                case "txid": 
                    url_path = "tx/" + query
        
        case "blockstream":
            match blockchain: 
                case "mainnet":
                    url_base = "https://blockstream.info/"

                case "testnet":
                    url_base = "https://blockstream.info/testnet/"

                case "signet":
                    url_base = "https://blockstream.info/signet/"

            match search_type: 
                case "address": 
                    url_path = "address/" + query

                case "block":
                    url_path = "block/" + query

                case "txid": 
                    url_path = "tx/" + query
            

        case "blockchain":
            match blockchain: 
                case "mainnet":
                    url_base = "https://www.blockchain.com/"

                    match search_type: 
                        case "address": 
                            url_path = "btc/address/" + query

                        case "block":
                            url_path = "explorer/blocks/btc/" + query

                        case "txid": 
                            url_path = "btc/tx/" + query   

                case "testnet":
                    url_base = "https://www.blockchain.com/"

                    match search_type: 
                        case "address": 
                            url_path = "btc-testnet/address/" + query

                        case "block":
                            url_path = "explorer/blocks/btc-testnet/" + query

                        case "txid": 
                            url_path = "btc-testnet/tx/" + query   

                case "signet":
                    # Blockchain.com does not support Signet. Falls back to Mempool.space
                    url_base = "https://mempool.space/signet/"

                    match search_type: 
                        case "address": 
                            url_path = "address/" + query

                        case "block":
                            url_path = "block/" + query

                        case "txid": 
                            url_path = "tx/" + query   
    final_url = url_base + url_path
    return final_url


output_url = urlBuild(search_type, query, block_explorer, blockchain)
sys.stdout.write(output_url)