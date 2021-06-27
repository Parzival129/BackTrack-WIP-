def getCount(arr, n, num1, num2):

    # Find num1
    for i in range(0,n):
        if (arr[i] == num1):
            break

    #If num1 is not present or present at end 
    if (i >= n-1): 
        return 0
  
    # Find num2 
    for j in range(n-1, i+1, -1): 
        if (arr[j] == num2): 
            break
  
    # If num2 is not present 
    if (j == i): 
        return 0
  
    # return number of elements between 
    # the two elements.
    return (j - i - 1)

# Driver Code
arr= ['empty', 'empty', 'df', ';fdgdfg', 'sdfrg', 'iusfyisudf', 'memes', 'dsfgkjg', 'idhg', 'e878345']
n=len(arr)
num1 = 'df'
num2 = 'e878345'
print(getCount(arr, n, num1, num2))

