#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Gabriel Santos IS- 211 9/05/2020

import urllib.request
import urllib
import csv
import argparse
import sys
import datetime
import logging
import urllib2

"""
Part I ­ Think about Design
When approaching programming problems, you should first step back and think about the problem at hand.
What exactly are we trying to accomplish, and what would be a good structure for your program? How would
you break the larger problem into a set of smaller steps? One thing to think about in this case, is how you
will want to store this data after reading it from the CSV.
"""


"""Part II ­ Download the Data

1. Create function called downloadData that takes string called 'url.'
    a. Use urllib2 to download content at the url and return it to the
    caller.
"""
 
def downloadData(url):
    info = urllib.request.urlopen(url).read().decode
    return info
 
"""Part III ­ Process Data

1. Write a function called processData that takes the file's contents as the
 first parameter,
process it line by line, and returns a dictionary.
2. It should return a tuple consisting of the name and birthday.
    a. The birthday should be converted into a Datetime object
     ('dd/mm/yyy' format)
3. If the data is missing or incorrect (e.g. invalid date), it should be
placed on a log called assignment 2'
4. The log mess should sent an error level message which states error processing
line # for ID #.""""

def processData(df):
    downloadData(url)
    global dict
    LOG_FILENAME = 'errors.log'
    logging.basicConfig(filename=LOG_FILENAME, level=logging.ERROR)
    dict = {}
    for ind in df.index:
        import datetime
        try:
            i = df['id'][ind]
            n = df['name'][ind]
            b = df['birthday'][ind]
            converted_date = datetime.datetime.strptime(b, '%d/%m/%Y').strftime("%x")
            dict.update({i: (n, converted_date)})
            except Exception as e:
                i = df['id'][ind]
                row = df.index[i]
                
                logging.error("Error processing line # {} for ID# {}: Exception Detail: {}".format(row, i, e), exc_info=True)
                pass
            
        print(dict)
        
"""Part IV ­ Display / User Input

1. Write a function called displayPerson that takes the first parameter, id as an integer
 and the second parameter as a dictionary called personData.
2. The function should return the name and birthday of the given user or
 display a message: Person # is <name>  with a birthday of <date>.
 """
def displayPerson(id):
        import sys
        processData(df)
        if id <= 0:
            sys.exit()
            else:
            try:
                print("Person #{} is {} with a birthday of {}".format(id, dict[id][0], dict[id][1]))
                except KeyError:
                    print("No user found with that id")
                    pass
                

                
""" Part V ­ Putting it all Together
1. Call the downloadData()function
2. The URL to pass to downloadData()is the URL given as a parameter to the script via argparse.
3. We need to set up a logger with the name ‘assignment2’
4. we need to take csvData and pass it to the processData()function.
5. use displayPerson()"""
                
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help='The url to find the birthday csv file', type=str)
    args = parser.parse_args()
    assignment2()  # function for initializing logger
    try:
        csvData = downloadData(args.url)
    except:
        logging.critical('{0}:  unable to resolve URL {1}'.format(sys.exc_info(), args.url))
        print('An error has occurred, Please see error log.')
        exit()
    try:
        csvData = processData(csvData)
    except:
        logging.critical('{0}:  Unresolvable processing error with file {1}'.format(sys.exc_info(), csvData))
        print('An error has occurred, Please see error log.')
        exit()

    while True:
        idlookup = int(input("Please enter an ID to lookup, or type 0 or a negative number to quit: "))
        displayPerson(idlookup, csvData) if idlookup > 0 else exit()


main()


# In[ ]:


downloadData(url)


# In[ ]:


processData(df)


# In[ ]:


displayPerson(3)

