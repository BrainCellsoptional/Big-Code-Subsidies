# week 4_2 List Practice

# 1. Create a list of five colors red, blue, green, black, white
col = ["red","blue","green","black","white"]
# 2. Add yellow to the list
col.append("yellow")
# 3. Remove the last item and print out " ____ was removed from the list" 
print(col.pop())

# 4. Remove the first item and print out "----- was removed from the list"
print(col.pop(0))
# 5. Set the list back to the original five colours
print(col.extend(["yello","red"]))
print(col)
# 6. Remove the 3rd item in the list
col.pop(3)
# 7. Add purple to list at index 3  # list_name.insert(index, item)
col.insert(2,"purple")
print(col)
# 8. Print the len of the list
print(len(col))
# 9. Store items in index 2, 3 and 4 to a new list 
col2 = []
col2.extend([col.pop(1),col.pop(2),col.pop(3)])
print(col2)
# Multi Dimensional Lists are very useful

grid = [
    [ 0,2,3,4,7,3],
    [ 1,8,3,4,8,3],
    [ 8,2,5,4,7,3],
    [ 0,2,3,4,9,3]
]

# You need to be able to access any number in the grid.
# What is grid[0][0], grid[1][0],grid[3][5],
print(grid[0][1])
print(grid[1][0])
print(grid[3][5])
# Use a loop to create this grid
# [1, 0, 0, 0, 0],
# [0, 1, 0, 0, 0],
# [0, 0, 1, 0, 0],
# [0, 0, 0, 1, 0],
# [0, 0, 0, 0, 1],
grid1 = [1,0,0,0,0]
print(grid1)
for x in grid:
    grid1.insert(0,0)
    grid1.pop()
    print(grid1)
    
    
    

# Grids are very useful to store data
# Your user does not want to learn Python
# You need to create an interface so that they can use the list.
# A catalogue app or a contact list app does this.