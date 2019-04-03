conda create -n python3.5  python=3.5 anaconda
call activate python3.5
conda install --yes --file requirements.txt
conda install --yes pil
conda install --yes numpy
conda install --yes -c anaconda csvkit
