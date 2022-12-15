# chibio
Get sequences containing one or two genes of interest in a plasmid.

### Input

`data/test/`: contains the fasta sequences

`data/filtered.fasta`: contains the amr genes

### Usage

1. Find seq. with plasmids **plasmidfinder**  

```
$ for file in data/test/*
> do
> name="$(basename $file)"
> mkdir out/$name
> python /fast-storage/miniconda3/envs/plasmidfinder/bin/plasmidfinder.py -p /fast-storage/miniconda3/envs/plasmidfinder/plasmidfinder_db/ -i $file -o out/$name
> done
```

Or, run **abricate** (v.1.0.1) - faster and easier

```
$ abricate --db plasmidfinder data/test/*.fna > out/abricate.tab
$ abricate --summary out/abricate.tab > out/summary.tab
```

2. run **blast** (v.2.12.0)

query: amr genes sequences (`data/filtered.fasta`)

```
$ for file in data/test/*
> do
> name="$(basename $file)"
> blastn -query data/filtered.fasta -out out/$name.csv -subject $file -outfmt "6 qseqid sseqid pident qlen slen length nident"
> done
```

3. Combine blast output

`workflow/scripts/combine.py`

4. Check for samples with mcr-1 + any other gene

`workflow/scripts/resistant.py`

5. Find interesect samples with plasmid presence + mcr-1 + other gene

