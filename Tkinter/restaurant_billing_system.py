from tkinter import *
import tkinter as tk
from time import strftime, localtime
from PIL import ImageTk, Image
from tkinter import messagebox


class restaurant_management():

    # ============== Total Bill Code =================

    def Total_Bill(self):
        self.crispy_chicken_caesar_price = 14.99
        self.greek_salad_price = 12.99
        self.truffle_fries_price = 9.99
        self.homemade_guacamole_price = 19.99
        self.ribs_burger_price = 24.99
        self.beef_quesadilla_price = 13.99
        self.spaghetti_bolognese_price = 15.99
        self.rib_eye_steak_price = 29.99

        if self.crispy_chicken_caesar_item.get() != "":
            self.crispy_chicken_caesar_cost = self.crispy_chicken_caesar_price * int(self.crispy_chicken_caesar_item.get())
        else:
            self.crispy_chicken_caesar_cost = 0
        if self.greek_salad_item.get() != "":
            self.greek_salad_cost = self.greek_salad_price * int(self.greek_salad_item.get())
        else:
            self.greek_salad_cost = 0
        if self.truffle_fries_item.get() != "":
            self.truffle_fries_cost = self.truffle_fries_price * int(self.truffle_fries_item.get())
        else:
            self.truffle_fries_cost = 0
        if self.homemade_guacamole_item.get() != "":
            self.homemade_guacamole_cost = self.homemade_guacamole_price * int(self.homemade_guacamole_item.get())
        else:
            self.homemade_guacamole_cost = 0
        if self.ribs_burger_item.get() != "":
            self.ribs_burger_cost = self.ribs_burger_price * int(self.ribs_burger_item.get())
        else:
            self.ribs_burger_cost = 0
        if self.beef_quesadilla_item.get() != "":
            self.beef_quesadilla_cost = self.beef_quesadilla_price * int(self.beef_quesadilla_item.get())
        else:
            self.beef_quesadilla_cost = 0
        if self.spaghetti_bolognese_item.get() != "":
            self.spaghetti_bolognese_cost = self.spaghetti_bolognese_price * int(self.spaghetti_bolognese_item.get())
        else:
            self.spaghetti_bolognese_cost = 0
        if self.rib_eye_steak_item.get() != "":
            self.rib_eye_steak_cost = self.rib_eye_steak_price * int(self.rib_eye_steak_item.get())
        else:
            self.rib_eye_steak_cost = 0

        self.Total_Bill = self.rib_eye_steak_cost + self.spaghetti_bolognese_cost + self.beef_quesadilla_cost + self.ribs_burger_cost + self.homemade_guacamole_cost + self.truffle_fries_cost + self.greek_salad_cost + self.crispy_chicken_caesar_cost

        if self.items_cost != "":
            self.items_cost.delete(0, END)
            self.items_cost.insert(END, f'{self.Total_Bill:.2f}')
        else:
            self.items_cost.insert(END, f'{self.Total_Bill:.2f}')
        if self.service_cost != "":
            self.service_cost.delete(0, END)
            self.service_cost.insert(END, f'{self.Total_Bill * 0.10:.2f}')
        else:
            self.service_cost.insert(END, f'{self.Total_Bill * 0.10:.2f}')
        if self.sub_cost != "":
            self.sub_cost.delete(0, END)
            self.sub_cost.insert(END, f'{float(self.items_cost.get()) + float(self.service_cost.get()):.2f}')
        else:
            self.sub_cost.insert(END, f'{float(self.items_cost.get()) + float(self.service_cost.get()):.2f}')
        if self.paid_tax != "":
            self.paid_tax.delete(0, END)
            self.paid_tax.insert(END, f'{float(float(self.sub_cost.get()) * 8 / 100):.2f}')
        else:
            self.paid_tax.insert(END, f'{float(float(self.sub_cost.get()) * 8 / 100):.2f}')

        if self.total_bill != "":
            self.total_bill.delete(0, END)
            self.total_bill.insert(END, f'{float(float(self.sub_cost.get()) + float(self.paid_tax.get())):.2f}')
        else:
            self.total_bill.insert(END, f'{float(float(self.sub_cost.get()) + float(self.paid_tax.get())):.2f}')



        # ===== Calculator code ================

    def nine(self):
        if 'error' in self.result.get() or '=' in self.result.get():
            self.result.delete(0, "end")
            self.result.insert("end", "9")
        else:
            self.result.insert("end", "9")
    def eight(self):
        if 'error' in self.result.get() or '=' in self.result.get():
            self.result.delete(0, "end")
            self.result.insert("end", "8")
        else:
            self.result.insert("end", "8")
    def seven(self):
        if 'error' in self.result.get() or '=' in self.result.get():
            self.result.delete(0, "end")
            self.result.insert("end", "7")
        else:
            self.result.insert("end", "7")
    def six(self):
        if 'error' in self.result.get() or '=' in self.result.get():
            self.result.delete(0, "end")
            self.result.insert("end", "6")
        else:
            self.result.insert("end", "6")
    def five(self):
        if 'error' in self.result.get() or '=' in self.result.get():
            self.result.delete(0, "end")
            self.result.insert("end", "5")
        else:
            self.result.insert("end", "5")
    def four(self):
        if 'error' in self.result.get() or '=' in self.result.get():
            self.result.delete(0, "end")
            self.result.insert("end", "4")
        else:
            self.result.insert("end", "4")
    def three(self):
        if 'error' in self.result.get() or '=' in self.result.get():
            self.result.delete(0, "end")
            self.result.insert("end", "3")
        else:
            self.result.insert("end", "3")
    def two(self):
        if 'error' in self.result.get() or '=' in self.result.get():
            self.result.delete(0, "end")
            self.result.insert("end", "2")
        else:
            self.result.insert("end", "2")
    def one(self):
        if 'error' in self.result.get() or '=' in self.result.get():
            self.result.delete(0, "end")
            self.result.insert("end", "1")
        else:
            self.result.insert("end", "1")
    def zero(self):
        if 'error' in self.result.get() or '=' in self.result.get():
            self.result.delete(0, "end")
            self.result.insert("end", "0")
        else:
            self.result.insert("end", "0")
    def plus(self):
        if 'error' in self.result.get() or '=' in self.result.get():
            self.result.delete(0, "end")
            self.result.insert("end", "+")
        else:
            self.result.insert("end", "+")
    def minus(self):
        if 'error' in self.result.get() or '=' in self.result.get():
            self.result.delete(0, "end")
            self.result.insert("end", "-")
        else:
            self.result.insert("end", "-")
    def mul(self):
        if 'error' in self.result.get() or '=' in self.result.get():
            self.result.delete(0, "end")
            self.result.insert("end", "*")
        else:
            self.result.insert("end", "*")
    def divide(self):
        if 'error' in self.result.get() or '=' in self.result.get():
            self.result.delete(0, "end")
            self.result.insert("end", "/")
        else:
            self.result.insert("end", "/")
    def equal(self):
        if self.result.get() == "":
            self.result.insert("end", "error")
        elif self.result.get()[0] == "0" or self.result.get()[0] == "+" or self.result.get()[0] == "*" or \
                self.result.get()[0] == "/":
            self.result.delete(0, "end")
            self.result.insert("end", "error")
        elif 'error' in self.result.get() or '=' in self.result.get():
            self.result.delete(0, "end")
        else:
            self.res = self.result.get()
            self.res = eval(self.res)
            self.result.insert("end", " = ")
            self.result.insert("end", self.res)


     #================ Clear Fields ===============

    def clear(self):
        self.result.delete(0, "end")
    def Clear(self):
        self.crispy_chicken_caesar_item.delete(0, "end")
        self.greek_salad_item.delete(0, "end")
        self.truffle_fries_item.delete(0, "end")
        self.ribs_burger_item.delete(0, "end")
        self.homemade_guacamole_item.delete(0, "end")
        self.spaghetti_bolognese_item.delete(0, "end")
        self.beef_quesadilla_item.delete(0, "end")
        self.rib_eye_steak_item.delete(0, "end")
        self.items_cost.delete(0, "end")
        self.service_cost.delete(0, "end")
        self.sub_cost.delete(0, "end")
        self.paid_tax.delete(0, "end")
        self.total_bill.delete(0, "end")

    # ==== Exit button code =================

    def Quit(self):
        self.message = messagebox.askquestion('Exit', "Do you want to exit the application")
        if self.message == "yes":
            self.root.destroy()
        else:
            "return"

    # ========== end ========================

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('500x300')
        self.root.title("Restaurant Billing System")
        self.root.attributes('-fullscreen',True)
        self.root['bg'] = "#2f2f2f"

        self.heading = Label(self.root, text="Restaurant Billing System", font=('ribbon-condensed', 25, 'bold'), fg="#FF8F00",
                             bg="#2f2f2f")
        self.heading.place(x=520, y=5)

        self.style1 = Label(self.root, bg="#000000", height=1, width=73)
        self.style1.place(x=0, y=50)
        self.style2 = Label(self.root, bg="#000000", height=1, width=95)
        self.style2.place(x=930, y=50)
        self.date = Label(self.root, text=strftime("%Y-%m-%d %H:%M:%S", localtime()), font=('ribbon-condensed', 15, 'bold'),
                          bg="#2f2f2f", fg="white")
        self.date.place(x=630, y=50)

        self.restaurant_icon = ImageTk.PhotoImage(Image.open('dish.png'))
        self.logo = Label(self.root, image=self.restaurant_icon, bg="#2f2f2f")
        self.logo.place(x=550, y=50)

        self.restaurant_icon2 = ImageTk.PhotoImage(Image.open('dish.png'))
        self.logo = Label(self.root, image=self.restaurant_icon2, bg="#2f2f2f")
        self.logo.place(x=850, y=50)

        self.image_of_restaurant = ImageTk.PhotoImage(Image.open('restaurant.jpg'))
        self.logo = Label(self.root, image=self.image_of_restaurant, bg="#2f2f2f")
        self.logo.place(x=932, y=69)

        # ================== Items ===================

        self.frame1 = LabelFrame(self.root, text="Menu", width=400, height=300, font=('orange', 20, 'bold'),
                                 borderwidth=5, relief=RIDGE, highlightthickness=4, bg="black", highlightcolor="#2f2f2f",
                                 highlightbackground="#2f2f2f", fg="#FF8F00")
        self.frame1.place(x=10, y=90)

        self.crispy_chicken_caesar = Label(self.frame1, text="Crispy Chicken Caesar", font=('verdana', 12, 'bold'), bg="black", fg="white")
        self.crispy_chicken_caesar.place(x=20, y=1)
        self.crispy_chicken_caesar_item = Entry(self.frame1, width=18, borderwidth=4, relief=SUNKEN, bg="#FF8F00")
        self.crispy_chicken_caesar_item.place(y=1, x=240)

        self.greek_salad = Label(self.frame1, text="Greek Salad", font=('verdana', 12, 'bold'), bg="black", fg="white")
        self.greek_salad.place(x=20, y=30)
        self.greek_salad_item = Entry(self.frame1, width=18, borderwidth=4, relief=SUNKEN, bg="#FF8F00")
        self.greek_salad_item.place(y=30, x=240)

        self.truffle_fries = Label(self.frame1, text="Truffle Fries", font=('verdana', 12, 'bold'), bg="black", fg="white")
        self.truffle_fries.place(x=20, y=59)
        self.truffle_fries_item = Entry(self.frame1, width=18, borderwidth=4, relief=SUNKEN, bg="#FF8F00")
        self.truffle_fries_item.place(y=59, x=240)

        self.homemade_guacamole = Label(self.frame1, text="Homemade Guacamole", font=('verdana', 12, 'bold'), bg="black", fg="white")
        self.homemade_guacamole.place(x=20, y=88)
        self.homemade_guacamole_item = Entry(self.frame1, width=18, borderwidth=4, relief=SUNKEN, bg="#FF8F00")
        self.homemade_guacamole_item.place(y=88, x=240)

        self.ribs_burger = Label(self.frame1, text="Ribs Burger", font=('verdana', 12, 'bold'), bg="black", fg="white")
        self.ribs_burger.place(x=20, y=117)
        self.ribs_burger_item = Entry(self.frame1, width=18, borderwidth=4, relief=SUNKEN, bg="#FF8F00")
        self.ribs_burger_item.place(y=117, x=240)

        self.beef_quesadilla = Label(self.frame1, text="Pizza", font=('verdana', 12, 'bold'), bg="black", fg="white")
        self.beef_quesadilla.place(x=20, y=146)
        self.beef_quesadilla_item = Entry(self.frame1, width=18, borderwidth=4, relief=SUNKEN, bg="#FF8F00")
        self.beef_quesadilla_item.place(y=146, x=240)

        self.spaghetti_bolognese = Label(self.frame1, text="Spaghetti Bolognese", font=('verdana', 12, 'bold'), bg="black", fg="white")
        self.spaghetti_bolognese.place(x=20, y=175)
        self.spaghetti_bolognese_item = Entry(self.frame1, width=18, borderwidth=4, relief=SUNKEN, bg="#FF8F00")
        self.spaghetti_bolognese_item.place(y=175, x=240)

        self.rib_eye_steak = Label(self.frame1, text="Rib Eye Steak", font=('verdana', 12, 'bold'), bg="black", fg="white")
        self.rib_eye_steak.place(x=20, y=204)
        self.rib_eye_steak_item = Entry(self.frame1, width=18, borderwidth=4, relief=SUNKEN, bg="#FF8F00")
        self.rib_eye_steak_item.place(y=204, x=240)


        # ============ Items Bill =================

        self.frame2 = LabelFrame(self.root, text="Total Bill", width=355, height=200,
                                 font=('orange', 20, 'bold'), borderwidth=3, relief=RIDGE, highlightthickness=4,
                                 bg="black", highlightcolor="black", highlightbackground="#2f2f2f", fg="#FF8F00")
        self.frame2.place(x=550, y=150)

        self.item_cost_lb = Label(self.frame2, text="Items Cost", font=('verdana', 14, 'bold'), bg="black", fg="white")
        self.item_cost_lb.place(x=20, y=1)
        self.items_cost = Entry(self.frame2, width=18, borderwidth=4, relief=SUNKEN, bg="#FF8F00")
        self.items_cost.place(y=2, x=180)

        self.service_cost_lb = Label(self.frame2, text="Service Cost", font=('verdana', 14, 'bold'), bg="black", fg="white")
        self.service_cost_lb.place(x=20, y=31)
        self.service_cost = Entry(self.frame2, width=18, borderwidth=4, relief=SUNKEN, bg="#FF8F00")
        self.service_cost.place(y=31, x=180)

        self.sub_cost_lb = Label(self.frame2, text="Sub Cost", font=('verdana', 14, 'bold'), bg="black", fg="white")
        self.sub_cost_lb.place(x=20, y=60)
        self.sub_cost = Entry(self.frame2, width=18, borderwidth=4, relief=SUNKEN, bg="#FF8F00")
        self.sub_cost.place(y=60, x=180)

        self.paid_tax_lb = Label(self.frame2, text="Paid Tax", font=('verdana', 14, 'bold'), bg="black", fg="white")
        self.paid_tax_lb.place(x=20, y=89)
        self.paid_tax = Entry(self.frame2, width=18, borderwidth=4, relief=SUNKEN, bg="#FF8F00")
        self.paid_tax.place(y=89, x=180)

        self.total_bill_lb = Label(self.frame2, text="Total Bill", font=('verdana', 14, 'bold'), bg="black", fg="white")
        self.total_bill_lb.place(x=20, y=118)
        self.total_bill = Entry(self.frame2, width=18, borderwidth=4, relief=SUNKEN, bg="#FF8F00")
        self.total_bill.place(y=118, x=180)


        # ================== Calculator ============

        self.frame3 = LabelFrame(self.root, text="Calculator", font=('verdana', 20, 'bold'), fg="#FF8F00",
                                 bg="black",
                                 highlightbackground="#2f2f2f", width=190, height=272, borderwidth=3, relief=RIDGE)
        self.frame3.place(x=630, y=392)
        self.result = Entry(self.frame3, width=29, relief=SUNKEN, borderwidth=3)
        self.result.place(x=2, y=20)
        self.nine = Button(self.frame3, text="9", padx=6, relief=RAISED, borderwidth=2,
                           font=('verdana', 15, 'bold'),
                           bg='#FF8F00', fg="white", command=self.nine)
        self.nine.place(x=0, y=60)
        self.eight = Button(self.frame3, text="8", padx=6, relief=RAISED, borderwidth=2,
                            font=('verdana', 15, 'bold'),
                            bg='#FF8F00', fg="white", command=self.eight)
        self.eight.place(x=45, y=60)
        self.seven = Button(self.frame3, text="7", padx=6, relief=RAISED, borderwidth=2,
                            font=('verdana', 15, 'bold'),
                            bg='#FF8F00', fg="white", command=self.seven)
        self.seven.place(x=90, y=60)
        self.plus = Button(self.frame3, text="+", padx=6, relief=RAISED, borderwidth=2,
                           font=('verdana', 15, 'bold'),
                           bg='white', fg="black", command=self.plus)
        self.plus.place(x=135, y=60)
        self.six = Button(self.frame3, text="6", padx=6, relief=RAISED, borderwidth=2, font=('verdana', 15, 'bold'),
                          bg='#FF8F00', fg="white", command=self.six)
        self.six.place(x=0, y=104)
        self.five = Button(self.frame3, text="5", padx=6, relief=RAISED, borderwidth=2,
                           font=('verdana', 15, 'bold'),
                           bg='#FF8F00', fg="white", command=self.five)
        self.five.place(x=45, y=104)
        self.four = Button(self.frame3, text="4", padx=6, relief=RAISED, borderwidth=2,
                           font=('verdana', 15, 'bold'),
                           bg='#FF8F00', fg="white", command=self.four)
        self.four.place(x=90, y=104)
        self.minus = Button(self.frame3, text="-", padx=8, relief=RAISED, borderwidth=2,
                            font=('verdana', 15, 'bold'),
                            bg='white', fg="black", command=self.minus)
        self.minus.place(x=136, y=104)
        self.three = Button(self.frame3, text="3", padx=6, relief=RAISED, borderwidth=2,
                            font=('verdana', 15, 'bold'),
                            bg='#FF8F00', fg="white", command=self.three)
        self.three.place(x=0, y=148)
        self.two = Button(self.frame3, text="2", padx=6, relief=RAISED, borderwidth=2, font=('verdana', 15, 'bold'),
                          bg='#FF8F00', fg="white", command=self.two)
        self.two.place(x=45, y=148)
        self.one = Button(self.frame3, text="1", padx=6, relief=RAISED, borderwidth=2, font=('verdana', 15, 'bold'),
                          bg='#FF8F00', fg="white", command=self.one)
        self.one.place(x=91, y=148)
        self.multiply = Button(self.frame3, text="*", padx=7, relief=RAISED, borderwidth=2,
                               font=('verdana', 15, 'bold'), bg='white', fg="black", command=self.mul)
        self.multiply.place(x=137, y=148)
        self.zero = Button(self.frame3, text="0", padx=6, relief=RAISED, borderwidth=2,
                           font=('verdana', 15, 'bold'),
                           bg='#FF8F00', fg="white", command=self.zero)
        self.zero.place(x=0, y=192)
        self.clear = Button(self.frame3, text="C", padx=6, relief=RAISED, borderwidth=2,
                            font=('verdana', 15, 'bold'),
                            bg='#FF8F00', fg="white", command=self.clear)
        self.clear.place(x=45, y=192)
        self.equal = Button(self.frame3, text="=", padx=6, relief=RAISED, borderwidth=2,
                            font=('verdana', 15, 'bold'),
                            bg='#FF8F00', fg="white", command=self.equal)
        self.equal.place(x=90, y=192)
        self.divide = Button(self.frame3, text="/", padx=7, relief=RAISED, borderwidth=2,
                             font=('verdana', 15, 'bold'),
                             bg='white', fg="black", command=self.divide)
        self.divide.place(x=138, y=192)
        self.Total_Bills_btn = Button(self.root, text="Total", relief=RAISED, borderwidth=2,
                                      font=('verdana', 38, 'bold'), bg='#000000', fg="white",
                                      command=self.Total_Bill)
        self.Total_Bills_btn.place(x=15, y=385)
        self.Clear_btn = Button(self.root, text="Clear", relief=RAISED, borderwidth=2, font=('verdana', 38, 'bold'),
                                bg='#000000', fg="white", command=self.Clear)
        self.Clear_btn.place(x=205, y=385)
        self.icon = ImageTk.PhotoImage(Image.open('exit.png'))
        self.Quit_btn = Button(self.root, image=self.icon, relief=RAISED, borderwidth=2,
                               font=('verdana', 5, 'bold'),
                               bg='#000000', fg="white", padx=0, command=self.Quit)
        self.Quit_btn.place(x=92, y=492)
        self.root.mainloop()


if __name__ == '__main__':
    restaurant_management()