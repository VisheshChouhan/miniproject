## import tkinter for GUI support
import tkinter

## importing simpledialog and message box exclusively for simpler use 
from tkinter import simpledialog, messagebox

## module for profiling
import cProfile

# module for reading profiled data 
import pstats
from pstats import SortKey

## dictionary to keep the quantity of each plant sold 
quantity_dictionary = dict()

## dictionary that keep track of plants price
price_dictionary = {"rose":50, "sunflower":40, "jasmine":60, "aloevera":50, 
                    "moneyplant":40, "jade":60, "adenium":100, "cactus":300, 
                    "palm":200}


## method to sell the plants
def buyrose():
    rose_simple_dialog_box = simpledialog.askinteger("Rose", "Qty.")
    quantity_dictionary["rose"] = rose_simple_dialog_box

## method to sell the plants    
def buysunflower():
    sunflower_simple_dialog_box = simpledialog.askinteger("Sunflower", "Qty.")
    quantity_dictionary["sunflower"] = sunflower_simple_dialog_box

## method to sell the plants 
def buyjasmine():
    jasmine_simple_dialog_box = simpledialog.askinteger("Jasmine", "Qty.")
    quantity_dictionary["jasmine"] = jasmine_simple_dialog_box

## method to sell the plants    
def buyaloevera():
    aloevera_simple_dialog_box = simpledialog.askinteger("Aloe Vera", "Qty.")
    quantity_dictionary["aloevera"] = aloevera_simple_dialog_box

## method to sell the plants
def buymoneyplant():
    moneyplant_simple_dialog_box = simpledialog.askinteger("Money Plant", 
                                                        "Qty.")
    quantity_dictionary["moneyplant"] = moneyplant_simple_dialog_box

## method to sell the plants
def buyjade():
    jade_simple_dialog_box = simpledialog.askinteger("Jade", "Qty.")
    quantity_dictionary["jade"] = jade_simple_dialog_box

## method to sell the plants
def buyadenium():
    adenium_simple_dialog_box = simpledialog.askinteger("Adenium", "Qty.")
    quantity_dictionary["adenium"] = adenium_simple_dialog_box

## method to sell the plants
def buycactus():
    cactus_simple_dialog_box = simpledialog.askinteger("Cactus", "Qty.")
    quantity_dictionary["cactus"] = cactus_simple_dialog_box


# method to sell the plants
def buypalm():
    palm_simple_dialog_box = simpledialog.askinteger("Palm", "Qty.")
    quantity_dictionary["palm"] = palm_simple_dialog_box


# methods to remove the sold plant from the list
def changerose():
    if "rose" in quantity_dictionary:
        rose_simple_dialog_box = simpledialog.askinteger("Rose", "Qty.")
        quantity_dictionary["rose"] = rose_simple_dialog_box
    else:
        invalidselection = messagebox.showinfo("Invalid option", 
                                                "Your selection is not in bill ")


# methods to remove the sold plant from the list
def changesunflower():
    if "sunflower" in quantity_dictionary:
        rose_simple_dialog_box = simpledialog.askinteger("sunflower", "Qty.")
        quantity_dictionary["sunflower"] = rose_simple_dialog_box
    else:
        invalidselection = messagebox.showinfo("Invalid option", 
                                                "Your selection is not in bill ")

# methods to remove the sold plant from the list
def changejasmine():
    if "jasmine" in quantity_dictionary:
        rose_simple_dialog_box = simpledialog.askinteger("Jasmine", "Qty.")
        quantity_dictionary["jasmine"] = rose_simple_dialog_box
    else:
        invalidselection = messagebox.showinfo("Invalid option", 
                                                "Your selection is not in bill ")

# methods to remove the sold plant from the list
def changealoevera():
    if "aloevera" in quantity_dictionary:
        rose_simple_dialog_box = simpledialog.askinteger("Aloevera", "Qty.")
        quantity_dictionary["aloevera"] = rose_simple_dialog_box
    else:
        invalidselection = messagebox.showinfo("Invalid option", 
                                                "Your selection is not in bill ")

# methods to remove the sold plant from the list
def changemoneyplant():
    if "moneyplant" in quantity_dictionary:
        rose_simple_dialog_box = simpledialog.askinteger("Moneyplant", "Qty.")
        quantity_dictionary["moneyplant"] = rose_simple_dialog_box
    else:
        invalidselection = messagebox.showinfo("Invalid option", 
                                                "Your selection is not in bill ")

# methods to remove the sold plant from the list
def changejade():
    if "jade" in quantity_dictionary:
        rose_simple_dialog_box = simpledialog.askinteger("Jade", "Qty.")
        quantity_dictionary["jade"] = rose_simple_dialog_box
    else:
        invalidselection = messagebox.showinfo("Invalid option", 
                                                "Your selection is not in bill ")

# methods to remove the sold plant from the list
def changeadenium():
    if "adenium" in quantity_dictionary:
        rose_simple_dialog_box = simpledialog.askinteger("adenium", "Qty.")
        quantity_dictionary["adenium"] = rose_simple_dialog_box
    else:
        invalidselection = messagebox.showinfo("Invalid option", 
                                                "Your selection is not in bill ")

# methods to remove the sold plant from the list
def changecactus():
    if "cactus" in quantity_dictionary:
        rose_simple_dialog_box = simpledialog.askinteger("cactus", "Qty.")
        quantity_dictionary["cactus"] = rose_simple_dialog_box
    else:
        invalidselection = messagebox.showinfo("Invalid option", 
                                                "Your selection is not in bill ")

# methods to remove the sold plant from the list
def changepalm():
    if "palm" in quantity_dictionary:
        rose_simple_dialog_box = simpledialog.askinteger("palm", "Qty.")
        quantity_dictionary["palm"] = rose_simple_dialog_box
    else:
        invalidselection = messagebox.showinfo("Invalid option", 
                                                "Your selection is not in bill ")

def rose_price_change():
    rose_simple_dialog_box = simpledialog.askinteger("Rose", "Price")
    price_dictionary["rose"] = rose_simple_dialog_box
else:
        invalidselection = messagebox.showinfo("Invalid option", 
                                                "Your selection is not in bill ")





# The given function will be assigned to the command of flower button
# Hence it will be called when button is clicked
def gotoflower():

    # Structure of the window that appears after entering the flower 
    # section
    flower_window = tkinter.Toplevel()
    flower_window.title("Flowers")
    flower_window.config(bg = "white")
    flower_window.geometry("1150x500+150+250")

    flowerlabel = tkinter.Label(flower_window, text = "Flowers", 
                            font = ("algerian", 25), 
                            image = fphoto, compound = "left", bg = "white", 
                            height = 100, width = 500).grid(row = 0, column = 0, 
                                                        columnspan = 2)


    ## Buttons denoting the plant name to be selected
    rose = tkinter.Button(flower_window, text = "Rose", image = fphoto, 
                        height = 100,width = 300, font = ("algerian", 25), 
                        compound = "left", bg = "white",
                        command = buyrose).grid(row = 1, column = 0)


    priceboxrose = tkinter.Label(flower_window, text = ("`", 
                               price_dictionary["rose"]), 
                               font = ("indian rupee", 25), 
                               bg = "white").grid(row = 1, column = 1)


    # for deletion 
    delrose = tkinter.Button(flower_window, text = "Change quantity",   image = cancelimage,  
                        height = 100,width = 300, font = ("algerian", 15), 
                        compound = "left", bg = "white",
                        command = changerose).grid(row = 1, column = 2)

    # for changing price 
    change_rose_price = tkinter.Button(flower_window, text = "Change price",   image = cancelimage,  
                        height = 100,width = 300, font = ("algerian", 15), 
                        compound = "left", bg = "white",
                        command = rose_price_change).grid(row = 1, column = 3)
    

    
    ## Buttons denoting the plant name to be selected
    sunflower = tkinter.Button(flower_window, text = "sunflower", 
                            image = fphoto, 
                            height = 100, width = 300, font = ("algerian", 25), 
                            compound = "left", bg = "white", 
                            command = buysunflower).grid(row = 2, column = 0)

    priceboxsunflower = tkinter.Label(flower_window, text = ("`", 
                                    price_dictionary["sunflower"]), 
                                    font = ("indian rupee", 25), 
                                    bg = "white").grid(row = 2, column = 1)

    # for deletion 
    delsunflower = tkinter.Button(flower_window, text = "Change quantity",   image = cancelimage,  
                        height = 100,width = 300, font = ("algerian", 15), 
                        compound = "left", bg = "white",
                        command = changesunflower).grid(row = 2, column = 2)
    
    
    ## Buttons denoting the plant name to be selected
    jasmine = tkinter.Button(flower_window, text = "jasmine", image = fphoto, 
                           height = 100, width = 300, font = ("algerian", 25), 
                           compound = "left", bg = "white", 
                           command = buyjasmine).grid(row = 3, column = 0)

    priceboxjasmine = tkinter.Label(flower_window, text = ("`", 
                                  price_dictionary["jasmine"]), 
                                  font = ("indian rupee", 25), 
                                  bg = "white").grid(row = 3, column = 1)

    # for deletion 
    deljasmine = tkinter.Button(flower_window, text = "Change quantity",   image = cancelimage,  
                        height = 100,width = 300, font = ("algerian", 15), 
                        compound = "left", bg = "white",
                        command = changejasmine).grid(row = 3, column = 2)

# The given function will be assigned to the command of decoration button
# Hence it will be called when button is clicked
def gotodecoration():
    # Structure of the window that appears after entering the flower 
    # section
    decoration_window = tkinter.Toplevel()
    decoration_window.title("Dedoration Plants")
    decoration_window.config(bg = "white")
    decoration_window.geometry("850x500+150+150")

    decorationlabel = tkinter.Label(decoration_window, 
                                  text = "Decoration Plants", 
                                  font = ("algerian", 25), image = fphoto, 
                                  compound = "left", bg = "white", height = 100, 
                                  width = 500).grid(row = 0, 
                                  column = 0, columnspan = 2)


    ## Buttons denoting the plant name to be selected
    aloevera = tkinter.Button(decoration_window, text = "Aloe vera",   
                            image = fphoto, height = 100, width = 300, 
                            font = ("algerian", 25), compound = "left", 
                            bg = "white", command = buyaloevera).grid(row = 1, 
                                                                column = 0)

    priceboxaloevera = tkinter.Label(decoration_window, text = ("`", 
                                   price_dictionary["aloevera"]), 
                                   font = ("indian rupee", 25), 
                                   bg = "white").grid(row = 1, column = 1)
    # for deletion 
    delaloevera = tkinter.Button(decoration_window, text = "Change quantity",   image = cancelimage,  
                        height = 100,width = 300, font = ("algerian", 15), 
                        compound = "left", bg = "white",
                        command = changealoevera).grid(row = 1, column = 2)

    
    
    ## Buttons denoting the plant name to be selected
    moneyplant = tkinter.Button(decoration_window, text = "Money Plant", 
                              image = fphoto, height = 100, width = 300, 
                              font = ("algerian", 25), compound = "left", 
                              bg = "white", 
                              command = buymoneyplant).grid(row = 2, 
                                                                column = 0)

    priceboxmoneyplant = tkinter.Label(decoration_window, text = ("`", 
                                    price_dictionary["moneyplant"]), 
                                    font = ("indian rupee", 25), 
                                    bg = "white").grid(row = 2, column = 1)

    # for deletion 
    delmoneyplant = tkinter.Button(decoration_window, text = "Change quantity",   image = cancelimage,  
                        height = 100,width = 300, font = ("algerian", 15), 
                        compound = "left", bg = "white",
                        command = changemoneyplant).grid(row = 2, column = 2)
    
    ## Buttons denoting the plant name to be selected
    jade = tkinter.Button(decoration_window, text = "Jade", image = fphoto, 
                        height = 100, width = 300, font = ("algerian", 25), 
                        compound = "left", bg = "white", 
                        command = buyjade).grid(row = 3, column = 0)

    priceboxjade = tkinter.Label(decoration_window, text = ("`", 
                                price_dictionary["jade"]), 
                                font = ("indian rupee", 25), 
                                bg = "white").grid(row = 3, column = 1)
        # for deletion 
    deljade = tkinter.Button(decoration_window, text = "Change quantity",   image = cancelimage,  
                        height = 100,width = 300, font = ("algerian", 15), 
                        compound = "left", bg = "white",
                        command = changejade).grid(row = 3, column = 2)


# The given function will be assigned to the command of desert button
# Hence it will be called when button is clicked  
def gotodesert():
    # Structure of the window that appears after entering the flower 
    # section
    decoration_window = tkinter.Toplevel()
    decoration_window.title("Desert plants")
    decoration_window.config(bg = "white")
    decoration_window.geometry("850x500+150+150")

    desertlabel = tkinter.Label(decoration_window, text = "Desert Plants", 
                              font = ("algerian", 25), image = fphoto, 
                              compound = "left", bg = "white", height = 100, 
                              width = 500).grid(row = 0, column = 0, 
                                                columnspan = 2)


    ## Buttons denoting the plant name to be selected
    adenium = tkinter.Button(decoration_window, text = "Adenium", 
                           image = fphoto, 
                           height = 100, width = 300, font = ("algerian", 25), 
                           compound = "left", bg = "white", 
                           command = buyadenium).grid(row = 1, column = 0)

    priceboxadenium = tkinter.Label(decoration_window, text = ("`", 
                                  price_dictionary["adenium"]), 
                                  font = ("indian rupee", 25), 
                                  bg = "white").grid(row = 1, column = 1)

    # for deletion 
    deladenium = tkinter.Button(decoration_window, text = "Change quantity",   image = cancelimage,  
                        height = 100,width = 300, font = ("algerian", 15), 
                        compound = "left", bg = "white",
                        command = changeadenium).grid(row = 1, column = 2)
    
    ## Buttons denoting the plant name to be selected
    cactus = tkinter.Button(decoration_window, text = "Cactus", image = fphoto, 
                          height = 100, width = 300, font = ("algerian", 25), 
                          compound = "left", bg = "white", 
                          command = buycactus).grid(row = 2, column = 0)

    priceboxcactus = tkinter.Label(decoration_window, text = ("`", 
                                price_dictionary["cactus"]), 
                                font = ("indian rupee", 25), 
                                bg = "white").grid(row = 2, column = 1)

    # for deletion 
    delcactus = tkinter.Button(decoration_window, text = "Change quantity",   image = cancelimage,  
                        height = 100,width = 300, font = ("algerian", 15), 
                        compound = "left", bg = "white",
                        command = changecactus).grid(row = 2, column = 2)
    
    
    ## Buttons denoting the plant name to be selected
    palm = tkinter.Button(decoration_window, text = "Palm", image = fphoto, 
                        height = 100, width = 300, font = ("algerian", 25), 
                        compound = "left", bg = "white", 
                        command = buypalm).grid(row = 3, column = 0)

    priceboxpalm = tkinter.Label(decoration_window, text = ("`", 
                               price_dictionary["palm"]), 
                               font = ("indian rupee", 25), 
                               bg = "white").grid(row = 3, column = 1)
    # for deletion 
    delpalm = tkinter.Button(decoration_window, text = "Change quantity",   image = cancelimage,  
                        height = 100,width = 300, font = ("algerian", 15), 
                        compound = "left", bg = "white",
                        command = changepalm).grid(row = 3, column = 2)
    

## The billf function will generate the bill 
## and is assigned to the command argument of bill button
def billf():
    ## bill window
    bill_window = tkinter.Toplevel()
    bill_window.title("BILL")
    bill_window.config(bg = "white")
    bill_window.geometry("600x650+150+0")


    ## The structure of the bill     
    billh = tkinter.Label(bill_window, text = "XYZ Nursery", 
                        font = ("agency fb", 20, "bold"), 
                        bg = "white").grid(row = 0, column = 1, 
                                                    columnspan = 5)

    address = tkinter.Label(bill_window, text = "MR 2, NEAR PQY PARK, AB ROAD", 
                         font = ("agency fb", 15), 
                         bg = "white").grid(row = 1, column = 1, columnspan = 5)

    mobno = tkinter.Label(bill_window, text = "Mob : 98765_____", 
                        font = ("agency fb", 15), 
                        bg = "white").grid(row = 2, column = 1, columnspan = 5)

    email = tkinter.Label(bill_window, text = "E Mail : xyznursery@gmail.com", 
                        font = ("agency fb", 15), 
                        bg = "white").grid(row = 3, column = 1, columnspan = 5)

    cashsalesinvoice = tkinter.Label(bill_window, text = "CASH SALES INVOICE", 
                                   font = ("agency fb", 15, "bold"), 
                                   bg = "white").grid(row = 4, column = 1, 
                                                    columnspan = 5)

    sno = tkinter.Label(bill_window, text = "{0:^5s}".format("S.No"), 
                     font = ("indian rupee", 15), bg = "white", borderwidth = 2, 
                     relief = "groove", width = 5).grid(row = 5, column = 0)

    description = tkinter.Label(bill_window, text = "{0:^40s}"
                            .format("Description of goods"), 
                            font = ("indian rupee", 15), bg = "white", 
                            borderwidth = 2, relief = "groove", 
                            width = 23).grid(row = 5, column = 1)

    quantity = tkinter.Label(bill_window, text = "{0:^15s}".format("Quantity"), 
                           font = ("indian rupee", 15), bg = "white", 
                           borderwidth = 2, relief = "groove", 
                           width = 8).grid(row = 5, column = 2)

    rate = tkinter.Label(bill_window, text = "{0:^10s}".format("Rate"), 
                       font = ("indian rupee", 15), bg = "white",
                       borderwidth = 2, 
                       relief = "groove", width = 8).grid(row = 5, column = 3)

    amount = tkinter.Label(bill_window, text = "{0:^10s}".format("Amount"), 
                        font = ("indian rupee", 15), bg = "white", 
                        borderwidth = 2, 
                        relief = "groove", width = 8).grid(row = 5, column = 4)



    row_number = 1
    total_amount = 0
    total_quantity = 0


    for i in quantity_dictionary:
            snor = tkinter.Label(bill_window, text = "{0:^5d}".format(row_number), 
                               font = ("indian rupee", 15), bg = "white", 
                               borderwidth = 2, relief = "groove", 
                               width = 5).grid(row = row_number+6, column = 0)

            descriptionr = tkinter.Label(bill_window, text = "{0:^40s}"
                                      .format(i.capitalize()), font = ("indian rupee", 15), 
                                      bg = "white", borderwidth = 2, 
                                      relief = "groove", 
                                      width = 23).grid(row = row_number+6, 
                                      column = 1)

            quantityr = tkinter.Label(bill_window, text = "{0:^15d}"
                                    .format(quantity_dictionary[i]), 
                                    font = ("indian rupee", 15), bg = "white", 
                                    borderwidth = 2, relief = "groove", 
                                    width = 8).grid(row = row_number+6, column = 2)

            rater = tkinter.Label(bill_window, text = "{0:^10d}"
                               .format(price_dictionary[i]), 
                               font = ("indian rupee", 15), bg = "white", 
                               borderwidth = 2, relief = "groove", 
                               width = 8).grid(row = row_number+6, column = 3)

            amountr = tkinter.Label(bill_window, text = "{0:^10d}"
                                .format(quantity_dictionary[i]
                                *price_dictionary[i]), 
                                font = ("indian rupee", 15), bg = "white", 
                                borderwidth = 2, relief = "groove", 
                                width = 8).grid(row = row_number+6, column = 4)

            row_number += 1
            total_amount += quantity_dictionary[i]*price_dictionary[i]
            total_quantity += quantity_dictionary[i]




    ## calculate the total of the bill
    total = tkinter.Label(bill_window, text = "{0:^40s}"
                        .format("Total"), font = ("indian rupee", 15), 
                        bg = "white", borderwidth = 2, relief = "groove", 
                        width = 23).grid(row = row_number+6, column = 1)

    quantityr = tkinter.Label(bill_window, text = "{0:^15d}"
                            .format(total_quantity), 
                            font = ("indian rupee", 15), bg = "white", 
                            borderwidth = 2, relief = "groove", 
                            width = 8).grid(row = row_number+6, column = 2)
    
    amountr = tkinter.Label(bill_window, text = "{0:^10d}"
                            .format(total_amount), 
                            font = ("indian rupee", 15), bg = "white", 
                            borderwidth = 2, relief = "groove", 
                            width = 8).grid(row = row_number+6, column = 4)


    def pay():
        simpledialog_box_ask_yes_no = messagebox.askyesno("", "Do you really \
                                            want to recieve transaction.")
        if simpledialog_box_ask_yes_no:
            messageboxpaydone = messagebox.showinfo("Thankyou", "Payment \
                                                    Successfull")

    pay_button = tkinter.Button(bill_window, text = "Recieve", 
                                font = ("algerian", 15), bg = "white", 
                                borderwidth = 3, relief = "raised", 
                                command = pay).place(x = 220, y = 600)
    
    sort_bill_button = tkinter.Button(bill_window, text = "Sort Bill", 
                                     font = ("algerian", 15), bg = "white", 
                                     borderwidth = 3, relief = "raised", 
                                     command = sortbill).place(x = 450, y = 600)


def sortbill():
    ## bill window
    bill_window = tkinter.Toplevel()
    bill_window.title("BILL")
    bill_window.config(bg = "white")
    bill_window.geometry("600x650+150+0")


    ## The structure of the bill     
    billh = tkinter.Label(bill_window, text = "XYZ Nursery", 
                        font = ("agency fb", 20, "bold"), 
                        bg = "white").grid(row = 0, column = 1, 
                                                    columnspan = 5)

    address = tkinter.Label(bill_window, text = "MR 2, NEAR PQY PARK, AB ROAD", 
                         font = ("agency fb", 15), 
                         bg = "white").grid(row = 1, column = 1, columnspan = 5)

    mobno = tkinter.Label(bill_window, text = "Mob : 98765_____", 
                        font = ("agency fb", 15), 
                        bg = "white").grid(row = 2, column = 1, columnspan = 5)

    email = tkinter.Label(bill_window, text = "E Mail : xyznursery@gmail.com", 
                        font = ("agency fb", 15), 
                        bg = "white").grid(row = 3, column = 1, columnspan = 5)

    cashsalesinvoice = tkinter.Label(bill_window, text = "CASH SALES INVOICE", 
                                   font = ("agency fb", 15, "bold"), 
                                   bg = "white").grid(row = 4, column = 1, 
                                                    columnspan = 5)

    sno = tkinter.Label(bill_window, text = "{0:^5s}".format("S.No"), 
                     font = ("indian rupee", 15), bg = "white", borderwidth = 2, 
                     relief = "groove", width = 5).grid(row = 5, column = 0)

    description = tkinter.Label(bill_window, text = "{0:^40s}"
                            .format("Description of goods"), 
                            font = ("indian rupee", 15), bg = "white", 
                            borderwidth = 2, relief = "groove", 
                            width = 23).grid(row = 5, column = 1)

    quantity = tkinter.Label(bill_window, text = "{0:^15s}".format("Quantity"), 
                           font = ("indian rupee", 15), bg = "white", 
                           borderwidth = 2, relief = "groove", 
                           width = 8).grid(row = 5, column = 2)

    rate = tkinter.Label(bill_window, text = "{0:^10s}".format("Rate"), 
                       font = ("indian rupee", 15), bg = "white",
                       borderwidth = 2, 
                       relief = "groove", width = 8).grid(row = 5, column = 3)

    amount = tkinter.Label(bill_window, text = "{0:^10s}".format("Amount"), 
                        font = ("indian rupee", 15), bg = "white", 
                        borderwidth = 2, 
                        relief = "groove", width = 8).grid(row = 5, column = 4)



    row_number = 1
    total_amount = 0
    total_quantity = 0

    # list that contains plant name in sorted order
    sorted_list = ["adenium","cactus","rose","sunflower","jasmine","jade","palm","moneyplant","aloevera"]
    sorted_list.sort()

    for i in sorted_list:
        if i in quantity_dictionary:
            snor = tkinter.Label(bill_window, text = "{0:^5d}".format(row_number), 
                               font = ("indian rupee", 15), bg = "white", 
                               borderwidth = 2, relief = "groove", 
                               width = 5).grid(row = row_number+6, column = 0)

            descriptionr = tkinter.Label(bill_window, text = "{0:^40s}"
                                      .format(i.capitalize()), font = ("indian rupee", 15), 
                                      bg = "white", borderwidth = 2, 
                                      relief = "groove", 
                                      width = 23).grid(row = row_number+6, 
                                      column = 1)

            quantityr = tkinter.Label(bill_window, text = "{0:^15d}"
                                    .format(quantity_dictionary[i]), 
                                    font = ("indian rupee", 15), bg = "white", 
                                    borderwidth = 2, relief = "groove", 
                                    width = 8).grid(row = row_number+6, column = 2)

            rater = tkinter.Label(bill_window, text = "{0:^10d}"
                               .format(price_dictionary[i]), 
                               font = ("indian rupee", 15), bg = "white", 
                               borderwidth = 2, relief = "groove", 
                               width = 8).grid(row = row_number+6, column = 3)

            amountr = tkinter.Label(bill_window, text = "{0:^10d}"
                                .format(quantity_dictionary[i]
                                *price_dictionary[i]), 
                                font = ("indian rupee", 15), bg = "white", 
                                borderwidth = 2, relief = "groove", 
                                width = 8).grid(row = row_number+6, column = 4)

            row_number += 1
            total_amount += quantity_dictionary[i]*price_dictionary[i]
            total_quantity += quantity_dictionary[i]

    ## calculate the total of the bill
    total = tkinter.Label(bill_window, text = "{0:^40s}"
                        .format("Total"), font = ("indian rupee", 15), 
                        bg = "white", borderwidth = 2, relief = "groove", 
                        width = 23).grid(row = row_number+6, column = 1)

    quantityr = tkinter.Label(bill_window, text = "{0:^15d}"
                            .format(total_quantity), 
                            font = ("indian rupee", 15), bg = "white", 
                            borderwidth = 2, relief = "groove", 
                            width = 8).grid(row = row_number+6, column = 2)
    
    amountr = tkinter.Label(bill_window, text = "{0:^10d}"
                            .format(total_amount), 
                            font = ("indian rupee", 15), bg = "white", 
                            borderwidth = 2, relief = "groove", 
                            width = 8).grid(row = row_number+6, column = 4)
    
    def pay():
        simpledialog_box_ask_yes_no = messagebox.askyesno("", "Do you really \
                                            want to recieve transaction.")
        if simpledialog_box_ask_yes_no:
            messageboxpaydone = messagebox.showinfo("Thankyou", "Payment \
                                                    Successfull")

    pay_button = tkinter.Button(bill_window, text = "Recieve", 
                                font = ("algerian", 15), bg = "white", 
                                borderwidth = 3, relief = "raised", 
                                command = pay).place(x = 220, y = 600)
        

   

    
    


## The runner of the code
def main():

    img = tkinter.Label(main_window, image = fphoto, compound = "left", 
                        bg = "white", height = 100, 
                        width = 500).grid(row = 0, column = 0)

    flower = tkinter.Button(main_window, text = "flowery plant", 
                            font = ("algerian", 25), bg = "white", width = 24, 
                            height = 2, command = gotoflower).grid(row = 1, 
                            column = 0)

    decoration = tkinter.Button(main_window, text = "decoration plant", 
                                font = ("algerian", 25), bg = "white",
                                 width = 24, 
                                height = 2, 
                                command = gotodecoration).grid(row = 2, 
                                column = 0)

    desert = tkinter.Button(main_window, text = "desert plant", 
                            font = ("algerian", 25), bg = "white", width = 24, 
                            height = 2, command = gotodesert).grid(row = 3, 
                            column = 0)

    space = tkinter.Label(main_window, bg = "white", width = 24, 
                         height = 2).grid(row = 4, column = 0)

    bill = tkinter.Button(main_window, text = "Bill", font = ("algerian", 15, 
                        "bold"), bg = "white", command = billf).grid(row = 5, 
                        column = 0)
    main_window.mainloop()

## The block that will be run by default
if __name__ ==  "__main__":
    main_window = tkinter.Tk()
    main_window.title("Nursery")
    main_window.config(bg = "white")
    main_window.geometry("500x500+150+150")
    photo = tkinter.PhotoImage(file = "photo.png")
    fphoto = photo.subsample(3, 3)

    photo1 = tkinter.PhotoImage(file = "cancel.png")
    cancelimage = photo1.subsample(3,3)
    
    ## module function for profiling
    
    cProfile.run("main()", "output.dat")

    

    ## creating the output file that contains the profiled data
    with open("output_time.txt", "w") as f:
        p = pstats.Stats("output.dat", stream = f)
        p.sort_stats("time").print_stats()
