#Conditional Expressions if, elif, else
#P1 find the greatest no of the four entered by user
'''num1 = int(input("Enter num 1"))
num2 = int(input("Enter num 2"))
num3 = int(input("Enter num 3"))
num4 = int(input("Enter num 4"))
if(num1>num2 and num1>num3 and num1>num4):
    print("num1 is greatest")
elif(num2>num3 and num2>num4 and num2>num1):
    print("num1 is greatest")
elif(num3>num2 and num3>num4 and num3>num1):
    print("num1 is greatest")
else:
    print("num4 is the greatest")'''

#P2  find out whether a student has passed or failed if it 
# requires a total of 40% and at least 33% in each subject to pass. 
'''sub1 = int(input("Enter marks of subject1: "))
sub2 = int(input("Enter marks of subject2: "))
sub3 = int(input("Enter marks of subject3: "))
total = ((sub1 + sub2 + sub3)*100)/300
if(total > 40 and sub1 > 33 and sub2 >33 and sub3 >33):
    print("pass")
else:
    print("fail")'''

#P3 detect spam in messages
'''p1 = "buy now"
p2 = "Make a lot of money"
p3 = "click this"
p4 = "Subscribe this"
message = input("Enter the message:")
if(p1 in message or p2 in message or p3 in message or p4 in message):
    print("spam")'''

#P4  find whether a given username contains less than 10 characters or not
'''username = input("enter username: ")
if (len(username) < 10):
    print("less than 10 characters")
else:
    print("more than 10 characters")'''

#P5 finds out whether a given name is present in a list or not
l1 = []
num = int(input("enter no of names: "))
for i in range(num):
    a = input("Enter name: ")
    l1.append(a)
    i = i+1
name = input("Enter the name you wanna search: ")
if (name in l1):
    print("it is in list")
else:
    print("it is not in list")