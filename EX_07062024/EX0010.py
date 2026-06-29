#List
#Add item
#Remove item
#Update item
#View item
#Exit

Shopping_list = ["milk","bread","Poha","Rice","butter"]
print(Shopping_list)
print(len(Shopping_list))
print(Shopping_list[0])
print(Shopping_list[4])

Shopping_list.append("curd")# add item to last in list
Shopping_list.append("coffee")
Shopping_list.extend(["jam","flour"]) #ADD MULTIPLE ITEMS AT END OF LIST
#Shopping_list.insert(_index= 3, _object= "Jam")
print(Shopping_list)

Shopping_list.remove("bread")
print(Shopping_list)
print(Shopping_list.pop())# remove the last iem from list
print(Shopping_list)
Shopping_list.reverse()
Shopping_list.sort()
print(Shopping_list)



my_list = [1,2,3,4,"Aaysha", True, 3.14]
print(type(my_list))