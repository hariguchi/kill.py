#!/usr/bin/env python
#
# kill.py [-d] 'regexp'
#

import getopt
import os
import re
import sys
import subprocess

def usage():
    sys.stderr.write('Usage: kill.py [-d] regexp\n')
    sys.exit(1)

def doit(procs, pat, dry, debug=False):
    p = re.compile(pat)
    p2 = re.compile(r'kill.py')
    for line in procs.split('\n'):
        if p.search(line[27:]) != None and p2.search(line[27:]) == None:
            col = re.compile(r'[ \t]+').split(line.strip())
            if dry == True:
                print '%s' % (line)
                #print col
                #print
            else:
                print "%s: %s" % (col[0], line)
                subprocess.call(['kill', '-9', col[0]])

def main():
    debug = False
    if len(sys.argv) <= 1:
        usage()

    try:
        opts, args = getopt.getopt(sys.argv[1:], "d")
    except getopt.GetoptError:
        # print help information and exit:
        usage()

    dry=False
    for o, a in opts:
        if o == "-d":
            dry = True

    result = os.popen('ps x').read()
    doit(result, args[0], dry)


if __name__ == '__main__':
    main()





