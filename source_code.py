from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg

from PIL import Image, ImageTk
import mysql.connector as mysql

def verify1():
    u=user.get()
    p=pas.get()
    if(u=="admin" and p=="12345"):
          root.destroy()
          main()
    else:
       msg.showinfo("Warning","please check id and password")   
           
          
    
def main():
     
     def get():
         
       Fra3=Frame(roo,height=380,width=720,bg="grey",borderwidth=5,highlightbackground="dark blue", highlightcolor="dark blue", highlightthickness=10)
       Fra3.place(x=470,y=120)  
       con=mysql.connect(host="localhost",user="root",password="Harshal@1008",database="st")
       cursor=con.cursor()
       cursor.execute("select * from student")
     
       rows=cursor.fetchall()
     
       l1=ttk.Treeview(Fra3,columns=(1,2,3,4),show="headings",selectmode='browse')
       ttk.Style().configure("Treeview", background="red",foreground="silver", fieldbackground="red")
       l1.pack(side='left')
       vsb = ttk.Scrollbar(Fra3, orient="vertical", command=l1.yview)
       vsb.pack(side='right', fill='y')
       l1.heading(1,text="ID")
       l1.column("1", minwidth=0, width=100, stretch=NO)
       l1.heading(2,text="NAME")
       l1.heading(3,text="EMAIL")
       l1.heading(4,text="PHONE NO")
       l1.configure(yscrollcommand=vsb.set)
           
       for row in rows:
           l1.insert('','end',values=row)
       con.close()      
     def get1():
        
        get()
             
         
     def delete():
     
      if(e21.get()==""):
        msg.showinfo("insert status","please enter id ")
            
    
      else:
       try:
        con=mysql.connect(host="localhost",user="root",password="",database="st")
        cursor=con.cursor()
        cursor.execute("delete from student where id='"+ e21.get() +"'")
        cursor.execute("commit");
        e21.delete(0,'end')
        
        msg.showinfo("delete status","Successfully deleted");
        get1()
       except:
        msg.showinfo("Delete status","id not found...!!!")   
        con.close(); 
    
     
     def insert1():
        def update():
          id=e_std_id.get()
          name=e_std_name.get()
          mail=e_std_mail.get()
          phone=e_std_phone.get()
          if(id=="" or name=="" or mail=="" or phone==""):
            msg.showinfo("insert status","Please insert all fields")
    
  
          else:
           con=mysql.connect(host="localhost",user="root",password="",database="st")
           cursor=con.cursor()
           cursor.execute("update student set name='"+ name +"',mail='"+ mail +"',phone='"+ phone +"' where id='"+ id +"' ")
           cursor.execute("commit");
           e_std_id.delete(0,'end')
           e_std_name.delete(0,'end')
           e_std_mail.delete(0,'end')
           e_std_phone.delete(0,'end')
           msg.showinfo("Update Status","Successfully Updated.");
           get1()
           con.close();
        def clr():
          e_std_id.delete(0,'end')
          e_std_name.delete(0,'end')
          e_std_mail.delete(0,'end')
          e_std_phone.delete(0,'end') 
        def insert():
         id=e_std_id.get()
         name=e_std_name.get()
         mail=e_std_mail.get()
         phone=e_std_phone.get()
  
        
         if(id=="" or name=="" or mail=="" or phone==""):
          msg.showinfo("insert status","Please insert all fields")
         else:
          try:
           con=mysql.connect(host="localhost",user="root",password="",database="st")
           cur=con.cursor()
           
     
       
           cur.execute("insert into student values('"+ id +"','"+ name +"','"+ mail +"','"+ phone +"')")
           cur.execute("commit");
           
      
      
           e_std_id.delete(0,'end')
           e_std_name.delete(0,'end')
           e_std_mail.delete(0,'end')
           e_std_phone.delete(0,'end')
           msg.showinfo("insert status","Successfully inserted");
           get1()
           
          except:
           msg.showinfo("insert status","id already present!!!")
             
        label=Label(Fra1,text="*  REGISTER STUDENT  *",fg="black",bg="silver",font=("times new roman",15,"bold"))
        label.place(x=60)
        std_id=Label(Fra1,text="STUDENT ID:",fg="black",bg="silver",font={'bold'})
        std_id.place(x=50,y=50)

        std_name=Label(Fra1,text="STUDENT NAME:",fg="black",bg="silver",font={'bold'})
        std_name.place(x=50,y=80)
 
        std_mail=Label(Fra1,text="EMAIL ID:",fg="black",bg="silver",font={'bold'})
        std_mail.place(x=50,y=110)

        std_phone=Label(Fra1,text="CONTACT NO:",fg="black",bg="silver",font={'bold'})
        std_phone.place(x=50,y=140)
 
        e_std_id=Entry(Fra1,fg="blue")
        e_std_id.place(x=180,y=50)

        e_std_name=Entry(Fra1,fg="blue")
        e_std_name.place(x=180,y=80)

        e_std_mail=Entry(Fra1,fg="blue")
        e_std_mail.place(x=180,y=110)

        e_std_phone=Entry(Fra1,fg="blue")
        e_std_phone.place(x=180,y=140)
        insert1=Button(Fra1,text="ADD",width=10,command=insert,font=("italic",10),bg="green",fg="white")
        insert1.place(x=50,y=200)
        get2=Button(Fra1,text="CLEAR",width=10,command=clr,font=("italic",10),bg="green",fg="white")
        get2.place(x=150,y=200)
        get3=Button(Fra1,text="UPDATE",width=10,command=update,font=("italic",10),bg="green",fg="white")
        get3.place(x=250,y=200)
        
        
    
    
    
        
         
       
    

          
             
     roo=Tk()
     roo.geometry("1250x600")
     roo.resizable(0,0)

     roo.title("STUDENT DATABASE ")

     stu=Label(roo,text="* STUDENT DATABASE *",bg="silver",fg="black",height=2,font=("times new roman",16,"bold"))
     stu.pack(fill=X,side=TOP)

    
     Fra1=Frame(roo,height=300,borderwidth=5,highlightbackground="dark blue", highlightcolor="dark blue", highlightthickness=10,width=370,bg="silver")
     Fra1.place(x=10,y=70)
     Fra4=Frame(roo,height=200,width=370,borderwidth=5,highlightbackground="dark blue", highlightcolor="dark blue", highlightthickness=10,bg="silver")
     Fra4.place(x=10,y=390)
     labe2=Label(Fra4,text="* DELETE STUDENT RECORD *",fg="black",bg="silver",font=("times new roman",15,"bold"))
     labe2.place(x=30,y=20)
     std_id1=Label(Fra4,text="STUDENT ID:",fg="black",bg="silver",font={'bold'})
     std_id1.place(x=50,y=70)
     e21=Entry(Fra4)
     e21.place(x=170,y=70)
    
     
        
     get()
       

     insert1()
    

     delete1=Button(Fra4,text="DELETE",width=10,command=delete,font=("italic",10),bg="green",fg="white")
     delete1.place(x=100,y=120)
     rec=Label(roo,text="* STUDENT RECORDS *",font=("times new roman",20,"bold"),fg="black")
     rec.place(x=700,y=70)


     update1=Button(roo,text="REFRESH",width=10,command=get1,font=("italic",10),bg="green",fg="white")
     update1.place(x=500,y=390)

     
    
     roo.mainloop()

       

root=Tk()
root.title("LOG IN")
img4 = ImageTk.PhotoImage(Image.open(r"C:\Users\sudhakar mankar\Desktop\pa.png"))
img5 = ImageTk.PhotoImage(Image.open(r"C:\Users\sudhakar mankar\Desktop\p.png"))
root.geometry("800x600+300+50")
root.configure(bg="grey")
root.resizable(0,0)

nn=Frame(root,bg="white",height=360,width=400)
nn.place(x=200,y=100)
l1=Label(nn,text="LOG IN",font=("times new roman",20,"bold"),fg="black",bg="white")
l1.place(x=150,y=20)
h2=Label(nn,text="User Name",image=img5,compound=LEFT,font=("times new roman",15,"bold"),bg="white" )
h2.place(x=50,y=80)
user=Entry(nn,width=40)
           
user.place(x=50,y=130)
u=Label(nn,text="Password",image=img4,compound=LEFT,font=("times new roman",15,"bold"),bg="white" )
u.place(x=50,y=180)
pas=Entry(nn,show="*",width=40)
pas.place(x=50,y=230)

btn=Button(nn,text="LOG IN",command=verify1,width=16,bg="green",fg="white",font=("times new roman",15,"bold"),relief=GROOVE)
btn.place(x=80,y=290)





root.mainloop()
















    
