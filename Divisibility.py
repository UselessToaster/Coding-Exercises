'''Problem
You are provided an array of size N that contains non-negative integers. 
Your task is to determine whether the number that is formed by selecting the last digit of all the N numbers is divisible by 10.

Note: View the sample explanation section for more clarification.

Input format

First line: A single integer N denoting the size of array A
Second line: N space-separated integers.

Output format

If the number is divisible by 10, then print Yes. Otherwise, print No.'''

N = int(input())
data = [int(x) for x in input().split()]

if data[len(data) - 1] % 10 == 0:
    print("Yes")
else: 
    print("No")
    
# notes:
## looked through discussion for help, once i understood the question, the solution was simple
## only need to test the last number for divisibility by 10
## for clearer code, data[len(data) - 1] can have its own variable
