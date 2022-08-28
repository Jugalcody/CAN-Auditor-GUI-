import tkinter as tk,mysql.connector as mycon,os
from tkinter import messagebox as mb;
root=tk.Tk()
root.geometry("900x400+210+100")
root.configure(bg="skyblue")
root.title("CAN Money Collection")
tk.Label(root,text="CAN Money Record",font=("Arial",25 ),fg="blue").place(x=270+30,y=20)
k=tk.Label(root,text="",font=('helvatica',10,'bold'))
k.place(x=580,y=80)
a=tk.Label(root,text="Name : ").place(x=270+30,y=120)
b=tk.Entry()
b.place(x=270+110,y=120,width=200)

c=tk.Label(root,text="Roll : ").place(x=270+30,y=160)
d=tk.Entry()
d.place(x=110+270,y=160,width=200)

e=tk.Label(root,text="year : ").place(x=30+270,y=200)
f=tk.Entry()
f.place(x=110+270,y=200,width=200)

o=tk.Label(root,text="paid amt : ").place(x=30+270,y=240)
p=tk.Entry()
p.place(x=110+270,y=240,width=200)

try:         
      global mydb
      mydb=mycon.connect(host="localhost",user="jugal",passwd="Jugal2002@")
      
except:
       os.system("service mysql start") 
        
def submit():
      if b.get()!="" and (d.get()!="" and f.get!=""):
         cursor=mydb.cursor()
         cursor.execute("create database if not exists CAN")
         cursor.execute("use CAN")
         cursor.execute("create table if not exists money( sno int auto_increment primary key, name varchar(100) not null, roll_no varchar(100) unique key, paid_money int(100) not null)")
         cursor.execute("Select sno from money order by sno desc limit 1")
         i=int(list(cursor.fetchone())[0])
         i+=1
         j="insert into money values(%s,%s,%s,%s,%s)"
         v=(i,b.get(),d.get(),p.get(),f.get())
         try:
             cursor.execute(j,v)
             mydb.commit()
         except:
               mb.showerror("error","duplicate roll number!")      
         cursor.execute("select sum(paid_money) from money")
         m=list(cursor.fetchone())[0]
         l=f"Total funds : Rs {m}"
         k.config(text=l)
      else:
            mb.showinfo("no data","no values entered")
         
h=tk.Button(root,text="Submit",cursor="plus",command=submit).place(x=120+270,y=280)

root.mainloop()
