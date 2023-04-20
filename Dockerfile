FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y apt-utils software-properties-common locales libssl-dev python3 python3-pip python-is-python3 graphviz wget git && \
    apt-get --yes autoremove && \
    apt-get --yes autoclean && \
    apt-get clean && \
    rm -rf /var/lib/apt/* && \
    locale-gen en_GB.UTF-8

ENV LANG en_GB.UTF-8
ENV LANGUAGE en_GB:en  
ENV LC_ALL en_GB.UTF-8
ENV PYTHONIOENCODING UTF-8

RUN yes | pip install slither-analyzer matplotlib networkx solidity-parser version-parser ujson pydot --quiet --exists-action i && \
    solc-select install 0.8.19 && solc-select install 0.4.0 && solc-select use 0.8.19

WORKDIR /root

# Clone the repositories
RUN git clone --recurse-submodules https://github.com/DarrenChangJR/SmartContractScanning.git

# Configure Refiner of Sailfish
RUN wget --quiet https://mirror.racket-lang.org/installers/7.7/racket-7.7-x86_64-linux.sh && \
    chmod +x racket-7.7-x86_64-linux.sh && \
    ./racket-7.7-x86_64-linux.sh --in-place --dest /usr/racket --create-links /usr && \
    rm -f racket-7.7-x86_64-linux.sh
RUN raco pkg install --deps search-auto --type github --checksum e4b56fa --name rosette emina/rosette
RUN wget --quiet -O /usr/bin/cvc4 https://github.com/CVC4/CVC4/releases/download/1.7/cvc4-1.7-x86_64-linux-opt && \
    chmod +x /usr/bin/cvc4
RUN cd /root/SmartContractScanning/sailfish/code/symbolic_execution && \
    git clean -fd && \
    ./build.py

WORKDIR /root/SmartContractScanning
