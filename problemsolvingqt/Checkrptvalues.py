input_value=input("enter the text :")
Check_value='r'

count=0
for i in input_value:
    if i in Check_value:
        count+=1
    else:
        count=0;    
print(f'{Check_value} repeted is {count}')    
    