from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk 

class Jewellery:
    def __init__(self, root):
        self.root = root
        self.root.title('JEWELLERY')
        self.root.geometry('1200x600')
        self.root.config(bg='#E4D0D0')

        # Variables
        self.GoldPrice = StringVar()
        self.Weight = StringVar()
        self.Wages = StringVar()
        self.Profit = StringVar()
        self.Tax = StringVar()

        #----------------------------------- Frames ---------------------------------------#
        Main_Frame = Frame(self.root, bg='#E4D0D0')
        Main_Frame.place(relwidth=1, relheight=1)

        Title_Frame = Frame(Main_Frame, bg='#D5B4B4', bd=2, padx=150, pady=20, relief=RIDGE)
        Title_Frame.pack(side=TOP)

        self.Title_Label = Label(Title_Frame, text='محاسبه هوشمند قیمت طلا: برنامه‌ای برای سرمایه‌گذاری مطمئن', bg='#D5B4B4', fg='#867070', font=('Mj_Farsi Simple Normal', 28, 'bold'))
        self.Title_Label.grid()

        #-------------------------------- Labels and Entry --------------------------------#
        self.Label_GoldPrice = Label(root, font=('Mj_Farsi Simple Normal', 20, 'bold'), text='قیمت روز طلا', bg='#E4D0D0', fg='#867070')
        self.Label_GoldPrice.place(x=450, y=150)

        self.text_GoldPrice = Entry(root, font=('Mj_Farsi Simple Normal', 18, 'bold'), textvariable=self.GoldPrice, width=30, bg='#fefefe', fg='#867070', highlightthickness=1)
        self.text_GoldPrice.place(x=200, y=150)

        self.Label_Weight = Label(root, font=('Mj_Farsi Simple Normal', 20, 'bold'), text='وزن', bg='#E4D0D0', fg='#867070')
        self.Label_Weight.place(x=480, y=200)

        self.text_Weight = Entry(root, font=('Mj_Farsi Simple Normal', 18, 'bold'), textvariable=self.Weight, width=30, bg='#fefefe', fg='#867070', highlightthickness=1)
        self.text_Weight.place(x=200, y=200)

        self.Label_Wages = Label(root, font=('Mj_Farsi Simple Normal', 20, 'bold'), text='اجرت', bg='#E4D0D0', fg='#867070')
        self.Label_Wages.place(x=470, y=250)

        self.text_Wages = Entry(root, font=('Mj_Farsi Simple Normal', 18, 'bold'), textvariable=self.Wages, width=30, bg='#fefefe', fg='#867070', highlightthickness=1)
        self.text_Wages.place(x=200, y=250)

        self.Label_Profit = Label(root, font=('Mj_Farsi Simple Normal', 20, 'bold'), text='سود', bg='#E4D0D0', fg='#867070')
        self.Label_Profit.place(x=480, y=300)

        self.text_Profit = Entry(root, font=('Mj_Farsi Simple Normal', 18, 'bold'), textvariable=self.Profit, width=30, bg='#fefefe', fg='#867070', highlightthickness=1)
        self.text_Profit.place(x=200, y=300)

        self.Label_Tax = Label(root, font=('Mj_Farsi Simple Normal', 20, 'bold'), text='مالیات', bg='#E4D0D0', fg='#867070')
        self.Label_Tax.place(x=470, y=350)

        self.text_Tax = Entry(root, font=('Mj_Farsi Simple Normal', 18, 'bold'), textvariable=self.Tax, width=30, bg='#fefefe', fg='#867070', highlightthickness=1)
        self.text_Tax.place(x=200, y=350)

        #-------------------------------- Adding Images --------------------------------#
        image1 = Image.open("image2.png")  
        image1 = image1.resize((230, 230),  Image.LANCZOS)
        self.image1 = ImageTk.PhotoImage(image1)

        image2 = Image.open("image1.png")  
        image2 = image2.resize((230, 230),  Image.LANCZOS)
        self.image2 = ImageTk.PhotoImage(image2)

        self.image_label1 = Label(root, image=self.image1, bg='#E4D0D0')
        self.image_label1.place(x=650, y=150)
        
        self.image_label2 = Label(root, image=self.image2, bg='#E4D0D0')
        self.image_label2.place(x=850, y=270)

        #-------------------------------- Button Widgets --------------------------------#
        self.Cal_Button = Button(root, text='محاسبه قیمت', font=('Mj_Farsi Simple Normal', 20, 'bold'), bg='#D5B4B4', fg='#867070', relief=RIDGE, borderwidth=1, command=self.calculate_price)
        self.Cal_Button.place(x=300, y=430)

        self.Del_Button = Button(root, text='حذف', font=('Mj_Farsi Simple Normal', 20, 'bold'), bg='#D5B4B4', fg='#867070', relief=RIDGE, borderwidth=1, command=self.clear_fields)
        self.Del_Button.place(x=200, y=430)

    
        #-------------------------------- Calculation Function --------------------------------#
    def calculate_price(self):
        try:
            gold_price = int(self.GoldPrice.get().split()[0])  
            weight = int(self.Weight.get())  
            wages = int(self.Wages.get())  
            profit = int(self.Profit.get())  
            tax = int(self.Tax.get())  

            # تبدیل درصدها به اعداد اعشاری
            wages_percent = wages / 100
            profit_percent = profit / 100
            tax_percent = tax / 100

            # مرحله اول: وزن × اجرت
            step1 = weight * wages

            # مرحله دوم: مرحله اول + سود
            step2 = step1 + (step1 * profit_percent)

            # مرحله سوم: مرحله دوم + مالیات
            step3 = step2 + (step2 * tax_percent)

            # مرحله چهارم: مرحله سوم × قیمت روز طلا
            total_price = step3 * gold_price

    
            result_window = Toplevel(self.root)
            result_window.title("نتیجه محاسبه")
            result_window.geometry("400x200")
            result_window.config(bg='#E4D0D0')

            result_label = Label(result_window, text=f"قیمت نهایی طلای شما: {total_price:,} ریال", font=('Mj_Farsi Simple Normal', 20, 'bold'), bg='#E4D0D0', fg='#867070')
            result_label.pack(pady=50)

        except ValueError:
            messagebox.showerror("خطا", "لطفاً مقادیر معتبر وارد کنید.")
    #-------------------------------- Clear Fields Function --------------------------------#
    def clear_fields(self):
        self.GoldPrice.set("")  
        self.Weight.set("")     
        self.Wages.set("")      
        self.Profit.set("")     
        self.Tax.set("")      

#-------------------------------- Main Program --------------------------------#
if __name__ == "__main__":
    root = Tk()
    application = Jewellery(root)
    root.mainloop()