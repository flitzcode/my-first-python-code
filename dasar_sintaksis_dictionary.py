users = {
 "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    #JSON didalam JSON
    "address": {
        "street": "Kulas Light",
        "suite": "Apt. 556",
        "city": "Gwenborough",
        "zipcode": "92998-3874",
        "geo": {
            "lat": "-37.3159",
            "lng": "81.1496"
                }
        }
}
print(users)
print(users["id"])
print(users["name"])
print(users["username"])
print(users["email"])
print(users["address"])
print(users["address"]["street"])
print(users["address"])
print(users["address"]["geo"]["lat"])
print(users["address"]["geo"]["lng"])

print(merubah python dictionary menjadi JSON)

