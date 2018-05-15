import requests
import json
import time
import os
from pathlib import Path
from natsort import natsort_keygen, ns
import re

#reduc = jq(".[].name").transform(json.loads(r.text))

#print(data[])

# id checker

check = '14DV5JzgIRhtqMMjtO4QOj'
headers = {'Authorization': 'Bearer BQBpGKn7fyQM3wTOVWiMgZrGlZUYHdrRn7UM-EThvx9qfBrxGZYmK09u_nvA7Pp8gXByh77JrgrLvfDPczs'}
r = requests.get('https://api.spotify.com/v1/albums/' + str(check), headers=headers)
check_r = json.loads(r.text)  # loads json data from API response
print(check_r)



artistDict = {}

# iterate through idDict, append

# currentField = {str(uri): name}


files = []

MBIDcorpus = []

# Create search indexes from corpus:
directory = os.fsencode("MBIDs")
'''
for file in os.listdir("MBIDs"):
    #if filename.endswith(".txt")
    filename = os.fsdecode(file)
    files.append(filename)
'''
#natsort_key = natsort_keygen(key=lambda y: y.lower())
#sorted_files = files.sort(key=natsort_key)
#print(files)

for filenum in range(1, 8476):
    #filenum = filename.split(".txt", 1)
    filename = str(filenum) + ".txt"
    #print(filenum[0]) # why is this being weird?
    cur_id = Path("MBIDs/" + filename).read_text()
    MBIDcorpus.append(cur_id)


print(MBIDcorpus)



# clean based on MBIDcorpus


idList = []
with open('mbspotify-mapping-2018-04-18', 'r') as f:
    idList = f.readlines()


for i in range(0, len(idList)):
    idDict = dict(zip(idList[i].split('\t', 4), idList))


MBIDs = [x.split()[1] for x in idList]
#print(MBIDs)

AlbumIDs = [x.split()[2] for x in idList]
#print(AlbumIDs)

idDict = dict(zip(MBIDs, AlbumIDs))

#print(idDict)


less = open("serveIDs2.txt", "a")

MBIDsPost = []
AlbumIDsPost = []

# could i fix this by iterating differently? uncomplete mapping problem


for i in range(len(MBIDcorpus)):
        if idDict.keys().__contains__(MBIDcorpus[i]):  # if MBID from corpus is in the mapping set
            # save uri from the relevant part of the field
            uri = idDict[MBIDcorpus[i]]
            #decoded_uri = encoded_uri.decode()
            #print(uri)
            MBIDsPost.append(MBIDcorpus[i])
            AlbumIDsPost.append(uri)
            less.write(str(uri) + "\n")
        else:
            less.write("unavai" + "\n")

# seems to be uncomplete mappings?


'''
for i in MBIDcorpus:
        if idDict.keys().__contains__(MBIDcorpus[i]):  # if MBID in MBIDcorpus
            # save uri from the relevant part of the field
            uri = idDict[MBIDcorpus[i]]
            #decoded_uri = encoded_uri.decode()
            #print(uri)
            MBIDsPost.append(MBIDcorpus[i])
            AlbumIDsPost.append(uri)
            if idDict[i] == mbspotify():  # AND if the mapping exists
                less.write(str(uri) + "\n")
            else:
                less.write("unavai")
'''
#idDictPost = dict(zip(AlbumIDsPost, MBIDsPost))

#print(idDictPost)



'''
f = open("sp_uri:artist_name-mapping.txt", "a")

artists = []
URIs = []

for sp_id in idDictPost.values():
    if sp_id.__contains__('spotify:album:'):  # for the hole in data sheet
        uriPost = sp_id.split('spotify:album:', 1)[1]
    else:
        uriPost = sp_id
    print(uriPost)
    time.sleep(0.03)
    # avoid over-requesting the API, leave for 45m - leaving ~15m till token expires.
    headers = {'Authorization': 'Bearer BQA5Gzl6qZjKy-DWA956ZiQSqFG_aStocZGmyV4y66jht70xPj76-aTSsTLe9GhHSm_lVy5Kj4LgMQMrirQ'}
    r = requests.get('https://api.spotify.com/v1/albums/' + str(uriPost), headers=headers)
    sp_data = json.loads(r.text)
    name = sp_data['artists'][0]['name']  # might not work so well if there are multiple artists
    artists.append(name)
    URIs.append(uriPost)
    #artistDict.update({str(uri): name})
    f.write(str(uriPost) + "    " + name + '\n')

uri_artistDict = dict(zip(artists, URIs))


aF = open("distinct_artists.txt",  "a")

# Extract the dictionary into a list of (key, value) tuples.
t = [(k, uri_artistDict[k]) for k in uri_artistDict]

# Sort the list -- by default it will sort by the key since it is
# first in the tuple.
t.sort()

# Reset the dictionary so it is ready to hold the new dataset.
d = {}

# Load key-values into the dictionary. Only the first value will be
# stored.
for k, v in t:
    if v in d.values():
        continue
    d[k] = v
    aF.write(str(d[k]))


print(d)

#type(data)
#print(r.text)
#print(artistDict.values())
'''