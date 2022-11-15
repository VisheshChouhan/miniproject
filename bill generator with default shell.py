##import mysql.connector as my
##mysql_database=my.connect(user="root",host="localhost",database="nursery",passwd="123")
##mysql_cursor=mysql_database.cursor()

import tkinter

from tkinter import simpledialog,messagebox

quantity_dictionary=dict()
price_dictionary={"rose":50,"sunflower":40,"jasmine":60,"aloevera":50,"moneyplant":40,"jade":60,"adenium":100,"cactus":300,"palm":200}

def buyrose():
    
    rose_simple_dialog_box=simpledialog.askinteger("Rose","Qty.")
    quantity_dictionary["rose"]=rose_simple_dialog_box
    
def buysunflower():
    sunflower_simple_dialog_box=simpledialog.askinteger("Sunflower","Qty.")
    quantity_dictionary["sunflower"]=sunflower_simple_dialog_box
    
def buyjasmine():
    jasmine_simple_dialog_box=simpledialog.askinteger("Jasmine","Qty.")
    quantity_dictionary["jasmine"]=jasmine_simple_dialog_box
    
def buyaloevera():
    aloevera_simple_dialog_box=simpledialog.askinteger("Aloe Vera","Qty.")
    quantity_dictionary["aloevera"]=aloevera_simple_dialog_box

def buymoneyplant():
    moneyplant_simple_dialog_box=simpledialog.askinteger("Money Plant","Qty.")
    quantity_dictionary["moneyplant"]=moneyplant_simple_dialog_box

def buyjade():
    jade_simple_dialog_box=simpledialog.askinteger("Jade","Qty.")
    quantity_dictionary["jade"]=jade_simple_dialog_box

def buyadenium():
    adenium_simple_dialog_box=simpledialog.askinteger("Adenium","Qty.")
    quantity_dictionary["adenium"]=adenium_simple_dialog_box


def buycactus():
    cactus_simple_dialog_box=simpledialog.askinteger("Cactus","Qty.")
    quantity_dictionary["cactus"]=cactus_simple_dialog_box


def buypalm():
    palm_simple_dialog_box=simpledialog.askinteger("Palm","Qty.")
    quantity_dictionary["palm"]=palm_simple_dialog_box




        





#flowers
def gotoflower():
    flower_window=tkinter.Toplevel()
    flower_window.title("Flowers")
    flower_window.config(bg="white")
    flower_window.geometry("500x500+150+150")

    flowerlabel=tkinter.Label(flower_window,text="Flowers",font=("algerian",25),image=fphoto,compound="left",bg="white",height=100,width=500).grid(row=0,column=0,columnspan=2)


    rose=tkinter.Button(flower_window,text="Rose",image=fphoto,height=100,width=300,font=("algerian",25),compound="left",bg="white",command=buyrose).grid(row=1,column=0)
    priceboxrose=tkinter.Label(flower_window,text=("`",price_dictionary["rose"]),font=("indian rupee",25),bg="white").grid(row=1,column=1)
    
    sunflower=tkinter.Button(flower_window,text="sunflower",image=fphoto,height=100,width=300,font=("algerian",25),compound="left",bg="white",command=buysunflower).grid(row=2,column=0)
    priceboxsunflower=tkinter.Label(flower_window,text=("`",price_dictionary["sunflower"]),font=("indian rupee",25),bg="white").grid(row=2,column=1)
    
    jasmine=tkinter.Button(flower_window,text="jasmine",image=fphoto,height=100,width=300,font=("algerian",25),compound="left",bg="white",command=buyjasmine).grid(row=3,column=0)
    priceboxjasmine=tkinter.Label(flower_window,text=("`",price_dictionary["jasmine"]),font=("indian rupee",25),bg="white").grid(row=3,column=1)

#deoration
def gotodecoration():
    decoration_window=tkinter.Toplevel()
    decoration_window.title("Dedoration Plants")
    decoration_window.config(bg="white")
    decoration_window.geometry("500x500+150+150")

    decorationlabel=tkinter.Label(decoration_window,text="Decoration Plants",font=("algerian",25),image=fphoto,compound="left",bg="white",height=100,width=500).grid(row=0,column=0,columnspan=2)


    aloevera=tkinter.Button(decoration_window,text="Aloe vera",image=fphoto,height=100,width=300,font=("algerian",25),compound="left",bg="white",command=buyaloevera).grid(row=1,column=0)
    priceboxaloevera=tkinter.Label(decoration_window,text=("`",price_dictionary["aloevera"]),font=("indian rupee",25),bg="white").grid(row=1,column=1)
    
    moneyplant=tkinter.Button(decoration_window,text="Money Plant",image=fphoto,height=100,width=300,font=("algerian",25),compound="left",bg="white",command=buymoneyplant).grid(row=2,column=0)
    priceboxmoneyplant=tkinter.Label(decoration_window,text=("`",price_dictionary["moneyplant"]),font=("indian rupee",25),bg="white").grid(row=2,column=1)
    
    jade=tkinter.Button(decoration_window,text="Jade",image=fphoto,height=100,width=300,font=("algerian",25),compound="left",bg="white",command=buyjade).grid(row=3,column=0)
    priceboxjade=tkinter.Label(decoration_window,text=("`",price_dictionary["jade"]),font=("indian rupee",25),bg="white").grid(row=3,column=1)

#desert    
def gotodesert():
    decoration_window=tkinter.Toplevel()
    decoration_window.title("Desert plants")
    decoration_window.config(bg="white")
    decoration_window.geometry("500x500+150+150")

    desertlabel=tkinter.Label(decoration_window,text="Desert Plants",font=("algerian",25),image=fphoto,compound="left",bg="white",height=100,width=500).grid(row=0,column=0,columnspan=2)


    adenium=tkinter.Button(decoration_window,text="Adenium",image=fphoto,height=100,width=300,font=("algerian",25),compound="left",bg="white",command=buyadenium).grid(row=1,column=0)
    priceboxadenium=tkinter.Label(decoration_window,text=("`",price_dictionary["adenium"]),font=("indian rupee",25),bg="white").grid(row=1,column=1)
    
    cactus=tkinter.Button(decoration_window,text="Cactus",image=fphoto,height=100,width=300,font=("algerian",25),compound="left",bg="white",command=buycactus).grid(row=2,column=0)
    priceboxcactus=tkinter.Label(decoration_window,text=("`",price_dictionary["cactus"]),font=("indian rupee",25),bg="white").grid(row=2,column=1)
    
    palm=tkinter.Button(decoration_window,text="Palm",image=fphoto,height=100,width=300,font=("algerian",25),compound="left",bg="white",command=buypalm).grid(row=3,column=0)
    priceboxpalm=tkinter.Label(decoration_window,text=("`",price_dictionary["palm"]),font=("indian rupee",25),bg="white").grid(row=3,column=1)
    



def billf():
    bill_window=tkinter.Toplevel()
    bill_window.title("BILL")
    bill_window.config(bg="white")
    bill_window.geometry("600x650+150+0")

    billh=tkinter.Label(bill_window,text="XYZ Nursery",font=("agency fb",20,"bold"),bg="white").grid(row=0,column=1,columnspan=5)
    address=tkinter.Label(bill_window,text="MR 2,NEAR PQY PARK,AB ROAD",font=("agency fb",15),bg="white").grid(row=1,column=1,columnspan=5)
    mobno=tkinter.Label(bill_window,text="Mob : 98765_____",font=("agency fb",15),bg="white").grid(row=2,column=1,columnspan=5)
    email=tkinter.Label(bill_window,text="E Mail : xyznursery@gmail.com",font=("agency fb",15),bg="white").grid(row=3,column=1,columnspan=5)
    cashsalesinvoice=tkinter.Label(bill_window,text="CASH SALES INVOICE",font=("agency fb",15,"bold"),bg="white").grid(row=4,column=1,columnspan=5)

    sno=tkinter.Label(bill_window,text="{0:^5s}".format("S.No"),font=("indian rupee",15),bg="white",borderwidth=2,relief="groove",width=5).grid(row=5,column=0)
    description=tkinter.Label(bill_window,text="{0:^40s}".format("Description of goods"),font=("indian rupee",15),bg="white",borderwidth=2,relief="groove",width=23).grid(row=5,column=1)
    quantity=tkinter.Label(bill_window,text="{0:^15s}".format("Quantity"),font=("indian rupee",15),bg="white",borderwidth=2,relief="groove",width=8).grid(row=5,column=2)
    rate=tkinter.Label(bill_window,text="{0:^10s}".format("Rate"),font=("indian rupee",15),bg="white",borderwidth=2,relief="groove",width=8).grid(row=5,column=3)
    amount=tkinter.Label(bill_window,text="{0:^10s}".format("Amount"),font=("indian rupee",15),bg="white",borderwidth=2,relief="groove",width=8).grid(row=5,column=4)



    row_number=1
    total_amount=0
    total_quantity=0
##    mysql_command="update stocks set stock_left=stock_left - %d where name_of_product= %s "
##    mysql_command_insert="insert into sales values(curdate(),%s,%d,%d)"
##    



    if "rose" in quantity_dictionary:
       
        snor=tkinter.Label(bill_window,text="{0:^5d}".format(row_number),font=("indian rupee",15),bg="white",borderwidth=2,relief="groove",width=5).grid(row=row_number+6,column=0)
        descriptionr=tkinter.Label(bill_window,text="{0:^40s}".format("Rose"),font=("indian rupee",15),bg="white",borderwidth=2,relief="groove",width=23).grid(row=row_number+6,column=1)
        quantityr=tkinter.Label(bill_window,text="{0:^15d}".format(quantity_dictionary["rose"]),font=("indian rupee",15),bg="white",borderwidth=2,relief="groove",width=8).grid(row=row_number+6,column=2)
        rater=tkinter.Label(bill_window,text="{0:^10d}".format(price_dictionary["rose"]),font=("indian rupee",15),bg="white",borderwidth=2,relief="groove",width=8).grid(row=row_number+6,column=3)
        amountr=tkinter.Label(bill_window,text="{0:^10d}".format(quantity_dictionary["rose"]*price_dictionary["rose"]),font=("indian rupee",15),bg="white",borderwidth=2,relief="groove",width=8).grid(row=row_number+6,column=4)
        row_number+=1
        total_amount+=quantity_dictionary["rose"]*price_dictionary["rose"]
        total_quantity+=quantity_dictionary["rose"]

##        mysql_command="update stocks set stock_left = stock_left - {q} where name_of_product= %s".format(q=quantity_dictionary["rose"])
##        value=("Rose",)
##        mysql_cursor.execute(mysql_command,value)
##
##
##
##
##        profit=(quantity_dictionary["rose"]*price_dictionary["rose"])/10
##        mysql_command_insert="insert into sales values(curdate(),%s,{q},{r})".format(q=quantity_dictionary["rose"],r=profit)
##        
##        value1=("Rose",)
##        mysql_cursor.execute(mysql_command_insert,value1)
##
##        
##        mysql_database.commit()

        

    if "sunflower" in quantity_dictionary:
        snor=tkinter.Label(bill_window,text="{0:^5d}".format(row_number),font=("indian rupee",15),bg="white",borderwidth=2,relief="groove",width=5).grid(row=row_number+6,column=0)
        descriptionr=tkinter.Label(bill_window,text="{0:^40s}".format("Sunflower"),font=("indian rupee",15),bg="white",borderwidth=2,relief="groove",width=23).grid(row=row_number+6,column=1)
        quantityr=tkinter.Label(bill_window,text="{0:^15d}".format(quantity_dictionary["sunflower"]),font=("indian rupee",15),bg="white",borderwidth=2,relief="groove",width=8).grid(row=row_number+6,column=2)
        rater=tkinter.Label(bill_window,text="{0:^10d}".format(price_dictionary["sunflower"]),font=("indian rupee",15),bg="white",borderwidth=2,relief="groove",width=8).grid(row=row_number+6,column=3)
        amountr=tkinter.Label(bill_window,text="{0:^10d}".format(quantity_dictionary["sunflower"]*price_dictionary["sunflower"]),font=("indian rupee",15),bg="white",borderwidth=2,relief="groove",width=8).grid(row=row_number+6,column=4)
        row_number+=1
        total_amount+=quantity_dictionary["sunflower"]*price_dictionary["sunflower"]
        total_quantity+=quantity_dictionary["sunflower"]

##
##        mysql_command="update stocks set stock_left = stock_left - {q} where name_of_product= %s".format(q=quantity_dictionary["sunflower"])
##        value=("Sunflower",)
##        mysql_cursor.execute(mysql_command,value)
##
##
##
##        profit=(quantity_dictionary["sunflower"]*price_dictionary["sunflower"])/10
##        mysql_command_insert="insert into sales values(curdate(),%s,{q},{r})".format(q=quantity_dictionary["sunflower"],r=profit)
##        
##        value1=("Sunflower",)
##        mysql_cursor.execute(mysql_command_insert,value1)
##
##        
##        mysql_database.commit()
##


        

    if "jasmine" in quantity_dictionary:
        snor=tkinter.Label(bill_window,text="{0:^5d}".format(row_number),font=("indian rupee",15),bg="white",borderwidth=2,relief="groove",width=5).grid(row=row_number+6,column=0)
        descriptionr=tkinter.Label(bill_window,text="{0:^40s}".format("Jasmine"),font=("indian rupee",15),bg="white",borderwidth=2,relief="groove",width=23).grid(row=row_number+6,column=1)
        quantityr=tkinter.Label(bill_window,text="{0:^15d}".format(quantity_dictionary["jasmine"]),font=("indian rupee",15),bg="white",borderwidth=2,relief="groove",width=8).grid(row=row_number+6,column=2)
        rater=tkinter.Label(bill_window,text="{0:^10d}".format(price_dictionary["jasmine"]),font=("indian rupee",15),bg="white",borderwidth=2,relief="groove",width=8).grid(row=row_number+6,column=3)
        amountr=tkinter.Label(bill_window,text="{0:^10d}".format(quantity_dictionary["jasmine"]*price_dictionary["jasmine"]),font=("indian rupee",15),bg="white",borderwidth=2,relief="groove",width=8).grid(row=row_number+6,column=4)
        row_number+=1
        total_amount+=quantity_dictionary["jasmine"]*price_dictionary["jasmine"]
        total_quantity+=quantity_dictionary["jasmine"]


##        mysql_command="update stocks set stock_left = stock_left - {q} where name_of_product= %s".format(q=quantity_dictionary["jasmine"])
##        value=("Jasmine",)
##        mysql_cursor.execute(mysql_command,value)
##
##        profit=(quantity_dictionary["jasmine"]*price_dictionary["jasmine"])/10
##        mysql_command_insert="insert into sales values(curdate(),%s,{q},{r})".format(q=quantity_dictionary["jasmine"],r=profit)
##        
##        value1=("Jasmine",)
##        mysql_cursor.execute(mysql_command_insert,value1)
##
##        
##        mysql_database.commit()

    if "aloevera" in quantity_dictionary:
        snor=tkinter.Label(bill_window,text="{0:^5d}".format(row_number),font=("indian rupee",15),bg="white",borderwidth=2,relief="groove",width=5).grid(row=row_number+6,column=0)
        descriptionr=tkinter.Label(bill_window,text="{0:^40s}".format("Aloe Vera"),font=("indian rupee",15),bg="white",borderwidth=2,relief="groove",width=23).grid(row=row_number+6,column=1)
        quantityr=tkinter.Label(bill_window,text="{0:^15d}".format(quantity_dictionary["aloevera"]),font=("indian rupee",15),bg="white",borderwidth=2,relief="groove",width=8).grid(row=row_number+6,column=2)
        rater=tkinter.Label(bill_window,text="{0:^10d}".format(price_dictionary["aloevera"]),font=("indian rupee",15),bg="white",borderwidth=2,relief="groove",width=8).grid(row=row_number+6,column=3)
        amountr=tkinter.Label(bill_window,text="{0:^10d}".format(quantity_dictionary["aloevera"]*price_dictionary["aloevera"]),font=("indian rupee",15),bg="white",borderwidth=2,relief="groove",width=8).grid(row=row_number+6,column=4)
        row_number+=1
        total_amount+=quantity_dictionary["aloevera"]*price_dictionary["aloevera"]
        total_quantity+=quantity_dictionary["aloevera"]


##        mysql_command="update stocks set stock_left = stock_left - {q} where name_of_product= %s".format(q=quantity_dictionary["aloevera"])
##        value=("Aloe Vera",)
##        mysql_cursor.execute(mysql_command,value)
##
##
##        profit=(quantity_dictionary["aloevera"]*price_dictionary["aloevera"])/10
##        mysql_command_insert="insert into sales values(curdate(),%s,{q},{r})".format(q=quantity_dictionary["aloevera"],r=profit)
##        
##        value1=("Aloe Vera",)
##        mysql_cursor.execute(mysql_command_insert,value1)
##
##        
##        mysql_database.commit()



        

    if "moneyplant" in quantity_dictionary:
        snor=tkinter.Label(bill_window,text="{0:^5d}".format(row_number),font=("indian rupee",15),bg="white",borderwidth=2,relief="groove",width=5).grid(row=row_number+6,column=0)
        descriptionr=tkinter.Label(bill_window,text="{0:^40s}".format("Money Plant"),font=("indian rupee",15),bg="white",borderwidth=2,relief="groove",width=23).grid(row=row_number+6,column=1)
        quantityr=tkinter.Label(bill_window,text="{0:^15d}".format(quantity_dictionary["moneyplant"]),font=("indian rupee",15),bg="white",borderwidth=2,relief="groove",width=8).grid(row=row_number+6,column=2)
        rater=tkinter.Label(bill_window,text="{0:^10d}".format(price_dictionary["moneyplant"]),font=("indian rupee",15),bg="white",borderwidth=2,relief="groove",width=8).grid(row=row_number+6,column=3)
        amountr=tkinter.Label(bill_window,text="{0:^10d}".format(quantity_dictionary["moneyplant"]*price_dictionary["moneyplant"]),font=("indian rupee",15),bg="white",borderwidth=2,relief="groove",width=8).grid(row=row_number+6,column=4)
        row_number+=1
        total_amount+=quantity_dictionary["moneyplant"]*price_dictionary["moneyplant"]
        total_quantity+=quantity_dictionary["moneyplant"]
##
##
##
##        mysql_command="update stocks set stock_left = stock_left - {q} where name_of_product= %s".format(q=quantity_dictionary["moneyplant"])
##        value=("Money Plant",)
##        mysql_cursor.execute(mysql_command,value)
##
##
##        profit=(quantity_dictionary["moneyplant"]*price_dictionary["moneyplant"])/10
##        mysql_command_insert="insert into sales values(curdate(),%s,{q},{r})".format(q=quantity_dictionary["moneyplant"],r=profit)
##        
##        value1=("Money Plant",)
##        mysql_cursor.execute(mysql_command_insert,value1)
##
##
##        
##        mysql_database.commit()


        

    if "jade" in quantity_dictionary:
        snor=tkinter.Label(bill_window,text="{0:^5d}".format(row_number),font=("indian rupee",15),bg="white",borderwidth=2,relief="groove",width=5).grid(row=row_number+6,column=0)
        descriptionr=tkinter.Label(bill_window,text="{0:^40s}".format("Jade"),font=("indian rupee",15),bg="white",borderwidth=2,relief="groove",width=23).grid(row=row_number+6,column=1)
        quantityr=tkinter.Label(bill_window,text="{0:^15d}".format(quantity_dictionary["jade"]),font=("indian rupee",15),bg="white",borderwidth=2,relief="groove",width=8).grid(row=row_number+6,column=2)
        rater=tkinter.Label(bill_window,text="{0:^10d}".format(price_dictionary["jade"]),font=("indian rupee",15),bg="white",borderwidth=2,relief="groove",width=8).grid(row=row_number+6,column=3)
        amountr=tkinter.Label(bill_window,text="{0:^10d}".format(quantity_dictionary["jade"]*price_dictionary["jade"]),font=("indian rupee",15),bg="white",borderwidth=2,relief="groove",width=8).grid(row=row_number+6,column=4)
        row_number+=1
        total_amount+=quantity_dictionary["jade"]*price_dictionary["jade"]
        total_quantity+=quantity_dictionary["jade"]

##
##        mysql_command="update stocks set stock_left = stock_left - {q} where name_of_product= %s".format(q=quantity_dictionary["jade"])
##        value=("Jade",)
##        mysql_cursor.execute(mysql_command,value)
##
##        profit=(quantity_dictionary["jade"]*price_dictionary["jade"])/10
##        mysql_command_insert="insert into sales values(curdate(),%s,{q},{r})".format(q=quantity_dictionary["jade"],r=profit)
##        
##        value1=("Jade",)
##        mysql_cursor.execute(mysql_command_insert,value1)
##
##
##        
##        mysql_database.commit()

        


    if "adenium" in quantity_dictionary:
        snor=tkinter.Label(bill_window,text="{0:^5d}".format(row_number),font=("indian rupee",15),bg="white",borderwidth=2,relief="groove",width=5).grid(row=row_number+6,column=0)
        descriptionr=tkinter.Label(bill_window,text="{0:^40s}".format("Adenium"),font=("indian rupee",15),bg="white",borderwidth=2,relief="groove",width=23).grid(row=row_number+6,column=1)
        quantityr=tkinter.Label(bill_window,text="{0:^15d}".format(quantity_dictionary["adenium"]),font=("indian rupee",15),bg="white",borderwidth=2,relief="groove",width=8).grid(row=row_number+6,column=2)
        rater=tkinter.Label(bill_window,text="{0:^10d}".format(price_dictionary["adenium"]),font=("indian rupee",15),bg="white",borderwidth=2,relief="groove",width=8).grid(row=row_number+6,column=3)
        amountr=tkinter.Label(bill_window,text="{0:^10d}".format(quantity_dictionary["adenium"]*price_dictionary["adenium"]),font=("indian rupee",15),bg="white",borderwidth=2,relief="groove",width=8).grid(row=row_number+6,column=4)
        row_number+=1
        total_amount+=quantity_dictionary["adenium"]*price_dictionary["adenium"]
        total_quantity+=quantity_dictionary["adenium"]



##        mysql_command="update stocks set stock_left = stock_left - {q} where name_of_product= %s".format(q=quantity_dictionary["adenium"])
##        value=("Adenium",)
##        mysql_cursor.execute(mysql_command,value)
##
##
##
##        profit=(quantity_dictionary["adenium"]*price_dictionary["adenium"])/10
##        mysql_command_insert="insert into sales values(curdate(),%s,{q},{r})".format(q=quantity_dictionary["adenium"],r=profit)
##        
##        value1=("Adenium",)
##        mysql_cursor.execute(mysql_command_insert,value1)
##
##
##        
##        mysql_database.commit()

        


    if "cactus" in quantity_dictionary:
        snor=tkinter.Label(bill_window,text="{0:^5d}".format(row_number),font=("indian rupee",15),bg="white",borderwidth=2,relief="groove",width=5).grid(row=row_number+6,column=0)
        descriptionr=tkinter.Label(bill_window,text="{0:^40s}".format("Cactus"),font=("indian rupee",15),bg="white",borderwidth=2,relief="groove",width=23).grid(row=row_number+6,column=1)
        quantityr=tkinter.Label(bill_window,text="{0:^15d}".format(quantity_dictionary["cactus"]),font=("indian rupee",15),bg="white",borderwidth=2,relief="groove",width=8).grid(row=row_number+6,column=2)
        rater=tkinter.Label(bill_window,text="{0:^10d}".format(price_dictionary["cactus"]),font=("indian rupee",15),bg="white",borderwidth=2,relief="groove",width=8).grid(row=row_number+6,column=3)
        amountr=tkinter.Label(bill_window,text="{0:^10d}".format(quantity_dictionary["cactus"]*price_dictionary["cactus"]),font=("indian rupee",15),bg="white",borderwidth=2,relief="groove",width=8).grid(row=row_number+6,column=4)
        row_number+=1
        total_amount+=quantity_dictionary["cactus"]*price_dictionary["cactus"]
        total_quantity+=quantity_dictionary["cactus"]



##        mysql_command="update stocks set stock_left = stock_left - {q} where name_of_product= %s".format(q=quantity_dictionary["cactus"])
##        value=("Cactus",)
##        mysql_cursor.execute(mysql_command,value)
##
##
##        profit=(quantity_dictionary["cactus"]*price_dictionary["cactus"])/10
##        mysql_command_insert="insert into sales values(curdate(),%s,{q},{r})".format(q=quantity_dictionary["cactus"],r=profit)
##        
##        value1=("Cactus",)
##        mysql_cursor.execute(mysql_command_insert,value1)
##
##        
##        mysql_database.commit()
##
##        




    if "palm" in quantity_dictionary:
        snor=tkinter.Label(bill_window,text="{0:^5d}".format(row_number),font=("indian rupee",15),bg="white",borderwidth=2,relief="groove",width=5).grid(row=row_number+6,column=0)
        descriptionr=tkinter.Label(bill_window,text="{0:^40s}".format("Palm"),font=("indian rupee",15),bg="white",borderwidth=2,relief="groove",width=23).grid(row=row_number+6,column=1)
        quantityr=tkinter.Label(bill_window,text="{0:^15d}".format(quantity_dictionary["palm"]),font=("indian rupee",15),bg="white",borderwidth=2,relief="groove",width=8).grid(row=row_number+6,column=2)
        rater=tkinter.Label(bill_window,text="{0:^10d}".format(price_dictionary["palm"]),font=("indian rupee",15),bg="white",borderwidth=2,relief="groove",width=8).grid(row=row_number+6,column=3)
        amountr=tkinter.Label(bill_window,text="{0:^10d}".format(quantity_dictionary["palm"]*price_dictionary["palm"]),font=("indian rupee",15),bg="white",borderwidth=2,relief="groove",width=8).grid(row=row_number+6,column=4)
        row_number+=1
        total_amount+=quantity_dictionary["palm"]*price_dictionary["palm"]
        total_quantity+=quantity_dictionary["palm"]


##        mysql_command="update stocks set stock_left = stock_left - {q} where name_of_product= %s".format(q=quantity_dictionary["palm"])
##        value=("Palm",)
##        mysql_cursor.execute(mysql_command,value)
##
##
##
##        profit=(quantity_dictionary["palm"]*price_dictionary["palm"])/10
##        mysql_command_insert="insert into sales values(curdate(),%s,{q},{r})".format(q=quantity_dictionary["palm"],r=profit)
##        
##        value1=("Palm",)
##        mysql_cursor.execute(mysql_command_insert,value1)
##
##
##        
##        mysql_database.commit()

        




    total=tkinter.Label(bill_window,text="{0:^40s}".format("Total"),font=("indian rupee",15),bg="white",borderwidth=2,relief="groove",width=23).grid(row=row_number+6,column=1)
    quantityr=tkinter.Label(bill_window,text="{0:^15d}".format(total_quantity),font=("indian rupee",15),bg="white",borderwidth=2,relief="groove",width=8).grid(row=row_number+6,column=2)
    
    amountr=tkinter.Label(bill_window,text="{0:^10d}".format(total_amount),font=("indian rupee",15),bg="white",borderwidth=2,relief="groove",width=8).grid(row=row_number+6,column=4)


    def pay():
        simpledialog_box_ask_yes_no=messagebox.askyesno("THANKYOU","Do you really want to make transaction.")
        if simpledialog_box_ask_yes_no:
            messageboxpaydone=messagebox.showinfo("Thankyou","Payment Successfull")





    pay_button=tkinter.Button(bill_window,text="Pay",font=("algerian",15),bg="white",borderwidth=3,relief="raised",command=pay).place(x=220,y=600)
    


    


        




def main():
    main_window=tkinter.Tk()
    main_window.title("Nursery")
    main_window.config(bg="white")
    main_window.geometry("500x500+150+150")
    photo=tkinter.PhotoImage(file="photo.png")
    fphoto=photo.subsample(3,3)



    img=tkinter.Label(main_window,image=fphoto,compound="left",bg="white",height=100,width=500).grid(row=0,column=0)

    flower=tkinter.Button(main_window,text="flowery plant",font=("algerian",25),bg="white",width=24,height=2,command=gotoflower).grid(row=1,column=0)
    decoration=tkinter.Button(main_window,text="decoration plant",font=("algerian",25),bg="white",width=24,height=2,command=gotodecoration).grid(row=2,column=0)
    desert=tkinter.Button(main_window,text="desert plant",font=("algerian",25),bg="white",width=24,height=2,command=gotodesert).grid(row=3,column=0)

    space=tkinter.Label(main_window,bg="white",width=24,height=2).grid(row=4,column=0)

    bill=tkinter.Button(main_window,text="Bill",font=("algerian",15,"bold"),bg="white",command=billf).grid(row=5,column=0)


    main_window.mainloop()


if __name__ == "__main__":
    import cProfile
    cProfile.run("main()","output.dat")

    import pstats
    from pstats import SortKey

    with open("output_time.txt","w") as f:
        p = pstats.Stats("output.dat",stream=f)
        p.sort_stats("time").print_stats()
