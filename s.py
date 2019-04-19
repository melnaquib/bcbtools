import threading
import time

threads = {}

def send(ds, aet):
  #TODO send

  del threads[ds]

def on_rcv(ds):
    aet = ''

    t = threading.Thread(target=send, args=(ds, aet,))
    threads[ds] = t
    t.start()
