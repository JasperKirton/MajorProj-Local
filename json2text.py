#import sys
import json
#from pprint import pprint
from os import listdir
import re
#from os.path import isfile, join

# This works as per folder recursively

docs = []

dirIter = [0, 0]  # stores decimal values for iteration
counter = 1


for i in range(16):  # for each 16 folders
        for j in range(16):  # max 44 files in sub folders?
            dirIter = [i, j]  # current location
            print(dirIter)
            dirIter = ''.join("{:01X}".format(a) for a in dirIter)  # convert to hex for indexing
            print(dirIter)
            # index into reviews folder using hex
            docs = [f for f in listdir(
                '/Users/jasperkirton/Downloads/critiquebrainz-20160611-cc-by-nc-sa-30-json/reviews/' + str(dirIter[0]) + '/' + str(dirIter[0]) + str(dirIter[1])) if f.endswith('.json')]

            # Printing the List of all Json Files loaded into the Memory
            for x in docs:
                print(x)
            for x in docs:
                with open('/Users/jasperkirton/Downloads/critiquebrainz-20160611-cc-by-nc-sa-30-json/reviews/' + str(
                        dirIter[0]) + '/' + str(dirIter[0]) + str(dirIter[1]) + '/' + x) as data_file:
                    data_item = json.load(data_file)
                    b = data_item['reviews']
                    for item in b:
                        name = '' + str(counter) + '.txt'
                        file = open(name, 'wb')
                        output = item['text']  # this field changes from 'entity_id' to 'text for MBID/review retrieval
                        output = " ".join(output.split())  # this concatenates the paragraphs
                        output = re.sub(r"http\S+", "", output)  # this removes URLs from the file
                        counter = counter + 1
                        file.write(output.encode('utf-8'))
                        file.close()


