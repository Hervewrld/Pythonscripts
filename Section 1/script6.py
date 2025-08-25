# list data type

my_list = [1, 2, 3, 4, 5, 6, 7]
print("My List: ",my_list)

servers = ['192.168.1.1', '192.168.1.2', '192.168.1.3', '192.168.1.4']
print("The list of servers:", servers)

my_list[0] = 0
print("The modified list", my_list)

# To update new record in the list of servers

servers.append('192.168.1.13')
print("The modified list of servers", servers)