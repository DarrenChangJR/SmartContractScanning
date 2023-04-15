import re
import etherscan_scrape
from typing import Dict

def get_addresses(filename) -> set:
    """
    Uses regex to detect all occurrences of a contract address in the form of (0x...)
    Args:
        filename (str): The filename of the text file to search.
    Returns:
        addresses (set): A set of all addresses with no parentheses.
    """
    with open(filename, "r") as f:
        text = f.read()
        addresses = re.findall(r"\(0x[a-zA-Z0-9]{40}\)", text)
        addresses = [address[1:-1] for address in addresses]
        addresses = set(addresses)
        return addresses

def scrape_all_interdependent_contracts(address: str, filename_to_address: Dict[str, str] = {}) -> Dict[str, str]:
    """
    Scrapes all interdependent contracts from a given contract address.
    Args:
        address (str): The contract address to scrape.
        filename_to_address (dict): A dictionary mapping filenames to contract addresses.
    Returns:
        filename_to_address (dict): A dictionary mapping filenames to contract addresses.
    """
    # scrape contract at given address
    filename = etherscan_scrape.get_contract_source_output_to_file(address)
    filename_to_address[filename] = address

    # get all addresses in the contract
    addresses = get_addresses(filename)

    # scrape all contracts at addresses
    for address in addresses:
        if address not in filename_to_address.values():
            scrape_all_interdependent_contracts(address, filename_to_address)
    return filename_to_address

def create_mapping_file(mapping_dict: Dict[str, str]):
    """
    Create mapping file of filename to address separated by comma, with each mapping separated by newline.
    Args:
        mapping_dict (dict): A dictionary mapping filenames to contract addresses.
    """
    mapping_file_name = "map.txt"
    with open(mapping_file_name, "w") as f:
        for filename, address in mapping_dict.items():
            f.write(f"{filename},{address}\n")
