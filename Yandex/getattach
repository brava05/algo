def RecurCombo(array, num):  
    print(num)
    if num == 0:  
        return [[]] # if length for combination is 0 
    l =[] # list to printed in result 
    # Using for loop to implement recursive approach 
    for j in range(0, len(array)):  
        emptyArray = array[j] # define an empty array to print list of sets 
        recurList = array[j + 1:] 
        # Recursion method on list defined in function 
        for x in RecurCombo(recurList, num-1):  
            l.append([emptyArray]+x) # appending list 
    return l # list as result of recursion 
if __name__=="__main__": 
    inputArray = input("Enter an input string to find combinations: ") 
    print("All possible combinations of three letter sets from the string given by you is: ") 
    print(RecurCombo([a for a in inputArray], 3))
