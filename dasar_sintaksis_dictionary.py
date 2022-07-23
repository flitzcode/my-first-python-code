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

#users = {
#    "Kucing": "pawpaw",
#    "Istri": "Vian",
#    "Buah": "Apel"
#}

print(users)
print(type(users)) #mengetahui tipe data, hasilnya tipe data "dict"
print("\nMerubah python dictionary menjadi JSON")
import json
result = json.dumps(users) #kalo dengan "s" itu ke data string
print(result)
print(type(result)) #mengetahui tipe data, hasilnya tipe data "str"

with open('result.json', 'w') as file:
    json.dump(users, file) #kalo ga pake "s" itu merubah ke filess


