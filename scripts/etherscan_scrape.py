from key import api_key
import requests
import os

# API documentation: https://docs.etherscan.io/api-endpoints/contracts

def get_contract_source_output_to_file(address: str) -> str:
    """
    Scrapes the contract source code from etherscan.io and outputs it to a file.
    Args:
        address (str): The contract address to scrape.
    Returns:
        filename (str): The filename of the output file.
    """
    url = "https://api.etherscan.io/api"
    params = {
        "module": "contract",
        "action": "getsourcecode",
        "address": address,
        "apikey": api_key
    }
    response = requests.get(url, params=params)
    response = response.json()
    
    if response['status'] == '1' and response['message'] == 'OK':
        try:
            contract_details = response['result'][0]
            filename = contract_details['ContractName'] + ".sol"
            source = contract_details['SourceCode']

            with open(filename, "w") as f:
                f.write(source)
            return filename
        
        except Exception as e:
            raise e
    else:
        print(f'{address} is not a valid contract address')
        return None
