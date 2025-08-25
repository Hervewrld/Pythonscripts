# Dictionary Data type

employee = {
    "name": "Herve",
    "age" : 26,
    "postion": "Senior Site Reliability Engineer",
    "salary": "285000"
}

print("The employee Position:",employee["postion"])
print("The employee salary:",employee["salary"])

employee["department"] = "IT"
print("Department:",employee["department"])

employee["salary"] = "300000"
print("The new salary is:", employee["salary"])

# In DevOps dictionary can store applicaiton and server configuration settings.

config = {
    "hostname": "server1.example.com",
    "port": "8080",
    "username": "admin",
    "password":"secret"
}
print(config["hostname"]) # Accessing the value using a key

# Output
# server1.example.com