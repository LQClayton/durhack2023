def file_handle(filename):
    with open(filename, 'r') as f:
        x = f.readlines()
    f.close()
    x = clean_list(x)
    return x

def clean_list(myList):
    for i in range(len(myList)):
        myList[i] = myList[i].replace('\n','')
    return myList

def brain_no_function():
    myFile1 = file_handle('emotions.txt')
    myFile2 = file_handle('phrases.txt')
    print(myFile1, myFile2)




brain_no_function()