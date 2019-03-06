import numpy as np
import pandas as pd

from collections import defaultdict

#Need to get the DOC of coverage for 1MB regions for each chromosome
#Then need to put into table with the TsTv infor
#This works on a small portion of the file
#Read in bins from TsTv file

def calculate_tstv():
    '''

    '''
    CHROM_T = []
    BinStart_T = []
    BinEnd_T = []
    SNP_count_T = []
    TsTv = []
    # Process the file
    with open("/home/mccuem/shared/Projects/HorseGenomeProject/Data/EquCab3/dz_cases/GB_pipeline/TsTv/TsTv_by_region/out.TsTv", "r") as input_file:
        header = input_file.readline()
        for line in input_file:
            chrom_t,binstart,snp_count,tstv = line.rstrip("\n").split("\t")
            CHROM_T.append(chrom_t)
            BinStart_T.append(binstart)
            SNP_count_T.append(snp_count)
            TsTv.append(tstv)
            BinEnd_T.append(int(binstart)+100000)


def calculate_mean_doc(doc_file):
    '''
        Reads in the DOC file one line at a time, the window is calcualted by dividing by the window size and
        converting to an integer. Once all of the values for a window have been read in, the mean DOC is 
        calculated for all the bases in the window.
    '''
    mean_docs = defaultdict(dict)
    # Process the doc file 
    with open(doc_file, "r") as input_file:
        # read in the header line
        header = input_file.readline()
        # Set default values for loop variables
        cur_chrom = None
        cur_window = None
        docs = []
        # Iterate over the file
        for i,line in enumerate(input_file):
            # split out the values in the line
            a,depth = line.strip().split("\t")
            chrom,pos = a.split(":")
            # Convert to appropriate types
            pos = int(pos)
            window = int(pos/1000000)
            depth = float(depth)
    
            # If we are at a new window, process the mean of the old window
            if window != cur_window or chrom != cur_chrom:
                print('Calculating mean DOC for window {}:{}'.format(cur_chrom,cur_window))
                # calculate mean for old window and store in the mean_docs dictionary
                mean_docs[chrom][window] = numpy.mean(docs) 
                # set up new variables 
                cur_chrom = chrom
                cur_window = window
                docs = []
            # always append the doc 
            docs.append(depth)
    # Create a table of the results
    doc_df = pd.DataFrame(mean_docs)
    return doc_df

# Process some files
dz_cases_DOC = calculate_mean_doc("/home/mccuem/shared/Projects/HorseGenomeProject/Data/EquCab3/dz_cases/GB_pipeline/DOC/dz_cases_DOC")
