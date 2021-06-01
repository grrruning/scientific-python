with open(snakemake.input[0], "r") as infile:
    count = len(infile.read().split())

with open(snakemake.output[0],"w+") as file:
    file.write(str(count))
