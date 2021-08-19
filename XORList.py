#A function that can take an int n, two lists list1 and list2 and, in a single line
#Return a bool that is True if n appears either in list1 or list2 and False if it doesn't 
#appear in either or appears in both. 

# example(1, [1, 2, 3], [4, 5, 6]) == True 
# example(1, [0, 2, 3], [1, 5, 6]) == True 
# example(1, [1, 2, 3], [1, 5, 6]) == False 
# example(1, [0, 0, 0], [4, 5, 6]) == False


def XORList(n,list1, list2):
	return (n in list1) != (n in list2)

list1 = [1,2,2]
list2 = [3,2,1]
n = 1
print(XORList(n, list1, list2))

