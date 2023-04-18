from key import api_key
import requests
import json
import re
import os
from typing import Tuple

# API documentation: https://docs.etherscan.io/api-endpoints/contracts

def extract_dir_and_file_path(file_path: str) -> Tuple[str, str]:
    """
    Extracts the directory path and file name from a file path.
    Args:
        file_path (str): The file path to extract from.
    Returns:
        dir_path (str): The directory path.
        file_name (str): The file name.
    """
    match = re.match(r"^(.*/)?([^/]*)$", file_path)
    if match:
        dir_path = match.group(1)
        file_name = match.group(2)
        return dir_path, file_name
    else:
        print("Invalid file path")
        return None, None

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
    
    # check if response is valid
    if response['status'] == '1' and response['message'] == 'OK':
        contract_details = response['result'][0]
        filename = contract_details['ContractName'] + ".sol"
        source_code = contract_details['SourceCode']
        
        # check if SourceCode is an underlying json object
        # means it imports libraries like SafeMath, OpenZeppelin, etc.
        if source_code[0] == '{':
            json_sources = json.loads(source_code[1:-1])
            for file_path, source_dict in json_sources['sources'].items():
                dir_path, file_name = extract_dir_and_file_path(file_path)
                if file_name == filename:
                    filename = dir_path + file_name
                os.makedirs(dir_path, exist_ok=True)
                with open(dir_path + file_name, "w") as f:
                    f.write(source_dict['content'])
        else:
            with open(filename, "w") as f:
                f.write(source_code)

        return filename
    
    # invalid address
    else:
        print(f'{address} is not a valid contract address')
        return None

if __name__ == '__main__':
    print(get_contract_source_output_to_file('0x32400084C286CF3E17e7B677ea9583e60a000324'))