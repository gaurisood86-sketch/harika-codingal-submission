from tkinter import tk
from tkinter import ttk,messagebox

class RestaurantOrderManagement:
    def __init__(self,root):
        self.root=root
        self.root.title('Restaurant management app')

        self.menuItems={
            'FRIES MEAL':2,
            'BURGER MEAL':3,
            'PIZZA MEAL':2.5,
            'SIDE DISHES':1.5,
            'DRINKS':2
        }

        self.exchange_rate=96
        self.setup_background(root)

        frame=ttk.Frame(root)
        frame.place(relx=0.5,rely=0.5,anchor=tk.CENTER)

        ttk.Label(
            frame,
            text="restaurant management app",
            font=('arial',20,'bold')
        ).grid(row=0,columnspan=3,padx=10,pady=10)

        self.menu_labels={}
        self.menu_quantities={}

        for i,(item,price) in enumerate(self.menuItems.items,start=1):
            label=ttk.Label(
                frame,
                text=f"{item}(${price})":
                font=("arial",12)
            )
            label.grid(row=i,column=0,padx=10,pady=5)

            self.menu_labels[item]=label

            quantity_entry=ttk.Entry(frame,width=5)
            quantity_entry.grid(row=i,column=1,padx=10,pady=5)
            self.menu_quantities[item]=quantity_entry

        self.currency_var=tk.StringVar()
        ttk.label(
            frame,
            text="currency!",
            font=("arial",12)
        ).grid(
            row=len(self.menuItems)+1,
            column=0,
            padx=10,
            pady=5
        )

        






