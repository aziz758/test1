import tkinter as tk
from tkinter import messagebox
import main
from DBHelper import dbop

root = tk.Tk()
root.title("تسجيل الدخول")
root.geometry("400x300")
root.configure(bg="#f0f0f0")
db = dbop()
def login():
    name = entry_user.get()
    passs = entry_pass.get()

    if db.check_user(name, passs):
        messagebox.showinfo("تاكيد","تم تسجيل الدخول بنجاح")
        root.destroy()
        main.open_main()
    else:
        messagebox.showerror("خطا", "لم يتم تسجيل الدخول")
#ادخل مستخدم
# db.inse_user()
lbl_title = tk.Label(root, text="تسجيل دخول", font=("Arial", 18, "bold"), bg="#f0f0f0")
lbl_title.place(x=120, y=30)

lbl_user = tk.Label(root, text="اسم المستخدم", font=("Arial", 12), bg="#f0f0f0")
lbl_user.place(x=50, y=100)
entry_user = tk.Entry(root, font=("Arial", 12))
entry_user.place(x=180, y=100, width=150)

lbl_pass = tk.Label(root, text="كلمة المرور", font=("Arial", 12), bg="#f0f0f0")
lbl_pass.place(x=50, y=150)
entry_pass = tk.Entry(root, font=("Arial", 12))
entry_pass.place(x=180, y=150, width=150)

btn_login = tk.Button(root, command=login, text="دخول", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white")
btn_login.place(x=160, y=210, width=80, height=30)

root.mainloop()