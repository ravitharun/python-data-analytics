# tuples are inmutable which cant chage it is constant -->(data1,data2,data3)
tuples=(1,2,"tharun")

print(tuples[0])
print(tuples.count(2))
print(tuples.index("tharun"))
t = (3, 5, 9)
print(max(t))   # Output: 9
print(min(t))   # Output: 3
print(sum(t))   # Output: 17
print(sorted(t))   # Output: [3,5,9]

t = 10, 20, 30
a, b, c = (10, 20, 30)
print(f'a={a} b={b} c={c}')
tuples=(1,2,"tharun")
print([tuples])
list_itm=[1,2,3,4]
print(tuple(list_itm))



