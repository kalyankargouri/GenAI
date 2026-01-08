import requests
try:
    url=""
    response=resquests.get(url)
    print("status code:",response.status_code)
    #print("response text",response.text)
    data = response.json()
    print("resp data: ", data)
except:
    print("some error occured.")