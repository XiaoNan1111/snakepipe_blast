# ——————————————————>>>>>>>>>>
# Project Name: snakemake of blastp 
# Author: Xiao Nan
# E-mail: xiaonan20021016@gmail.com
# Update log:
#     2024/3/11: start project
# ——————————————————>>>>>>>>>>
import os
import json
# ------------------------------------------------------------------->>>>>>>>>>
# FUNCTIONS
# ------------------------------------------------------------------->>>>>>>>>>
def print_head(SAMPLES,THREAD):
    print('----------\nSAMPLES:')
    [print('\t' + i) for i in SAMPLES]
    # print('        ' + i) for i in SAMPLES]
    print('----------\nTHREAD:')
    print(f'        {THREAD}')
    print('----------\n\n')
    

def check_cmd(x):
    return any(
        os.access(os.path.join(path, x), os.X_OK) 
        for path in os.environ["PATH"].split(os.pathsep)
    )
# ------------------------------------------------------------------->>>>>>>>>>
# SAMPLE INFO
# ------------------------------------------------------------------->>>>>>>>>>
with open('./samples.json') as f:
    dt = json.loads(f.read())

SAMPLES = dt['samples']
THREAD = dt['thread']

print_head(SAMPLES,THREAD)
# ------------------------------------------------------------------->>>>>>>>>>
# RUN INFO
# ------------------------------------------------------------------->>>>>>>>>>
# THREAD = os.cpu_count() - 1
# ------------------------------------------------------------------->>>>>>>>>>
# DATABASE INFO
# ------------------------------------------------------------------->>>>>>>>>>
# None
# ------------------------------------------------------------------->>>>>>>>>>
# SOFTWARE INFO
# ------------------------------------------------------------------->>>>>>>>>>
# check if cmd exists
assert check_cmd("blastp")
# manually set cmd path
BLASTP = "blastp"

# ------------------------------------------------------------------->>>>>>>>>>
# rule all
# ------------------------------------------------------------------->>>>>>>>>>
rule all:
    input:
# 这是一个 expand 函数调用，用于生成输入文件列表。expand 函数在Snakemake中常用于基于一组给定的参数生成多个文件路径。
        expand("../blast_info/blastp_result/{sample}.csv", sample=SAMPLES)

# ------------------------------------------------------------------->>>>>>>>>>
# rule blastp
# ------------------------------------------------------------------->>>>>>>>>>
rule blastp: 
    input: 
        "../blast_info/fasta_split_1000/{sample}.fasta"
    output:
        "../blast_info/blastp_result/{sample}.csv"
    params:
        # db="/mnt/blastdb_tmpfs/nr.blastdb/nr.blastdb",
        db='/dev/shm/blastdb_tmpfs/nr.blastdb/nr.blastdb',
        # out="../blast_info/blastp_result/{sample}.csv",
        mode="blastp-fast",
        fmt="10 qseqid stitle sseqid pident evalue",
        hits="10"
    shell:
        """
        echo {input}
        {BLASTP} -query {input} -db {params.db} -out {output} -task {params.mode} -outfmt "{params.fmt}" -max_target_seqs {params.hits} -num_threads {THREAD}
        """