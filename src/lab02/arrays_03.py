#3_flatten
def flatten(mat: list[list | tuple]) -> list:
    result = []
    for row in mat:
        if isinstance(row,(tuple,list)):
            result.extend(row)
        else:
            raise TypeError
    return(result)

print(flatten([[1, 2], [3, 4]]))
print(flatten(([1, 2], (3, 4, 5))))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], "ab"]))