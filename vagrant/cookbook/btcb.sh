#!/usr/bin/env bash

cd

git clone --recursive http://github.com/bitcoin-black-bcb/btcb
cd btcb/utils/
./bootstrap

mkdir btcb_build
cd btcb_build
cmake -DACTIVE_NETWORK=btcb_live_network \
    -DBoost_INCLUDE_DIR=/usr/local/boost/include \
    -DCPACK_BINARY_DEB=ON -D -DCMAKE_BUILD_TYPE=Release  ../btcb
make -j2
cd

if ps cax | grep lightdm > /dev/null; then
    echo "Desktop environment already running"
else
    echo "Starting desktop environment"
    sudo lightdm &
    echo "Cleanup folders"
    cd /home/vagrant/
    rm -r -f Documents
    rm -r -f Examples
    rm -r -f Extras
    rm -r -f Music
    rm -r -f Pictures
    rm -r -f Templates
    rm -r -f Videos
fi
