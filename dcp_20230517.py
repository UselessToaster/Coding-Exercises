#**EASY**#
#Good morning! Heres your coding interview problem for today.  

#This problem was asked by Netflix.

#Given an array of integers, determine whether it contains a Pythagorean triplet. 
#Recall that a Pythogorean triplet (a, b, c) is defined by the equation a2+ b2= c2.


#Thoughts: 
# - if statement to determine pythagorean triplet
# - must itterate through every number in every position
~~# - remember a and b individually are always less than c~~
~~# however a + b must always be greater than c~~

import random 

def main():
    #test array
    arr_len = int(input("How long do you want your array to be? "))
    arr = rand_arr(arr_len)
    
    print(f"Given list: {arr}")

    calc_results = [] 

    print("Pythagorean triples in the given list:")

    no_triples = True 
    for c in arr:
        for b in arr:
            for a in arr:
                if (a**2 + b**2 == c**2):
                    calc_results.append(c)
                    no_triples = False

                    #only prints first iteration of triple
                    if calc_results.count(c) == 1:
                        print(f"({a}, {b}, {c})")                 

    if no_triples == True:
        print("There were no Pythagorean triplets in this list.")


def rand_arr(length):
    box = []
    for i in range(length):
        box.append(random.randint(1,100))
    return box

main()
