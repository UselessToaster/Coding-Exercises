#Daily Coding Problem: EASY
#Good morning! Heres your coding interview problem for today.  

#Given an array of integers, determine whether it contains a Pythagorean triplet. 
#Recall that a Pythogorean triplet (a, b, c) is defined by the equation a2+ b2= c2.


#Thoughts: 
# - if statement to determine pythagorean triplet
# - must itterate through every number in every position

import random 

def main():
    #test array
    arr_len = int(input("How long do you want your array to be? "))
    arr = list(set(rand_arr(arr_len)))
    
    print(f"Given list: {arr}")

    display(pythag_checker(arr))


def rand_arr(length):
    box = []
    for i in range(length):
        box.append(random.randint(1,100))
    return box


def pythag_checker(pc_arr):
    triples_matrix = []

    for c in pc_arr:
        triples = []
        for a in pc_arr:
            for b in pc_arr:
                if (a**2 + b**2 == c**2):
                    triples = [a, b, c]

                    #only notates first iteration of triple
                    if sorted(triples) not in triples_matrix:
                        triples_matrix.append(triples)
    return triples_matrix


def display(d_triples_matrix):
    print(f"There are {len(d_triples_matrix)} Pythagorean triples in the given list.")
    for i in d_triples_matrix:
        print(i)   

main()
