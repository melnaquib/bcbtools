#!/usr/bin/env bash

cd

git clone --recursive http://github.com/bitcoin-black-bcb/btcb
cd btcb/util/build_prep
sudo ./bootstrap_boost.sh

cd

mkdir btcb_build
cd btcb_build
cmake -DACTIVE_NETWORK=btcb_live_network \
    -DBoost_INCLUDE_DIR=/usr/local/boost/include \
    -DCPACK_BINARY_DEB=ON -D -DCMAKE_BUILD_TYPE=Release  ../btcb
make
sudo make install
sudo cp btcb_node /usr/local/bin/
cd

