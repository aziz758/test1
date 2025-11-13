from tkinter import *
from tkinter import ttk, messagebox
from DBHelper import dbop


def open_main():
    root = Tk()
    root.title('التحكم بادارة النظام')
    root.geometry('1280x650+50+30')
    root.resizable(False, False)
    root.configure(bg='#2c3e50')

    db = dbop

    # المتغيرات
    dowra_name = StringVar()
    dowra_id = StringVar()
    dowra_prais = StringVar()

    #جلب البيانات من قاعده الادارات
    dowra = []
    try:
        for dow in db.fetch_dawra():
            dowra.append(dow[1])  #يفترض ان العمود الثاني هو اسم الادارة
    except:
        dowra = []

        #اطار الادخال
    entries_frame = Frame(root, bg='#2c3e50')
    entries_frame.place(x=0, y=0, width=360, height=650)

    Label(entries_frame, text='بيانات الدوراة', font=('Calibri', 20, 'bold'),
          bg='#2c3e50', fg='white').place(x=90, y=10)

    fields = [
        ("اسم الدورة", dowra_name),
        ("رقم الدورة", dowra_id),
        ("سعر الدورة", dowra_prais),
    ]

    y_pos = 70
    for label_text, var in fields:
        Label(entries_frame, text=label_text, font=('Calibri', 14), bg='#2c3e50',
              fg='white').place(x=10, y=y_pos)
        Entry(entries_frame, textvariable=var, width=22, font=('Calibri',
                                                               14)).place(x=140, y=y_pos)
        y_pos += 45

    # Label(entries_frame, text='الجنس', font=('Calibri', 14), bg='#2c3e50',
    #       fg='white').place(x=10, y=y_pos)
    # comboGender = ttk.Combobox(entries_frame, state='readonly', textvariable=gender,
    #                            width=20, font=('Calibri', 14), values=genders)
    # comboGender.place(x=140, y=y_pos)
    # y_pos += 45

    Label(entries_frame, text='الاداره', font=('Calibri', 14), bg='#2c3e50',
          fg='white').place(x=10, y=y_pos)
    # comboDept = ttk.Combobox(entries_frame, state='readonly', textvariable=dept_id,
    #                          width=20, font=('Calibri', 14), values=dowra)
    # comboDept.place(x=140, y=y_pos)
    y_pos += 55

    def clear():
        for var in (dowra_prais, dowra_name, dowra_id):
            var.set("")

    def AllData():
        tv.delete(*tv.get_children())
        for row in db.fetch_dawra()
            tv.insert("", END, values=row)

    def add_data():
        print("")

    def AllData():
        print("")

    def add_data():
        print("")

    def update_data():
        print("")

    def delete_data():
        print("")

    def getData(event):
        print("")

        # ازرار

    btn_frame = Frame(entries_frame, bg='#2c3e50')
    btn_frame.place(x=15, y=y_pos, width=320, height=130)

    buttons = [
        ("اضافه", add_data, '#16a085'),
        ("تحديث", update_data, '#2980b9'),
        ("حذف", delete_data, '#c0392b'),
        ("مسح", clear, '#f39c12')
    ]

    for i, (text, cmd, color) in enumerate(buttons):
        Button(btn_frame, text=text, command=cmd, width=13, font=('Calibri', 14),
               fg='white', bg=color, bd=0).grid(row=i // 2, column=i % 2, padx=5, pady=5)

        # الجداول
    tree_frame = Frame(root, bg='white')
    tree_frame.place(x=370, y=10, width=890, height=630)

    style = ttk.Style()
    style.configure("mystyle.Treeview", font=('Calibri', 12), rowheight=35)
    style.configure("mystyle.Treeview.Heading", font=('Calibri', 13, 'bold'))

    tv = ttk.Treeview(tree_frame, columns=(1, 2, 3),
                      style="mystyle.Treeview")
    headings = ["اسم الدوره", "رقم الدوره", "سعر الدوره"]
    for i, h in enumerate(headings, start=1):
        tv.heading(i, text=h)
        tv.column(i, anchor=CENTER, width=100)

    tv.bind("<ButtonRelease-1>", getData)
    tv['show'] = 'headings'
    tv.pack(fill=BOTH, expand=True)

    AllData()
    root.mainloop()


if __name__ == "__main__":
    open_main()


