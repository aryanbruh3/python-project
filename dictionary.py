#dict() or {key:value}to store elements
# method with examples
product={"pid":9001,"mobile":"samsung","price":90000,"pid":9001,"mobile":"samsung","price":90000}
print(type(product))
for i in product.keys():
    print(i,end=" ")
print("\r")
for i in product.values():
    print(i,end=" ")
print("\r")
print("----------------------")
for key,value in product.items():
    print(key,"=",value)
# .copy()
# fromkeys():
print("to add keys and values")
keys=('a','b','c')
value=4
new_dict=dict.fromkeys(keys,value)
print(new_dict)
#get()->to find out the value
print("product is=",new_dict.get('a'))
#pop()->here we have to tell the key that what key you wanted to delete
d={'name':'ram','age':19}
d.pop('age')
print(d)
#
key=input("enter the data you wanted to delte")
print("old data")
print(product)
product.pop(key)
print("new data")
print(product)
#popitem()-to delte the last data or key from the dictionary
product.popitem()
print("remaining data after delte last record")
print(product)
#setdefault->return the value of a key if it is in the dictionary
d={'name':'ram'}
d.setdefault('name',"vaibhav")
print(d)
#update()->to update in the first dictionary
#clear()->to delete full dictionary
#del keyword->to delete whole dict.with structure and data
student={}
stu=[]
a=int(input("how much student record you want to store"))
for i in range(1,a+1,1):
    print(f"enter {i} student record")
    student["name"]=input("enter the name")
    student["rollno"]=int(input("enter rollno"))
    student["age"]=int(input("enter age"))
    stu.append(student)
    student={}
while(True):
    print("----------------------menu---------------------")
    print("1-view all records\n2-update record one or multiple\n3-add new record\n4-delte record\n5- search by roll no.")
    ch=int(input("enter your choice"))
    if ch==1:
        for k in range(0,len(stu),1):
            for key,value in stu[k].items():
                print(key,":",value)
    if ch==2:
        index=int(input("which student record you want to update"))
        index=index-1
        for i in stu[index].keys():
            print(i)
        g=int(input("how much student record you want to update"))
        if g==1:
            key=input("select key name you want to update")
            value=input("enter the value for which you choose to update")
            stu[index][key]=value
        elif g>1:
            l=int(input("which of the student you want to update"))
            for i in range(g):
                print(f"enter {i+1}  student for updation")
                key=input("select key name you want to update")
                value=input("enter the value for which you choose to update")
                stu[index][key]=value
    if ch==3:
        m=int(input("how much student you want to add"))
        for i in range(0,m,1):
            student["name"]=input("enter the name")
            student["rollno"]=int(input("enter rollno"))
            student["age"]=int(input("enter age"))
            stu.append(student)
        print("new record added")
    if ch==4:
        j=int(input("which student record you wanted to delete"))
        for i in stu:
            print(i)
        stu.pop(j-1)
    if ch==5:
        k=int(input("enter roll number you want to search"))
        for i in range(0,len(stu),1):
            if stu[i]["rollno"]==k:
                print("roll number founded in the dictionary ")
                print(stu[i]["name"])
                print(stu[i]["age"])


        
            
            

            







