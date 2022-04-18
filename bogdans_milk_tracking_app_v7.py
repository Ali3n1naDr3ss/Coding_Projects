#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 15:52:42 2022

@author: holly
"""

"""
Possible bugs:
phone number too long
phone number too short
phone number does not start with 07

"""

import csv

"""
def milk_app_options(file):
    with open(file, 'a', newline='') as milk_data:
        for option in range(1, 3):
            option = input()
            # option = int(option) # C error with char vs float. type(number)= str ????
            if option == '1':
                return "code to view all data"
            elif option == '2':
                add_new_data()  # class
            # call function
            elif option == '3':
                return 'code for exit file'
            else:
                return 'different option:'
"""


class MilkTracker:
    def __init__(self):
        print(
            '\nWhat do you want, you idiot?'
            '\nSelect Option 1 to View all sales.'
            '\nSelect Option 2 to Add new sale.'
            '\nSelect Option 3 to Exit.')

    def milk_app_options(self, option):
        # option = int(option) # C error with char vs float. type(number)= str ????
        if option == 1:
            return "code to view all data"
        elif option == 2:
            self.add_new_data()
        # call function
        elif option == 3:
            return 'code for exit file'
        else:
            return 'different option:'

    # Option 1
    def view_data(self, file_name):
        with open(file_name) as milk_data:
            for i in csv.reader(milk_data):
                print(', '.join(i))

    # Option 2
    def add_new_data(self):
        print("Do ya wanna add a Customer Name?")
        response1 = input("Press 'Y' to add. Press 'N' to skip.\n")

        print("Do ya wanna add a Customer Contact?")
        response2 = input("Press 'Y' to add. Press 'N' to skip.\n")

        print("Do ya wanna add an Order Number?")
        response3 = input("Press 'Y' to add. Press 'N' to skip.\n")

        print("Do ya wanna add an Order Value?")
        response4 = input("Press 'Y' to add. Press 'N' to skip.\n")
        
        all_responses = {ShouldAddCNa:response1, ShouldAddCNu:response2, ShouldAddONu:response3, ShouldAddOVa:response4}
# if any response == Y, open file
        #if all == N, go back to main menu
        if response1 == (N or n) and response2 == (N or n) and response3 == (N or n) and response4 == (N or n):
            print('You don\'t want to change anything. Go back to main menu?')
            response5 = input("Press 'Y' to go back. Press 'N' to choose again.\n")
            # loop over add_new_data
        elif response1 == (Y or y) or response2 == (Y or y) or response3 == (Y or y) or response4 == (Y or y):
            print('You want to change some stuff. cool lol')
            
        else:
            # assume responses == Y (ifx issues or invalid input later)
            print("ya mum gay")
            
        for response in all_responses:
        #create a dict of responses and if the entry for response 1 is yes then add name to new row
        # loop over dictionary/ check through all dict entries
        if response1 == (Y or y): 
        print('Enter a new Customer Name.')
            NewCustomerName = input("Your entry:\n")
        if response2 == (Y or y):     
            print('Enter a new Customer Contact.')
            NewCustomerContact = input("Your entry:\n")
            
            print('Enter a new Order Number.')
            NewOrderNumber = input("Your entry:\n")
            
            print('Enter a new Order Value.')
            NewOrderValue = input("Your entry:\n")
            
        #new row to be appended to csv
        New_Data = all_responses{ShouldAddCNa:NewCustomerContact, ShouldAddCNu:NewCustomerContact, ShouldAddONu:NewOrderNumber, ShouldAddOVa:NewOrderValue}
            

            
            #with open(file, 'a', newline='') as milk_data:
             #   milk_data.Write(NewName)
                
   # def add_new_customer(self, name, contact, number, value):
        #print("code")


# new_customer = {'name': opt2name, 'contact': opt2contact, 'number': opt2number, 'value': opt2value}
# MilkTracker

# TODO!
'''
option 1
options 2.1,2.2,2.3
option 3
'''
