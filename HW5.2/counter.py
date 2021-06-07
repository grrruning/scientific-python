for f in snakemake.input:
    result = {}
    with open(f) as in_file:
        filename = f.replace("input/", "")
        data = in_file.read().lower()
        alphas = ''.join(x for x in data if x.isalpha())
        unique = list(set(alphas))
        unique.sort()
        for i in unique:
            result[i] = alphas.count(i)
            with open("output/"+ filename, "w") as out_file:
                for item in result.items():
                    out_file.write(f"{item[0]}:{item[1]}\n")


