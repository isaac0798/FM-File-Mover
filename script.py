import os, fnmatch, shutil

result = []
print('Checking files...')
path = '/Users/isaactennant/Downloads/'
dest = '/Users/isaactennant/Desktop/'

for root, dirs, files in os.walk(path):
    for file in files:
        if (fnmatch.fnmatch(file, '*.fmf')):
            print('file match: ' + file)
            shutil.move(os.path.join(path, file), os.path.join(dest, file))
            print('Moved ' + path + file + ' To Desktop')

    for dir in dirs:
        print('Checking: ' + dir)
        for root, dirs, files in os.walk(root + dir):
            for file in files:
                if (fnmatch.fnmatch(file, '*.fmf')):
                    print('file match: ' + file + ' in ' + dir)
                    shutil.move(path + dir + '/' + file, dest + dir +'/' + file)
                    print('Moved ' + path + file + ' To Desktop')