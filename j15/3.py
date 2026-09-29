from tkinter import *

bg_color = "#646464"
fg_color = "#eeeeee"

main_font = ("vazir", 18, "bold")
second_font = ("vazir", 14, "bold")

root = Tk()

root.title("fullname app")
root.geometry("450x450")
root.configure(background=bg_color)
root.resizable(0, 0)

fname_lbl = Label(root, text="نام", bg=bg_color, fg=fg_color, font=main_font).grid(row=0, column=0)
fname_ent = Entry(root, font=second_font, justify="center").grid(row=0, column=1, padx=20)

lname_lbl = Label(
    root, text="نام خانوادگی", bg=bg_color, fg=fg_color, font=main_font).grid(row=1, column=0)
lname_ent = Entry(root, font=second_font, justify="center").grid(row=1, column=1, padx=20)

fullname_btn = Button(root, text="نمایش نام", bg="lightgreen", font=main_font).grid(row=2, column=1, pady=30, padx=10)

root.mainloop()
