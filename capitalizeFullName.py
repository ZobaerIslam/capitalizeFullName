#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 11:43:01 2020

@author: zim
"""

# Define wordCapital as Outer function
def word_capital(fullName):
    """Returns the full name with capital word."""
    
    # Define local variable and assign empty string
    sentence = ''
    
    # Split full name
    list_name = fullName.split(' ')
    
    # Define capit() as Inner function
    def capit(word):
        """Concatenate capital word"""
        
        # Access local variable by nonlocal keyword
        nonlocal sentence
        
        # Concatenate word
        if sentence == '' :
            sentence = sentence + word.capitalize()
        else :
            sentence = sentence + ' ' + word.capitalize()
    
    # Iterate over list_name 
    for word in list_name:
        # Call inner function
        capit(word)
    
    # Return the full name with capitalize
    return sentence

# Call word_capital() with passing full name and assign return value in: fname
fName = word_capital("golam martuza shimul")

# Print fName
print(fName)