from tkcalendar import *
from tabnanny import check
from tkinter import *
from tkinter import ttk
import pandas as pd
win = Tk()
win.geometry("800x300")
# calendar = Calendar(win)
canvas = Canvas(win,width=300, height=200)
def them():
    # data = pd.ExcelFile("customer.xlsx")
    df1 = pd.read_excel('customer.xlsx')
    df2 = df1.drop(df1.filter(regex='Unnamed'), axis=1)
    ma = ent1.get()
    ten = ent2.get()
    bir = ent3.get()
    diachi = ent4.get()
    dienthoai = ent5.get()
    # data1 = {'Hãng DT':[hang], 'Mã điện thoại':[ma], 'Tên điện thoại':[ten], 'Màu sắc':["Đen"], 'Số Lượng':[soluong], 'Đơn giá':[diachi]}
    df1 = pd.DataFrame({'Mã KH':[ma], 'Tên khách hang':[ten], 'Ngày sinh':[bir], 'Gioi tinh':["Nam"], 'Địa chỉ':[diachi], 'Điện thoai':[dienthoai]})
    # writer = pd.ExcelWriter('customer.xlsx')
    df1.to_excel('customer.xlsx', sheet_name="Sheet1", index=False)
    for  row in df1.iterrows():
        sho.insert(END, row)
def sua():
    global df
    df = pd.read_excel('customer.xlsx')
    ma = ent1.get()
    ten = ent2.get()
    bir = ent3.get()
    diachi = ent4.get()
    dienthoai = ent5.get()
    ent1.delete(0, END)
    ent1.insert(0, df.at[ma, 'Mã KH'])
    ent2.delete(0, END)
    ent2.insert(0, df.at[ten, 'Tên Kh'])
    ent3.delete(0, END)
    ent3.insert(0, df.at[bir, 'Ngày sinh'])
    ent4.delete(0,END)
    ent4.insert(0, df.at[diachi, 'Địa chỉ'])
    ent5.delete(0,END)
    ent5.insert(0, df.at[dienthoai, 'Điện thoại'])
    def save():
        global df
        df = pd.read_excel('customer.xlsx')
        df.at[ma, 'Mã khách hàng'] == ma
        # writer = pd.ExcelFile('customer.xlsx')
        df.to_excel('customer.xlsx', sheet_name='Sheet1', index=False)
        # writer.save()
    for index, row in df.iterrows():
        sho.insert(index, row)
def xoa():
    df = pd.read_excel('customer.xlsx')
    ma = ent1.get()
    df[df['Mã KH']] != ma
    df.drop(df.filter(regex='Mã KH'), axis=1)
    df.to_excel('customer.xlsx', index=False)
    for index, row in df.iterrows():
        sho.insert(index, row)
def huy():
    ent1.delete(0, END)
    ent2.delete(0, END)
    ent3.delete(0, END)
    ent4.delete(0, END)
    ent5.delete(0, END)
def thoat():
    win.destroy()
# Tao ra cac chuc nang tren giao dien
la1 = Label(win, text="Thong tin khach hang")
# la2 = Label(win, text="Danh sach hoa don")


sho = Listbox(win, width=100)
lab1 = Label(win, text="Ma KH")
ent1 = Entry(win, width=15)
lab2 = Label(win, text="Tenkh")
ent2 = ttk.Combobox(win, width=20)
ent2["value"] = ["Nguyen Chi Huan", "Tran Cao Trung", "Cao Van Giau"]
lab3 = Label(win, text="Ngay sinh")
#ent5 = Spinbox(win, from_=1, to=31, wrap=True, width=2)
ent5 = ttk.Combobox(win, width=15)# tao ra chonj lichj
#ent5.set_date(datetime.date.today())

# lab3 = Label(win, text="Ten KH")
# ent3 = ttk.Combobox(win, width=10)
# ent3["value"] = ["Admin", "Manager","Account"]
la3 = Label(win, text="Dia chi")
ent3 = Entry(win, width=15)
la4 = Label(win, text="Dien thoai")
ent4 = Entry(win, width=15)
# Tạo đối tượng DateEntry với ngày hiện tại
dateentry = DateEntry(canvas)
dateentry.pack()
# Thiết lập giá trị mặc định cho Combobox là ngày hiện tại
ent5.set(dateentry.get())
# lab4 = Label(win, text="Khach hang")
# ent4 = ttk.Combobox(win, width=10)
# ent4["value"] = ["Nguyen Chi Huan", "Tran Cao Trung", "Cao Van Giau"]
la5 = Checkbutton(win, text="Nam", onvalue=1, offvalue=0, variable=check)
la6 = Checkbutton(win, text="Nu", onvalue=1, offvalue=0, variable=check)
btn1 = Button(win, text="Luu", command=them)
btn2 = Button(win, text="Cap nhat", command=sua)
btn3 = Button(win, text="Xoa", command=xoa)
btn4 = Button(win, text="Huy", command=huy)
# btn5 = Button(win, text="Thoat")
la1.place(x=5)
# la2.place(x=300)

sho.place(x=300, y=20)
lab1.place(x=5, y=40)
ent1.place(x=80, y=40)
lab2.place(x=5, y=80)
ent2.place(x=80, y=80)
lab3.place(x =5, y=120)
ent5.place(x=80, y=120)
la5.place(x=5, y=160)
la6.place(x=50, y=160)
# lab3.place(x=5, y=60)
# ent3.place(x=80, y=60)
# lab4.place(x=5, y=80)
# ent4.place(x=80, y=80)
la3.place(x=5, y=200)
ent3.place(x= 80, y=200)
la4.place(x= 5, y=240)
ent4.place(x=80, y=240)
btn1.place(x=250, y=240)
btn2.place(x = 300, y=240)
btn3.place(x=370, y=240)
btn4.place(x=410, y=240)
# btn5.place(x=100, y=240)
win.mainloop()