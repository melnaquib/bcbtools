import json
import subprocess

import requests
from PyQt5.QtCore import QProcess

NODE_CMD = 'btcb_node'
#NODE_CMD = '/home/melnaquib/work/client/freelancer.com/bb/code/btcb_build_beta/' + NODE_CMD
# NODE_URL = "http://[::1]:15000"
NODE_URL = "http://[::1]:17076"


def cmd(args, timeout = -1, end = None):
    p = QProcess()
    p.setProgram(NODE_CMD)
    p.setArguments(args)
    p.start()

    out, err = '', ''


    if type(end) == str:

        while timeout > 0:
            INTERVAL = 2000
            timeout -= INTERVAL
            p.waitForFinished(INTERVAL)
            o = p.readAllStandardOutput().data().decode()
            out += o
            if end in o:
                break
        err = p.readAllStandardError().data().decode()
        p.terminate()

    else:
        p.waitForFinished(timeout)

    return out, err


def start_daemon():
    cmd(['--daemon'])

def rpc(args):
    rsp = requests.post(NODE_URL, data = json.dumps(args))
    res = json.loads(rsp.text)
    return res


def expand_seed(seed):
    args = {
        "action": "deterministic_key",
        "seed": seed,
        "index": "0"
    }
    res = rpc(args)
    return res["private"], res["public"], res["account"]


def genesis(prvk):
    std, err = cmd(['--debug_bootstrap_generate', '--key', prvk],  100000, '}')
    start = std.index('{')
    end = std.index('}')
    res = std[start: end + 1]
    return res
