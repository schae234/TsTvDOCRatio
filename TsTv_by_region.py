#Need to get the DOC of coverage for 1MB regions for each chromosome
#Then need to put into table with the TsTv infor

#This works on a small portion of the file
#Read in bins from TsTv file
CHROM_T = list()
BinStart_T = list()
BinEnd_T = list()
SNP_count_T = list()
TsTv = list()

with open("/home/mccuem/shared/Projects/HorseGenomeProject/Data/EquCab3/dz_cases/GB_pipeline/TsTv/TsTv_by_region/out.TsTv", "r") as input_file:
#with open("out.TsTv", "r") as input_file:
    input_file.readline()
    for line in input_file:
        line = line.rstrip("\n")
        line = line.split("\t")
        CHROM_T.append(line[0])
        BinStart_T.append(line[1])
        SNP_count_T.append(line[2])
        TsTv.append(line[3])
        a = int(line[1])+100000
        BinEnd_T.append(a)

#Plan:
#While DOC_CHROM == TsTv_dict['CHROM_T']
#If DOC_pos (need to split from chrom) >= TsTv_dict['BinStart'][i] and <TsTv_dict['BinStart'[i+1] then add to count 
#Do for chrX first
#Try reading in by bin size 

#Tried to do this for all chromosomes in a loop and it error'd out. So will probably just have to do it one chromosome at a time.
DOC_bin = list()
DOC_chr = list()
DOC_pos = list()
count = 0 
start = 0
with open("/home/mccuem/shared/Projects/HorseGenomeProject/Data/EquCab3/dz_cases/GB_pipeline/DOC/dz_cases_DOC", "r") as input_file:
    input_file.readline()
    for line in input_file:
        line = line.rstrip("\n")
        line = line.split("\t")
        a = line[0].split(":")
        b = float(line[2])
        pos = int(a[1])
        if a[0] == "chr1":
            if pos >= start and pos < (start+1000000):
                    count +=b
            else:
                mean = count/1000000
                DOC_bin.append(mean)
                DOC_chr.append(a[0])
                DOC_pos.append(a[1])
                count = 0
                start += 1000000
        else:
            break
count = 0
start = 0
with open("/home/mccuem/shared/Projects/HorseGenomeProject/Data/EquCab3/dz_cases/GB_pipeline/DOC/dz_cases_DOC", "r") as input_file:
    input_file.readline()
    for line in input_file:
        line = line.rstrip("\n")
        line = line.split("\t")
        a = line[0].split(":")
        b = float(line[2])
        pos = int(a[1])
        if a[0] == "chr2":
            if pos >= start and pos < (start+1000000):
                    count +=b
            else:
                mean = count/1000000
                DOC_bin.append(mean)
                DOC_chr.append(a[0])
                DOC_pos.append(a[1])
                count = 0
                start += 1000000
        else:
            pass
#As a precaution write the output file before it gets killed:
with open("dz_cases_DOC_bins.txt", "w") as output_file:
    for i in range(len(DOC_bin)):
        print(DOC_chr[i], DOC_pos[i], DOC_bin[i], file = output_file, sep= "\t")

count = 0
start = 0
with open("/home/mccuem/shared/Projects/HorseGenomeProject/Data/EquCab3/dz_cases/GB_pipeline/DOC/dz_cases_DOC", "r") as input_file:
    input_file.readline()
    for line in input_file:
        line = line.rstrip("\n")
        line = line.split("\t")
        a = line[0].split(":")
        b = float(line[2])
        pos = int(a[1])
        if a[0] == "chr3":
            if pos >= start and pos < (start+1000000):
                    count +=b
            else:
                mean = count/1000000
                DOC_bin.append(mean)
                DOC_chr.append(a[0])
                DOC_pos.append(a[1])
                count = 0
                start += 1000000
        else:
            pass

#Start again from here as was killed
DOC_bin = list()
DOC_chr= list()
DOC_pos = list()
count = 0
start = 0
with open("/home/mccuem/shared/Projects/HorseGenomeProject/Data/EquCab3/dz_cases/GB_pipeline/DOC/dz_cases_DOC", "r") as input_file:
    input_file.readline()
    for line in input_file:
        line = line.rstrip("\n")
        line = line.split("\t")
        a = line[0].split(":")
        b = float(line[2])
        pos = int(a[1])
        if a[0] == "chr4":
            if pos >= start and pos < (start+1000000):
                    count +=b
            else:
                mean = count/1000000
                DOC_bin.append(mean)
                DOC_chr.append(a[0])
                DOC_pos.append(a[1])
                count = 0
                start += 1000000
        else:
            pass

#As a precaution write the output file before it gets killed:
with open("dz_cases_DOC_bins_chr4.txt", "w") as output_file:
    for i in range(len(DOC_bin)):
        print(DOC_chr[i], DOC_pos[i], DOC_bin[i], file = output_file, sep= "\t")



count = 0
start = 0
with open("/home/mccuem/shared/Projects/HorseGenomeProject/Data/EquCab3/dz_cases/GB_pipeline/DOC/dz_cases_DOC", "r") as input_file:
    input_file.readline()
    for line in input_file:
        line = line.rstrip("\n")
        line = line.split("\t")
        a = line[0].split(":")
        b = float(line[2])
        pos = int(a[1])
        if a[0] == "chr5":
            if pos >= start and pos < (start+1000000):
                    count +=b
            else:
                mean = count/1000000
                DOC_bin.append(mean)
                DOC_chr.append(a[0])
                DOC_pos.append(a[1])
                count = 0
                start += 1000000
        else:
            pass

#As a precaution write the output file before it gets killed:
with open("dz_cases_DOC_bin_crh5.txt", "w") as output_file:
    for i in range(len(DOC_bin)):
        print(DOC_chr[i], DOC_pos[i], DOC_bin[i], file = output_file, sep= "\t")


count = 0
start = 0
with open("/home/mccuem/shared/Projects/HorseGenomeProject/Data/EquCab3/dz_cases/GB_pipeline/DOC/dz_cases_DOC", "r") as input_file:
    input_file.readline()
    for line in input_file:
        line = line.rstrip("\n")
        line = line.split("\t")
        a = line[0].split(":")
        b = float(line[2])
        pos = int(a[1])
        if a[0] == "chr6":
            if pos >= start and pos < (start+1000000):
                    count +=b
            else:
                mean = count/1000000
                DOC_bin.append(mean)
                DOC_chr.append(a[0])
                DOC_pos.append(a[1])
                count = 0
                start += 1000000
        else:
            pass

#As a precaution write the output file before it gets killed:
with open("dz_cases_DOC_bin_crh6.txt", "w") as output_file:
    for i in range(len(DOC_bin)):
        print(DOC_chr[i], DOC_pos[i], DOC_bin[i], file = output_file, sep= "\t")


count = 0
start = 0
with open("/home/mccuem/shared/Projects/HorseGenomeProject/Data/EquCab3/dz_cases/GB_pipeline/DOC/dz_cases_DOC", "r") as input_file:
    input_file.readline()
    for line in input_file:
        line = line.rstrip("\n")
        line = line.split("\t")
        a = line[0].split(":")
        b = float(line[2])
        pos = int(a[1])
        if a[0] == "chr7":
            if pos >= start and pos < (start+1000000):
                    count +=b
            else:
                mean = count/1000000
                DOC_bin.append(mean)
                DOC_chr.append(a[0])
                DOC_pos.append(a[1])
                count = 0
                start += 1000000
        else:
            pass

#As a precaution write the output file before it gets killed:
with open("dz_cases_DOC_bin_crh7.txt", "w") as output_file:
    for i in range(len(DOC_bin)):
        print(DOC_chr[i], DOC_pos[i], DOC_bin[i], file = output_file, sep= "\t")


count = 0
start = 0
with open("/home/mccuem/shared/Projects/HorseGenomeProject/Data/EquCab3/dz_cases/GB_pipeline/DOC/dz_cases_DOC", "r") as input_file:
    input_file.readline()
    for line in input_file:
        line = line.rstrip("\n")
        line = line.split("\t")
        a = line[0].split(":")
        b = float(line[2])
        pos = int(a[1])
        if a[0] == "chr8":
            if pos >= start and pos < (start+1000000):
                    count +=b
            else:
                mean = count/1000000
                DOC_bin.append(mean)
                DOC_chr.append(a[0])
                DOC_pos.append(a[1])
                count = 0
                start += 1000000
        else:
            pass

count = 0
start = 0
with open("/home/mccuem/shared/Projects/HorseGenomeProject/Data/EquCab3/dz_cases/GB_pipeline/DOC/dz_cases_DOC", "r") as input_file:
    input_file.readline()
    for line in input_file:
        line = line.rstrip("\n")
        line = line.split("\t")
        a = line[0].split(":")
        b = float(line[2])
        pos = int(a[1])
        if a[0] == "chr9":
            if pos >= start and pos < (start+1000000):
                    count +=b
            else:
                mean = count/1000000
                DOC_bin.append(mean)
                DOC_chr.append(a[0])
                DOC_pos.append(a[1])
                count = 0
                start += 1000000
        else:
            pass

count = 0
start = 0
with open("/home/mccuem/shared/Projects/HorseGenomeProject/Data/EquCab3/dz_cases/GB_pipeline/DOC/dz_cases_DOC", "r") as input_file:
    input_file.readline()
    for line in input_file:
        line = line.rstrip("\n")
        line = line.split("\t")
        a = line[0].split(":")
        b = float(line[2])
        pos = int(a[1])
        if a[0] == "chr10":
            if pos >= start and pos < (start+1000000):
                    count +=b
            else:
                mean = count/1000000
                DOC_bin.append(mean)
                DOC_chr.append(a[0])
                DOC_pos.append(a[1])
                count = 0
                start += 1000000
        else:
            pass
