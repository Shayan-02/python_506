# import
from tkinter import *
from tkinter import messagebox


MAIN_FONT = ('Courier New', 20, 'bold')


def calc(op):
    try:
        num1 = int(num1_ent.get())
        num2 = int(num2_ent.get())
        if op == "+":
            messagebox.showinfo("result", f"{num1} {op} {num2} = {num1 + num2}")
        elif op == "-":
            messagebox.showinfo("result", f"{num1} {op} {num2} = {num1 - num2}")
        elif op == "*":
            messagebox.showinfo("result", f"{num1} {op} {num2} = {num1 * num2}")
        elif op == "/":
            messagebox.showinfo("result", f"{num1} {op} {num2} = {num1 / num2}")
        elif op == "x":
            messagebox.showinfo("x", num3)
    # except ZeroDivisionError:
    #     messagebox.showerror("error", "Cannot devide by zero!")
    # except ValueError:
    #     messagebox.showerror("error", "enter a number for num1 and num2")
    # except NameError:
    #     messagebox.showerror("error", "invalid variable")
    except Exception as e:
        messagebox.showerror("error", e)
    finally:
        messagebox.showinfo("finally", "finally executed")


root = Tk()
root.title("calculator")
root.geometry("450x350")
root.resizable(False, False)

num1_lbl = Label(root, text="num1", font=MAIN_FONT)
num1_lbl.grid(row=0, column=0, pady=10)

num1_ent = Entry(root, font=MAIN_FONT, width=15)
num1_ent.grid(row=0, column=1, pady=10)

num2_lbl = Label(root, text="num2", font=MAIN_FONT)
num2_lbl.grid(row=1, column=0)

num2_ent = Entry(root, font=MAIN_FONT, width=15)
num2_ent.grid(row=1, column=1)

add_btn = Button(root, text="+", font=MAIN_FONT, command=lambda:calc("+"))
add_btn.grid(row=2, column=0, pady=10)

sub_btn = Button(root, text="-", font=MAIN_FONT, command=lambda:calc("-"))
sub_btn.grid(row=2, column=1, pady=10)

mul_btn = Button(root, text="*", font=MAIN_FONT, command=lambda:calc("*"))
mul_btn.grid(row=3, column=0, pady=10)

div_btn = Button(root, text="/", font=MAIN_FONT, command=lambda:calc("/"))
div_btn.grid(row=3, column=1, pady=10)

div_btn = Button(root, text="x", font=MAIN_FONT, command=lambda: calc("x"))
div_btn.grid(row=4, column=1, pady=10)

root.mainloop()
