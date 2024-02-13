#frontend 
from tkinter import *
import tkinter.messagebox
import stDatabase_BackEnd 
class Student:
    def __init__(self, root):
        self.root=root
        self.root.title("student database system")
        self.root.geometry("1350x7500+0+0")
        self.root.config(bg="cadet blue")

        self.stid=StringVar()
        print(self.stid)
        self.firstname=StringVar()
        self.surname=StringVar()
        self.Dob=StringVar()
        self.Age=StringVar()
        self.Gender=StringVar()
        self.Address=StringVar()
        self.Mobile=StringVar()
        #===================functions==========================
        def iExit():
            iExit=tkinter.messagebox.askyesno("student database system","confirm if you want to exit ")
            self.root.destory()
            return
        def clearDate():
           self.txtstdid.delete(0,END)
           self.txtfirst.delete(0,END)
           self.txtsurnam.delete(0,END)
           self.txtdob.delete(0,END)
           self.txtage.delete(0,END)
           self.txtgender.delete(0,END) 
           self.txtaddress.delete(0,END)
           self.txtmobile.delete(0,END)
        def addDate():
           stid=self.stid
           print(self.stid)
           firstname=self.firstname
           surname=self.surname
           dob=self.Dob
           age=self.Age
           gender=self.Gender
           address=self.Address
           mobile=self.Mobile
           stDatabase_BackEnd.addStRec(stid, firstname,surname, dob,age,gender,\
                                address,mobile)
           studentlist.delete(0,END)
           studentlist.insert(END,(stid.get(),firstname.get(),surname.get(), dob.get(),age.get(),gender.get(),\
                                address.get(),mobile.get()))
        def DisplayData():
            studentlist.delete(0,END)
            for row in  stDatabase_BackEnd.viewDate():
                studentlist.insert(END,row,str(""))

        def studentRec(event):
           self.sd
           search = studentlist.curselection()[0]
           sd = studentlist.get(search)
           print(sd)
        #    search=studentlist.curselection()[0]
        #    sd=studentlist.get(search)
           self.txtstdid.delete(0,END)
           self.txtstdid.insert(END,self.sd[1])
           self.txtfirst.delete(0,END)
           self.txtfirst.insert(END,self.sd[2])
           self.txtsurnam.delete(0,END)
           self.txtsurnam.insert(END,self.sd[2])
           self.txtdob.delete(0,END)
           self.txtdob.insert(END,self.sd[3])
           self.txtage.delete(0,END)
           self.txtage.insert(END,self.sd[4])
           self.txtgender.delete(0,END) 
           self.txtgender.insert(END,self.sd[5])
           self.txtaddress.delete(0,END)
           self.txtaddress.insert(END,self.sd[6])
           self.txtmobile.delete(0,END)
           self.txtmobile.insert(END,self.sd[7])

        def deleteData():
           if(len(self.stid.get())!=0):
               stDatabase_BackEnd.deleteRec(self.sd[0]) 
               clearDate()  
               DisplayData()  
        def searchdatabase():
           studentlist.delete(0,END)
           for row in stDatabase_BackEnd.searchData(self.stid.get(),self.firstname.get(),self.surname.get(), self.Dob.get(),self.Age.get(),self.Gender.get(),\
                                self.Address.get(),self.Mobile.get()):
                       studentlist.insert(END,row,str(""))
        def update():
            if(len(self.stid.get())!=0):
                stDatabase_BackEnd.dataUpdate(self.sd[0])
            if(len(self.stid.get())!=0):
                stDatabase_BackEnd.addStRec(self.stid.get(),self.firstname.get(),self.surname.get(), self.Dob.get(),self.Age.get(),self.Gender.get(),\
                                self.Address.get(),self.Mobile.get())    
                studentlist.delete(0,END)
                studentlist.insert(END,(self.stid.get(),self.firstname.get(),self.surname.get(), self.Dob.get(),self.Age.get(),self.Gender.get(),\
                                self.Address.get(),self.Mobile.get()))       
        #=======================================Frame=============================
        MainFrame=Frame(self.root,bg="cadet blue")
        MainFrame.grid()
        titFrame=Frame(MainFrame,bd=2,padx=200,pady=8,bg="Ghost White",relief=RIDGE)
        titFrame.pack(side=TOP)
        self.lbltit=Label(titFrame,font=('arial',47,'bold'),text="student Database Management System",bg="Ghost White" )
        self.lbltit.grid()

        ButtonFrame=Frame(MainFrame,bd=2,width=1350,height=70,padx=18,pady=10,bg="Ghost White",relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)
        
        DataFrame=Frame(MainFrame,bd=1,width=1300,height=400,padx=20,pady=20,relief=RIDGE,bg="cadet blue")
        DataFrame.pack(side=BOTTOM)

        DataFrameLeft=LabelFrame(DataFrame,bd=1,width=1000,height=600,padx=20,relief=RIDGE,bg="Ghost White",font=('arial',20,'bold'),text="student info" )
        DataFrameLeft.pack(side=LEFT)

        DataFrameRight=LabelFrame(DataFrame,bd=1,width=450,height=300,padx=31,pady=3,relief=RIDGE,bg="Ghost White",font=('arial',20,'bold'),text="studrnt details" )
        DataFrameRight.pack(side=RIGHT)
        #============================================Labels and entry widgets================
        self.lblstdid=Label(DataFrameLeft,font=('arial',20,'bold'),text="student id",padx=2,pady=2,bg="Ghost White")
        self.lblstdid.grid(row=0,column=0,sticky=W) 

        self.txtstdid=Entry(DataFrameLeft,font=('arial',20,'bold'),textvariable=self.stid,width=39)
        self.txtstdid.grid(row=0,column=1,sticky=W) 

        self.lblfirst=Label(DataFrameLeft,font=('arial',20,'bold'),text="firstname",padx=2,pady=2,bg="Ghost White")
        self.lblfirst.grid(row=1,column=0,sticky=W) 

        self.txtfirst=Entry(DataFrameLeft,font=('arial',20,'bold'),textvariable=self.firstname,width=39)
        self.txtfirst.grid(row=1,column=1,sticky=W) 

        self.lblsurname=Label(DataFrameLeft,font=('arial',20,'bold'),text="surname",padx=2,pady=2,bg="Ghost White")
        self.lblsurname.grid(row=2,column=0,sticky=W) 

        self.txtsurnam=Entry(DataFrameLeft,font=('arial',20,'bold'),textvariable=self.surname,width=39)
        self.txtsurnam.grid(row=2,column=1,sticky=W)

        self.lbldob=Label(DataFrameLeft,font=('arial',20,'bold'),text="DOB",padx=2,pady=2,bg="Ghost White")
        self.lbldob.grid(row=3,column=0,sticky=W) 

        self.txtdob=Entry(DataFrameLeft,font=('arial',20,'bold'),textvariable=self.Dob,width=39)
        self.txtdob.grid(row=3,column=1,sticky=W)

        self.lblage=Label(DataFrameLeft,font=('arial',20,'bold'),text="Age",padx=2,pady=2,bg="Ghost White")
        self.lblage.grid(row=4,column=0,sticky=W) 

        self.txtage=Entry(DataFrameLeft,font=('arial',20,'bold'),textvariable=self.Age,width=39)
        self.txtage.grid(row=4,column=1,sticky=W)

        self.lblgender=Label(DataFrameLeft,font=('arial',20,'bold'),text="Gender",padx=2,pady=2,bg="Ghost White")
        self.lblgender.grid(row=5,column=0,sticky=W) 

        self.txtgender=Entry(DataFrameLeft,font=('arial',20,'bold'),textvariable=self.Gender,width=39)
        self.txtgender.grid(row=5,column=1,sticky=W)

        self.lbladdress=Label(DataFrameLeft,font=('arial',20,'bold'),text="Address",padx=2,pady=2,bg="Ghost White")
        self.lbladdress.grid(row=6,column=0,sticky=W) 

        self.txtaddress=Entry(DataFrameLeft,font=('arial',20,'bold'),textvariable=self.Address,width=39)
        self.txtaddress.grid(row=6,column=1,sticky=W)

        self.lblmobile=Label(DataFrameLeft,font=('arial',20,'bold'),text="Mobile",padx=2,pady=2,bg="Ghost White")
        self.lblmobile.grid(row=7,column=0,sticky=W) 

        self.txtmobile=Entry(DataFrameLeft,font=('arial',20,'bold'),textvariable=self.Mobile,width=39)
        self.txtmobile.grid(row=7,column=1,sticky=W)
#================================= listBox & scroll box============================
        scrollbar=Scrollbar(DataFrameRight)
        scrollbar.grid(row=0,column=0,sticky='ns')

        studentlist=Listbox(DataFrameRight,width=41,height=16,font=('arial',12,'bold'), yscrollcommand=scrollbar.set)
        studentlist.bind("<<listboxselect>>",studentRec)
        studentlist.grid(row=0,column=0,padx=0)
        scrollbar.config(command=studentlist.yview)
        #=====================Button widget========================
        self.butnAddDate=Button(ButtonFrame,text="Add New",font=('arial',20,'bold'),height=1,width=10,bd=4,command=addDate)
        self.butnAddDate.grid(row=0,column=0)

        self.butndisplay=Button(ButtonFrame,text="Display",font=('arial',20,'bold'),height=1,width=10,bd=4,command=DisplayData)
        self.butndisplay.grid(row=0,column=1)

        self.butnclear=Button(ButtonFrame,text="Clear",font=('arial',20,'bold'),height=1,width=10,bd=4,command=clearDate)
        self.butnclear.grid(row=0,column=2)
        self.butndelete=Button(ButtonFrame,text="Delete",font=('arial',20,'bold'),height=1,width=10,bd=4,command=deleteData)
        self.butndelete.grid(row=0,column=3)
        self.butnsearch=Button(ButtonFrame,text="Search",font=('arial',20,'bold'),height=1,width=10,bd=4,command=searchdatabase)
        self.butnsearch.grid(row=0,column=4)
        self.butnupdate=Button(ButtonFrame,text="Update",font=('arial',20,'bold'),height=1,width=10,bd=4,command=update)
        self.butnupdate.grid(row=0,column=5)
        self.butnexit=Button(ButtonFrame,text="Exit",font=('arial',20,'bold'),height=1,width=10,bd=4,command=iExit)
        self.butnexit.grid(row=0,column=6)
if __name__=='__main__':
    root=Tk()
    application=Student(root)
    root.mainloop()
