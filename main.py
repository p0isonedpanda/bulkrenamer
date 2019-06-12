import os

ext = input('choose extension to rename: ')
prefix = input('choose prefix for files: ')

# get list of files to rename
files = list(filter(lambda f: ext in f, os.listdir()))

for i in range(len(files)):
    os.rename(files[i], prefix + str(i + 1) + ext)

print('done!')
