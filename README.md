# SmartContractScanning

HKUS3Lab - Scripts, modifications of repos, and other utils for smart contract scanning.
Currently,

## Table of Contents

- [SmartContractScanning](#smartcontractscanning)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [License](#license)

## Installation

1. Download the [Dockerfile](Dockerfile).
2. Run `docker build -t <image_name> .` to build the image.
3. Run `docker run -it <image_name>` to run the image.
<!-- 1. `git clone --recurse-submodules` this repo
1. Run `pip show slither-analyzer` to find the directory at which slither is installed, and make [these changes](must_reads/slither_changes_required.txt). -->



## Usage

1. Create an API key at [etherscan.io](https://docs.etherscan.io/getting-started/viewing-api-usage-statistics) and add it to scripts/key.py: `api_key = "EXAMPLEKEYXXXXXXXXX"`
2. Create a directory for the contracts you want to scan. For example, `mkdir ProjectA`
3. Run `python scripts/scan.py 0x1234567890123456789012345678901234567890 ProjectA/` to scan the contract at address 0x1234567890123456789012345678901234567890. The results will be saved in `ProjectA/<contract_name>/`

## Contributing


## License

[MIT](LICENSE) © HKUS3Lab
