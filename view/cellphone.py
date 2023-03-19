from tabnanny import check
from tkinter import *
from tkinter import ttk
from openpyxl import *
import pandas as pd
win = Tk()
win.geometry("600x400")
win.title("Profilecellphone")

def them():

    df1 = pd.read_excel('cellphone.xlsx')
    df2 = df1.drop(df1.filter(regex='Unnamed'), axis=1)
    hang = nhap1.get()
    ma = nhap2.get()
    ten = nhap3.get()
    soluong = chon.get()
    diachi = chon1.get()
    # data1 = {'Hãng DT':[hang], 'Mã điện thoại':[ma], 'Tên điện thoại':[ten], 'Màu sắc':["Đen"], 'Số Lượng':[soluong], 'Đơn giá':[diachi]}
    df = pd.DataFrame({'Hãng DT':[hang], 'Mã điện thoại':[ma], 'Tên điện thoại':[ten], 'Màu sắc':["Đen"], 'Số Lượng':[soluong], 'Đơn giá':[diachi]})
    df1.append(df)
    df1.to_excel('cellphone.xlsx', sheet_name="Sheet1", index=False)
    for  row in df1.iterrows():
        ds.insert(END, row)
def sua():
    global df
    df = pd.read_excel('cellphone.xlsx')
    hang = nhap1.get()
    ma = nhap2.get()
    ten = nhap3.get()
    soluong = chon.get()
    diachi = chon1.get()
    nhap1.delete(0, END)
    nhap1.insert(0, df.at[hang, 'Hãng DT'])
    nhap2.delete(0, END)
    nhap2.insert(0, df.at[ma, 'Mã điện thoại'])
    nhap3.delete(0, END)
    nhap3.insert(0, df.at[ten, 'Tên điện thoại'])
    chon.delete(0,END)
    chon.insert(0, df.at[soluong, 'Số lượng'])
    chon1.delete(0,END)
    chon1.insert(0, df.at[diachi, 'Đơn giá'])
    def save():
        global df
        df = pd.read_excel('cellphone.xlsx')
        df.at[ma, 'Mã điện thoại'] == ma
        # writer = pd.ExcelFile('cellphone.xlsx')
        df.to_excel('cellphone.xlsx', sheet_name='Sheet1', index=False)

    for index, row in df.iterrows():
        ds.insert(index, row)
def xoa():
    df = pd.read_excel('cellphone.xlsx')
    ma = nhap2.get()
    #df[df['Mã điện thoại']] != ma
    df.drop(df.filter(regex='Mã điện thoại'), axis=1)
    df.to_excel('cellphone.xlsx', index=False)
    for index, row in df.iterrows():
        ds.insert(index, row)
def huy():
    nhap1.delete(0, END)
    nhap2.delete(0, END)
    nhap3.delete(0, END)
    chon.delete(0, END)
    chon1.delete(0, END)
def thoat():
    win.destroy()
label1 = Label(win, text="Thôn tin điện thoại")
label1.place(x=5, y=5)
# label1.pack()
label2 = Label(win, text="Danh sách điện thoại")
label2.place(x=300, y=5)
label3 = Label(win, text="Hãng điện thoại")
# tao ra combobox
slecect = StringVar()
nhap1 = ttk.Combobox(win, textvariable=slecect, width=10)
nhap1['values'] = ["Oppo", "Samsung", "Iphone","Readmi", "Xiaomi","Nokia", "Lumia"]
nhap1["state"] = "readonly"
label3.place(x=5, y=30)
nhap1.place(x=100, y=30)
ds  = Listbox(win, width=60, height=20)
ds.place(x= 300, y=40)
label4= Label(win, text="Mã điện thoại")
label4.place(x=5, y=60)
nhap2 = Entry(win, width=10)
nhap2.place(x=100, y=70)
label5 = Label(win, text="Tên điện thoại")
label5.place(x=5, y=100)
nhap3 = Entry(win, width=10)
nhap3.place(x= 100, y = 100)
label6 = Label(win, text="Màu sắc")
label6.place(x= 5, y=120)
nut1 = Checkbutton(win, text="Trắng", onvalue=1, offvalue=0, variable=check)
nut1.place(x= 60, y=130)
nut2 = Checkbutton(win, text="Đen", onvalue=1, offvalue=0, variable=check)
nut2.place(x= 120, y=130)
label7 = Label(win, text="Số lượng")
label7.place(x= 5, y=160)
chon = Entry(win, width=10)
chon.place(x=100, y=160)
label8 = Label(win, text="Đơn giá")
label8.place(x=5, y=200)
chon1 = Entry(win, width=10)
chon1.place(x=100, y=200)
btn1 = Button(win, text="Thêm", activebackground="green", command=them)
btn1.place(x=15, y=240)
btn2 = Button(win, text="Xóa", activebackground="red", command=xoa)
btn2.place(x= 80, y=240)
btn3 = Button(win, text="Sửa",activebackground="yellow", command=sua)
btn3.place(x=160, y=240)
btn4 = Button(win, text="Cập nhật",activebackground="green", command=sua)
btn4.place(x=5, y=280)
btn5 = Button(win, text="Hủy",activebackground="yellow", command=huy)
btn5.place(x=80, y=280)
btn6 = Button(win, text="Thoát", activebackground="white")
btn6.place(x=160, y=280)
win.mainloop()