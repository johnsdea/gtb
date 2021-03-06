import sys
import argparse

sys.dont_write_bytecode = True
from gtb import app

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--ip", help="listen to this IP address",
                    default="0.0.0.0")
parser.add_argument("-p", "--port", help="listen to this port",
                    default="3000", type=int)
parser.add_argument("-d", "--debug", help="turn debugging on",
                    default=True)

args = parser.parse_args()

app.run(args.ip, args.port, args.debug)
