from tkinter import *
import random
import os
from tkinter.messagebox import showerror,showinfo
from tkinter import messagebox

class BillManagement():
    def __init__(self,root):
        self.root=root
        font = ('Helvetica', 25, 'bold')
        font_text= ('Andale Mono', 14, 'bold')
        font_supTitle= ('Times', 12, 'bold')
        root.geometry("1400x700")
        root.title("Bill Management System By Akshay")
        TitleLabel=Label(self.root,text="Bill Management System",font=font,fg="FireBrick",bd=12,bg="DarkSlateGray")
        TitleLabel.pack(side=TOP,fill=X)

        # REQUIRED VARIABLES
        self.Name=StringVar()
        self.Number=StringVar()
        self.Bill=StringVar()

        # COSMETICS VARIABLES
        self.HairgelPrice=IntVar()
        self.FacecreamPrice=IntVar()
        self.FacepowderPrice=IntVar()
        self.BodyloshanPrice=IntVar()
        self.HairshampooPrice=IntVar()
        self.ShavingcreamPrice=IntVar()
        self.TotalCosmeticPrice=IntVar()
        self.TotalCosmeticTax=IntVar()

        # GROCERY VARIABLES
        self.WheatPrice=IntVar()
        self.RicePrice=IntVar()
        self.DaalPrice=IntVar()
        self.FoodoilPrice=IntVar()
        self.SpicesPrice=IntVar()
        self.TeaPrice=IntVar()
        self.TotalGroceryPrice = IntVar()
        self.TotalGroceryTax = IntVar()

        # SNACKS VARIABLES
        self.ChipsPrice=IntVar()
        self.ColddrinkPrice=IntVar()
        self.ChoclatePrice=IntVar()
        self.BiscuitsPrice=IntVar()
        self.IcecreamPrice=IntVar()
        self.CupcakesPrice=IntVar()
        self.TotalSnacksPrice = IntVar()
        self.TotalSnacksTax = IntVar()

        CustDetFrame=LabelFrame(self.root,text="Customer Details",bd=5,fg="Yellow",relief=GROOVE,bg="Teal",font=font_supTitle)
        CustDetFrame.place(x=5,y=70,width=1400)
        NameLabel=Label(CustDetFrame,text="Customer Name:",font=font_text,bg="Teal")
        NameLabel.grid(row=0,column=0,pady=1,sticky='w')
        NameEntry=Entry(CustDetFrame,font=font_text,bg="FloralWhite",textvariable=self.Name,bd=2,relief=GROOVE,width=16)
        NameEntry.grid(row=0,column=1,padx=4)

        PhoneLabel = Label(CustDetFrame, text="Phone Number:", font=font_text,bg="Teal")
        PhoneLabel.grid(row=0, column=2, pady=1, sticky='w',padx=6)
        PhoneEntry = Entry(CustDetFrame, font=font_text, bg="FloralWhite",textvariable=self.Number,bd=2,relief=GROOVE,width=16)
        PhoneEntry.grid(row=0, column=3, padx=6)

        BillLabel = Label(CustDetFrame, text="Bill Number:", font=font_text,bg="Teal")
        BillLabel.grid(row=0, column=4, pady=1, sticky='w',padx=6)
        BillEntry = Entry(CustDetFrame, font=font_text,width=16,textvariable=self.Bill, bg="FloralWhite",bd=2,relief=GROOVE)
        BillEntry.grid(row=0, column=5,padx=6)

        SearchButton=Button(CustDetFrame,text="Search",font=font_text,bg="cyan",relief=GROOVE,width=15,bd=6,command=self.find_bill)
        SearchButton.grid(row=0,column=6,padx=8)

        # ITEMS FRAME INCLUDING GROCERY COSMETICS AND DRINKS

        # COSMETICS
        CosmeticsFrame=LabelFrame(self.root,text="Cosmetics",fg="Yellow",relief=GROOVE,font=font_supTitle,bg="Teal")
        CosmeticsFrame.place(x=5,y=150,width=325,height=380)

        HairGel=Label(CosmeticsFrame,text="Hair Gel",font=font_text,bg="Teal",fg="Maroon")
        HairGel.grid(row=0,column=0)
        HairGElEntry=Entry(CosmeticsFrame,font=font_text,textvariable=self.HairgelPrice,bg="FloralWhite",bd=2,relief=GROOVE,width=12)
        HairGElEntry.grid(row=0,column=1,pady=14,padx=1)

        FaceCream = Label(CosmeticsFrame, text="Face Cream", font=font_text,bg="Teal",fg="Maroon")
        FaceCream.grid(row=1, column=0)
        FaceCreamEntry = Entry(CosmeticsFrame, font=font_text,textvariable=self.FacecreamPrice, bg="FloralWhite", bd=2, relief=GROOVE, width=12)
        FaceCreamEntry.grid(row=1, column=1, pady=14, padx=4)

        Powder = Label(CosmeticsFrame, text="Face Powder", font=font_text,bg="Teal",fg="Maroon")
        Powder.grid(row=2, column=0)
        PowderEntry = Entry(CosmeticsFrame, font=font_text,textvariable=self.FacepowderPrice, bg="FloralWhite", bd=2, relief=GROOVE, width=12)
        PowderEntry.grid(row=2, column=1, pady=14, padx=4)

        BodyLoshan = Label(CosmeticsFrame, text="Body Loshan", font=font_text,bg="Teal",fg="Maroon")
        BodyLoshan.grid(row=3, column=0)
        BodyLoshanEntry = Entry(CosmeticsFrame, font=font_text,textvariable=self.BodyloshanPrice, bg="FloralWhite", bd=2, relief=GROOVE, width=12)
        BodyLoshanEntry.grid(row=3, column=1, pady=14, padx=4)

        Shampoo = Label(CosmeticsFrame, text=" Hair Shampoo", font=font_text,bg="Teal",fg="Maroon")
        Shampoo.grid(row=4, column=0)
        ShampooEntry = Entry(CosmeticsFrame, font=font_text,textvariable=self.HairshampooPrice, bg="FloralWhite", bd=2, relief=GROOVE, width=12)
        ShampooEntry.grid(row=4, column=1, pady=14, padx=4)

        Shave=Label(CosmeticsFrame, text="Shaving Cream", font=font_text,bg="Teal",fg="Maroon")
        Shave.grid(row=5, column=0)
        ShaveEntry = Entry(CosmeticsFrame, font=font_text,textvariable=self.ShavingcreamPrice, bg="FloralWhite", bd=2, relief=GROOVE, width=12)
        ShaveEntry.grid(row=5, column=1, pady=14, padx=19)

        # SNACKS
        SnacksFrame = LabelFrame(self.root, text="Snacks", fg="Yellow", relief=GROOVE, font=font_supTitle,
                                    bg="Teal")
        SnacksFrame.place(x=340,y=150,width=325,height=380)

        Chips= Label(SnacksFrame, text="Chips", font=font_text, bg="Teal", fg="Maroon")
        Chips.grid(row=0, column=0)
        ChipsEntry = Entry(SnacksFrame, font=font_text,textvariable=self.ChipsPrice, bg="FloralWhite", bd=2, relief=GROOVE, width=12)
        ChipsEntry.grid(row=0, column=1, pady=14, padx=1)

        Drink = Label(SnacksFrame, text="Cold Drink", font=font_text, bg="Teal", fg="Maroon")
        Drink.grid(row=1, column=0)
        DrinkEntry = Entry(SnacksFrame, font=font_text,textvariable=self.ColddrinkPrice, bg="FloralWhite", bd=2, relief=GROOVE, width=12)
        DrinkEntry.grid(row=1, column=1, pady=14, padx=4)

        Choclate= Label(SnacksFrame, text="Choclate", font=font_text, bg="Teal", fg="Maroon")
        Choclate.grid(row=2, column=0)
        ChoclateEntry = Entry(SnacksFrame, font=font_text,textvariable=self.ChoclatePrice, bg="FloralWhite", bd=2, relief=GROOVE, width=12)
        ChoclateEntry.grid(row=2, column=1, pady=14, padx=4)

        Biscuits= Label(SnacksFrame, text="Biscuits", font=font_text, bg="Teal", fg="Maroon")
        Biscuits.grid(row=3, column=0,padx=9)
        BiscuitsEntry = Entry(SnacksFrame, font=font_text,textvariable=self.BiscuitsPrice, bg="FloralWhite", bd=2, relief=GROOVE, width=12)
        BiscuitsEntry.grid(row=3, column=1, pady=14, padx=8)

        IceCream= Label(SnacksFrame, text="Ice-Cream", font=font_text, bg="Teal", fg="Maroon")
        IceCream.grid(row=4, column=0)
        IceCreamEntry = Entry(SnacksFrame, font=font_text,textvariable=self.IcecreamPrice, bg="FloralWhite", bd=2, relief=GROOVE, width=12)
        IceCreamEntry.grid(row=4, column=1, pady=14, padx=4)

        CupCakes=Label(SnacksFrame, text="CupCakes", font=font_text, bg="Teal", fg="Maroon")
        CupCakes.grid(row=5, column=0)
        CupCakesEntry = Entry(SnacksFrame, font=font_text,textvariable=self.CupcakesPrice, bg="FloralWhite", bd=2, relief=GROOVE, width=12)
        CupCakesEntry.grid(row=5, column=1, pady=14, padx=39)

        # GROCERY
        GroceryFrame = LabelFrame(self.root, text="Grocery", fg="Yellow", relief=GROOVE, font=font_supTitle,
                                  bg="Teal")
        GroceryFrame.place(x=675, y=150, width=325, height=380)

        Wheat = Label(GroceryFrame, text="Wheat", font=font_text, bg="Teal", fg="Maroon")
        Wheat.grid(row=0, column=0)
        WheatEntry = Entry(GroceryFrame, font=font_text,textvariable=self.WheatPrice, bg="FloralWhite", bd=2, relief=GROOVE, width=12)
        WheatEntry.grid(row=0, column=1, pady=14, padx=1)

        Rice = Label(GroceryFrame, text="Rice", font=font_text, bg="Teal", fg="Maroon")
        Rice.grid(row=1, column=0)
        RiceEntry = Entry(GroceryFrame, font=font_text,textvariable=self.RicePrice, bg="FloralWhite", bd=2, relief=GROOVE, width=12)
        RiceEntry.grid(row=1, column=1, pady=14, padx=4)

        Daal = Label(GroceryFrame, text="Daal", font=font_text, bg="Teal", fg="Maroon")
        Daal.grid(row=2, column=0)
        DaalEntry = Entry(GroceryFrame, font=font_text,textvariable=self.DaalPrice, bg="FloralWhite", bd=2, relief=GROOVE, width=12)
        DaalEntry.grid(row=2, column=1, pady=14, padx=4)

        Oil = Label(GroceryFrame, text="Food Oil", font=font_text, bg="Teal", fg="Maroon")
        Oil.grid(row=3, column=0, padx=9)
        OilEntry = Entry(GroceryFrame, font=font_text,textvariable=self.FoodoilPrice, bg="FloralWhite", bd=2, relief=GROOVE, width=12)
        OilEntry.grid(row=3, column=1, pady=14, padx=8)

        Spices = Label(GroceryFrame, text="Spices", font=font_text, bg="Teal", fg="Maroon")
        Spices.grid(row=4, column=0)
        SpicesEntry = Entry(GroceryFrame, font=font_text,textvariable=self.SpicesPrice, bg="FloralWhite", bd=2, relief=GROOVE, width=12)
        SpicesEntry.grid(row=4, column=1, pady=14, padx=4)

        Tea = Label(GroceryFrame, text="Tea", font=font_text, bg="Teal", fg="Maroon")
        Tea.grid(row=5, column=0)
        TeaEntry = Entry(GroceryFrame, font=font_text,textvariable=self.TeaPrice, bg="FloralWhite", bd=2, relief=GROOVE, width=12)
        TeaEntry.grid(row=5, column=1, pady=14, padx=39)

        # BILL FIELD
        BillFrame=Frame(self.root,bd=8,relief=GROOVE)
        BillFrame.place(x=1010,y=150,width=300,height=380)
        BillTitle=Label(BillFrame,text="Bill Section" ,font=('Arial',15,'bold'),bd=7,relief=GROOVE,bg='cyan')
        BillTitle.pack(side=TOP,fill=X)
        scrollY=Scrollbar(BillFrame,orient=VERTICAL)
        self.txtarea=Text(BillFrame,yscrollcommand=scrollY.set)
        scrollY.pack(side=RIGHT,fill=Y)
        scrollY.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=X,expand=1)

        #BILL MENU FRAME
        MenuFrame=LabelFrame(self.root,text="Purchase Details", fg="Yellow",bd=4, relief=GROOVE, font=font_supTitle,bg="Teal")
        MenuFrame.place(x=5,y=535,width=760,height=170)

        TcosmeticsLabel = Label(MenuFrame, text="Total Cosmetic Expense:", font=font_text, bg="Teal",fg="Goldenrod")
        TcosmeticsLabel.grid(row=0, column=0, pady=10, sticky='w')
        TcosmeticsEntry = Entry(MenuFrame, font=font_text, bg="FloralWhite",textvariable=self.TotalCosmeticPrice, bd=2, relief=GROOVE, width=10)
        TcosmeticsEntry.grid(row=0, column=1, padx=4,pady=10)

        TcosmeticTaxLabel = Label(MenuFrame, text="Total Cosmetic Tax:", font=font_text, bg="Teal",fg="Goldenrod")
        TcosmeticTaxLabel.grid(row=0, column=2, pady=10, sticky='w', padx=6)
        TcosmeticTaxEntry = Entry(MenuFrame, font=font_text, bg="FloralWhite", bd=2,textvariable=self.TotalCosmeticTax, relief=GROOVE, width=10)
        TcosmeticTaxEntry.grid(row=0, column=3, padx=6,pady=10)

        TgroceryLabel = Label(MenuFrame, text="Total Grocery Expense:", font=font_text, bg="Teal",fg="Goldenrod")
        TgroceryLabel.grid(row=1, column=0, pady=10, sticky='w', padx=6)
        TgroceryEntry = Entry(MenuFrame, font=font_text, width=10, bg="FloralWhite",textvariable=self.TotalGroceryPrice, bd=2, relief=GROOVE)
        TgroceryEntry.grid(row=1, column=1, padx=6,pady=10)


        TgroceryTaxLabel = Label(MenuFrame, text="Total Grocery Tax:", font=font_text, bg="Teal",fg="Goldenrod")
        TgroceryTaxLabel.grid(row=1, column=2, pady=1, sticky='w', padx=6)
        TgroceryTaxEntry = Entry(MenuFrame, font=font_text, width=10, bg="FloralWhite",textvariable=self.TotalGroceryTax, bd=2, relief=GROOVE)
        TgroceryTaxEntry.grid(row=1, column=3, padx=6)

        TsnacksLabel= Label(MenuFrame, text="Total Snacks Expense:", font=font_text, bg="Teal",fg="Goldenrod")
        TsnacksLabel.grid(row=2, column=0, pady=10, sticky='w', padx=6)
        TsnacksEntry = Entry(MenuFrame, font=font_text, width=10, bg="FloralWhite",textvariable=self.TotalSnacksPrice, bd=2, relief=GROOVE)
        TsnacksEntry.grid(row=2, column=1, padx=6,pady=10)

        TsnacksTaxLabel = Label(MenuFrame, text="Total Snacks Tax:", font=font_text, bg="Teal",fg="Goldenrod")
        TsnacksTaxLabel.grid(row=2, column=2, pady=10, sticky='w', padx=6)
        TsnacksTaxEntry = Entry(MenuFrame, font=font_text, width=10, bg="FloralWhite",textvariable=self.TotalSnacksTax, bd=2, relief=GROOVE)
        TsnacksTaxEntry.grid(row=2, column=3, padx=6,pady=10)

        # TOTAL GENERATE BILL CLEAR AND PRINT BUTTON
        ButtonFrame=Frame(self.root,bd=5,relief=GROOVE,bg="Teal")
        ButtonFrame.place(x=800,y=535,width=600,height=200)

        TotalButton=Button(ButtonFrame,text="Total ",font=font_text,bg="Yellow",fg="Red",width=7,height=2,command=self.totalFun)
        TotalButton.grid(row=0,column=0,padx=9,pady=50)

        GenerateButton = Button(ButtonFrame, text="Generate", font=font_text, bg="Yellow", fg="Red",width=7,height=2,command=self.billGen)
        GenerateButton.grid(row=0, column=1, padx=9, pady=50)

        ClearButton = Button(ButtonFrame, text="Clear ", font=font_text, bg="Yellow", fg="Red",width=7,height=2,command=self.clearFun
                             )
        ClearButton.grid(row=0, column=2, padx=9, pady=50)

        PrintButton = Button(ButtonFrame, text="Print ", font=font_text, bg="Yellow", fg="Red",width=7,height=2)
        PrintButton.grid(row=0, column=3, padx=9, pady=50)

        self.billTemp()
    # FUNCTION FOR FINDING TOTAL OF PRODUCT
    def totalFun(self):
        if self.Name.get()=="":
            showerror("Name Required","Customer Name is required!!")
        elif self.Number.get()=="":
            showerror("Number Required","Customer Number is required!!")
        elif (self.HairgelPrice.get()==0 and
              self.FacecreamPrice.get()==0 and
              self.FacepowderPrice.get()==0 and
              self.BodyloshanPrice.get()==0 and
              self.HairshampooPrice.get()==0 and
              self.ShavingcreamPrice.get()==0 and
              self.ChipsPrice.get()==0 and
              self.ColddrinkPrice.get()==0 and
              self.ChoclatePrice.get()==0 and
              self.BiscuitsPrice.get()==0 and
              self.IcecreamPrice.get()==0 and
              self.CupcakesPrice.get()==0 and
              self.WheatPrice.get()==0 and
              self.RicePrice.get()==0 and
              self.DaalPrice.get()==0 and
              self.FoodoilPrice.get()==0 and
              self.SpicesPrice.get()==0 and
              self.TeaPrice.get()==0
            ):
            showerror("Items Not found","Nothing Purchased")

        else:
            self.HairTotal=self.HairgelPrice.get()*80
            self.CreamTotal=self.FacecreamPrice.get()*120
            self.PowderTotal=self.FacepowderPrice.get()*75
            self.LoshanTotal=self.BodyloshanPrice.get()*180
            self.ShampooTotal=self.HairshampooPrice.get()*120
            self.ShaveTotal=self.ShavingcreamPrice.get()*55

            self.ChipsTotal = self.ChipsPrice.get() * 10
            self.DrinkTotal = self.ColddrinkPrice.get() * 25
            self.ChoclateTotal = self.ChoclatePrice.get() * 15
            self.BiscuitsTotal = self.BiscuitsPrice.get() * 25
            self.IcecreamTotal = self.IcecreamPrice.get() * 30
            self.CupcakesTotal = self.CupcakesPrice.get() * 20

            self.WheatTotal = self.WheatPrice.get() * 23
            self.RiceTotal = self.RicePrice.get() * 30
            self.DaalTotal = self.DaalPrice.get() * 60
            self.FoodoilTotal = self.FoodoilPrice.get() * 80
            self.SpicesTotal = self.SpicesPrice.get() * 200
            self.TeaTotal = self.TeaPrice.get() * 300

            self.TotalCos=self.HairTotal+self.CreamTotal+self.PowderTotal+self.LoshanTotal+self.ShampooTotal+self.ShaveTotal
            self.TotalCosTax=round(self.TotalCos*0.15,2)
            self.TotalCosmeticPrice.set(f"₹ {str(self.TotalCos)}")
            self.TotalCosmeticTax.set(f"₹ {str(self.TotalCosTax)}")

            self.TotalGro = self.WheatTotal + self.RiceTotal + self.DaalTotal + self.FoodoilTotal + self.SpicesTotal + self.TeaTotal
            self.TotalGroTax = round(self.TotalGro * 0.15,2)
            self.TotalGroceryPrice.set(f"₹ {str(self.TotalGro)}")
            self.TotalGroceryTax.set(f"₹ {str(self.TotalGroTax)}")

            self.TotalSnac = self.ChipsTotal + self.DrinkTotal + self.ChoclateTotal + self.BiscuitsTotal + self.IcecreamTotal + self.CupcakesTotal
            self.TotalSnacTax = round(self.TotalSnac * 0.15, 2)
            self.TotalSnacksPrice.set(f"₹ {str(self.TotalSnac)}")
            self.TotalSnacksTax.set(f"₹ {str(self.TotalSnacTax)}")

            # TOTAL PRICE
            self.totalPrice=str(self.TotalCos+self.TotalGro+self.TotalSnac)
            self.totalTax=str(self.TotalCosTax+self.TotalSnacTax+self.TotalGroTax)

    # FUNCTION FOR CLEARING DATA OF FIELDS
    def clearFun(self):
        # REQUIRED VARIABLES

        self.Name.set("")
        self.Number.set("")
        self.txtarea.delete('1.0',END)


        # COSMETICS VARIABLES
        self.HairgelPrice.set(0)
        self.FacecreamPrice.set(0)
        self.FacepowderPrice.set(0)
        self.BodyloshanPrice.set(0)
        self.HairshampooPrice.set(0)
        self.ShavingcreamPrice.set(0)
        self.TotalCosmeticPrice.set(0)
        self.TotalCosmeticTax.set(0)

        # GROCERY VARIABLES
        self.WheatPrice.set(0)
        self.RicePrice.set(0)
        self.DaalPrice.set(0)
        self.FoodoilPrice.set(0)
        self.SpicesPrice.set(0)
        self.TeaPrice.set(0)
        self.TotalGroceryPrice.set(0)
        self.TotalGroceryTax.set(0)

        # SNACKS VARIABLES
        self.ChipsPrice.set(0)
        self.ColddrinkPrice.set(0)
        self.ChoclatePrice.set(0)
        self.BiscuitsPrice.set(0)
        self.IcecreamPrice.set(0)
        self.CupcakesPrice.set(0)
        self.TotalSnacksPrice.set(0)
        self.TotalSnacksTax.set(0)

    # FUNCTION FOR DISPLAYING TEMPLATE OF BILL
    def billTemp(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,f"    Welcome To SoulCoder Store\n")
        self.txtarea.insert(END,f"\n Bill Number(A):")
        self.txtarea.insert(END,f"\n Customer Name :    {self.Name.get()}")
        self.txtarea.insert(END,f"\n Customer Mobi :    {self.Number.get()}\n")
        self.txtarea.insert(END,"\n********************************")
        self.txtarea.insert(END,f"\n GOODS\t\tQTY\t  COST")
        self.txtarea.insert(END,"\n********************************")

    # FUNCTION FOR BUTTON BILL GENERATE
    def billGen(self):
        self.bill_num = str(random.randint(1000, 9999))
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, f"    Welcome To SoulCoder Store\n")
        self.txtarea.insert(END, f"\n Bill Number(A):    {self.bill_num}")
        self.txtarea.insert(END, f"\n Customer Name :    {self.Name.get()}")
        self.txtarea.insert(END, f"\n Customer Mobi :    {self.Number.get()}\n")
        self.txtarea.insert(END, "\n********************************")
        self.txtarea.insert(END, f"\n GOODS\t\tQTY\t  COST")
        self.txtarea.insert(END, "\n********************************")

        # COSMETICS
        if self.HairgelPrice.get()!=0:

            self.txtarea.insert(END,f"\n Hair Gel\t\t{self.HairgelPrice.get()}\t  {self.HairTotal}")
        if self.FacecreamPrice.get()!=0:
            self.txtarea.insert(END,f"\n Face Cream\t\t{self.FacecreamPrice.get()}\t  {self.CreamTotal}")
        if self.FacepowderPrice.get()!=0:
            self.txtarea.insert(END,f"\n Face Powder\t\t{self.FacepowderPrice.get()}\t  {self.PowderTotal}")
        if self.BodyloshanPrice.get()!=0:
            self.txtarea.insert(END,f"\n Body Loshan\t\t{self.BodyloshanPrice.get()}\t  {self.LoshanTotal}")
        if self.HairshampooPrice.get()!=0:
            self.txtarea.insert(END,f"\n Hair Shampoo\t\t{self.HairshampooPrice.get()}\t  {self.ShampooTotal}")
        if self.ShavingcreamPrice.get()!=0:
            self.txtarea.insert(END,f"\n Shaving Cream\t\t{self.ShavingcreamPrice.get()}\t  {self.ShaveTotal}")

        # SNACKS
        if self.ChipsPrice.get()!=0:
            self.txtarea.insert(END,f"\n Chips\t\t{self.ChipsPrice.get()}\t  {self.ChipsTotal}")
        if self.ColddrinkPrice.get()!=0:
            self.txtarea.insert(END,f"\n Cold Drinks\t\t{self.ColddrinkPrice.get()}\t  {self.DrinkTotal}")
        if self.ChoclatePrice.get() != 0:
            self.txtarea.insert(END, f"\n Choclates\t\t{self.ChoclatePrice.get()}\t  {self.ChoclateTotal}")
        if self.BiscuitsPrice.get()!=0:
            self.txtarea.insert(END,f"\n Biscuits\t\t{self.BiscuitsPrice.get()}\t  {self.BiscuitsTotal}")
        if self.IcecreamPrice.get()!=0:
            self.txtarea.insert(END,f"\n Ice Cream\t\t{self.IcecreamPrice.get()}\t  {self.IcecreamTotal}")
        if self.CupcakesPrice.get()!=0:
            self.txtarea.insert(END,f"\n Cup Cakes\t\t{self.CupcakesPrice.get()}\t  {self.CupcakesTotal}")

        # GROCERY
        if self.WheatPrice.get() != 0:
            self.txtarea.insert(END, f"\n Wheat\t\t{self.WheatPrice.get()}\t  {self.WheatTotal}")
        if self.RicePrice.get() != 0:
            self.txtarea.insert(END, f"\n Rice\t\t{self.RicePrice.get()}\t  {self.RiceTotal}")
        if self.DaalPrice.get() != 0:
            self.txtarea.insert(END, f"\n Daal\t\t{self.DaalPrice.get()}\t  {self.DaalTotal}")
        if self.FoodoilPrice.get() != 0:
            self.txtarea.insert(END, f"\n Food Oil\t\t{self.FoodoilPrice.get()}\t  {self.FoodoilTotal}")
        if self.SpicesPrice.get() != 0:
            self.txtarea.insert(END, f"\n Spices\t\t{self.SpicesPrice.get()}\t  {self.SpicesTotal}")
        if self.TeaPrice.get() != 0:
            self.txtarea.insert(END, f"\n Tea\t\t{self.TeaPrice.get()}\t  {self.TeaTotal}")
        self.txtarea.insert(END, "\n--------------------------------")
        self.txtarea.insert(END,f"\n Total\t\t₹ {self.totalPrice}")
        self.txtarea.insert(END,f"\n GST\t\t₹ {self.totalTax}")
        self.txtarea.insert(END, "\n--------------------------------")
        self.saveBill()

    # FUN FOR SAVING BILL RECEIPT AT BACKEND IF ADMIN WANTS
    def saveBill(self):
        message=messagebox.askyesno("Save Bill!!","Do You Want to Save Bill For Future Reference?")
        if message>0:
            self.data=self.txtarea.get('1.0',END)
            bill_file=open("bills/"+str(self.bill_num)+".txt","w")
            bill_file.write(self.data)
            bill_file.close()
        else:
            return

    # FUNCTION FOR FINDING SPECIFIC BILL OF USER:
    def find_bill(self):
        self.clearFun()
        check=False
        for data in os.listdir("bills/"):
            if data.split('.')[0]==self.Bill.get():
                file=open(f"bills/{data}","r")
                self.txtarea.delete('1.0', END)
                for i in file:
                    self.txtarea.insert(END,i)
                file.close()
                check=True
        if check==False:
            showerror("Not Found","Bill not Found!!")
root=Tk()
bill=BillManagement(root)
root.mainloop()
