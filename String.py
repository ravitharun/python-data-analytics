name='Ravi tharun'
print(f'n Datatype of the value :  {type(name)}')
print(f'length on the name : {len(name)}')

print(f'Uppercase  :{name.upper()}')
print(f'lower case : {name.lower()}')
print(f'Index : {name.index("a")}')

print(f' counting the letter a : {name.count("a")}')
print(f'get the index of the value : {name.index("a",5,11)}')
print(f'get the index of  the value : {name[name.index("a",5,11)]}')
# first letter will be captilize -->Ravi tharun
print(f'captilize  : {name.capitalize()}')
print(f'casefold  : {name.casefold()}')

print(f'index medthod  gt the index value of the letter : {name.find("a")}')


print(name.center(50,"*"))

