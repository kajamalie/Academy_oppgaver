import logging
logging.basicConfig(
    filename= 'logday4.log'
    level = logging.debug,
    format = '%(asctime)s/%(levelname)s/%(module)s:%(message)s'))

logging.debug('The code got to this')
logging.info('The code also got this') 

#%%
num_list = []
text = 'Hei på deg kl 14 og kl 19 , ta med 5.7 kr.'
words = (text.split( ))

def extract_number(text):
    word = text.split()
    for word in words:
        if word.isdigit():
            num_list.append(float(word))
        else:
            print(f'{word}:This is not numeric')
    return(num_list)


#%%
 #e.	Write a new function ‘extract_numb_exp(text)’ and do the same as question
    #a) for this new function

num_list = []
text = 'Hei på deg kl 14 og kl 19 , ta med 5.7 kr.'
words = (text.split( ))

def extract_number_exp(text):
    numb_list = []
    words = text.split(' ')
    
    for word in words:
        try:
            num_list.append(float(word))
        except:
            print(f'{word} is not a number')
    return(num_list)

#%%
#write a function “combine(numbers)“ that takes as input numbers (list of numbers) and returns the 
#list combined into one number.example combine ([1,2,3,4]) -> 1234
 
 numbers = [1,2,3,4]
def combine(numbers):
    for num in numbers:
        print(num, end = '')
        
#%% 
#List medium:Write a function “is_ palindrome (suspect)” that’s takes as input, suspect a list 
#(of whatever type) and returns True if the suspect is a palindrome 
#(same forward and backward like [‘r’, ‘a’, ‘c’, ‘e’, ‘c’, ‘a’, ‘r’]), else False. 

#%%
 # a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

#and write a program that prints out all the elements of the list that are less than 5.
    
lis = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def return_lowerthan_5(lis):
    liste = []
    for num in lis:
        if num < 6:
            liste.append(num)
        else:
            pass
    return(liste)

#%%
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print([num for num in a if num < 6])

#%%

nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
def findLargestNum(nums):
    return(max(nums))
#%%
chickens = 2

def animals(chickens, cows, pigs):
    return((chickens * 2) + (cows * 4) + (pigs * 4))

#%%
def how_many_seconds(hours):
    return(hours * 60 * 60 )

#%%
#create a nested loop (loop in loop), which create every combination of number 0 to (and including) 10.
# Multiply them together, and print the value if its an even number (hint a number is even when numb%2=0)

import random 
def nest_loop():
    









