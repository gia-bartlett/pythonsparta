#SETS:

# create a set:

car_parts = {"wheels", "windows", "turbo", "rocker_cover"}
print(car_parts) # {'windows', 'turbo', 'wheels', 'rocker_cover'}

car_parts.add("roll_cage")
print(car_parts)

# frozen set

counting = frozenset([1, 2, 3, 4])
print(counting) # frozenset({1, 2, 3, 4})
print(type(counting)) # <class 'frozenset'>