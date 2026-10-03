from tkinter import *
from tkinter import messagebox, filedialog
from random import choice


def add_to_file():
    user = user_ent.get() + "\n"
    with open("users.txt", "a", encoding="utf-8") as f:
        f.write(user)
        messagebox.showinfo("وضعیت ثبت", f"{user} با موفقیت اضافه شد")

    with open("users.txt", encoding="utf-8") as f:
        messagebox.showinfo("تعداد اعضا", f"تعداد اعضا حال حاضر {len(f.readlines())}")


def latari():
    with open("users.txt", encoding="utf-8") as f:
        users  = f.readlines()
        winner = choice(users)
        messagebox.showinfo("برنده", f"برنده {winner} شد")

bg_color = "#2D497E"
fg_color = "#F1F6FF"

main_font = ("vazir", 18, "bold")
second_font = ("vazir", 14, "bold")

root = Tk()

root.title("latari")
root.geometry("400x400")
root.resizable(False, False)
root.configure(bg=bg_color)

user_lbl = Label(root, text="نام شرکت کنندگان را وارد کنید", bg=bg_color, fg=fg_color, font=main_font).pack(pady=10)
user_ent = Entry(root, font=second_font, justify="center")
user_ent.pack()

user_add_btn = Button(root, text="اضافه کردن به لیست", fg=fg_color, bg="lightgreen", font=main_font, command=lambda : add_to_file())
user_add_btn.pack(pady=20)

latari_btn = Button(root, text="قرعه کشی", fg=fg_color, bg="lightgreen", font=main_font, command=lambda : latari() )
latari_btn.pack()

root.mainloop()