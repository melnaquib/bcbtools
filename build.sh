#!/usr/bin/env bash

rm -rf dist build medleap/build medleap/dist

mkdir -p build/src

cd  ./medleap/

pyrcc5 ./ui/qml.qrc > ./ui/qml.py
python ./setup.py build_ext
python ./setup.py build
mv medleap ../build/src/
cd ..
cp ./main.py ./build/src/
cp -r ./hooks/ ./build/src/hooks
cp -r ./pkg/ ./build/src/pkg
cd ./build/src


cp -r ../../settings ./
cp ../../.vendor.ini ../../settings.ini ../../.env.ini ./

pyinstaller --distpath ../../dist -y --clean --additional-hooks-dir=./hooks \
            --windowed \
            -i ./pkg/logo_small.ico\
            --exclude-module bcbtools \
            --add-data=settings:settings\
            --add-data=.vendor.ini:.vendor.ini\
            --add-data=.env.ini:.env.ini\
            --add-data=settings.ini:settings.ini\
            --add-data=bcbtools:bcbtools \
            --hidden-import=PyQt5\
            --hidden-import=PyQt5.QtCore \
            --hidden-import=PyQt5.QtGui \
            --hidden-import=PyQt.QtWidgets\
            --hidden-import=PyQt5.QtQuick\
            --hidden-import=PyQt5.QtQml\
            --hidden-import=json \
            --hidden-import=sqlalchemy \
            --hidden-import=sqlalchemy.schema \
            --hidden-import=sqlalchemy.ext.serializer \
            --hidden-import=sqlalchemy.sql.expression \
            --hidden-import=PyQt5.QtSql \
            --hidden-import=PyQt5.QtSerialPort \
            --hidden-import=curses\
            --hidden-import=curses.ascii\
            ./main.py
