# snakepipes_blastp
## about author

> author: [肖楠| Nan Xiao](https://github.com/XiaoNan1111)
>
> email: xiaonan20021016@gmail.com

## doc
`snakepipes_blastp` is a snakemake process for local blastp on a large scale. However, note that this does not include the process of building a local library, if you want to build a local library, you can look up the use of "makeblastdb" online. 

- input file: a complex form (this is relevant to our project). If you only want to batch enter fasta files, ignore "meta_step.04.GetFile", start with "meta_step.04.GetFileName", and then execute "meta_step.04.blastp_Snakefile.py".
- output file:
    - "../blast_info/blastp_result/{sample}.csv
- requirement
    - raw FASTQ file must put in `../blast_info/fasta_split_1000/` directory
    - run Jupyter notebook to abtain the config for snakemake -> `sample.json`


## env:
```
tree .
.
└── blast_info/fasta_split_1000

git clone https://github.com/XiaoNan1111/snakepipe_blastp.git
cd snakepipe_blastp


conda env create -f conda_env.yml
conda activate 
```
## run
```shell
# run Jupyter notebook to abtain the config
# run this cmd
# or
# open notebook and run all cells
runipy meta_step.04.GetFile # !!! If you only want to batch enter fasta files, ignore "meta_step.04.GetFile"!!!
runipy meta_step.04.GetFileName
# dry run for test
snakemake -pr -j 1 -s meta_step.04.blastp_Snakefile.py -n
# run calculation
snakemake -pr -j 1 -s meta_step.04.blastp_Snakefile.py
```


## project structure
```shell
╰─○ tree -L 2
.
├── blast_info
│   ├── blastp_result
│   ├── df_seqs_rep.pkl.gz
│   └── fasta_split_1000
├── snakepipe_blastp
│   ├── conda_env.yml
│   ├── meta_step.04.blastp_Snakefile.py
│   ├── meta_step.04.GetFile.ipynb
│   ├── meta_step.04.GetFileName.ipynb
│   ├── README.md
│   └── samples.json
```


    