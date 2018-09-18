
import itertools
#первая задача
list = []
for i in range(4):
    list.append (i)
print(list)
list_new = [ b ** 2 for b in list]
print (list_new)
#вторая задача

fruit1 = ["banana" , "orange" , "apple", "pine" , "strawberry" ]
fruit2 = ["qiwi" , "peach" , "pineapple"]
sort_list = []
for item in itertools.chain(fruit1, fruit2):
    sort_list.append(item)
print(sort_list)
#третяя задача

list_old = []
for i in range(-10,10):
    list_old.append (i)
print(list_old)
list_fresh = [x for x in list_old if x % 3 == 0 and x > 0 and x % 4 !=0]
print(list_fresh)





