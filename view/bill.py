import calendar
from tkinter import *
from tkinter import ttk

import pandas as pd
win = Tk()
win.geometry("500x300")

# Them Widget
# date = ipysheet.date(days=['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'])
# ipysheet.cell(0,0,date)
def them():
    # data = pd.ExcelFile("bill.xlsx")
    df1 = pd.read_excel('bill.xlsx')
    df2 = df1.drop(df1.filter(regex='Unnamed'), axis=1)
    ma = ent1.get()
    ngay = ent2.get()
    nhanvien = ent3.get()
    khachang = ent4.get()

    # data1 = {'Hãng DT':[hang], 'Mã điện thoại':[ma], 'Tên điện thoại':[ten], 'Màu sắc':["Đen"], 'Số Lượng':[soluong], 'Đơn giá':[diachi]}
    df = pd.DataFrame({'Mã HD':[ma], 'Ngày lập HD':[ngay], 'Nhân viên':[nhanvien], 'Khách hàng':[khachang]})
    # writer = pd.ExcelWriter('bill.xlsx')
    df1.append(df)
    df1.to_excel('bill.xlsx', sheet_name="Sheet1", index=False)
    for  row in df1.iterrows():
        sho.insert(END, row)
def sua():
    global df
    df = pd.read_excel('bill.xlsx')
    ma = ent1.get()
    ngay = ent2.get()
    nhanvien = ent3.get()
    khachang = ent4.get()

    ent1.delete(0, END)
    ent1.insert(0, df.at[ma, 'Mã HD'])
    ent2.delete(0, END)
    ent2.insert(0, df.at[ngay, 'Ngày lập hóa đơn'])
    ent3.delete(0, END)
    ent3.insert(0, df.at[nhanvien, 'Nhân viên'])
    ent4.delete(0,END)
    ent4.insert(0, df.at[khachang, 'Khách hàng'])
    df.to_excel('bill.xlsx')
    def save():
        global df
        df = pd.read_excel('bill.xlsx')
        df.at[ma, 'Mã HD'] == ma
        # writer = pd.ExcelFile('bill.xlsx')
        df.to_excel('bill.xlsx', sheet_name='Sheet1', index=False)
        # writer.save()
    for index, row in df.iterrows():
        sho.insert(index, row)
def xoa():
    df = pd.read_excel('bill.xlsx')
    ma = ent1.get()
    df[df['Mã HD']] != ma
    df.drop(df.filter(regex='Mã hóa đơn'), axis=1)
    df.to_excel('bill.xlsx', index=False)
    for index, row in df.iterrows():
        sho.insert(index, row)
def huy():
    ent1.delete(0, END)
    ent2.delete(0, END)
    ent3.delete(0, END)
    ent4.delete(0, END)

def thoat():
    win.destroy()
la1 = Label(win, text="Thong tin hoa don")
la2 = Label(win, text="Danh sach hoa don")
fra = Frame(win, height=500, width=400, background="green")
sho = Listbox(fra, height=15, width=60)
lab1 = Label(win, text="Ma HD")
ent1 = Entry(win, width=15)
lab2 = Label(win, text="Ngay lap HD")
ent2 = ttk.Combobox(win,width=15)
ent2['value'] = calendar.month(2022,10)
print(calendar)

lab3 = Label(win, text="Nhan vien")
ent3 = ttk.Combobox(win, width=10)
ent3["value"] = ["Admin", "Manager","Account"]
lab4 = Label(win, text="Khach hang")
ent4 = ttk.Combobox(win, width=10)
ent4["value"] = ["Nguyen Chi Huan", "Tran Cao Trung", "Cao Van Giau"]
btn1 = Button(win, text="Lap hoa don", command=them)
btn2 = Button(win, text="Cap nhat", command=sua)
btn3 = Button(win, text="Chi tiet hoa don")
btn4 = Button(win, text="Xoa HD", command=xoa)
btn5 = Button(win, text="Thoat", command=thoat)
la1.place(x=5)
la2.place(x=300)
fra.place(x=280, y=20)
sho.place(x=5, y=20)
lab1.place(x=5, y=20)
ent1.place(x=80, y=20)
lab2.place(x=5, y=40)
ent2.place(x=80, y=40)
lab3.place(x=5, y=60)
ent3.place(x=80, y=60)
lab4.place(x=5, y=80)
ent4.place(x=80, y=80)
btn1.place(x=5, y=110)
btn2.place(x = 90, y=110)
btn3.place(x=160, y=110)
btn4.place(x=20, y=140)
btn5.place(x=100, y=140)
win.mainloop()