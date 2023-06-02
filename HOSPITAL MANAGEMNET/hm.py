from tkinter import *
from tkinter import messagebox
import mysql.connector as m




mydatabase=m.connect(host="localhost",user="root",password="Itsneverlate@1",database="project")

class  Hospital:
     def __init__(self,root):
         self.root=root
         self.root.title("Hospital Management System")
         self.root.geometry("1000x800")

         lbltitle=Label(self.root,bd=10,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",fg="black",bg="blue",font=("ariel",20,"bold"))
         lbltitle.pack(side=TOP,fill=X)

# =========================================Data frame====================================================

         Dataframe=Frame(self.root,bd=10,relief=RIDGE,bg="black")
         Dataframe.place(x=150,y=60,width=900,height=400)

         Dataframeleft=LabelFrame(Dataframe,bd=20,padx=10,pady=15,relief=RIDGE,font=("ariel",15,"bold"),text="Patient Information",fg="black",bg="orange")
         Dataframeleft.place(x=5,y=5,width=850,height=350)

#====================================Buttons frame=================================================

         Buttonframe=Frame(self.root,bd=20,relief=RIDGE,bg='green')
         Buttonframe.place(x=150,y=460,width=900,height=70)

#======================================Details frame================================================

         Detailsframe=Frame(self.root,bd=20,relief=RIDGE,bg="brown")
         Detailsframe.place(x=150,y=530,width=900,height=250)
         Detailsframe1=Text(Detailsframe,width=100,height=50)
         Detailsframe1.pack()
         
#====================labels and entry field==========================================================
         val_first_name=StringVar()
         val_last_name=StringVar
         val_age=IntVar()
         val_address=StringVar()
         val_DoA=StringVar()
         val_DoD=StringVar()
         val_NOT=StringVar()
         val_Doses=IntVar()
         val_DocId=IntVar()




         lblFirstname=Label(Dataframeleft,text="First Name",font=("ariel",13),bg='cyan',relief="groove")
         lblFirstname.grid()

         self.entryFirstname = Entry(Dataframeleft,textvariable="val_first_name",font=('arial', 10), bg="yellow", relief='groove')
         self.entryFirstname.grid(row=0,column=1,padx=20,pady=15)

         lbllastname=Label(Dataframeleft,text="Last name",font=("arial",13),bg="cyan",relief="groove")
         lbllastname.grid()
        
         self.entrylastname=Entry(Dataframeleft,textvariable="val_last_name",font=("arial",10),bg="yellow",relief='groove')
         self.entrylastname.grid(row=1,column=1,padx=20,pady=7)


         lblage=Label(Dataframeleft,text="Age",font=("arial",13),bg='cyan',relief='groove')
         lblage.grid()

         self.entryage = Entry(Dataframeleft,textvariable="val_age", font=("arial", 10), bg="yellow", relief='groove')
         self.entryage.grid(row=2, column=1, padx=20, pady=12)
         
         lbladdress=Label(Dataframeleft,text="Address",font=('arial',13),bg='cyan',relief='groove')
         lbladdress.grid(pady=20)

         self.entryaddress=Entry(Dataframeleft,textvariable="val_address",font=('arial',10),bg='yellow',relief='groove')
         self.entryaddress.grid(row=3,column=1)
         
         lblDOA=Label(Dataframeleft,text="Admit Date",font=('arial',13),bg='cyan',relief='groove')
         lblDOA.grid(row=4,column=0, padx=10,pady=6)

         self.entryDOA = Entry(Dataframeleft,textvariable="val_DoA", font=("arial", 10), bg="yellow", relief='groove')
         self.entryDOA.grid(row=4, column=1, padx=5, pady=15)

         lblDOD=Label(Dataframeleft,text="Date of discharge",font=('arial',13),bg="cyan",relief='groove')
         lblDOD.grid(row=0,column=2,padx=10,pady=20)


         self.entryDOD=Entry(Dataframeleft,textvariable="val_DoD",font=('arial',10),bg="yellow",relief="groove")
         self.entryDOD.grid(row=0,column=3,padx=10,pady=20)


         def submit_patient():
            first_name=self.entryFirstname.get()
            last_name=self.entrylastname.get()
            age=self.entryage.get()
            address=self.entryaddress.get()
            DoA=self.entryDOA.get()
            DoD=self.entryDOD.get()
            Tablet=self.entryNOT.get()
            Doses=self.entryDoses.get()
            DocId=self.entryDocId.get()

   
            cursor=mydatabase.cursor()
            query="insert into patientinfo( First_name,Last_name,Age,Address,Admit_Date,Discharge_Date,Name_of_Tablets,Doses,DocId) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(query,[first_name,last_name,age,address,DoA,DoD,Tablet,Doses,DocId])
            mydatabase.commit()




         def search_patient():
            first_name = self.entryFirstname.get()
            last_name = self.entrylastname.get()
            address = self.entryaddress.get()
        
            cursor = mydatabase.cursor()
            query = "SELECT * FROM patientinfo WHERE First_name LIKE %s AND Last_name LIKE %s AND Address LIKE %s"
        
            cursor.execute(query, [first_name, last_name, address])
            result = cursor.fetchall()
        
            if result:
                Detailsframe1.delete("1.0", END)
        
                for row in result:
                    patient_name = f"{row[1]} {row[2]}"
                    age = row[3]
                    location = row[4]
                    admission_date = row[5]
                    discharge_date = row[6]
                    tablets = row[7]
                    doses = row[8]
                    doctor_id = row[9]
        
                    details = f"Patient Name: {patient_name}\nAge: {age}\nLocation: {location}\nAdmission Date: {admission_date}\nDischarge Date: {discharge_date}\nTablets: {tablets}\nDoses: {doses}\nDoctor ID: {doctor_id}\n\n"
                    Detailsframe1.insert(END, details)
            else:
                messagebox.showerror("Error", "Patient not found!")




         def delete_patient():
              first_name = self.entryFirstname.get()
              last_name = self.entrylastname.get()
          
              cursor = mydatabase.cursor()
              query = "DELETE FROM patientinfo WHERE First_name = %s AND Last_name = %s"
          
              cursor.execute(query, [first_name, last_name])
              mydatabase.commit()
          
              messagebox.showinfo("Success", "All records of the patient deleted successfully.")
          
              
              self.entryFirstname.delete(0, END)
              self.entrylastname.delete(0, END)
         


         
         btnSubmit = Button(Dataframeleft, text="Submit", font=("arial", 12), bg="green", fg="white", command=submit_patient)
         btnSubmit.grid(row=4, column=2, padx=100, pady=8)

         btnSearch = Button(Dataframeleft, text="Search", font=("arial", 12), bg="green", fg="white", command= search_patient)
         btnSearch.grid(row=4, column=3, padx=100, pady=20)
        

         lblNOT=Label(Dataframeleft,text="Tablets",font=("arial",13),bg="cyan",relief="groove")
         lblNOT.grid(row=1,column=2,padx=10,pady=15)

         self.entryNOT=Entry(Dataframeleft,textvariable="val_NOT",font=('arial',10),bg="yellow",relief="groove")
         self.entryNOT.grid(row=1,column=3,padx=10,pady=1)

         lblDoses=Label(Dataframeleft,text='Doses',font=('arial',13),bg='cyan',relief='groove')
         lblDoses.grid(row=2,column=2,padx=10,pady=10)
          
         self.entryDoses=Entry(Dataframeleft,textvariable="val_Doses",font=("arial",10),bg="yellow",relief="groove")
         self.entryDoses.grid(row=2,column=3,padx=10,pady=10)

         lblDocId=Label(Dataframeleft,text="Doctor ID",font=('ariel',13),bg='cyan',relief='groove')
         lblDocId.grid(row=3,column=2,padx=10,pady=10)

         self.entryDocId=Entry(Dataframeleft,textvariable='val_DocId',font=('arial',10),bg='yellow',relief='groove')
         self.entryDocId.grid(row=3,column=3,padx=10,pady=10)
         


         btnSubmit = Button(Buttonframe, text="DELETE", font=("arial", 12), bg="black", fg="white", command=delete_patient)
         btnSubmit.grid(row=0, column=10,padx=400)
         


root=Tk()
ob=Hospital(root)
root.mainloop()