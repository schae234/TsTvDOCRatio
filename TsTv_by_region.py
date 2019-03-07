import sys

import numpy as np


#Need to get the DOC of coverage for 1MB regions for each chromosome
#Then need to put into table with the TsTv infor
#This works on a small portion of the file
#Read in bins from TsTv file

def calculate_tstv():
    '''
        I dont know if you still need this function? In the original script
        I didn't see it really print anything out, maybe you were going to 
        use that information later? 
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
            chrom_t,binstart,snp_count,tstv,*_ = line.rstrip("\n").split("\t")
            CHROM_T.append(chrom_t)
            BinStart_T.append(binstart)
            SNP_count_T.append(snp_count)
            TsTv.append(tstv)
            BinEnd_T.append(int(binstart)+100000)


def calculate_mean_doc(doc_file, output_file=None):
    '''
        Reads in the DOC file one line at a time, the window is calcualted by dividing by the window size and
        converting to an integer. Once all of the values for a window have been read in, the mean DOC is 
        calculated for all the bases in the window.

        Prints the average DOC to `output_file`. If not specified, the default output file
        is stdout. This lets you pipe the output
    '''
    if output_file is None:
        output_file = sys.stdout
    # Process the doc file 
    with open(doc_file, "r") as input_file:
        print("Processing {}".format(doc_file),file=sys.stderr)
        # read in the header line
        header = input_file.readline()
        # Set default values for loop variables
        cur_chrom = None
        cur_window = None
        cur_min = None
        cur_max = None
        docs = []
        # print a header for 
        print('chrom\twindow\tstart\tstop\tmean_doc', file=output_file) 
        # Iterate over the file
        for i,line in enumerate(input_file):
            # split out the values in the line
            a,depth,*_ = line.strip().split("\t")
            chrom,pos = a.split(":")
            # Convert to appropriate types
            pos = int(pos)
            window = int(pos/1000000)
            depth = float(depth)
            if cur_chrom is None:
                cur_chrom = chrom
                cur_window = window
                cur_min = pos
                cur_max = pos
            # If we are at a new window, process the mean of the old window
            if window != cur_window or chrom != cur_chrom:
                print('Calculating mean DOC for window {}:{}'.format(cur_chrom,cur_window),file=sys.stderr)
                # calculate mean for old window and store in the mean_docs dictionary
                #mean_docs[chrom][window] = np.mean(docs) 
                print("{}\t{}\t{}\t{}\t{}".format(cur_chrom,cur_window,cur_min,cur_max,np.mean(docs)),file=output_file)
                # set up new variables 
                cur_chrom = chrom
                cur_window = window
                cur_min = pos
                cur_max = pos
                docs = []
            # always append the doc 
            docs.append(depth)
            cur_min = min(pos,cur_min)
            cur_max = max(pos,cur_max)

