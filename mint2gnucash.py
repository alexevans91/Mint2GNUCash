#!/usr/bin/python

# Mint2GNUCash.py
# Description: Converts transaction data downloaded from Mint
#              to a format that GNUCash can easily handle.
#
# Author: Alex Evans
# Created: 03/03/2017
# Version: 0.1

from decimal import Decimal
from tqdm import tqdm
import sys


def convert(ifile, ofile):
    input = open(ifile, 'r')
    lines = input.readlines()
    input.close()
    f = open(ofile, 'w')
    lines = lines[1:]
    for i in tqdm(lines):
        data = i.split('","')
        date = data[0].replace('"', '')
        description = data[2].replace('"', '')
        if data[4] == "credit":
            amount = Decimal(data[3].replace('"', ''))
        else:
            amount = Decimal(data[3].replace('"', '')) * -1
        f.write('"%s","%s","%s"\n' % (str(date), str(description), str(amount)))
    f.close()      

if "__main__" in __name__:
    args = sys.argv
    if len(args) < 3:
        print "Invalid number of arguments...\n"
        print "./mint2GNUCash.py inputfile.csv outputfile.csv"
    else:
        input = args[1]
        output = args[2]
        print "Conversion Started...\n"
        convert(input, output)
        print "\nConversion Complete...\n"
    
    