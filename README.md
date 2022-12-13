# chibio
Get sequences containing one or two genes of interest in a plasmid.

For that:

1. run plasmidfinder 

```
> for file in data/test/*
> do
> name="$(basename $file)"
> mkdir out/$name
> python /fast-storage/miniconda3/envs/plasmidfinder/bin/plasmidfinder.py -p /fast-storage/miniconda3/envs/plasmidfinder/plasmidfinder_db/ -i $file -o out/$name
> done
```

2. run blast with the plasmids sequences output from plasmidfinder + amr genes database


