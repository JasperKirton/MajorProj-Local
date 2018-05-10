import pandas as pd
import ijson
import pickle

from json import JSONDecoder
from functools import partial

# output = open('exampleOutput.txt', 'a')
# input = MBID  # to do: index from the review


filename = "/Volumes/jaspers hdd/mbdump/release"
release_data = []

# https://stackoverflow.com/questions/21708192/how-do-i-use-the-json-module-to-read-in-one-json-object-at-a-time
def json_parse(fileobj, decoder=JSONDecoder(), buffersize=2048):
    buffer = ''
    for chunk in iter(partial(fileobj.read, buffersize), ''):
        buffer += chunk
        while buffer:
            try:
                result, index = decoder.raw_decode(buffer)
                yield result
                buffer = buffer[index:]
            except ValueError:
                # Not enough data to decode, read more
                break



with open(filename, 'r') as f:
    #objects = ijson.items(f, 'item')
    for row in json_parse(f):
        selected_row = dict()
        selected_row = {"id": row["id"]}
        release_data.append(selected_row)


release_df = pd.DataFrame.from_dict(release_data)
pickle_out = open('release_data.pickle', 'wb')
pickle.dump(release_df, pickle_out)
pickle_out.close()

#release_df = pd.read_pickle('release_data.pickle')