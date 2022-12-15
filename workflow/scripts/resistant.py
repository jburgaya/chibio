#!/usr/bin/env python

import os
import argparse
import pandas as pd

def get_options():
    description = 'Get strains containg both colistin and carbapenem resistant genes'
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument('combined',
                         help='Output from combine.py script (combined results from blast)')
    parser.add_argument('output',
                         help='Output directory')

    return parser.parse_args()


if __name__ == '__main__':
    options = get_options()

    b = pd.read_csv(options.combined, sep='\t', names = ['qseqid', 'sseqid', 'pident', 'qlen',
                                                         'slen', 'length', 'nident', 'fasta'])

    # add mock row to test script
    m = {'qseqid':['mcr-1.10'], 'sseqid':['contigy'], 'pident':['100.0'], 'qlen':['810'],
         'slen':['9980'], 'length':['39'], 'nident':['39'], 'fasta':['F1S1R1D2B4P5H04_fasta.fna.csv']}
    mock = pd.DataFrame(data=m)
    b = b.append(mock)

    # remove .csv from fasta id
    b['fasta'] = b['fasta'].str.replace('.csv','' )

    # get presence/abscence matrix of genes per each fasta sequence
    g = b[['fasta', 'qseqid']]
    matrix = g.pivot_table(index='fasta', columns='qseqid', aggfunc=len, fill_value=0).fillna(0)

    # get sequences with colistin AND carbapenem resistant genes
    resistant = matrix.loc[(matrix > 0).sum(axis=1) >= 2]
    print(resistant)

    # save
    resistant.to_csv(os.path.join(options.output, 'resistant.csv'), sep='\t')
