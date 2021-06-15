import requests, json


BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "login/"+"tempUser")
print(response)
# print(response.content)


dd = {}
# response = requests.get("https://jsonplaceholder.typicode.com/posts")
# print(response.json())
    
while(True):
    s = input()
    t = input()
    BASE = "http://aneeket.pythonanywhere.com/send"
    d ={"name":"tempUser", "user":s, "message":t}
    response = requests.get(BASE, params=d)
    print(response)
    # print(response.url)
    print(response.json())
    d = {"name":"tempUser"}
    BASE = "http://aneeket.pythonanywhere.com/recieve"
    response = requests.get(BASE, params=d)
    print(response.url)
    print(response.json())
    
# threading.Thread(target=a).start()
# threading.Thread(target=b).start()