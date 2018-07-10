import pandas as pd
meta = pd.read_csv('metadata.csv', delimiter='|')
meta_df = pd.DataFrame(meta)
count = 0
for line in range(len(meta_df.values)):
    if line == None:
        count = count + 1
print(count)