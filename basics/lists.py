# LISTS:

# Create a list of cities:

cities = ["Tokyo", "Paris", "Prague", "Luxembourg", "Auckland", "Reykjavik"]

# print(cities); #['Tokyo', 'Paris', 'Prague', 'Luxembourg', 'Auckland', 'Reykjavik']

# print(type(cities)); # <class 'list'>
#
# print(cities[3]); # Luxembourg (starts at 0)
# print(cities[0]); # Tokyo
#
# cities[2] = "Amsterdam"
# print(cities); # Luxembourg is replaced with Amsterdam now
#
# cities.append("Vilnius")
# print(cities); # Vilnius gets added to the end
#
# cities.remove(cities[1]) # cities.remove("Paris) will do the same thing
# print(cities) # Paris gets removed from the list

# cities.pop()
# print(cities) # removes the last entry from the list

# cities.insert(0, "London")
# print(cities) # London gets added in chosen index position and then just pushes everything else along

# mix_string_list = [1, 2, 3, "A", "B", "C"]
# print(mix_string_list) # [1, 2, 3, 'A', 'B', 'C']
#
# print(type(mix_string_list)); # <class 'list'>
#
# int_list = [1, 2, 3,]
# string_list = ["A", "B", "C"]
# print(int_list + string_list); # [1, 2, 3, 'A', 'B', 'C']

multi_list = [[1, 2, 3], ["a", "b", "c"]]
extra_list = ["blah", "blah"]
print(multi_list) # [[1, 2, 3], ['a', 'b', 'c']]
print(multi_list + extra_list) # [[1, 2, 3], ['a', 'b', 'c'], 'blah', 'blah']
