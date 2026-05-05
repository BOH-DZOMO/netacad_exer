user = {"name":"jupeter", "email": "bohdzomobobpeter@gmail.com", "age":20, "is_active": True}
name = user.get("name","boh")
user["role"]= "student"
user["age"]= 50
user["address"] = {"city": "Bafoussam","country": "Cameroon"}
for i, j in user.items():
    if type(j) == dict:
        for x, y in j.items():
             print(f"{x}: {y} | ",end=" " )
        continue
    print(f"{i}: {j} |" ,end=" ")
print()    

users = [{"name":"jupeter", "email": "bohdzomobobpeter@gmail.com", "age":20, "is_active": True},{"name":"peter", "email": "bohpeter@gmail.com", "age":90, "is_active": True},{"name":"bob", "email": "boh@gmail.com", "age":96, "is_active": False}]
active_users = [user for user in users if user["is_active"] == True ]

print(f"Active users: {len(active_users)} out of {len(users)}")
