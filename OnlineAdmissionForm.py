# module importing
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk,ImageDraw,ImageFont
import tkinter.messagebox as message_box
import mysql.connector as sql_con

# to clear the details entered by user
def clear():
    txt_full_name.delete(0,"end")
    txt_parent_name.delete(0,"end")
    txt_parent_occupation.delete(0,"end")
    cmb_date.current(0)
    cmb_month.current(0)
    cmb_year.current(0)
    cmb_gender.current(0)
    txt_permanent_address.delete(0,"end")
    txt_contact_number.delete(0,"end")
    txt_email_id.delete(0,"end")

# to fetch data provided by user
def register_data():
    fn = txt_full_name.get()
    pn = txt_parent_name.get()
    op = txt_parent_occupation.get()
    dt = cmb_date.get()
    mt = cmb_month.get()
    yr = cmb_year.get()
    gd = cmb_gender.get()
    ad = txt_permanent_address.get()
    no = txt_contact_number.get()
    em = txt_email_id.get()
    cb = check_box_var.get()
    if fn=="" or pn=="" or op=="" or dt=="Date" or mt=="Month"or yr=="Year"or gd=="Gender"or ad==""or no==""or em=="":
        message_box.showinfo("ERROR","ALL FIELDS ARE REQUIRED")
    elif cb=="off":
        message_box.showinfo("ERROR","PLEASE AGREE OUR TERMS AND CONDITIONS")
    else:
        con=sql_con.connect(host="localhost", user="root", password="2003", database="bbit")
        cur=con.cursor()
        cur.execute("insert into admissionform2k23(Applicant_Name, Parent_Name, Parent_Occupation,Date_of_Birth, Month_of_Birth,Year_of_Birth, Gender,Permanent_Address, Contact_number, Email_ID)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(fn,pn,op,dt,mt,yr,gd,ad,no,em))
        con.commit()
        message_box.showinfo("NOTIFICATION","APPLIED SYCCESSFULLY")
        clear()
        con.close()

# main menu
root=Tk()
root.title("Registration window")
root.geometry("1300x750")

#background image
root.bg=ImageTk.PhotoImage(file="C:\\Users\\user\\Downloads\\free-registration-forms.jpg")
bg=Label(root, image=root.bg).place(x=-45,y=-63)
frame=Frame(root,bg="blueviolet")
frame.place(x=620, y=0, width=810, height=855)

#texts
title = Label(frame,text="ADMISSION FORM", font= ("showcard gothic", 35,"underline"),
    bg="blueviolet",fg="yellow").place(x=120,y=60)
full_name = Label (frame, text="APPLICANT's FULL NAME : ", font=("cooper black", 13),
    bg="blueviolet", fg="yellow").place (x=50,y=170)
parent_name = Label (frame,text="PARENT's FULL NAME : ", font=("cooper black", 13),
    bg="blueviolet", fg="yellow").place (x=50,y=220)
parent_occupation = Label (frame,text="PARENT's OCCUPATION : ", font= ("cooper black", 13),
    bg="blueviolet", fg="yellow").place (x=50,y=270)
date_of_birth = Label (frame,text="DATE OF BIRTH : ", font=("cooper black", 13),
    bg="blueviolet", fg="yellow").place (x=50,y=320)
gender = Label (frame,text="GENDER : ", font=("cooper black", 13),
    bg="blueviolet", fg="yellow").place (x=50,y=370)
permanent_address = Label (frame,text="PERMANENT ADDRESS : ", font= ("cooper black", 13),
    bg="blueviolet", fg="yellow").place (x=50,y=420)
contact_number = Label (frame,text="CONTACT NUMBER : ", font= ("cooper black", 13),
    bg="blueviolet", fg="yellow").place (x=50,y=470)
email_id = Label (frame,text="EMAIL ID : ", font= ("cooper black", 13),
    bg="blueviolet", fg="yellow").place (x=50,y=520)

#ENTRY BOXES
txt_full_name = Entry(frame,font=("mv boli",13),bg="azure",bd=0)
txt_parent_name = Entry(frame,font=("mv boli",13),bg="azure",bd=0)
txt_parent_occupation = Entry(frame, font=("mv boli",13),bg="azure",bd=0)
txt_permanent_address = Entry(frame, font=("mv boli",13) ,bg="azure",bd=0)
txt_contact_number = Entry (frame,font=("mv boli",13),bg="azure",bd=0)
txt_email_id = Entry(frame,font=("mv boli",13) ,bg="azure",bd=0)
#POSITIONS
txt_full_name.place (x=340,y=170,width=290)
txt_parent_name.place (x=340,y=220,width=290)
txt_parent_occupation.place (x=340,y=270,width=290)
txt_permanent_address.place (x=340,y=420,width=290)
txt_contact_number.place (x=340,y=470,width=290)
txt_email_id.place (x=340,y=520,width=290)
#COMBO BOXEs
cmb_date = ttk.Combobox (frame, font= ("mv boli",13,"bold"),state="readonly", justify=CENTER)
cmb_date ["values"]= ("Date", "1", "2", "3", "4", "5", "6", "7", "8", "g", "10", "11", "12", "13", "14", "15", "16", "17", "18",
"19", "20", "21", "22", "23", "24", "25","26", "27", "28", "29", "30" ,"31")
cmb_date.place (x=340,y=320,width=85)
cmb_date.current (0)
cmb_month = ttk.Combobox(frame, font=("mv boli",13, "bold"),state="readonly",justify=CENTER)
cmb_month["values"] = ("Month", "January", "February", "March","April"
"May", "June", "July", "August", "September", "October", "November", "December")
cmb_month.place (x=433,y=320,width=100)
cmb_month.current (0)
cmb_year = ttk.Combobox(frame,font=("mv boli",13,"bold"),state="readonly", justify=CENTER)
cmb_year["values"] = ("Year","1990","1991","1992","1993","1994","1995","1996","1997","1998","1999","2000","2001",
"2002", "2003","2004","2005","2006","2007","2008","2009","2010")
cmb_year.place (x=540,y=320,width=90)
cmb_year.current (0)
cmb_gender = ttk.Combobox(frame, font=("mv boli",13, "bold"),state="readonly",justify=CENTER)
cmb_gender["values"] = ("Gender", "Male", "Female", "Others")
cmb_gender.place (x=340,y=370,width=290)
cmb_gender.current (0)

#CHECK воX
check_box_var = StringVar()
check_box = Checkbutton(frame,text="I AGREE THE TERMS AND CONDITIONS", variable=check_box_var ,
 onvalue="on",offvalue="off",cursor="hand2",font=("mv boli",13,"bold"),
  bg="gold",fg="black")
check_box.deselect()
check_box.place(x=140,y=580)
#BUTTON
registration_button=Button(frame,text="SUBMIT",font=("cooper black",15,"bold"), command=register_data)
registration_button.place(x=280,y=650)
root.mainloop()
