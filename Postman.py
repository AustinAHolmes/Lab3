import requests

url = "https://www.indeed.com/jobs?q=Software Developer&l=Charlotte"

payload={}
headers = {
  'Cookie': 'CSRF=1Wsrz6D4IGr6EmoHm4yfg1rejG7CyWOW; CTK=1g9hbibr1i16g800; __cf_bm=t79Y6zorBIJKAJ5pAKfiHSySVQxTMVg_ZUCPH.TX_A4-1659513679-0-AS9v8564n2vp8ZMBHsJTRwiUZ4ggBAwkUpoJ3+q21gwNs3+No5agUL1aBRqnan2C+lTJcsIicmhQQVupLtshRhI=; _cfuvid=ei3MoseIypwZSwFOyEmm02745isFtXxcBaV7O1H3ObA-1659513679741-0-604800000; CTK=1g9hbibr1i16g800; INDEED_CSRF_TOKEN=UVbPFCUXcZb7ylzrODDxwGrWHNJ5exc0; JSESSIONID=A50EDC8CD767ED221183F78A5DBCF0A6; LV="LA=1659513679:CV=1659513679:TS=1659513679"; PREF="TM=1659513824900:L=Charlotte"; RQ="q=Software+Developer&l=Charlotte&ts=1659513824933:q=Software+Developer&l=&ts=1659513794283"; UD="LA=1659513824:CV=1659513777:TS=1659513777:SG=733be64433bd9cb8ba421dbdefe05b78"; indeed_rcc="LV:CTK:UD"; jaSerpCount=3; loctip=1'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
