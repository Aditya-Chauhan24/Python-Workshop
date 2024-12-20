#21 oct 2024(Dictionary)

#union of unique elements in sets
def union_of_sets(*sets):
    result = set()
    for s in sets:
        result = result.union(s)
    return result

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {5, 6, 7}

print(union_of_sets(set1, set2, set3))  
# Output: {1, 2, 3, 4, 5, 6, 7}
