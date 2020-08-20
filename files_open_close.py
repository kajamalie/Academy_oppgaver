# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 12:24:34 2020

@author: Kaja Amalie
"""
#%%

simple_file = open(file = 'simple.txt', mode ='r')
text = simple_file.readlines()
simple_file.close()

#%%

# for å være sikker på at filen lukker seg er det lurst å bruke denne: 

with open(file = 'simple.txt', mode ='r') as simple_file2:
    text = simple_file2.readlines()

#%%
    
    
with open(file = 'simple.txt', mode ='w+') as simple_file_w:
    simple_file_w.writelines('dette er en ny en igjen, ')
    simple_file_w.writelines('dette er mer')
    
#%% 
with open(file = 'simple.txt', mode = 'r') as read_file:
    text = read_file.readline()
    
#%%

#Pickle: du kan lagte en hel 
    
 import pickle
 
 my_list = [1,45,56,32,5,6,7,43]
 
 with open('test_pickle.pickle', mode = 'wb') as my_file:
     pickle.dump(my_list, my_file )

#%%

 with open('test_pickle.pickle', mode = 'rb') as my_file:
     my_loaded_list = pickle.load(my_file)
     
#%%
machinelearning_model = get_mr()