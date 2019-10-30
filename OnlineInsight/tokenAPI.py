import requests, json
tag = 'APIInfo.SysTimeSec'
url = f'https://online.wonderware.com/apis/Historian/v2/ProcessValues?$filter=FQN+eq+%27{tag}%27+and+DateTime+ge+2019-05-30T09:00:00Z+and+DateTime+le+2019-10-30T19:00:00Z&RetrievalMode=BestFit&Resolution=1000'
token_url = 'https://online.wonderware.com/apis/Historian/v2/'
api_key = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImQxMTM1YWJjLWM0YjMtNDE0NC04ZWEzLTYzYzEyODFhNzkxNiJ9.eyJ0eXBlIjoic2VydmljZSIsInZlcnNpb24iOiIxLjAiLCJ0ZW5hbnRpZCI6ImJjYjU3YThiLThiODAtNGFlYi1hNjhmLTA2YWU4MjhmOTFiMCIsInNpaWQiOiJjZTIwMThiYi1mODE3LTQ4NGEtYjQyNi1iNDEyYTc0Y2RkYjIiLCJqdGkiOiJhNjUzMDQ0MS1iNGNkLTQ5NzctODBlNC1iODgxNjkzOWM2NWIiLCJpc3MiOiJwcm9vZm9maWRlbnRpdHlzZXJ2aWNlIn0.3WpKsptiLHvAZm2hiCBcxwzz4iyn4_wx87-6d_ck1ky92Y5MVa9I72Vuz5mrn1WK9lLLZScl0LSpTGI_VpgPuXmI978-0M8EH1I1O2AqfRvprIYbE1Fy_WWXgHxaA1MVx9uoG4ehNVeXWDHOqzfMmrD4LAVw1R0iRBzlJea44TcxhcZ0Rcv_yNrSSbhMn5qw_XcpP-5adgfLh9_FRkIwoO3ElK7KJlI1NH6_FM_sEjgpfgnspIyaX4_O6O6RT5rR2_1MH42qGAqGxTCJUEhuApd7k0S-ZRGWR9clNZCaedU2D_oVEtoDamjwaGW1v676FlXKezxzPo3muBmigSXOmQ'

header = {
    'Authorization': api_key,
    'content-type': 'application/json'
}

r = requests.get(url, headers=header)

print(r.content)
