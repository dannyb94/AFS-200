csv = 'Eric,John,Michael,Terry,Graham,TerryG,Brian'
friends_list = []

s = csv.split(",")

friends_list.append(s[0])
friends_list.append(s[1])
friends_list.append(s[2])
friends_list.append(s[3])
friends_list.append(s[4])
friends_list.append(s[5])
friends_list.append(s[6])

print(friends_list)