import os

def main(): 
    i = 0
    path = str(input("Input your path address"))
    #path = "C:/Users/USER/Pictures/pypic/"
    File_name = str(input("Enter General File name"))
    File_format = str(input("Enter File Format"))
    for filename in os.listdir(path):
        my_dest =  File_name + str(i) + File_format
        my_source = path + filename
        my_dest = path + my_dest
        os.rename(my_source, my_dest)
        i +=1
if __name__ == '__main__':
    main()
