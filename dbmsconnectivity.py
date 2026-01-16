import mysql.connector

print("driver loaded")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="e-commerce"
)

print("connected successfully")

mycursor=mydb.cursor()

print("1 - add stock name\n2 - add product\n3 - customer reg\n4 - order place with billname\n" \
"5 - view cus details by cusid\n6 - cus billing details by order id\n7 - details by order id")
ch=int(input("enter your choice = "))
if ch==1:
    stnm=input("enter stock name u want to add= ")
    sql="insert into stock_cat(stockcatnm) values('%s')" %(stnm)
    mycursor.execute(sql)
    mydb.commit()
    print("record inserted")

if ch==2:
    prnm=input("enter product name,price,stock id u want to add= ")
    sql="insert into product(prodnm,prodprice,stockid) values(%s,%s,%s)" %(prnm)
    mycursor.execute(sql)
    mydb.commit()
    print("record inserted")

if ch==3:
    prnm=input("enter customer reg u want to add= ")
    sql="insert into customer(cusnm,qnt,mobno,prodid) values(%s,%s,%s,%s)" %(prnm)
    mycursor.execute(sql)
    mydb.commit()
    print("record inserted")

if ch==4:
    prnm=input("enter order date and cus id of order u want to add= ")
    sql="insert into product(orddate,cusid) values(%s,%s)" %(prnm)
    mycursor.execute(sql)
    mydb.commit()
    print("record inserted")

if ch==5:
    mycursor.execute("SELECT cusid FROM customer")

    myresult = mycursor.fetchall()
    print(myresult)



    cusid=int(input("enter customer id = "))
    t=0
    
    for id in myresult: 
       print(id)
       
       
       if cusid == id[0]:
        t=1
        sql="select * from customer where cusid=%s" %(cusid)
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
        break
        
    
    if t==0:
         print(" record not found")

if ch==6:
    ordid=int(input("enter order id = "))
    sql="SELECT cusid FROM order_table where ordid=%s" %(ordid)
    mycursor.execute(sql)

    myresult = mycursor.fetchone()
    print(myresult)

    if myresult is None:
        print("record not found")
    else:
        cusid = myresult[0]   
        print("customer id = ", cusid)

    sql="SELECT * FROM customer WHERE cusid = %s" %(cusid)
    mycursor.execute(sql)
    customer = mycursor.fetchall()

    for x in customer:
        print(x)    
    
if ch==7:
    list=[]
    ordid=int(input("enter order id = "))
    list.append(ordid)
    sql="select cusid from order_table where ordid=%s" %(ordid)
    mycursor.execute(sql)
    myresult=mycursor.fetchone()
    for x in myresult:
        print(x)
    list.append(x)

    sql="select prodid from customer where cusid=%s" %(x)
    mycursor.execute(sql)
    myresult=mycursor.fetchone()
    for y in myresult:
        print(y)
    list.append(y)

    sql="select stockid from product where prodid=%s" %(y)
    mycursor.execute(sql)
    myresult=mycursor.fetchone()
    for z in myresult:
        print(z)
    list.append(z)

    print(list)

    sgl="SELECT stock_cat.stockcatnm, product.prodnm,product.prodprice,customer.cusnm," \
    "customer.qnt,customer.mobno,order_table.orddate,order_table.ordid FROM order_table " \
    "INNER JOIN customer on customer.cusid=%s and order_table.cusid=%s " \
    "INNER JOIN  product on product.prodid=%s and customer.prodid=%s " \
    "INNER JOIN  stock_cat on stock_cat.stockid=%s and product.stockid=%s"%(list[1],
    list[1],list[2],list[2],list[3],list[3])
    mycursor.execute(sgl)
    result3=mycursor.fetchall()
    if result3:
            print(result3)
            print("----------------Billing Details------------")
            print(" Order date = ",result3[0][6])
            print(" Order ID = ",result3[0][7])
            print(" Stock Name = ",result3[0][0])
            print(" item Name = ",result3[0][1])
            print(" item price = ",result3[0][2])
            print(" Customer Name = ",result3[0][3])
            print(" Quantity = ",result3[0][4])
            print(" Mobile number = ",result3[0][5])
            print("total amount of your bill = ",result3[0][2]*result3[0][4])