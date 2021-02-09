import requests
from requests.structures import CaseInsensitiveDict
while True:
    url = "https://discord.com/api/v8/channels/<id>/messages" #replace with actual ID.
    headers = CaseInsensitiveDict()
    headers["Authorization"] = "Auth_key" #replace with your actual key
    headers["Content-Type"] = "application/json"
    #data = '{"content":"test #2"}'
    r = requests.get(url, headers=headers)
    getdata = r.json()
    tag = r.json()
    db = getdata[0]['author']['username']

    try:
        count = getdata[0]['content']
        print(count)
        convert = int(count)
        end = convert + 1
        print(end)
        data = '{"content":"%s"}' % end
        if db == 'Username':
            #replace with actual username
            print("")
        else:
            r = requests.post(url, headers=headers, data=data)
    except:
        continue
