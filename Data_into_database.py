from tkinter import *
from tkinter import messagebox
import mysql.connector

window = Tk()
window.title("Client Information Updation")
window.configure(background="#0D4064",borderwidth=2,relief= GROOVE)
window.geometry('550x480')
window.resizable(False,False)

#Connection Establishment
client = mysql.connector.connect(host='localhost', user='root', password='',
                                     port='3306', database='know_your_client')
c = client.cursor()

#Run the below excution once to create a table named kyc. Multiple execution will result in error hence comment it after execution.

c.execute('''create table kyc(
Name varchar(30),
Age int,
Contact_info varchar(30),
Address varchar(50))''');
client.commit()
def submit():
    try:
        f_name = entry_firstname.get().title()
        l_name = entry_lastname.get().title()
        Name1 = f_name +" "+l_name
        Age1 = int(entry_age.get())
        Contact_info1 = entry_email.get().lower()
        address = entry_address.get()
        city = entry_city.get().title()
        state= entry_state.get().title()
        country = entry_country.get().title()
        pin = entry_pin.get()
        Address1 = address+","+city+",\n"+state+",\n"+country+"-"+pin

        c = client.cursor()
        c.execute('''INSERT INTO kyc (Name, Age, Contact_info, Address) VALUES (%s, %s, %s, %s)''',
                  (Name1, Age1, Contact_info1, Address1))
        client.commit()
        entry_firstname.delete(0,END)
        entry_lastname.delete(0,END)
        entry_age.delete(0,END)
        entry_email.delete(0,END)
        entry_address.delete(0,END)
        entry_city.delete(0,END)
        entry_state.delete(0,END)
        entry_country.delete(0,END)
        entry_pin.delete(0,END)
        messagebox.showinfo("Success","client details added successfully!..")
    except:
        messagebox.showinfo("Warning", "Age should be of integer literal")

label_head = Label(window, text="Client Information Updation Form ", font=("Times New Roman",16),fg="white",bg="#0D4064",justify=CENTER)
label_head.grid(row=0,column=0,columnspan=2,padx=10,pady=5,ipadx=10)

label_firstname = Label(window, text="First Name ", font=("Times New Roman",12),fg="white",bg="#0D4064",justify=LEFT)
label_firstname.grid(row=2,column=0,padx=10,pady=5,ipadx=10)
entry_firstname = Entry(window, font=("Times New Roman",12),bg="#0D4064",relief=SUNKEN ,fg="White")
entry_firstname.grid(row=2,column=1,padx=10,pady=10,ipadx=90)


label_lastname = Label(window, text="Last Name ", font=("Times New Roman",12),fg="white",bg="#0D4064",justify=LEFT)
label_lastname.grid(row=3,column=0,padx=10,pady=5,ipadx=10)
entry_lastname = Entry(window, font=("Times New Roman",12),bg="#0D4064",relief=SUNKEN,fg="White")
entry_lastname.grid(row=3,column=1,padx=10,pady=10,ipadx=90)

label_email = Label(window, text="Contact Information ", font=("Times New Roman",12),fg="white",bg="#0D4064",justify=LEFT)
label_email.grid(row=4,column=0,padx=10,pady=5,ipadx=10)
entry_email = Entry(window, font=("Times New Roman",12),bg="#0D4064",relief=SUNKEN,fg="White")
entry_email.grid(row=4,column=1,padx=10,pady=10,ipadx=90)

label_age = Label(window, text="Age ", font=("Times New Roman",12),fg="white",bg="#0D4064",justify=LEFT)
label_age.grid(row=5,column=0,padx=10,pady=5,ipadx=10)
entry_age = Entry(window, font=("Times New Roman",12),bg="#0D4064",relief=SUNKEN,fg="White")
entry_age.grid(row=5,column=1,padx=10,pady=10,ipadx=90)

label_address = Label(window, text="Address ", font=("Times New Roman",12),fg="white",bg="#0D4064",justify=LEFT)
label_address.grid(row=6,column=0,padx=10,pady=5,ipadx=10)
entry_address = Entry(window, font=("Times New Roman",12),bg="#0D4064",relief=SUNKEN,fg="White")
entry_address.grid(row=6,column=1,padx=10,pady=10,ipadx=90)

label_city = Label(window, text="City ", font=("Times New Roman",12),fg="white",bg="#0D4064",justify=LEFT)
label_city.grid(row=7,column=0,padx=10,pady=5,ipadx=10)
entry_city = Entry(window, font=("Times New Roman",12),bg="#0D4064",relief=SUNKEN,fg="White")
entry_city.grid(row=7,column=1,padx=10,pady=10,ipadx=90)

label_state = Label(window, text="State ", font=("Times New Roman",12),fg="white",bg="#0D4064",justify=LEFT)
label_state.grid(row=8,column=0,padx=10,pady=5,ipadx=10)
entry_state = Entry(window, font=("Times New Roman",12),bg="#0D4064",relief=SUNKEN,fg="White")
entry_state.grid(row=8,column=1,padx=10,pady=10,ipadx=90)

label_country= Label(window, text="Country ", font=("Times New Roman",12),fg="white",bg="#0D4064",justify=LEFT)
label_country.grid(row=9,column=0,padx=10,pady=5,ipadx=10)
entry_country = Entry(window, font=("Times New Roman",12),bg="#0D4064",relief=SUNKEN,fg="White")
entry_country.grid(row=9,column=1,padx=10,pady=10,ipadx=90)


label_pin= Label(window, text="Pincode ", font=("Times New Roman",12),fg="white",bg="#0D4064",justify=LEFT)
label_pin.grid(row=10,column=0,padx=10,pady=5,ipadx=10)
entry_pin = Entry(window, font=("Times New Roman",12),bg="#0D4064",relief=SUNKEN,fg="White")
entry_pin.grid(row=10,column=1,padx=10,pady=10,ipadx=90)


button_submit =Button(window, text="Submit", font=("Times New Roman",12),fg="white",bg="#0D4064",justify=CENTER, command=submit).grid(row=11,column=0,columnspan=2,ipadx=15,pady=10)

window.mainloop()
