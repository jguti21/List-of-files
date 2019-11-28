import os

os.chdir('C:/Users/gutierj/Desktop/Tmp')
with open('list.csv', 'w') as csvlist:
    for root, dirs, files in os.walk("C:/Users/gutierj/Desktop/Tmp"):
        for file in files:
            if file.endswith(".pdf"):
                csvlist.write(file)
                csvlist.write('\n')
    csvlist.close()            
                           