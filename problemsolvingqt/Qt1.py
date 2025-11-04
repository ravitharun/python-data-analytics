# to prigrm to check number is postive
# num =int(input("enter the value :"))
# if(num>=0):
#     print(f' the number you enterd {num} is postive (+ve) number')
  
# else:
#     print(f"the number you enterd {num } is negtive (-ve)number") 

# program check the number is odd/even;
# print("the numbe is even")if(num%2==0)else print('the number is odd ')
# chekc weather ltter is vowel or no
# vowel-->a,e,i,o,u
# letter='aeiou'
# if letter=='a' or letter=='e'or letter=='i'or letter=='o'or letter=='u':
#     print("the letter is vowel ")
# else:
#     print("the letter is no the vowel letter")    
# area calulator
choose=""" 
       press 1 :Area of the Rectangle
       press 2 :Area of the Triangle
       press 3 :Area of the Circle
      
      """
print("area of the calcuator")
print(choose)
choice=int(input(f"enter {choose}"))
if(choice==1):
    len=int(input("enter the len of the rectangle : "))
    brdth=int(input("enter the len of the rectangle : "))
    print(len*brdth)
elif choice==2:
    base=float(input('enter the base value : ')) 
    heigth=float(input("enter the float value :"))   
    print(0.5*base*heigth)
elif choice==3:
    pi=3.4
    radius=float(input("enter the radius (r) : "))
    print(pi*radius**radius)    