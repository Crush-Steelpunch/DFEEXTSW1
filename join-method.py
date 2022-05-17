# Help for join 
# |  join(self, iterable, /)
# |      Concatenate any number of strings.
# |     An iterable is something with a numbered index like a list or a tuple
# |      The string whose method is called is inserted in between each given string.
# |      The result is returned as a new string.
# |
# |      Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'

list1 = ["cats", "dogs", "mice", "sheep", "ocelots", "frogs"]
var1 = " and "

print(var1.join(list1)) # put the value in the var between each item in the list

print(" ".join(list1))
print(", ".join(list1))
