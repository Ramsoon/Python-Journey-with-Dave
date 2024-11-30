users = ['Dave', 43, True]
data = ['Sadiq', 'John', 'Sara']
emptylist = []

print ("Sadiq" in data)

print(users[0])
print(users[-2])
print(data.index('Sara'))

print(data[0:2])
print(data[1:])
print(data[-3:-1])

print(len(users))

data.append('Elsa')
print(data)

data += ['Jason']
print(data)

data.extend(['Robert', 'Jimmy'])
print(data)

# data.extend(data)
# print(users)

data.insert(0, 'Bob')
print(data)

data[2:2] = ['Eddie', 'Alex']
print(data)

data[1:3] = ['Robert', 'JPJ']
print(data)

data.remove('Bob')
print(data)

print(data.pop())
print(data)

del data[0]
print(data)

#del users
users.clear()
print(users)

data[1:2] = ['sadiq']
data.sort()
print(data)

data.sort(key=str.lower) # to include lowercase alphabets in the alphebetical order
print(data)

nums = [4,42,78,1,5]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)

print(sorted(nums, reverse=True))
print(nums)

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))

mylist = list([1,"Neil", True])
print(mylist)

#Tuples

mytuple = tuple(('Sadiq',42,True))
anothertuple = (1,4,2,3,8,2,2)
print(mytuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append('Neil')
newtuple = tuple(newlist)
print(newtuple)
print('')
print(newlist)

(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)

print(anothertuple.count(2))