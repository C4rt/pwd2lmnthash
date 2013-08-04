#!/usr/bin/env python
# -*- coding: utf-8 -*

'''
Small python script to create a list of "LM_hash:NT_hash" from a list of passwords.
Sometimes usefull in pentesting
...
'''

__author__ = "C4rt"
__date__ = "04/08/2013"
__version__ = "1.0"
__maintainer__ = "C4rt"
__email__ = "eric.c4rtman@gmail.com"
__status__ = "Production"

try:
  from passlib.hash import lmhash
  from passlib.hash import nthash
  import optparse
  import traceback
except ImportError, err:
    raise
    print >>sys.stderr, "[X] Unable to import : %s\n" % err
    sys.exit(1)

def main():
    parser = optparse.OptionParser(
        "Usage: pswd2lmnthash.py -d <Password names file>")
    parser.add_option('-d', dest='passfile', type='string',
                          help='specify dictionnary with passwords')
    (options, args) = parser.parse_args()

    passfile = options.passfile

    if passfile == None:
        print parser.usage
        exit(0)
    #
    hashlist=[]
    passnames = open(passfile).read().splitlines()
    print "\nStarting hashing\n======================"
    for pwd in passnames:
      lm = lmhash.encrypt(pwd)
      nt = nthash.encrypt(pwd)
      hashlist.append((lm+":"+nt))
    for hash in hashlist:
      print hash

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print "\n\n[%] Process interrupted by user..", "r", "error"
    except:
        print "\n\n\n\n", traceback.format_exc()
