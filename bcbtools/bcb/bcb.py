import json
import subprocess

import requests
from PyQt5.QtCore import QProcess

NODE_CMD = 'btcb_node'
#NODE_CMD = '/home/melnaquib/work/client/freelancer.com/bb/code/btcb_build_beta/' + NODE_CMD
# NODE_URL = "http://[::1]:15000"
# NODE_URL = "http://[::1]:17076"
NODE_URL = "http://[::ffff:127.0.0.1]:17076"


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

def frontier(addr):
    args = {
        "action": "accounts_frontiers",
        "accounts": [addr]
    }
    res = rpc(args)
    res = res['frontiers'][addr] if addr in res['frontiers'] else ''
    return res

def balance(addr):
    args = {
        "action": "account_balance",
        "account": addr
    }
    res = rpc(args)
    return res["balance"], res["pending"]

def genesis(prvk):
    std, err = cmd(['--debug_bootstrap_generate', '--key', prvk],  100000, '}')
    start = std.index('{')
    end = std.index('}')
    res = std[start: end + 1]
    return res

'''
{  
  "action": "block_create",  
  "type": "open",  
  "key": "0000000000000000000000000000000000000000000000000000000000000001",   
  "account": "xrb_3kdbxitaj7f6mrir6miiwtw4muhcc58e6tn5st6rfaxsdnb7gr4roudwn951",   
  "representative": "xrb_1hza3f7wiiqa7ig3jczyxj5yo86yegcmqk3criaz838j91sxcckpfhbhhra1",   
  "source": "19D3D919475DEED4696B5D13018151D1AF88B2BD3BCFF048B45031C1F36D1858"   
}

{  
  "action": "block_create",  
  "type": "receive",  
  "wallet": "000D1BAEC8EC208142C99059B393051BAC8380F9B5A2E6B2489A277D81789F3F",   
  "account": "xrb_3kdbxitaj7f6mrir6miiwtw4muhcc58e6tn5st6rfaxsdnb7gr4roudwn951",   
  "source": "19D3D919475DEED4696B5D13018151D1AF88B2BD3BCFF048B45031C1F36D1858",   
  "previous": "F47B23107E5F34B2CE06F562B5C435DF72A533251CB414C51B2B62A8F63A00E4"
}


{  
  "action": "block_create",  
  "type": "send",  
  "wallet": "000D1BAEC8EC208142C99059B393051BAC8380F9B5A2E6B2489A277D81789F3F",   
  "account": "xrb_3kdbxitaj7f6mrir6miiwtw4muhcc58e6tn5st6rfaxsdnb7gr4roudwn951",   
  "destination": "xrb_18gmu6engqhgtjnppqam181o5nfhj4sdtgyhy36dan3jr9spt84rzwmktafc",   
  "balance": "20000000000000000000000000000000",   
  "amount": "10000000000000000000000000000000",   
  "previous": "314BA8D9057678C1F53371C2DB3026C1FAC01EC8E7802FD9A2E8130FC523429E"  
}


{  
  "action": "block_create",  
  "type": "change",  
  "wallet": "000D1BAEC8EC208142C99059B393051BAC8380F9B5A2E6B2489A277D81789F3F",   
  "account": "xrb_3kdbxitaj7f6mrir6miiwtw4muhcc58e6tn5st6rfaxsdnb7gr4roudwn951",   
  "representative": "xrb_18gmu6engqhgtjnppqam181o5nfhj4sdtgyhy36dan3jr9spt84rzwmktafc",     
  "previous": "F958305C0FF0551421D4ABEDCCF302079D020A0A3833E33F185E2B0415D4567A"  
}


'''


def send(src_prvk, src_addr, src_balance, amount, dst_addr, prev):
    args = {
      "action": "block_create",
      "type": "send",
      "key": src_prvk,
      "account": src_addr,
      "destination": dst_addr,
      "balance": src_balance,
      "amount": amount,
      "previous": prev
    }
    res = rpc(args)
    return res


def repr_set(src_prvk, src_addr, repr_addr, prev):
    args = {
      "action": "block_create",
      "type": "change",
      "key": src_prvk,
      "account": src_addr,
      "representative": repr_addr,
      "previous": prev
    }
    res = rpc(args)
    return res

def open(src_prvk, src_addr, repr_addr, prev):
    args = {
        "action": "block_create",
        "type": "open",
        "key": src_prvk,
        "account": src_addr,
        "representative": repr_addr,
        "source": prev
    }

    res = rpc(args)
    return res
