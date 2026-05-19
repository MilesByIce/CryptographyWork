

def collision(number_of_people, number_of_days):
# Input: the number_of_people at the party,
# and the number_of_days in a year, i.e., 365 for a non leap year
# Output: the probability of at least two people at the party have the same birthday 

# checks that people and days are integers and stops if they are not ints
    if not isinstance(number_of_people,int) or not isinstance(number_of_days, int):
        print("not a proper choice, input an integer ")
        return
# define product to find probability of no collision
    product = 1
    #loop through the range of 1 to the total number of people (we start with 1 because there cant be -1 people)
    #and we do people + 1 because when we do the initial 1-people, we start from 1 instead
    #of the typical 0
    for i in range(1 , number_of_people + 1):
        result = 1 - ((i - 1)/number_of_days)
        #multiply each loop by the previous result
        product *= result
    #return the probability of collision 
    return 1 - product

# test case
number_of_people = 23 
number_of_days = 365 
# no leap year 
print("The probability of at least two people sharing a birthday is ", collision(number_of_people, number_of_days))
# expected: Given a group of 23 people, the probability of at least two people having the same birthday is  0.5072972343239854

#test 2: probability of finding a collision for people in the same birthday month with a group of 5
number_of_days = 28
number_of_people = 5
print("The probability of at least two people sharing a birthday is ", collision(number_of_people, number_of_days))

#test 3: probability of finding a collision for people in the same birthday month with a group of 5
number_of_days = "abcd"
number_of_people = 5
print("The probability of at least two people sharing a birthday is ", collision(number_of_people, number_of_days))
