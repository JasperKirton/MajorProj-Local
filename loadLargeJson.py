import numpy as np
import pandas as pd

# create a store
store = pd.HDFStore('releaseStore.h5')

# this is the key to your storage:
#    this maps your fields to a specific group, and defines
#    what you want to have as data_columns.
#    you might want to create a nice class wrapping this
#    (as you will want to have this map and its inversion)
group_map = dict(
    A = dict(fields = ['field_1','field_2',.....], dc = ['field_1',....,'field_5']),
    B = dict(fields = ['field_10',......        ], dc = ['field_10']),
    .....
    REPORTING_ONLY = dict(fields = ['field_1000','field_1001',...], dc = []),

)

group_map_inverted = dict()
for g, v in group_map.items():
    group_map_inverted.update(dict([ (f,g) for f in v['fields'] ]))




for f in files:
   # read in the file, additional options hmay be necessary here
   # the chunksize is not strictly necessary, you may be able to slurp each
   # file into memory in which case just eliminate this part of the loop
   # (you can also change chunksize if necessary)
   for chunk in pd.read_table(f, chunksize=50000):
       # we are going to append to each table by group
       # we are not going to create indexes at this time
       # but we *ARE* going to create (some) data_columns

       # figure out the field groupings
       for g, v in group_map.items():
             # create the frame for this group
             frame = chunk.reindex(columns = v['fields'], copy = False)

             # append it
             store.append(g, frame, index=False, data_columns = v['dc'])


