import requests, json
from requests_ntlm import HttpNtlmAuth
r = requests.get('http://192.168.101.200:32569/Historian/v2/ProcessValues?$filter=FQN+eq+%27SysTimeSec%27+and+DateTime+ge+2019-05-30T09:00:00Z+and+DateTime+le+2019-05-30T10:00:00Z&RetrievalMode=BestFit&Resolution=1000', auth=HttpNtlmAuth('domain\\username', 'password'))
data = r.json()
for k in data['value']:
    print(k['DateTime'])
    print(k['Value'])
