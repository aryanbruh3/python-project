str="""
0- create new file
1- view student old data
2- to add new student data
3- view top two student data
4- view individual student data
5- view last student record
6- add student data
7- dalete student data
8- delete whole data from student record
9- dalete complete file with data
10- update student data
"""
import os

def get_txt_filenames(directory_path):
        
            txt_files = []
            try:
                # List all entries in the directory
                for entry in os.listdir(directory_path):
                    # Construct the full path to the entry
                    full_path = os.path.join(directory_path, entry)
                    
                    # Check if it's a file and ends with .txt
                    if os.path.isfile(full_path) and entry.lower().endswith('.txt'):
                        txt_files.append(entry)
            except FileNotFoundError:
                print(f"Error: Directory not found at '{directory_path}'")
            except Exception as e:
                print(f"An error occurred: {e}")
            return txt_files

        # Example usage:
folder_path = "C:/Users/hp/OneDrive/Desktop/python coaching"  # Replace with your actual folder path
txt_filenames = get_txt_filenames(folder_path)

if txt_filenames:
            print(f"Text files in '{folder_path}':")
            for filename in txt_filenames:
                print(filename)
else:
            print(f"No .txt files found in '{folder_path}' or directory does not exist.")

while(1):
    print(str)
    ch=int(input("enter your choice = "))
    if ch==0:
        filename=input("enter new file name with extension = ")
        myfile=open(filename,"w")
        myfile.write("rollno")
        myfile.write("\t")
        myfile.write("name")
        myfile.write("\t")
        myfile.write("age")
        print("file created successfully")
        myfile.close()

    if ch==1:



        filename1=input("Enter file name to view data = ")
        myfile=open(filename1,"r")
        filedata=myfile.read()
        print(filedata)
        myfile.close()
    
    if ch==2:
        myfile=open(filename1,"a+")
        newroll=input("enter student rollno u want to add = ")
        newname=input("enter student name u want to add = ")
        newage=input("enter student age u want to add = ")
        myfile.write("\n"),
        myfile.write(newroll),
        myfile.write("\t"),
        myfile.write(newname),
        myfile.write("\t"),
        myfile.write(newage),
        print("added successfully")
        myfile.close()
    
    if ch==3:
        myfile=open(filename1,"r")
        print(myfile.readline())
        print(myfile.readline())
        print(myfile.readline())
        myfile.close()

    if ch==4:
        lineno=int(input("enter which student data u want to see = "))
        myfile=open(filename1,"r")
        print(myfile.readline())
        data=myfile.readlines()
        print(data[lineno-1])
        
        
        myfile.close()

    if ch==5:
        myfile=open(filename1,"r")
        print(myfile.readline())
        data=myfile.readlines()
        print(data[len(data)-1])
        myfile.close()

    if ch==6:
          newroll1=input("enter new student roll no u want to add = ")
          newname1=input("enter new student name no u want to add = ")
          newage1=input("enter new student age no u want to add = ")
          myfile=open(filename1,"a+")
          myfile.write("\n")
          myfile.write(newroll1)
          myfile.write("\t")
          myfile.write(newname1)
          myfile.write("\t")
          myfile.write(newage1)
          print("stored successfuly")

    if ch==7:
        #   myfile=open(filename1,"r")
        #   myfile=open(filename1,"w")
        #   n=int()
        a1=[]
        lineno1=int(input("enter which student data u want to delete = "))
        myfile=open(filename1,"r")
        data=myfile.readlines()
        data.pop(lineno1)
        a1.append(data)
        myfile.close()
        myfile=open(filename1,"w")
        for i in a1:
            for k in i:
                myfile.write(k)
                myfile.write("\t")
        print("deletd successfuly")
        myfile.close()

    if ch==10:
        a1=[]
        roll=input("enter rollno of student u want to update data = ")
        myfile=open(filename1,'r')
        data=myfile.readlines()
        #a1.append(data)
        print(data[0])
        print(data[1])
        print(data[2])
        print(data[3])
        a2=[]
        for i in range(0, len(data),1):
             a2.append(data[i].split())
        print(a2)

        print(a2[1][1])
        a2[1][1]='arya'
        print(a2[1][1])
       

       



        """count=0
        for i in a1:
            count+=1
            for k in i:
                if roll==k[0]:
                    print("found")
                    count1=count
                    a2=[]
                    dat=int(input("enter what data u want to update (name(1) or age(2))= "))
                    myfile=open(filename1,"r")

                    data=myfile.readlines()

                    if dat==1:
                         nm=input("enter name = ")
                         print(a1[count1][k[1]])
                         a1[count1][k[1]]=nm
                         
                         print("name updated")
                    a2.append(data)
                    # print(a2)
                    # myfile.close()
                    # myfile=open(filename1,"w")
                    # for j in a2:
                    #     for c in j:
                    #         myfile.write(c)
                    #         myfile.write("\t")
                    # print("updated successfuly")
                    # myfile.close()
                    break
        """