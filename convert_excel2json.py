import pandas as pd
import json
import sys

df = pd.read_excel('./data/ORG_ID-excerpt.xlsx', sheet_name='Sheet1')
# disable force_ascii with original(utf-8) encoding
result = df.to_json(orient='records', force_ascii=False)
with open('./data/ORG_ID-1.json','w', encoding='utf-8') as fp:
    fp.write(result)
    fp.close()
    
#print(result)
parsed = json.loads(result)

json_data2 = json.dumps(parsed, indent=2, ensure_ascii=False)
with open('./data/ORG_ID-3.json','w',encoding='utf-8') as fh:
    fh.write(json_data2)
    fh.close()
    
#fh = open('./ORG_ID.json','w')

# disable ensure_ascii to dump with original(utf-8) encoding
#json.dump(parsed, sys.stdout, indent=2, ensure_ascii=False)
#fh.close()
#------------------------------------------------------
# with open('df.json','w',encoding='utf-8') as file:
#     df.to_json(file, orient='records', force_ascii=False)
#     file.close()


# with open('df.json','r', encoding='utf-8') as fp:
#     json_data = json.load(fp)
#     fp.close()

# json_data2 = json.dumps(json_data, indent=2, ensure_ascii=False)
# print(json_data2)
# with open('json_data2.json','w', encoding='utf-8') as fh:
#     fh.write(json_data2)
