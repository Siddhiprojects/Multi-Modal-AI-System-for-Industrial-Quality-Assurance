'''pip install <module name> 
import <module name>'''
# name = input("Enter your name: ") print(f"Good Afternoon {name} ")

# P1 replace name and date acc to user input
"""letter = '''Dear <Name>
You are Selected !
<Date>'''
print(letter.replace("<Name>", "Amy").replace("<Date>", "2/10/2050"))"""

# P2 find returns substring index in parent string
'''name = "Hello  World"
print(name.find("  ")) #returns -1 if no double space is present'''

# Strings, tuple are immutable, Lists are mutable
# list.append("addstring"), list.sort(), list.reverse(), list.insert(index,element to be added), 
# list.pop(index), list.remove(elememt to be removed)
# dic.items, dic.keys, dic["Key"], dic.values, dic.update, dic.get
# s = set() Dont use s = {} this creates an empty dictionary. Used when you do not want repeat elements
# Set can have heterogenous datatypes, does not have indexing, cannot contain list
# s.add(), s.remove(), s.clear, s.union, s.intersection
# 1 == 1.0 returns true

# P3 collect 8 nos from user and print unique set
'''s = set()
i = 0
for i in range(8):
    num = int(input("Enter a number"))
    s.add(num)
    i = i+1
print(s)'''

#P4 ask four friends to type their favourite language as dictionary
'''d = {}
for i in range(4):
    name = input("Enter name :")
    lang = input("Enter lang :")
    d.update({name:lang})
print(d)'''

