
# lists--> a list is an ordered,mutable,indexed and heterogenous collection
# we use [] to represent lists
details =[1,'raju','pfs7','vizag',56.7]
print(len(details))
print(type(details))


stu_ids =['cgvi0134','cgvio135','cgvio136']
#print(stu_ids[1])

stu_ids[0] ='codegnan'
print(stu_ids)

# tuples--> tuples are also immutable,ordered,indexed and heterogenous
# collection,we use () parenthesis
# dimensions,coordinates

place =('hyderabad','vizag','vjywd')
print (place)
place[0]='chennai'
print(place)

dimensions = 10,20,30
print(dimensions)
print(type(dimensions))

# sets --> a set is a unique collection (removes duplicates)
# a set is an unordered, unindexed, mutable collection
ids =set() # empty set
print(ids)
ids = set((123,124,125))
print(ids)
courses ={'pfs','jfs','da'}
print(courses)
print(type(courses))
print(courses[0]) # as  set is unordered there is no index

# dictionaries --> a dictionaries (mapping object) is a collection of
# key value pairs --> dict ={k:v},we access only by keys (indexed by keys)
#dictionary is also mutable collection
details ={'branch':'vizag', 'batches':['pfs-vsp-007','pfs-vsp-006'], 'courses':'pfs', 'count':19}
print(details)
print(type(details))
print(len(details))
print(details['batches']) # we access by giving only keys

# every built-in datatype is a built-in function
# int, float, complex, bool, str
# lists--> tuples,sets,dict

marks=[35,24,54]
a= tuple(marks)
print(a)
b=set(marks)
print(b)
c=str(marks)
print(c)
print(len(c))

d=dict(marks)
print(d)

marks=[35,24,54]
e= dict.fromkeys(marks)
print(e)

marks=(45,34,64)
a=list(marks)
print(a)
b=set(marks)
print(b)
c=str(marks)
print(c)

d=dict(marks)
print(d)

# dictionaries --> lists,tuples,sets
ids ={1:123,2:124}
a=list(ids)
print(a)
b=tuple(ids)
print(b)
c=set(ids)
print(c)
d=str(ids)
print(d)
print(len(d))

# frozensets --> it is an immutable set, unindexed,unordered
# we can typecase it to list,tuple,set
a= frozenset((12,32,12,32))
print(a)
print(type(a))
print(len(a))
b=list(a)
c=tuple(a)
d=set(a)
e=dict.fromkeys(a)
f=str(a)
print(c,d,e,f)
print(len(f))
print(b)

d= 'raju'
e= list(d)
f=tuple(d)
g=set(d)
h=dict.fromkeys(d)
print(e,f,g,h)

#operators --> arithmetic operators,assignment,comparision,
#logical,membership,identify,bitwise operators
#arithmetic operators--> +, -, *, **, /, //, (floor division) quotient,%(moduls)remainder
a=3
b=2
print(a*b)
print(a**b)
print(a/b)
print(a//b)
print(a%b)
