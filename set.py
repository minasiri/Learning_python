s={}
print(type(s))
s = {1,2,3}
s = {1,1,2,3}
print(s)
S1 = {1,2,3}
(S1.add(4))
print(S1)
(S1.update([4,5,6]))
print(S1)
S1 = {1,2,3,4}
(S1.discard(4))
print(S1)
(S1.discard(5))
print(S1)
(S1.remove(3))
print(S1)
(S1.remove(2))
print(S1)

#Task
print("Task")
a = {1,2,3,4}
b = {3,4,5,6}
print(a.intersection(b))
print(a.union(b))
print(a.difference(b))
print(a.symmetric_difference(b))
