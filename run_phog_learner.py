import subprocess
from pickle import load
import logging
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='result_time.log',
    filemode='a',
)
with open('../processed_data.pickle','rb') as f:
    d = load(f)

d_rev = {}
for k in d:
    key = d[k][-1] #cluster id
    if key in d_rev:
        d_rev[key].append(k)
    else:
        d_rev[key] = [k]

with open('../preprocessed-split.pkl','rb') as f:
    db = load(f)

### Training
phog_learner_command = "bin/run_phog_learner phog_str_{} {}"
# for k in d_rev:
#     files = " ".join(list(map(lambda x:f'benchmarks/string/train/{x}.sl' ,db['{}-train'.format(k)])))
#     command = phog_learner_command.format(k,files)
#     ret = subprocess.run(command, capture_output=True, shell=True)
#     print(ret.stdout.decode())
#     print(f'cluster {k} is done')

## Testing
from timeit import timeit
from tqdm import tqdm
cluster_test_time = {}
cluster_output = {}
phog_guide_command = "time timeout 3m bin/run_with_new_phog {} {}" 

small_problems = ['exceljet1','exceljet4','exceljet3','stackoverflow4','stackoverflow1','stackoverflow3'
                  ,'stackoverflow8','stackoverflow5','stackoverflow9','phone-5','phone-5-long',
                  'phone-5-long-repeat','phone-5-short','phone-6','phone-6-long',
                  'phone-6-long-repeat','phone-6-short','phone-7','phone-7-long',
                  'phone-7-long-repeat','phone-7-short']
# small_problems = ['stackoverflow1']
cluster_threshold = 10
logging.info('----------- Testing Start ----------------')
for k in d_rev:
    grammar_cluster = f"phog_str_{k}"
    grammar_all = "phog_str3all_train"

    test_files = list(map(lambda x:f'benchmarks/string/test/{x}.sl' ,db['{}-test'.format(k)]))
    cluster_test_time[k] = []
    cluster_output[k] = []
    logging.info(f"Testing CLuster {k}")
    ### Add timeout
    import time
    if len(test_files)<cluster_threshold:
        logging.info(f'Skipping Cluster {k}')
    for t in tqdm(test_files):
        if t.split('/')[-1][:-3] not in small_problems:
            continue
        command = phog_guide_command.format(grammar_cluster,t)
        # print(f"SOlVING {t} WITH COMMAND {command}")
        
        cluster_time = subprocess.run(command, capture_output=True, shell=True)
        # cluster_time = timeit(stmt = stmts, setup = "import subprocess", number = 1)
        command = phog_guide_command.format(grammar_all,t)
        all_phog_time = subprocess.run(command, capture_output=True, shell=True) #euphony
        # all_phog_time = timeit(stmt = stmts, setup = "import subprocess", number = 1)
        cluster_test_time[k].append((t,cluster_time.stderr.decode(),all_phog_time.stderr.decode()))
        cluster_output[k].append((t,cluster_time.stdout.decode(),all_phog_time.stdout.decode()))

for k in cluster_test_time:
    all_time = []
    if cluster_test_time[k]!=[]:
        for p in cluster_test_time[k]:
            all_time.append(p[1])
            print(p[0])
            print(p[1])
            print(p[2])
            print('------------')

print(f'average_time : {sum(all_time)/len(all_time)}')

