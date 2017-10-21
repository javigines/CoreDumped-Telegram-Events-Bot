#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import listdir, sep                                 ## System module
from os.path import isfile, join, dirname, abspath          ## System module
import datetime                                             ## System module
from pathlib import Path                                    ## pip install pathlib

import database as db                                       ## Own module


"""
The file database is done with this structure.
    month/day.pkl --> {@username:Year}

"""


dirSep = sep
mainDirectory = dirname(abspath(__file__)) + dirSep + 'Birthday' + dirSep

# Check if Birthday is already saved
def checkBirthday(username) :
    birthday = listBirthday()
    if birthday is not None and username in birthday.keys():
        return True
    return False

# Check who the birthday is today or if before is True who  is the birthday tomorrow
def nextBirthday(before) :
    date = datetime.date.today()
    if before:
        file = db.load_obj(mainDirectory + date.strftime("%m") + dirSep + str(int(date.strftime("%d"))+1) + ".pkl")
    else:
        file = db.load_obj(mainDirectory + date.strftime("%m") + dirSep + date.strftime("%d") + ".pkl")

    if not file:
        return None
    
    result=[]
    i=0
    while(i<len(file)):
        result += [list(file.keys())[i] + ':' + list(file.values())[i]]
        i+=1
    return result


# Add a new birthday to the database
def addBirthday(username, date):
    if not checkBirthday(username):
        try:
            newFile(date)
            data = db.load_obj(mainDirectory + str(int(date.split('/')[1])) + dirSep + str(int(date.split('/')[0])) + '.pkl')
            data[username] = date.split('/')[2]
            db.save_obj(data, mainDirectory + str(int(date.split('/')[1])) + dirSep + str(int(date.split('/')[0])) + '.pkl')
            return True
        except:
            return False
    else:
        return False


# Remove birthday from database
def removeBirthday(username):
    if checkBirthday(username):
        date = dict(listBirthday()).get(username)
        if(date != None):  # Birthday should be here but better check it
            data = db.load_obj(mainDirectory + str(int(str(date).split('/')[1])) + dirSep + str(int(str(date).split('/')[0])) + '.pkl')
            data.pop(username, None)
            db.save_obj(data, mainDirectory + str(int(str(date).split('/')[1])) + dirSep + str(int(str(date).split('/')[0])) + '.pkl')
            return True
    return False


# Return a Birthday List with every birthday in the database
def listBirthday():
    birthdayList = {}
    i = 1
    while(i<13):
        onlyfiles = [f for f in listdir(mainDirectory + str(i) + dirSep) if not f.startswith('.') and f != "" and isfile(join(mainDirectory + str(i) + dirSep, f))]
        j=0
        while(j<len(onlyfiles)):
            cumpleFile = db.load_obj(mainDirectory + dirSep + str(i) + dirSep + onlyfiles[j])
            if (cumpleFile != '' and cumpleFile != {} and  isinstance(cumpleFile, dict)):
                k=0
                while(k<len(cumpleFile)):
                    birthdayList[list(cumpleFile.keys())[k]] = (onlyfiles[j].replace(".pkl", "")+'/'+str(i)+'/'+list(cumpleFile.values())[k])
                    k+=1
            j+=1
        i+=1
    return (birthdayList if (birthdayList != {}) else None)
        

# Create day file if is not created
def newFile(date):
    my_file = Path(mainDirectory + str(int(date.split('/')[1])) + dirSep + str(int(date.split('/')[0])) + '.pkl')
    if not my_file.is_file():
        db.save_obj({}, mainDirectory + str(int(date.split('/')[1])) + dirSep + str(int(date.split('/')[0])) + '.pkl')


print("BirthdayManager Module Loaded Correctly.")

