#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Calculate GC-content of nucleotide sequences in fasta format.
"""
from __future__ import print_function

__author__ = "Frédéric Mahé <mahe@rhrk.uni-kl.de>"
__date__ = "2012/02/15"
__version__ = "$Revision: 1.0"

# Copyright 2012 Frédéric Mahé <mahe@rhrk.uni-kl.de>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
from Bio import SeqIO
from Bio.SeqUtils import GC
from optparse import OptionParser

#**********************************************************************#
#                                                                      #
#                            Functions                                 #
#                                                                      #
#**********************************************************************#

def option_parse():
    """
    Calculate GC-content of nucleotide sequences in fasta format.
    """
    parser = OptionParser(usage="usage: %prog --input_file filename",
                          version="%prog 1.0")

    parser.add_option("-i", "--input_file",
                      metavar="FILE",
                      action="store",
                      dest="input_file",
                      help="set FILE as input")

    (options, args) = parser.parse_args()
    return options.input_file


#**********************************************************************#
#                                                                      #
#                              Body                                    #
#                                                                      #
#**********************************************************************#

if __name__ == '__main__':

    input_file = option_parse()

    with open(input_file, "rU") as input_file:
        records = SeqIO.parse(input_file, "fasta")
        while True:
            try:
                record = records.next()
                print(record.id, GC(record.seq), len(record.seq), sep="\t",
                      file=sys.stdout)
            except StopIteration:
                break

sys.exit(0)
