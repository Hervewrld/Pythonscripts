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

# Also Dictionary can be used to manage the infrastucture 

servers = {
    "webserver" : {"ip": "192.168.1.110", "role": "frontend"},
    "db_server" : {"ip": "192.168.1.210", "role": "database"},
    "cache_server" : {"ip": "192.168.1.250", "role": "caching"}
}
print(servers["webserver"]["role"])