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
lis_1 = [0,1,2,3,4,5,6,7,8,9,10]
 
lis_2 = [0,1,2,3,4,5,6,7,8,9,10]

import random 
def nest_loop(lis_1, lis_2):
    lis = []
    for i in lis_1:
        for j in lis_2:
            if (i * j)%2 ==0:
                lis.append(i*j)
            else:
                 pass
    print(lis, end = ', ')

#%%
#String medium (requires the use of loops or lists):Use “import os” and os.getcwd() to get the root path. 
#Make a function that takes no input, but returns the root folder.
#For example if root is “C:\Users\rodvei\Documents\Code\Python\my_project” the function should return my_project

import os

def get_cwd():
    path = os.getcwd()
    parts = path.split(os.sep)
    print(parts[-1])
    
#%%

#Write a function called check_location, that takes a string for location as input. The format of the input is 
#“<location>, <zip-code>” (like for postal address)The function should return True if the input format is correct
# with a string and a four-digit code separated by comma.

def check_location(location):
  #%%

def chek_location(location):
    location == “<location>, <zip-code>”
    
#%%
    #  Write a function that takes a list of elements and returns only the integers.

lst = ['a','o',4,1,5,'m',7]

def return_only_integer(lst):
    new_lst = []
    for item in lst:
        try:
            new_lst.append(float(item))
        except:
            pass
    return new_lst
      
#%%


def extract_numb_exp(text):
    numb_list = []
    words = text.split(" ")
    for item in words:
        try:
            numb_list.append(float(item))
        except:
            print(f'{item} is not a number!')
    return numb_list

    
    #%%

n = 5
count = 0
increasing = True
while count >= 0:
    if count < n and increasing:
        count = count + 1 
    elif (not increasing) or (count == n):
        count = count - 1 
        increasing = False 
    print('*' * count)


#%%

    print_lens = list(range(1, n+1))
    print_lens = print_lens[0:-1] + print_lens[::-1]
    for print_len in print_lens:
        print('*' * print_len)
        

#%%
        
# Create an empty dictionary called simple_people_dict = {}, 
#Each key should be name and the value is the persons phone number, add at least 3 people with phone numbers. 
        
sample_people_dict = {}
sample_people_dict['Kaja'] = '23345432'
sample_people_dict['Kai'] = '45632145'
sample_people_dict['Maia'] = '34543234'

print(sample_people_dict)

#%%
def censure_phone(fun_dict, name):
    personal_dict = fun_dict[name]
    if 'Phone_numb' in personal_dict:
        personal_dict['Phone_numb'] = None
    print(fun_dict[name]['Phone_numb'])


people_dict = {}
kaja = {'age': 30, 'Phone_numb': 34542342, 'higth': 172}
ole = {'age': 31, 'Phone_numb': 33542342, 'higth': 192}
anna = {'age': 29, 'higth': 182}
people_dict['Kaja'] = kaja
people_dict['Ole'] = ole
people_dict['Anna'] = anna

print(people_dict)
    
    #%%
def censure_all(fun_dict):
    for key in fun_dict_keys:
        censure_phone(fun_dict, name)



#%%
#Create an empty dictionary called simple_people_dict = {}, Each key should be name and the value is 
#the persons phone number, add at least 3 people with phone numbers

simple_people_dict = {} 

simple_people_dict['kaja'] = 293845645
simple_people_dict['kai'] = 2998543245
simple_people_dict['karl'] = 584932345

print(simple_people_dict)

#%%

#Create a new empty dictionary called people_dict = {}, where again each key is a name. but value now is a 
#new dictionary with the keys ‘age’, ‘phone_number’ and ‘hight’.fill inn at least 3 people with all values. 
#And two persons with no phone numbers 
#%%
people_dict = {}

kaja = {'name': 'Kaja', 'age': 28, 'phone': 34593845}
kai = {'name': 'Kai', 'age': 34}
milly = {'name': 'Milly', 'age': 24}
lilly = {'name': 'Lilly', 'age': 30, 'phone': 47382345}

people_dict['Kaja'] = kaja
people_dict['Kai'] = kai
people_dict['Lilly'] = lilly
print(people_dict) 

#%%

#Create a function ‘censure_phone(people_dict, name)’ that takes the above people_dict as input, 
#and name of the person to censure phone number. Set the number to None.make sure to handle the 
#situation for the two people above without phone numbers

def censure_phone(withouth_dic, name):
    people_dict = withouth_dic[name]
    if 'phone' in people_dict:
        people_dict['phone'] = None
    print(withouth_dic[name][phone])
    


def censure_phone(fun_dict, name):
    personal_dict = fun_dict[name]
    if 'Phone_numb' in personal_dict:
        personal_dict['Phone_numb'] = None
    print(fun_dict[name]['Phone_numb'])
    
#%%
    
#Number and String, Medium (requires the use of lists or loops):Create a function that is 
#called “extract_number”, which takes a string as input, and return the first available 
#number in the string. If there is no number, it returns None.Input = 
#‘I have 3 apples’, returns -> 3input = ‘the price is 53.73’, returns -> 53.73


text =  "I have 3 apples and 2 lemons"

def extract_number(text):
    for word in text:
        try:
            word.isnumeric():
            print(float(word))
            break
        except:
            pass
    
#%%
string= "I have 3 apples and 2 lemons"
    
def extract_number(string):
    words = string.split(" ")
    for word in words:
        if word.isnumeric():
            print(float(word))
            break
        else:
            pass
         

#%%
    
import random

def roll_die():
    ones = 0
    twos = 0
    threes = 0
    fours = 0
    fives = 0
    sixes = 0
    for i in range(1, 10):
        dice = random.randint(1,7)
        if dice == 1:
            ones = ones + 1
        elif dice == 2:
            twos = twos + 1
        elif dice == 3:
            threes = threes + 1
        elif dice == 4:
            fours = fours + 1
        elif dice == 5:
            fives = fives + 1
        elif dice == 6:
            sixes = sixes + 1
    print(ones)
    print(twos)
    print(threes)
    print(fours)
    print(fives)
    print(sixes)
    



