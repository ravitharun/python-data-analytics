
Value='rfr'
# count_volw=0
# count_conso=0
# for i in Value:
#     if i=='a' or i=='e' or i=='i' or i=='o' or i =='u':
#      count_volw+=1
#     else:
#         count_conso+=1
               
# print(f'consoant :{count_conso}')       
# print(f'vowles :{count_volw}')       
  
check=False 

if Value=='':
    print("enter the value to check")
else:    
    for i in Value:
        if i=='a' or i=='e' or i=='i' or i=='o' or i =='u':
            check=True
        else:
            check=False
               
if check:
    print("it is volwes")
else:
    print("it is consonants")
    