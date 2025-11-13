import tkinter as tk
from tkinter import ttk, messagebox
import user
import dawra



def open_main():
    root = tk.Tk()
    root.title("الرئيسية")
    root.geometry("400x400")
    root.resizable(False, False)

    title = tk.Label(root, text="النظام", font=("Arial", 20, "bold"), bg="#004080", fg="white", pady=15)
    title.pack(fill=tk.X)

    frame = tk.Frame(root, bg="#f0f0f0", padx=20, pady=30)
    frame.pack(expand=True, fill="both")

    lbl = tk.Label(frame, text="الاقسام", font=("Arial", 14),bg="#f0f0f0")
    lbl.pack(pady=20)

    def open_dawra():
        messagebox.showinfo("قسم الدورات")
        root.destroy()
        #هنا اسم الواجهه

    def open_mutadrib():
        messagebox.showinfo("قسم المتدربين")
        root.destroy()
        #اسم الواجهه

    def open_users():
        messagebox.showinfo("قسم المستخدمين")
        root.destroy()
        #اسم الواجهه

    btn_dawra = tk.Button(frame, command=open_dawra, text="الدورات", font=("Arial", 12, "bold"), width=25)
    btn_dawra.pack(pady=10)

    btn_users = tk.Button(frame, command=open_dawra, text="المستخدمين", font=("Arial", 12, "bold"), width=25)
    btn_users.pack(pady=10)

    btn_mutadrib = tk.Button(frame, command=open_mutadrib, text="المتدربين", font=("Arial", 12, "bold"), width=25)
    btn_mutadrib.pack(pady=10)

    btn_exit = tk.Button(frame, command=root.quit, text="خروج", font=("Arial", 12, "bold"), width=25)
    btn_exit.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    open_main()