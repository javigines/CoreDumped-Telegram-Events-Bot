#!/usr/bin/env python
# -*- coding: utf-8 -*-


from os import listdir, sep                                 ## System module
from os.path import isfile, join, dirname, abspath          ## System module

import database as db
import birthdayManager.py as bm

# user_id, sort and manually inserted 
user_id_list = []

dirSep = sep
mainDirectory = dirname(abspath(__file__)) + dirSep + 'Birtday' + dirSep


# list and clean the old database
def listBirthday():
    birthdayList = {}
    i = 1
    while(i<13):
        onlyfiles = [f for f in listdir(mainDirectory + str(i) + dirSep) if not f.startswith('.') and f != "" and isfile(join(mainDirectory + str(i) + dirSep, f))]
        j=0
        while(j<len(onlyfiles)):
            cumpleFile = db.load_obj(mainDirectory + dirSep + str(i) + dirSep + onlyfiles[j])
            db.save_obj({}, mainDirectory + dirSep + str(i) + dirSep + onlyfiles[j])
            if (cumpleFile != '' and cumpleFile != {} and  isinstance(cumpleFile, dict)):
                k=0
                while(k<len(cumpleFile)):
                    birthdayList[list(cumpleFile.keys())[k]] =  (onlyfiles[j].replace(".pkl", "")+'/'+str(i)+'/'+list(cumpleFile.values())[k])
                    k+=1
            j+=1
        i+=1
    return (birthdayList if (birthdayList != {}) else None)


# add with the new format to the new database
def addBirthday(username, date, user_id):
    try:
        newFile(date)
        data = db.load_obj(mainDirectory + str(int(date.split('/')[1])) + dirSep + str(int(date.split('/')[0])) + '.pkl')
        data[user_id] = username + ":" + date.split('/')[2]
        db.save_obj(data, mainDirectory + str(int(date.split('/')[1])) + dirSep + str(int(date.split('/')[0])) + '.pkl')
        return True
    except:
        return False



def newFile(date):
    my_file = Path(mainDirectory + str(int(date.split('/')[1])) + dirSep + str(int(date.split('/')[0])) + '.pkl')
    if not my_file.is_file():
        db.save_obj({}, mainDirectory + str(int(date.split('/')[1])) + dirSep + str(int(date.split('/')[0])) + '.pkl')


oldBirthday = listBirthday()
i=0
while(i<len(oldBirthday)):
    addBirthday(list(oldBirthday.keys())[i],
                   list(oldBirthday.values())[i],
                   user_id_list[i])

print("Done")
