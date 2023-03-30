names = [
    'John',
    'William',
    'Daniel',
    'Mike'
]

# List Comprehension
length = [len(name) for name in names]
print(length)

# Dictionary Comprehension
length = {name: len(name) for name in names}
print(length)