import sqlite3
import os

conn = sqlite3.connect('reviews.sqlite')
c = conn.cursor()
'''
c.execute('DROP TABLE release_db')

c.execute('CREATE TABLE release_db'\
          ' (mbid TEXT, release TEXT, cossim FLOAT, rating INTEGER) ')

example1 = 'song a'
c.execute("INSERT INTO release_db"\
          " (mbid, release, cossim, rating) VALUES"\
          " (?, ?, 1, 4)", (example1, 0))
example2 = 'song b'
c.execute("INSERT INTO release_db"\
          " (mbid, release, cossim, rating) VALUES"\
          " (?, ?, 0.5, 5)", (example2, 1))
conn.commit()
conn.close()
'''

c.execute("SELECT * FROM release_db")
results = c.fetchall()
conn.close()
print(results)