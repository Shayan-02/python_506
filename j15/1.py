from tkinter import *

bg_color = "#646464"
fg_color = "#eeeeee"

main_font = ("vazir", 18, "bold")
second_font = ("vazir", 14, "bold")

root = Tk()

root.title("fullname app")
root.geometry("400x450")
root.configure(background=bg_color)
root.resizable(0, 0)

fname_lbl = Label(root, text="نام", bg=bg_color, fg=fg_color, font=main_font).pack(pady=10)
fname_ent = Entry(root, font=second_font, justify="center").pack()

lname_lbl = Label(root, text="نام خانوادگی", bg=bg_color, fg=fg_color, font=main_font).pack(pady=10)
lname_ent = Entry(root, font=second_font, justify="center").pack()

fullname_btn = Button(root, text="نمایش نام", bg="lightgreen", font=main_font).pack(pady=20)

root.mainloop()