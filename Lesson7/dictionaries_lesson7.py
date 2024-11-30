# Dictionaries
band = {
    "vocals": "Plant",
    "guitar": "Page"
}

band2 = dict(vocals = "Plant", guitar="Page")

print(band)
print(band2)
print(type(band))
print(len(band))

#Access items
print(band["vocals"])
print(band.get("guitar"))

#list all keys
print(band.keys())

#list all values
print(band.values())

#list of key/value pairs as tuples
print(band.items)

# verify a key exists
print("guitar" in band)
print("triangles" in band)

#change values
band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})

print(band)

# Remove items
print(band.pop("bass"))
print(band)

# add a new value
band["drums"] ="Bonham"
print(band)

# Remove last item that was added
print(band.popitem()) # tuple
print(band)

# Delete and clear item
band["drums"] = "Bonham"
del band["drums"]
print(band)

band2.clear()
print(band2)
del band2

# Copy in dictionaries

# band2 = band # create a reference
# print("Bad copy!")
# print(band)

# band2["drums"] = "Sadiq"
# print(band)

band2 = band.copy()
band2["drums"] = "Sadiq"
print("Good copy")
print(band)
print(band2)

# copy use the dict() constructor function
band3 = dict(band)
print("Good copy")
print(band3)

# Nested dictionaries

member1 = {
    "name": "Plant",
    "instrument": "vocals"
}
member2 = {
    "name": "Page",
    "instrument": "Guitar"
}
band = {
    "member1": member1,
    "member2": member2
}
print(band)
print(band["member1"]["instrument"])

# sets
nums = { 1, 2, 3, 4}
num2 = set((1,2,3,4))
print(nums)
print(num2)
print(type(nums))
print(len(nums))

# No duplicates are allowed

nums = {1,2,2,3}
print(nums)

# True is a dupe of 1, False is a dupe of zero
nums = {1,True,2,False,3,4,0}
print(nums)

# Check if a value is in a set
print(2 in nums)

# but you cannot refer to an element in a set with an index position or a key

# add a new element to a set
nums.add(8)
print(nums)

# Add elements from one set to another
morenums = {5,6,7}
nums.update(morenums)
print(nums)

# You can use update with lists, tuples, and dictionaries, too.

# Merge two sets to create a new set
one = {1,2,3}
two = {5,6,7}

mynewset = one.union(two)
print(mynewset)

# Keep only the duplicates from two diff sets
one = {1,2,3}
two = {1,2,7}

one.intersection_update(two)
print(one)

# Keep everythin except the duplicates
one = {1,2,3}
two = {1,2,7}

one.symmetric_difference_update(two)
print(one)