import requests


link = 'https://httpbin.org/post'
data = {"comments": "kflkls[l",
        "custemail": "gkjjgkfjgkf@mail.com",
        "custname": "jkrjtr",
        "custtel": "909090909090",
        "delivery": "21:00",
        "size": "small",
        "topping": "bacon"}
response = requests.post(link, data=data)
print(response.status_code)


