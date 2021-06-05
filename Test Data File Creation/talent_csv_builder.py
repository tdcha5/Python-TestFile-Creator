# -*- coding: utf-8 -*-
"""
Created on Sat May 22 09:18:55 2021

@author: torid

"""
import names
import random as rand
import datetime
todaysDate = str(datetime.date.today())

"""
    Needs: 
    # Choose a random first, last name
    # Create a faux email address using mailinator (lastname_firstinitial_rstest_randomnumber@mailinator.com)
    # After gathering the name, generate the CSV format 
    # CSV Format: 
        Header: firstname,lastname,email,phone
        Following rows: random first and last name, generated email and phone

"""

class Talent:
    """ Point class for representing and manipulating x,y coordinates. """
    # clean up 
    
    def __init__(self, firstName, lastName, phone):
        """ Create a new point at the given coordinates. """
        self.firstName = firstName
        self.lastName = lastName
        self.phone = phone
        
    def talFirstName(self):
        # random select first name         
        for nameChoice in range(len(names.firstnames)):
            countOfNames = len(names.firstnames)
            firstNamePick = rand.randint(0,(countOfNames-1))
            talFirstName = names.firstnames[firstNamePick]
        return talFirstName
    
    def talLastName(self):
        countFamilyName = len(names.lastnames) - 1
        chooseFamilyName = rand.randint(0,countFamilyName)
        lastName = names.lastnames[chooseFamilyName]
        return lastName
    
    def talPhone(self):
        phone = "000-"+ str(rand.randint(100,999)) + "-" + str(rand.randint(1000,9999))
        return phone
    
def createFile(talentsToAdd):
    rowCount = 0
    
    if(talentsToAdd == 0):       
       print("There must be at least 1 talent requested to build a file.")
    elif(talentsToAdd > 0):
        fileName = "testfiles\\" + (str(talentsToAdd)) + "_Talents" + str(rand.randint(10000,99999)) + ".csv"
        print(fileName)
         
        testFile = open(fileName, "w")
        # print top row
        testFile.write("firstName,lastName,emailAddress,phoneNumber" + '\n')
        for i in range(talentsToAdd):
            TalentDetails = Talent(" ", " "," ")
            firstName = str(TalentDetails.talFirstName())
            lastName = str(TalentDetails.talLastName())
            
            # clean up class to acquire the firstName
            email = ""
            email += lastName.lower() + "_"
            email += firstName[0:3].lower()
            email += "_rstest0" + str(rand.randint(10000,99999))
            email += "@testRandomURL.com"
            
            row = ""
            row += firstName + ","
            row +=  lastName + "," 
            row += email + ","
            row += TalentDetails.talPhone() + ""
            testFile.write(row + '\n')
            rowCount += 1
            # print(row)
    print(rowCount, " talents generated and added to the file")
    
    # Add lines to report to track how many times I have used this tool
    reportingFile = open("reportingFile.txt","a")
    newLineinReporting = "" 
    newLineinReporting += '\n'
    newLineinReporting += todaysDate + " " + str(rowCount)
   # print(newLineinReporting)
    reportingFile.write(newLineinReporting)
    reportingFile.close()
    testFile.close()
