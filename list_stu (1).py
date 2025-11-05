stu=["vaibhav","Aryan"," Gaurav" ,"manish"," Shivi","Aryan"]
str="""
  0-view whole list record.
  1- add new Student Name  in a existing list.// run time how many student
  2- add new Student Name at a given position 
  3- delete last  Student Name from the list
  4- delete  Student Name  from  given index value.
  5- remove Student Name from the list        // check student name available then delete
  6- print the index position of any given  Student Name.
  7- find duplicate Student Name in a given list
  8- copy old list data to new list (backup copy)
  9-  create new list and add in existing list 
  10- print whole list in Reverse order
  11- print list in asc and desc order
  12-to clear whole list data
  13- to delete whole list permanent
  """
print(str)
ch=int(input("Enter Your choice:"))
while(1):
    if ch==0:
            
            for i in stu:
                 print(i)
    if ch==1:
              nm=input(" Enter  new student name:")
              stu.append(nm)
              print(" Name added in list")
              print(stu)

    if ch==2:
              nm=input(" Enter  new student name:")
              index=int(input("Enter Index position:"))
              stu.insert(index, nm)
              print(" Name added in  given position")
              print(stu)
    if ch==3:
             print(" Original Data")
             print(stu)
             stu.pop()
             print(" last student name deleted")
             print(stu)
    if ch==4:
             
              index=int(input("Enter Index position:"))
              stu.pop(index)
              print(" Name deleted from given index")
              print(stu)
    if ch==5:
           nm=input(" Enter  new student name:")
           stu.remove(nm)
           print(" Name Deleted")
           print(stu)
    if ch==6:
            
              nm=input(" Enter  new student name:")
              pos=stu.index(nm)
              print(nm, " found in ", pos)
    if ch==7:
           
              nm=input(" Enter  new student name:")
              n=stu.count(nm)
              if n>1:
                  print(nm, " found",n,"times")
              else:
                   print(nm, "  same name student not available")
    if ch==8:
           stu1=[]
           stu1=stu.copy()
           print(" Original data", stu)
           print(" Backup data:",stu1)
    if ch==9:
           stu2=["jay","vijay","Aman"]
           stu.extend(stu2)
           print(" Updated new data in old list")
           print(stu)

    if ch==10:
        print(" list in reverse order")
        print(stu.reverse())
    if ch==11:
          print(" Original Data",stu)
          stu.sort()
          print(" Name list in asc order")
          print(stu)
          print(" name list in decs order")
          print(stu[::-1])
    if ch==12:
           stu.clear()
           print(" all data deleted ")
           print(stu)
    if ch==13:
           del stu
           print(" All data with list is deleted permanent")
           print(stu)