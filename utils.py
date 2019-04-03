def f2(msg):
    d = {
        b'<STX>':  b'\x02',
        b'<ETX>':  b'\x03',
        b'<ETB>':  b'\x17',
        b'<CR>':   b'\x0D',
        b'<LF>':   b'\x0A',
        b'<CRLF>': b'\x0D\x0A',
        b'<EOT>': b'\x04'
        }
    res = bytes(msg, 'ascii')
    res = res.replace(b'\r', b'')
    res = res.replace(b'\n', b'')
    for symbol, bval in d.items():
        res = res.replace(symbol, bval)

    # print(res)
    return res

def f(msg):
    d = {
        b'[STX]':  b'\x02',
        b'[ETX]':  b'\x03',
        b'[ETB]':  b'\x17',
        b'[CR]':   b'\x0D',
        b'[LF]':   b'\x0A',
        # b'[CRLF]': b'\x0D\x0A',
        b'[EOT]': b'\x04'
        }

    res = bytes(msg, 'ascii')
    res = res.replace(b'\r', b'')
    res = res.replace(b'\n', b'')
    # print("RES : ",res)
    for symbol, bval in d.items():
        res = res.replace(symbol, bval)

    print("RES:",res)
    return res

def read_file(file_name):
    print("READ FILE NAME : ",file_name)
    file = open(file_name,'r')
    m = file.read()
    msg = f(m)
    fi = open(file_name + 'astm', 'w')
    fi.write(msg.decode('ascii'))
    fi.close()
    return msg


def generate_astm_file():
    import os
    path = 'data/cs_400'
    onlyfiles = []
    for r, d, f in os.walk(path):
        for file in f:
                onlyfiles.append( os.path.join(r, file))

    for file in onlyfiles:

        read_file(file)


if __name__ == '__main__':
    generate_astm_file()