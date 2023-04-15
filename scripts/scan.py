import etherscan_scrape
import inter_contract_utils
import os
import sys
from sailfish.code.static_analysis.analysis import analyze_contracts

# default parameters
patterns = ['DAO', 'TOD']
# output_dir = os.path.expanduser('~/outputs')
range_type = 'range'
dump_graph = False
static_only = False
call_heuristic = True
icc = True
contract_mapping_file = "map.txt"
solver_type = 'cvc4'

# analyze_contracts(filename, patterns, output_dir, range_type, dump_graph, static_only, call_heuristic, icc, contract_mapping_path, solver_type)

if __name__ == '__main__':
    # get contract address from command line argument
    if len(sys.argv) < 3:
        print("Usage: python scan.py <contract_address> <output_dir>")
        exit(1)
    contract_address = sys.argv[1]
    output_dir = sys.argv[2]
    # change directory to output directory
    os.chdir(output_dir)
    # scrape all interdependent contracts
    filename_to_address = inter_contract_utils.scrape_all_interdependent_contracts(contract_address)
    # create mapping file
    inter_contract_utils.create_mapping_file(filename_to_address, contract_mapping_file)


    # analyze contract at given address
    initial_filename = filename_to_address.keys()[0]
    analyze_contracts(initial_filename, patterns, output_dir, range_type, dump_graph, static_only, call_heuristic, icc, contract_mapping_file, solver_type)
