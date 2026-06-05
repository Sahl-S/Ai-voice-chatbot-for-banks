from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage,Entry,messagebox,IntVar,Text,Label
from tkinter.ttk import Combobox,Radiobutton,Style
import tkinter as tk
import re
import camera
import databases
import dbinsert
from camera import textcapt


imgname='null'

def applogincapt():
    global phone,email,fullname,useridno,account_no,balance,countacc
    facial_fail=2
    camera.imgcapt()
    facial_fail=camera.facerecog()
    print("facial fail is",facial_fail)
    if facial_fail==0:
        databases.checkfacedb()
        fullname=databases.dbfullname()
        phone=databases.phone()
        email=databases.dbemail()
        balance=databases.dbaccountbalance()
        home_page()
        countacc=databases.dbcount()
        account_no=databases.dbaccountno()









OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.geometry("700x550")
window.configure(bg="#FFFFFF")
window.resizable(False,False)

button_images={ "button_card": PhotoImage(file=relative_to_assets("button_card.png")),
                "button_back": PhotoImage(file=relative_to_assets("button_back.png")),
                "button_viewacc": PhotoImage(file=relative_to_assets("button_viewacc.png")),
                "button_account": PhotoImage(file=relative_to_assets("button_account.png")),
                "button_closeacc": PhotoImage(file=relative_to_assets("button_closeacc.png")),
                "button_createacc": PhotoImage(file=relative_to_assets("button_createacc.png")),
                "button_faq": PhotoImage(file=relative_to_assets("button_faq.png")),
                "button_malayalam": PhotoImage(file=relative_to_assets("button_malayalam.png")),
                "button_mergeacc": PhotoImage(file=relative_to_assets("button_mergeacc.png")),
                "button_notifications": PhotoImage(file=relative_to_assets("button_notifications.png")),
                "button_signout": PhotoImage(file=relative_to_assets("button_signout.png")),
                "button_submit": PhotoImage(file=relative_to_assets("button_submit.png")),
                "button_moneytransfer": PhotoImage(file=relative_to_assets("button_moneytransfer.png")),
                "entry_image": PhotoImage(file=relative_to_assets("entry_image.png")),
                "bg_image": PhotoImage(file=relative_to_assets("bg_image.png")),
                "notifications_image": PhotoImage(file=relative_to_assets("notifications_image.png")),
                "button_customize": PhotoImage(file=relative_to_assets("button_customize.png")),
                "button_account_malayalam": PhotoImage(file=relative_to_assets("button_account_malayalam.png")),
                "button_card_malayalam": PhotoImage(file=relative_to_assets("button_card_malayalam.png")),
                "button_moneytransfer_malayalam": PhotoImage(file=relative_to_assets("button_moneytransfer_malayalam.png")),
                "button_faq_malayalam": PhotoImage(file=relative_to_assets("button_faq_malayalam.png")),
                "button_signoutmal": PhotoImage(file=relative_to_assets("button_signout_malayalam.png")),
                "button_notifications_malayalam": PhotoImage(file=relative_to_assets("button_notifications_malayalam.png")),
                "button_english": PhotoImage(file=relative_to_assets("button_english.png")),
                "button_viewacc_malayalam": PhotoImage(file=relative_to_assets("button_viewacc_malayalam.png")),
                "button_createacc_malayalam": PhotoImage(file=relative_to_assets("button_createacc_malayalam.png")),
                "button_closeacc_malayalam": PhotoImage(file=relative_to_assets("button_closeacc_malayalam.png")),
                "button_mergeacc_malayalam": PhotoImage(file=relative_to_assets("button_mergeacc_malayalam.png")),
                "button_submit_malayalam": PhotoImage(file=relative_to_assets("button_submit_malayalam.png")),
                "button_back_malayalam": PhotoImage(file=relative_to_assets("button_back_malayalam.png"))
               }
              


current_page=None
current_language="english"
def welcome_page():
    global repetitions,canvas,rectangle_id,text_id,welcome_id,login_button,create_account_button
    def toggle_visibility():
        global repetitions
        if repetitions == 0:
            return
        if canvas.itemcget(text_id, "state") == "hidden":
            canvas.itemconfigure(text_id, state="normal")
        else:
            canvas.itemconfigure(text_id, state="hidden")
        repetitions -= 1
        canvas.after(interval, toggle_visibility)
    
    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 600,
        width = 800,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
    canvas.place(x = 0, y = 0)

    canvas.create_image(
    350.0,
    275.0,
    image=button_images["bg_image"]
    )
    welcome_id=canvas.create_text(
    230.0,
    164.0,
    anchor="nw",
    text="WELCOME !",
    fill="#302E27",
    font=("Inter", 55 * -1),
    tags="welcome_id"
    )

    text_id=canvas.create_text(
        180.0,
        275.0,
        anchor="nw",
        text="We are glad you are here!",
        fill="#EBA7A7",
        font=("Inter", 36 * -1),
        tags="welcome_id"
    )

    interval = 500  # milliseconds
    repetitions = 6  # Number of times to blink
    toggle_visibility()

    login_button = Button(
        window,
        text="SIGN IN",
        font=("Helvetica", 14),
        command=applogincapt,
        bg="#302E27",
        fg="white",
        relief="flat",
        cursor="hand2"
    )
    login_button.place(
        x=330,
        y=350,
        width=120,
        height=40
    )

    create_account_button = Button(
        window,
        text="Create Account",
        font=("Helvetica", 14),
        command=new_account,
        bg="#67210B",
        fg="white",
        relief="flat",
        cursor="hand2"
    )
    create_account_button.place(
        x=530,
        y=10,
        width=150,
        height=30
    )



def new_account():
    canvas.delete("welcome_id")
    login_button.destroy()
    
    english_button = Button(
        window,
        text="ENGLISH",
        font=("Helvetica", 14),
        command=english_new_account,
        bg="#302E27",
        fg="white",
        relief="flat",
        cursor="hand2"
    )
    english_button.place(
        x=315,
        y=180,
        width=120,
        height=40
    )

    malayalam_button = Button(
        window,
        text="മലയാളം",
        font=("Helvetica", 14),
        command=malayalam_new_account,
        bg="#302E27",
        fg="white",
        relief="flat",
        cursor="hand2"
    )
    malayalam_button.place(
        x=315,
        y=260,
        width=120,
        height=40
    )

    def exit():
        english_button.destroy()
        malayalam_button.destroy()
        welcome_page()

    create_account_button.config(text="Exit",command=exit)
    
def malayalam_new_account():
    global current_language
    current_language="malayalam"
    new_account_page()

def english_new_account():
    global current_language
    current_language="english"
    new_account_page()

def new_account_page():
    canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=550,
    width=700,
    bd=0,
    highlightthickness=0,
    relief="ridge"
    )
    canvas.place(x=0, y=0)

    rectangle_id=canvas.create_rectangle(
        0.0,
        0.0,
        712.0,
        80.0,
        fill="#AECCE8",
        outline=""
    )

    welcome_text_id = canvas.create_text(
        29.0,
        26.0,
        anchor="nw",
        text="WELCOME TO BANK",
        fill="#0D5D45",
        font=("RobotoRoman ExtraBold", 20 * -1)
    ) 

    def exit():
        welcome_page()

    def scan_details():
        captured_data = textcapt()
        entry_1.insert(0, captured_data["Name"])
        entry_2.insert(0, "")
        entry_3.insert(0, captured_data["Aadhar No"])
        entry_4.insert(0, captured_data["Address"])
        entry_5.insert(0, captured_data["Mobile No"])
        entry_6.insert(0, captured_data["Email"])
        entry_7.insert(0, captured_data["DOB"])
    if current_language=="english":
        canvas.create_text(
            177.0,
            161.0,
            anchor="nw",
            text="NAME:",
            fill="#0B694D",
            font=("RobotoRoman Medium", 15 * -1),
            tags="create_account_text"
        )

        canvas.create_text(
            177.0,
            200.0,
            anchor="nw",
            text="ACCOUNT TYPE:",
            fill="#0B694D",
            font=("RobotoRoman Medium", 15 * -1),
            tags="create_account_text"
        )

        canvas.create_text(
            177.0,
            239.0,
            anchor="nw",
            text="AADHAR NUMBER:",
            fill="#0B694D",
            font=("RobotoRoman Medium", 15 * -1),
            tags="create_account_text"
        )

        canvas.create_text(
            177.0,
            278.0,
            anchor="nw",
            text="ADDRESS:",
            fill="#0B694D",
            font=("RobotoRoman Medium", 15 * -1),
            tags="create_account_text"
        )

        canvas.create_text(
            177.0,
            317.0,
            anchor="nw",
            text="PHONE:",
            fill="#0B694D",
            font=("RobotoRoman Medium", 15 * -1),
            tags="create_account_text"
        )

        canvas.create_text(
            177.0,
            356.0,
            anchor="nw",
            text="EMAIL:",
            fill="#0B694D",
            font=("RobotoRoman Medium", 15 * -1),
            tags="create_account_text"
        )

        canvas.create_text(
            177.0,
            395.0,
            anchor="nw",
            text="D.O.B:",
            fill="#0B694D",
            font=("RobotoRoman Medium", 15 * -1),
            tags="create_account_text"
        )

        canvas.create_text(
            177.0,
            434.0,
            anchor="nw",
            text="BRANCH:",
            fill="#0B694D",
            font=("RobotoRoman Medium", 15 * -1),
            tags="create_account_text"
        )

        canvas.create_text(
        278.0,
        103.0,
        anchor="nw",
        text="PLEASE ENTER YOUR DETAILS",
        fill="#631313",
        font=("RobotoRoman SemiBold", 15 * -1),
        tags="create_account_text"
        )
    else:
        canvas.create_text(
        177.0,
        161.0,
        anchor="nw",
        text="പേര്:",
        fill="#0B694D",
        font=("RobotoRoman Medium", 15 * -1),
        tags="create_account_text"
        )

        canvas.create_text(
            177.0,
            200.0,
            anchor="nw",
            text="അക്കൗണ്ട് തരം:",
            fill="#0B694D",
            font=("RobotoRoman Medium", 15 * -1),
            tags="create_account_text"
        )

        canvas.create_text(
            177.0,
            239.0,
            anchor="nw",
            text="ആധാർ നമ്പർ:",
            fill="#0B694D",
            font=("RobotoRoman Medium", 15 * -1),
            tags="create_account_text"
        )

        canvas.create_text(
            177.0,
            278.0,
            anchor="nw",
            text="വിലാസം:",
            fill="#0B694D",
            font=("RobotoRoman Medium", 15 * -1),
            tags="create_account_text"
        )

        canvas.create_text(
            177.0,
            317.0,
            anchor="nw",
            text="ഫോൺ:",
            fill="#0B694D",
            font=("RobotoRoman Medium", 15 * -1),
            tags="create_account_text"
        )

        canvas.create_text(
            177.0,
            356.0,
            anchor="nw",
            text="ഇമെയിൽ:",
            fill="#0B694D",
            font=("RobotoRoman Medium", 15 * -1),
            tags="create_account_text"
        )

        canvas.create_text(
            177.0,
            395.0,
            anchor="nw",
            text="ജനന തിയതി:",
            fill="#0B694D",
            font=("RobotoRoman Medium", 15 * -1),
            tags="create_account_text"
        )

        canvas.create_text(
            177.0,
            434.0,
            anchor="nw",
            text="ബ്രാഞ്ച്:",
            fill="#0B694D",
            font=("RobotoRoman Medium", 15 * -1),
            tags="create_account_text"
        )

        canvas.create_text(
            278.0,
            103.0,
            anchor="nw",
            text="ദയവായി നിങ്ങളുടെ വിവരങ്ങൾ നൽകുക",
            fill="#631313",
            font=("RobotoRoman SemiBold", 15 * -1),
            tags="create_account_text"
        )

    entry_bg_1 = canvas.create_image(
    490.0,
    165.5,
    image=button_images["entry_image"],
    tags="create_account_text"
    )
    entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    cursor="hand2"
    )
    entry_1.place(
    x=350.0,
    y=155.0,
    width=280.0,
    height=19.0
    )

    entry_bg_2 = canvas.create_image(
    490.0,
    205.5,
    image=button_images["entry_image"],
    tags="create_account_text"
    )
    entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    cursor="hand2"
    )
    entry_2.place(
    x=350.0,
    y=195.0,
    width=280.0,
    height=19.0
    )
    entry_bg_3 = canvas.create_image(
        490.0,
        245.5,
        image=button_images["entry_image"],
        tags="create_account_text"
    )
    entry_3 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0,
        cursor="hand2"
    )
    entry_3.place(
        x=350.0,
        y=235.0,
        width=280.0,
        height=19.0
    )

    entry_bg_4 = canvas.create_image(
        490.0,
        284.5,
        image=button_images["entry_image"],
        tags="create_account_text"
    )
    entry_4 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0,
        cursor="hand2"
    )
    entry_4.place(
        x=350.0,
        y=274.0,
        width=280.0,
        height=19.0
    )

    entry_bg_5 = canvas.create_image(
        490.0,
        324.5,
        image=button_images["entry_image"],
        tags="create_account_text"
    )
    entry_5 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0,
        cursor="hand2"
    )
    entry_5.place(
        x=350.0,
        y=314.0,
        width=280.0,
        height=19.0
    )


    entry_bg_6 = canvas.create_image(
        490.0,
        364.5,
        image=button_images["entry_image"],
        tags="create_account_text"
    )
    entry_6 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0,
        cursor="hand2"
    )
    entry_6.place(
        x=350.0,
        y=354.0,
        width=280.0,
        height=19.0
    )


    entry_bg_7 = canvas.create_image(
        490.0,
        404.5,
        image=button_images["entry_image"],
        tags="create_account_text"
    )
    entry_7 =Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0,
        cursor="hand2"
    )
    entry_7.place(
        x=350.0,
        y=394.0,
        width=280.0,
        height=19.0
    )

    entry_bg_8 = canvas.create_image(
        490.0,
        444.5,
        image=button_images["entry_image"],
        tags="create_account_text"
    )
    entry_8 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0,
        readonlybackground="#D9D9D9",
        state="readonly"
    )
    entry_8.place(
        x=350.0,
        y=434.0,
        width=280.0,
        height=19.0
    )
    if current_language=="english":
        locked_text_label = Label(window, text="PERINTHALMANNA", bg="#D9D9D9", fg="#000716")
        locked_text_label.place(x=350.0, y=434.0)
    else:
        locked_text_label = Label(window, text="പെരിന്തൽമണ്ണ", bg="#D9D9D9", fg="#000716")
        locked_text_label.place(x=350.0, y=434.0)

    def validate_name(name):
        # Only allow alphabets, spaces, and hyphens, minimum length 2
        return re.match(r'^[A-Za-z -]{2,}$', name)

    def validate_account_type(account_type):
        # Only allow "Current" or "Saving" (case insensitive)
        return account_type.lower() in ['current', 'saving']

    def validate_aadhar(aadhar):
        # Aadhar should be exactly 12 digits
        return re.match(r'^\d{12}$', aadhar)

    def validate_address(address):
        # Address validation, can be more specific if needed
        return len(address) > 0

    def validate_phone(phone):
        # Phone number should be exactly 10 digits
        return re.match(r'^\d{10}$', phone)

    def validate_email(email):
        # Email format validation
        return re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)

    def validate_dob(dob):
        # DOB should be in the format dd-mm-yyyy
        pattern = r'^\d{1,2}-\d{1,2}-\d{4}$'
        if not re.match(pattern, dob):
            return False
        day, month, year = map(int, dob.split('-'))
        # Basic validation for day, month, and year
        if day < 1 or day > 31 or month < 1 or month > 12 or year < 1900:
            return False
        # Additional validation based on month (can be more specific)
        if month in [4, 6, 9, 11] and day > 30:
            return False
        if month == 2:
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                if day > 29:
                    return False
            elif day > 28:
                return False
        return True

    if current_language=="english":
        def submit_details():
            name = entry_1.get().strip()
            account_type = entry_2.get().strip()
            aadhar = entry_3.get().strip()
            address = entry_4.get().strip()
            phone = entry_5.get().strip()
            email = entry_6.get().strip()
            dob = entry_7.get().strip()


            if not validate_name(name):
                messagebox.showerror("Error", "Invalid Name")
            elif not validate_account_type(account_type):
                messagebox.showerror("Error", "Invalid Account Type")
            elif not validate_aadhar(aadhar):
                messagebox.showerror("Error", "Invalid Aadhar Number")
            elif not validate_address(address):
                messagebox.showerror("Error", "Invalid Address")
            elif not validate_phone(phone):
                messagebox.showerror("Error", "Invalid Phone Number")
            elif not validate_email(email):
                messagebox.showerror("Error", "Invalid Email")
            elif not validate_dob(dob):
                messagebox.showerror("Error", "Invalid Date of Birth")
            else:
                # If all validations pass, proceed with submission
                dbinsert.userreq(name,dob,phone,address,aadhar,address,imgname)
                entry_1.delete(0, tk.END)
                entry_2.delete(0, tk.END)
                entry_3.delete(0, tk.END)
                entry_4.delete(0, tk.END)
                entry_5.delete(0, tk.END)
                entry_6.delete(0, tk.END)
                entry_7.delete(0, tk.END)
                entry_8.delete(0, tk.END)
                # Delete other entry fields and submit details
                messagebox.showinfo("Success", "Details Submitted Successfully")
                camera.facecapt()
                canvas.destroy()
                welcome_page()
        button_submit = Button(
        image=button_images["button_submit"],
        borderwidth=0,
        highlightthickness=0,
        command=submit_details,
        relief="flat",
        cursor="hand2"
        )

        button_submit.place(
        x=450.0,
        y=486.0,
        width=87.02251434326172,
        height=21.0
        )

        text_button = Button(
            window,
            text="SCAN",
            font=("Helvetica", 14),
            command=scan_details,
            bg="#302E27",
            fg="white",
            relief="flat",
            cursor="hand2"
        )
        text_button.place(
            x=330.0,
            y=486.0,
            width=87.02251434326172,
            height=21.0
        )


        button_back = Button(
        image=button_images["button_back"],
        borderwidth=0,
        highlightthickness=0,
        command=exit,
        relief="flat",
        cursor="hand2"
        )  
        button_back.place(
        x=63.11627197265625,
        y=100.0,
        width=72.5931396484375,
        height=21.0
        ) 
    else:
        def submit_details():
            name = entry_1.get().strip()
            account_type = entry_2.get().strip()
            aadhar = entry_3.get().strip()
            address = entry_4.get().strip()
            phone = entry_5.get().strip()
            email = entry_6.get().strip()
            dob = entry_7.get().strip()

            if not validate_name(name):
                messagebox.showerror("Error", "അസാധുവായ പേര്")
            elif not validate_account_type(account_type):
                messagebox.showerror("Error", "അസാധുവായ അക്കൗണ്ട് തരം")
            elif not validate_aadhar(aadhar):
                messagebox.showerror("Error", "അസാധുവായ ആധാർ നമ്പർ")
            elif not validate_address(address):
                messagebox.showerror("Error", "അസാധുവായ വിലാസം")
            elif not validate_phone(phone):
                messagebox.showerror("Error", "അസാധുവായ ഫോൺ നമ്പർ")
            elif not validate_email(email):
                messagebox.showerror("Error", "അസാധുവായ ഇമെയിൽ")
            elif not validate_dob(dob):
                messagebox.showerror("Error", "അസാധുവായ ജനന തിയതി")
            else:
                # If all validations pass, proceed with submission
                #databases.userreq(name, dob, phone, email, aadhar, address, imgname)
                entry_1.delete(0, tk.END)
                entry_2.delete(0, tk.END)
                entry_3.delete(0, tk.END)
                entry_4.delete(0, tk.END)
                entry_5.delete(0, tk.END)
                entry_6.delete(0, tk.END)
                entry_7.delete(0, tk.END)
                entry_8.delete(0, tk.END)
                dbinsert.userreq(name, dob, phone, address, aadhar, address, imgname)
                # Delete other entry fields and submit details
                messagebox.showinfo("Success", "വിവരങ്ങൾ വിജയകരമായി സമർപ്പിച്ചു")
                camera.facecapt()

                canvas.destroy()
                welcome_page()
        button_submit = Button(
        image=button_images["button_submit_malayalam"],
        borderwidth=0,
        highlightthickness=0,
        command=submit_details,
        relief="flat",
        cursor="hand2"
        )

        button_submit.place(
        x=450.0,
        y=486.0,
        width=123.587890625,
        height=21.0
        )

        text_button = Button(
            window,
            text="സ്കാൻ",
            font=("Helvetica", 14),
            command=scan_details,
            bg="#302E27",
            fg="white",
            relief="flat",
            cursor="hand2"
        )
        text_button.place(
            x=330.0,
            y=486.0,
            width=87.02251434326172,
            height=21.0
        )

        button_back = Button(
            image=button_images["button_back_malayalam"],
            borderwidth=0,
            highlightthickness=0,
            command=exit,
            relief="flat",
            cursor="hand2"
        )  
        button_back.place(
            x=45.0,
            y=100.0,
            width=102.09426879882812,
            height=21.0
        )

def home_page():
    global button_images,welcome_text_id,button_account,button_malayalam,canvas,rectangle_id,current_page,current_language,button_card,button_faq,button_moneytransfer,button_notifications,button_signout,button_english
    current_page="home"
    current_language=="english"
    canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=550,
    width=700,
    bd=0,
    highlightthickness=0,
    relief="ridge"
    )
    canvas.place(x=0, y=0)

    rectangle_id=canvas.create_rectangle(
        0.0,
        0.0,
        712.0,
        80.0,
        fill="#AECCE8",
        outline=""
    )

    welcome_text_id = canvas.create_text(
        29.0,
        26.0,
        anchor="nw",
        text="WELCOME TO BANK",
        fill="#0D5D45",
        font=("RobotoRoman ExtraBold", 20 * -1)
    ) 

    if current_language=="english":
        button_account = Button(
            image=button_images["button_account"],
            borderwidth=0,
            highlightthickness=0,
            command=account_page,
            relief="flat",
            cursor="hand2"
        )
        button_account.place(x=60.0, y=108.0, width=224.0, height=81.0)
        
        button_card = Button(
        image=button_images["button_card"],
        borderwidth=0,
        highlightthickness=0,
        command=card_page,
        relief="flat",
        cursor="hand2"
        )
        button_card.place(x=60.0, y=330.0, width=224.0, height=81.0)

        button_moneytransfer = Button(
            image=button_images["button_moneytransfer"],
            borderwidth=0,
            highlightthickness=0,
            command=money_transfer_page,
            relief="flat",
            cursor="hand2"
        )
        button_moneytransfer.place(x=421.0, y=107.0, width=224.0, height=81.0)

        button_faq = Button(
            image=button_images["button_faq"],
            borderwidth=0,
            highlightthickness=0,
            command=faq_page,
            relief="flat",
            cursor="hand2"
        )
        button_faq.place(x=421.0, y=330.0, width=224.0, height=81.0)

        button_signout = Button(
            image=button_images["button_signout"],
            borderwidth=0,
            highlightthickness=0,
            command=welcome_page,
            relief="flat",
            cursor="hand2"
        )
        button_signout.place(x=332.0, y=30.0, width=122.44898223876953, height=20.0)
        
        button_malayalam = Button(
        image=button_images["button_malayalam"],
        borderwidth=0,
        highlightthickness=0,
        command=malayalam_page,
        relief="flat",
        cursor="hand2"
        )
        button_malayalam.place(x=576.0, y=30.0, width=120.0, height=20.0)

        button_notifications = Button(
        image=button_images["button_notifications"],
        borderwidth=0,
        highlightthickness=0,
        command=notifications_page,
        cursor="hand2"
        )
        button_notifications.place(x=454.0, y=30.0, width=122.14286041259766, height=20.0)
    else:
        button_account = Button(
            image=button_images["button_account_malayalam"],
            borderwidth=0,
            highlightthickness=0,
            command=account_page,
            relief="flat",
            cursor="hand2"
        )
        button_account.place(x=60.0, y=108.0, width=224.0, height=81.0)

        button_card = Button(
        image=button_images["button_card_malayalam"],
        borderwidth=0,
        highlightthickness=0,
        command=card_page,
        relief="flat",
        cursor="hand2"
        )
        button_card.place(x=60.0, y=330.0, width=224.0, height=81.0)

        button_moneytransfer = Button(
            image=button_images["button_moneytransfer_malayalam"],
            borderwidth=0,
            highlightthickness=0,
            command=money_transfer_page,
            relief="flat",
            cursor="hand2"
        )
        button_moneytransfer.place(x=421.0, y=107.0, width=224.0, height=81.0)

        button_faq = Button(
            image=button_images["button_faq_malayalam"],
            borderwidth=0,
            highlightthickness=0,
            command=faq_page,
            relief="flat",
            cursor="hand2"
        )
        button_faq.place(x=421.0, y=330.0, width=224.0, height=81.0)

        button_signout = Button(
            image=button_images["button_signoutmal"],
            borderwidth=0,
            highlightthickness=0,
            command=welcome_page,
            relief="flat",
            cursor="hand2"
        )
        button_signout.place(x=332.0, y=30.0, width=122.44898223876953, height=20.0)

        button_english = Button(
        image=button_images["button_english"],
        borderwidth=0,
        highlightthickness=0,
        command=english_page,
        relief="flat",
        cursor="hand2"
        )
        button_english.place(x=576.0, y=30.0, width=120.0, height=20.0)

        
        button_notifications = Button(
        image=button_images["button_notifications_malayalam"],
        borderwidth=0,
        highlightthickness=0,
        command=notifications_page,
        relief="flat",
        cursor="hand2"
        )
        button_notifications.place(x=454.0, y=30.0, width=122.14286041259766, height=20.0)
        
def account_page():
    global button_viewacc,button_mergeacc,button_closeacc,button_createacc,button_back
    button_account.destroy()
    button_account.destroy()
    button_card.destroy()
    button_faq.destroy()
    button_moneytransfer.destroy()
    button_notifications.destroy()
    button_signout.place(x=454.0, y=30.0, width=122.14286041259766, height=20.0)
    

    def back():
        button_viewacc.destroy()
        button_createacc.destroy()
        button_closeacc.destroy()
        button_mergeacc.destroy()
        home_page()

    if current_language=="english":
        button_viewacc = Button(
        image=button_images["button_viewacc"],
        borderwidth=0,
        highlightthickness=0,
        command=view_account_page,
        relief="flat",
        cursor="hand2",
        text="View Account"
        )
        button_viewacc.place(x=222.0, y=96.0, width=224.0, height=81.0)

        button_createacc = Button(
        image=button_images["button_createacc"],
        borderwidth=0,
        highlightthickness=0,
        command=create_account_page,
        relief="flat",
        cursor="hand2"
        )
        button_createacc.place(x=222.0, y=324.0, width=224.0, height=81.0)

        button_closeacc = Button(
        image=button_images["button_closeacc"],
        borderwidth=0,
        highlightthickness=0,
        command=close_account_page,
        relief="flat",
        cursor="hand2",
        text="Close Account" 
        )
        button_closeacc.place(x=222.0, y=207.0, width=224.0, height=81.0)

        button_mergeacc = Button(
        image=button_images["button_mergeacc"],
        borderwidth=0,
        highlightthickness=0,
        command=close_account_page,
        relief="flat",
        cursor="hand2"
        )
        button_mergeacc.place(x=222.0, y=435.0, width=224.0, height=81.0)

        button_back = Button(
        image=button_images["button_back"],
        borderwidth=0,
        highlightthickness=0,
        command=back,
        relief="flat",
        cursor="hand2"
        )  
        button_back.place(
        x=63.11627197265625,
        y=100.0,
        width=72.5931396484375,
        height=21.0
        )
        button_malayalam.place_forget() 

    else:
        button_viewacc = Button(
        image=button_images["button_viewacc_malayalam"],
        borderwidth=0,
        highlightthickness=0,
        command=view_account_page,
        relief="flat",
        cursor="hand2",
        text="View Account"
        )
        button_viewacc.place(x=222.0, y=96.0, width=224.0, height=81.0)

        button_createacc = Button(
        image=button_images["button_createacc_malayalam"],
        borderwidth=0,
        highlightthickness=0,
        command=create_account_page,
        relief="flat",
        cursor="hand2"
        )
        button_createacc.place(x=222.0, y=324.0, width=224.0, height=81.0)

        button_closeacc = Button(
        image=button_images["button_closeacc_malayalam"],
        borderwidth=0,
        highlightthickness=0,
        command=close_account_page,
        relief="flat",
        cursor="hand2",
        text="Close Account" 
        )
        button_closeacc.place(x=222.0, y=207.0, width=224.0, height=81.0)

        button_mergeacc = Button(
        image=button_images["button_mergeacc_malayalam"],
        borderwidth=0,
        highlightthickness=0,
        command=merge_account_page,
        relief="flat",
        cursor="hand2"
        )
        button_mergeacc.place(x=222.0, y=435.0, width=224.0, height=81.0)

        button_back = Button(
        image=button_images["button_back_malayalam"],
        borderwidth=0,
        highlightthickness=0,
        command=back,
        relief="flat",
        cursor="hand2"
        )  
        button_back.place(
        x=45.0,
        y=100.0,
        width=102.09426879882812,
        height=21.0
        )
        button_english.place_forget() 

def select_account_page_view():
    global button_submit,account_dropdown_view
    button_viewacc.destroy()
    button_createacc.destroy()
    button_closeacc.destroy()
    button_mergeacc.destroy()

    if current_language=="english":
        canvas.create_text(
        194.0,
        187.0,
        anchor="nw",
        text="SELECT YOUR ACCOUNT:",
        fill="#631313",
        font=("RobotoRoman SemiBold", 15 * -1),
        tags="select_account_view_text"
        )

        if countacc==3:
            account_options_view = ["Account 1", "Account 2", "Account 3"]
        elif countacc==2:
            account_options_view = ["Account 1", "Account 2"]
        else:
            account_options_view = ["Account 1"]
        account_dropdown_view = Combobox(window,values=account_options_view, state="readonly",cursor="hand2")
        account_dropdown_view.place(x=390.0, y=183.0, width=170.0, height=25.0)
        account_dropdown_view.set("Select Your Account")  # Set a default value

        def submit_account_view():
            selected_account = account_dropdown_view.get()
            if selected_account == "Select Your Account":
                messagebox.showerror("Error", "Please select an account.")
            else:
                view_account_page()

        button_submit = Button(
        image=button_images["button_submit"],
        borderwidth=0,
        highlightthickness=0,
        command=submit_account_view,
        relief="flat",
        cursor="hand2"
        )

        button_submit.place(
        x=421.0,
        y=235.0,
        width=87.02251434326172,
        height=21.0
        )


    else:
        canvas.create_text(
        194.0,
        187.0,
        anchor="nw",
        text="നിങ്ങളുടെ അക്കൗണ്ട് :",
        fill="#631313",
        font=("RobotoRoman SemiBold", 12),
        tags="select_account_view_text"
        )

        
        account_options_view = ["Account 1", "Account 2", "Account 3"]
        account_dropdown_view = Combobox(window,values=account_options_view, state="readonly",cursor="hand2")
        account_dropdown_view.place(x=390.0, y=183.0, width=285.0, height=25.0)
        account_dropdown_view.set("നിങ്ങളുടെ അക്കൗണ്ട് തിരഞ്ഞെടുക്കുക")  # Set a default value

        def submit_account_view():
            selected_account = account_dropdown_view.get()
            if selected_account == "നിങ്ങളുടെ അക്കൗണ്ട് തിരഞ്ഞെടുക്കുക":
                messagebox.showerror("Error", "ദയവായി ഒരു അക്കൗണ്ട് തിരഞ്ഞെടുക്കുക")
            else:
                view_account_page()

        button_submit = Button(
        image=button_images["button_submit_malayalam"],
        borderwidth=0,
        highlightthickness=0,
        command=submit_account_view,
        relief="flat",
        cursor="hand2"
        )

        button_submit.place(
        x=421.0,
        y=235.0,
        width=123.587890625,
        height=21.0
        )

    def back_to_select_account_view():
        canvas.delete("view_account_text")
        select_account_page_view()

    button_back.configure(command=back_to_select_account_view)

    def back_to_account():
        button_submit.destroy()
        canvas.delete("select_account_view_text")
        account_dropdown_view.destroy()
        account_page()
        
    button_back.config(command=back_to_account)

def select_account_page_close():
    global button_submit,account_dropdown_close
    button_viewacc.destroy()
    button_createacc.destroy()
    button_closeacc.destroy()
    button_mergeacc.destroy()

    if current_language=="english":
        canvas.create_text(
        194.0,
        187.0,
        anchor="nw",
        text="SELECT YOUR ACCOUNT:",
        fill="#631313",
        font=("RobotoRoman SemiBold", 15 * -1),
        tags="select_account_close_text"
        )

        if countacc==3:
            account_options_close = ["Account 1", "Account 2", "Account 3"]
        elif countacc==2:
            account_options_close = ["Account 1", "Account 2"]
        else:
            account_options_close = ["Account 1"]
        account_dropdown_close = Combobox(window,values=account_options_close, state="readonly",cursor="hand2")
        account_dropdown_close.place(x=390.0, y=183.0, width=170.0, height=25.0)
        account_dropdown_close.set("Select Your Account")  # Set a default value

        def submit_account_close():
            selected_account = account_dropdown_close.get()
            if selected_account == "Select Your Account":
                messagebox.showerror("Error", "Please select an account.")
            else:
                close_account_page()

        button_submit = Button(
        image=button_images["button_submit"],
        borderwidth=0,
        highlightthickness=0,
        command=submit_account_close,
        relief="flat",
        cursor="hand2"
        )

        button_submit.place(
        x=421.0,
        y=235.0,
        width=87.02251434326172,
        height=21.0
        )


    else:
        canvas.create_text(
        194.0,
        187.0,
        anchor="nw",
        text="നിങ്ങളുടെ അക്കൗണ്ട് :",
        fill="#631313",
        font=("RobotoRoman SemiBold", 12),
        tags="select_account_close_text"
        )

        
        account_options_close = ["Account 1", "Account 2", "Account 3"]
        account_dropdown_close = Combobox(window,values=account_options_close, state="readonly",cursor="hand2")
        account_dropdown_close.place(x=390.0, y=183.0, width=285.0, height=25.0)
        account_dropdown_close.set("നിങ്ങളുടെ അക്കൗണ്ട് തിരഞ്ഞെടുക്കുക")  # Set a default value

        def submit_account_close():
            selected_account = account_dropdown_close.get()
            if selected_account == "നിങ്ങളുടെ അക്കൗണ്ട് തിരഞ്ഞെടുക്കുക":
                messagebox.showerror("Error", "ദയവായി ഒരു അക്കൗണ്ട് തിരഞ്ഞെടുക്കുക")
            else:
                close_account_page()

        button_submit = Button(
        image=button_images["button_submit_malayalam"],
        borderwidth=0,
        highlightthickness=0,
        command=submit_account_close,
        relief="flat",
        cursor="hand2"
        )

        button_submit.place(
        x=421.0,
        y=235.0,
        width=123.587890625,
        height=21.0
        )

    def back_to_select_account_close():
        canvas.delete("close_account_text")
        select_account_page_close()

    button_back.configure(command=back_to_select_account_close)

    def back_to_account():
        button_submit.destroy()
        canvas.delete("select_account_close_text")
        account_dropdown_close.destroy()
        account_page()
        
    button_back.config(command=back_to_account)

def view_account_page():
    button_viewacc.destroy()
    button_createacc.destroy()
    button_closeacc.destroy()
    button_mergeacc.destroy()
    if current_language=="english":
        canvas.create_text(
        177.0,
        161.0,
        anchor="nw",
        text="ACCOUNT NO:",
        fill="#0B694D",
        font=("RobotoRoman Medium", 15 * -1),
        tags="view_account_text"
        )

        canvas.create_text(
            177.0,
            200.0,
            anchor="nw",
            text="ACCOUNT TYPE",
            fill="#0B694D",
            font=("RobotoRoman Medium", 15 * -1),
            tags="view_account_text"
        )

        canvas.create_text(
            177.0,
            239.0,
            anchor="nw",
            text="CUSTOMER NAME:",
            fill="#0B694D",
            font=("RobotoRoman Medium", 15 * -1),
            tags="view_account_text"
        )

        canvas.create_text(
            177.0,
            278.0,
            anchor="nw",
            text="EMAIL:",
            fill="#0B694D",
            font=("RobotoRoman Medium", 15 * -1),
            tags="view_account_text"
        )

        canvas.create_text(
            177.0,
            317.0,
            anchor="nw",
            text="PHONE:",
            fill="#0B694D",
            font=("RobotoRoman Medium", 15 * -1),
            tags="view_account_text"
        )

        canvas.create_text(
            177.0,
            358.0,
            anchor="nw",
            text="BALANCE:",
            fill="#0B694D",
            font=("RobotoRoman Medium", 15 * -1),
            tags="view_account_text"
        )

        balance=databases.dbaccountbalance()
        canvas.create_text(
            372.0,
            160.0,
            anchor="nw",
            text=balance[0][0],
            fill="#631313",
            font=("RobotoRoman Medium", 15 * -1),
            tags="view_account_text"
        )
        balance=databases.dbaccountbalance()
        canvas.create_text(
            370.0,
            199.0,
            anchor="nw",
            text=balance[0][1],
            fill="#631313",
            font=("RobotoRoman Medium", 15 * -1),
            tags="view_account_text"
        )
        fullname = databases.dbfullname()
        canvas.create_text(
            372.0,
            240.0,
            anchor="nw",
            text=fullname,
            fill="#631313",
            font=("RobotoRoman Medium", 15 * -1),
            tags="view_account_text"
        )

        canvas.create_text(
            372.0,
            277.0,
            anchor="nw",
            text="TIRUR",
            fill="#631313",
            font=("RobotoRoman Medium", 15 * -1),
            tags="view_account_text"
        )
        phone=databases.phone()
        canvas.create_text(
            372.0,
            317.0,
            anchor="nw",
            text=phone,
            fill="#631313",
            font=("RobotoRoman Medium", 15 * -1),
            tags="view_account_text"
        )
        balance=databases.dbaccountbalance()
        bal=str(balance[0][2])
        canvas.create_text(
            372.0,
            356.0,
            anchor="nw",
            text=8329492.93,
            fill="#00008b",
            font=("RobotoRoman Medium", 18 * -1),
            tags="view_account_text"
        )



    else:
        canvas.create_text(
        177.0,
        161.0,
        anchor="nw",
        text="അക്കൗണ്ട് നമ്പർ:",
        fill="#0B694D",
        font=("RobotoRoman Medium", 15 * -1),
        tags="view_account_text"
        )

        canvas.create_text(
            177.0,
            200.0,
            anchor="nw",
            text="അക്കൗണ്ട് തരം",
            fill="#0B694D",
            font=("RobotoRoman Medium", 15 * -1),
            tags="view_account_text"
        )

        canvas.create_text(
            177.0,
            239.0,
            anchor="nw",
            text="കസ്റ്റമർ പേര്:",
            fill="#0B694D",
            font=("RobotoRoman Medium", 15 * -1),
            tags="view_account_text"
        )

        canvas.create_text(
            177.0,
            278.0,
            anchor="nw",
            text="ഇമെയിൽ:",
            fill="#0B694D",
            font=("RobotoRoman Medium", 15 * -1),
            tags="view_account_text"
        )

        canvas.create_text(
            177.0,
            317.0,
            anchor="nw",
            text="ഫോൺ:",
            fill="#0B694D",
            font=("RobotoRoman Medium", 15 * -1),
            tags="view_account_text"
        )

        canvas.create_text(
            177.0,
            358.0,
            anchor="nw",
            text="ബാലൻസ്:",
            fill="#0B694D",
            font=("RobotoRoman Medium", 15 * -1),
            tags="view_account_text"
        )

        balance=databases.dbaccountbalance()
        canvas.create_text(
            372.0,
            160.0,
            anchor="nw",
            text=balance[0][0],
            fill="#631313",
            font=("RobotoRoman Medium", 15 * -1),
            tags="view_account_text"
        )
        balance=databases.dbaccountbalance()
        canvas.create_text(
            370.0,
            199.0,
            anchor="nw",
            text=balance[0][1],
            fill="#631313",
            font=("RobotoRoman Medium", 15 * -1),
            tags="view_account_text"
        )
        fullname = databases.dbfullname()
        canvas.create_text(
            372.0,
            240.0,
            anchor="nw",
            text=fullname,
            fill="#631313",
            font=("RobotoRoman Medium", 15 * -1),
            tags="view_account_text"
        )

        canvas.create_text(
            372.0,
            277.0,
            anchor="nw",
            text="തിരൂർ",
            fill="#631313",
            font=("RobotoRoman Medium", 15 * -1),
            tags="view_account_text"
        )
        phone = databases.phone()
        canvas.create_text(
            372.0,
            317.0,
            anchor="nw",
            text=phone,
            fill="#631313",
            font=("RobotoRoman Medium", 15 * -1),
            tags="view_account_text"
        )

        canvas.create_text(
            372.0,
            356.0,
            anchor="nw",
            text="8329492.93",
            fill="#00008b",
            font=("RobotoRoman Medium", 18 * -1),
            tags="view_account_text"
        )


    def back_to_account():
        canvas.delete("view_account_text")
        account_page()

    button_back.configure(command=back_to_account)

def create_account_page():
    button_viewacc.destroy()
    button_createacc.destroy()
    button_closeacc.destroy()
    button_mergeacc.destroy()
    if current_language=="english":

        canvas.create_text(
            177.0,
            161.0,
            anchor="nw",
            text="NAME:",
            fill="#0B694D",
            font=("RobotoRoman Medium", 15 * -1),
            tags="create_account_text"
        )

        canvas.create_text(
            177.0,
            200.0,
            anchor="nw",
            text="ACCOUNT TYPE:",
            fill="#0B694D",
            font=("RobotoRoman Medium", 15 * -1),
            tags="create_account_text"
        )

        canvas.create_text(
            177.0,
            239.0,
            anchor="nw",
            text="AADHAR NUMBER:",
            fill="#0B694D",
            font=("RobotoRoman Medium", 15 * -1),
            tags="create_account_text"
        )

        canvas.create_text(
            177.0,
            278.0,
            anchor="nw",
            text="ADDRESS:",
            fill="#0B694D",
            font=("RobotoRoman Medium", 15 * -1),
            tags="create_account_text"
        )

        canvas.create_text(
            177.0,
            317.0,
            anchor="nw",
            text="PHONE:",
            fill="#0B694D",
            font=("RobotoRoman Medium", 15 * -1),
            tags="create_account_text"
        )

        canvas.create_text(
            177.0,
            356.0,
            anchor="nw",
            text="EMAIL:",
            fill="#0B694D",
            font=("RobotoRoman Medium", 15 * -1),
            tags="create_account_text"
        )

        canvas.create_text(
            177.0,
            395.0,
            anchor="nw",
            text="D.O.B:",
            fill="#0B694D",
            font=("RobotoRoman Medium", 15 * -1),
            tags="create_account_text"
        )

        canvas.create_text(
            177.0,
            434.0,
            anchor="nw",
            text="BRANCH:",
            fill="#0B694D",
            font=("RobotoRoman Medium", 15 * -1),
            tags="create_account_text"
        )

        canvas.create_text(
        278.0,
        103.0,
        anchor="nw",
        text="PLEASE ENTER YOUR DETAILS",
        fill="#631313",
        font=("RobotoRoman SemiBold", 15 * -1),
        tags="create_account_text"
        )
    else:
        canvas.create_text(
        177.0,
        161.0,
        anchor="nw",
        text="പേര്:",
        fill="#0B694D",
        font=("RobotoRoman Medium", 15 * -1),
        tags="create_account_text"
        )

        canvas.create_text(
            177.0,
            200.0,
            anchor="nw",
            text="അക്കൗണ്ട് തരം:",
            fill="#0B694D",
            font=("RobotoRoman Medium", 15 * -1),
            tags="create_account_text"
        )

        canvas.create_text(
            177.0,
            239.0,
            anchor="nw",
            text="ആധാർ നമ്പർ:",
            fill="#0B694D",
            font=("RobotoRoman Medium", 15 * -1),
            tags="create_account_text"
        )

        canvas.create_text(
            177.0,
            278.0,
            anchor="nw",
            text="വിലാസം:",
            fill="#0B694D",
            font=("RobotoRoman Medium", 15 * -1),
            tags="create_account_text"
        )

        canvas.create_text(
            177.0,
            317.0,
            anchor="nw",
            text="ഫോൺ:",
            fill="#0B694D",
            font=("RobotoRoman Medium", 15 * -1),
            tags="create_account_text"
        )

        canvas.create_text(
            177.0,
            356.0,
            anchor="nw",
            text="ഇമെയിൽ:",
            fill="#0B694D",
            font=("RobotoRoman Medium", 15 * -1),
            tags="create_account_text"
        )

        canvas.create_text(
            177.0,
            395.0,
            anchor="nw",
            text="ജനന തിയതി:",
            fill="#0B694D",
            font=("RobotoRoman Medium", 15 * -1),
            tags="create_account_text"
        )

        canvas.create_text(
            177.0,
            434.0,
            anchor="nw",
            text="ബ്രാഞ്ച്:",
            fill="#0B694D",
            font=("RobotoRoman Medium", 15 * -1),
            tags="create_account_text"
        )

        canvas.create_text(
            278.0,
            103.0,
            anchor="nw",
            text="ദയവായി നിങ്ങളുടെ വിവരങ്ങൾ നൽകുക",
            fill="#631313",
            font=("RobotoRoman SemiBold", 15 * -1),
            tags="create_account_text"
        )

    entry_bg_1 = canvas.create_image(
    490.0,
    165.5,
    image=button_images["entry_image"],
    tags="create_account_text"
    )
    entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    cursor="hand2"
    )
    entry_1.place(
    x=350.0,
    y=155.0,
    width=280.0,
    height=19.0
    )

    entry_bg_2 = canvas.create_image(
    490.0,
    205.5,
    image=button_images["entry_image"],
    tags="create_account_text"
    )
    entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    cursor="hand2"
    )
    entry_2.place(
    x=350.0,
    y=195.0,
    width=280.0,
    height=19.0
    )
    entry_bg_3 = canvas.create_image(
        490.0,
        245.5,
        image=button_images["entry_image"],
        tags="create_account_text"
    )
    entry_3 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0,
        cursor="hand2"
    )
    entry_3.place(
        x=350.0,
        y=235.0,
        width=280.0,
        height=19.0
    )

    entry_bg_4 = canvas.create_image(
        490.0,
        284.5,
        image=button_images["entry_image"],
        tags="create_account_text"
    )
    entry_4 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0,
        cursor="hand2"
    )
    entry_4.place(
        x=350.0,
        y=274.0,
        width=280.0,
        height=19.0
    )

    entry_bg_5 = canvas.create_image(
        490.0,
        324.5,
        image=button_images["entry_image"],
        tags="create_account_text"
    )
    entry_5 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0,
        cursor="hand2"
    )
    entry_5.place(
        x=350.0,
        y=314.0,
        width=280.0,
        height=19.0
    )


    entry_bg_6 = canvas.create_image(
        490.0,
        364.5,
        image=button_images["entry_image"],
        tags="create_account_text"
    )
    entry_6 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0,
        cursor="hand2"
    )
    entry_6.place(
        x=350.0,
        y=354.0,
        width=280.0,
        height=19.0
    )


    entry_bg_7 = canvas.create_image(
        490.0,
        404.5,
        image=button_images["entry_image"],
        tags="create_account_text"
    )
    entry_7 =Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0,
        cursor="hand2"
    )
    entry_7.place(
        x=350.0,
        y=394.0,
        width=280.0,
        height=19.0
    )

    entry_bg_8 = canvas.create_image(
        490.0,
        444.5,
        image=button_images["entry_image"],
        tags="create_account_text"
    )
    entry_8 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0,
        readonlybackground="#D9D9D9",
        state="readonly"
    )
    entry_8.place(
        x=350.0,
        y=434.0,
        width=280.0,
        height=19.0
    )
    if current_language=="english":
        locked_text_label = Label(window, text="PERINTHALMANNA", bg="#D9D9D9", fg="#000716")
        locked_text_label.place(x=350.0, y=434.0)
    else:
        locked_text_label = Label(window, text="പെരിന്തൽമണ്ണ", bg="#D9D9D9", fg="#000716")
        locked_text_label.place(x=350.0, y=434.0)



    def validate_name(name):
        # Only allow alphabets, spaces, and hyphens, minimum length 2
        return re.match(r'^[A-Za-z -]{2,}$', name)

    def validate_account_type(account_type):
        # Only allow "Current" or "Saving" (case insensitive)
        return account_type.lower() in ['current', 'saving']

    def validate_aadhar(aadhar):
        # Aadhar should be exactly 12 digits
        return re.match(r'^\d{12}$', aadhar)

    def validate_address(address):
        # Address validation, can be more specific if needed
        return len(address) > 0

    def validate_phone(phone):
        # Phone number should be exactly 10 digits
        return re.match(r'^\d{10}$', phone)

    def validate_email(email):
        # Email format validation
        return re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)

    def validate_dob(dob):
        # DOB should be in the format dd-mm-yyyy
        pattern = r'^\d{1,2}-\d{1,2}-\d{4}$'
        if not re.match(pattern, dob):
            return False
        day, month, year = map(int, dob.split('-'))
        # Basic validation for day, month, and year
        if day < 1 or day > 31 or month < 1 or month > 12 or year < 1900:
            return False
        # Additional validation based on month (can be more specific)
        if month in [4, 6, 9, 11] and day > 30:
            return False
        if month == 2:
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                if day > 29:
                    return False
            elif day > 28:
                return False
        return True


    if current_language=="english":
        def submit_details():
            name = entry_1.get().strip()
            account_type = entry_2.get().strip()
            aadhar = entry_3.get().strip()
            address = entry_4.get().strip()
            phone = entry_5.get().strip()
            email = entry_6.get().strip()
            dob = entry_7.get().strip()

            if not validate_name(name):
                messagebox.showerror("Error", "Invalid Name")
            elif not validate_account_type(account_type):
                messagebox.showerror("Error", "Invalid Account Type")
            elif not validate_aadhar(aadhar):
                messagebox.showerror("Error", "Invalid Aadhar Number")
            elif not validate_address(address):
                messagebox.showerror("Error", "Invalid Address")
            elif not validate_phone(phone):
                messagebox.showerror("Error", "Invalid Phone Number")
            elif not validate_email(email):
                messagebox.showerror("Error", "Invalid Email")
            elif not validate_dob(dob):
                messagebox.showerror("Error", "Invalid Date of Birth")
            else:
                # If all validations pass, proceed with submission
                entry_1.delete(0, tk.END)
                entry_2.delete(0, tk.END)
                entry_3.delete(0, tk.END)
                entry_4.delete(0, tk.END)
                entry_5.delete(0, tk.END)
                entry_6.delete(0, tk.END)
                entry_7.delete(0, tk.END)
                entry_8.delete(0, tk.END)
                # Delete other entry fields and submit details
                messagebox.showinfo("Success", "Details Submitted Successfully")
                canvas.destroy()
                home_page()
        button_submit = Button(
        image=button_images["button_submit"],
        borderwidth=0,
        highlightthickness=0,
        command=submit_details,
        relief="flat",
        cursor="hand2"
        )

        button_submit.place(
        x=450.0,
        y=486.0,
        width=87.02251434326172,
        height=21.0
        ) 
    else:
        def submit_details():
            name = entry_1.get().strip()
            account_type = entry_2.get().strip()
            aadhar = entry_3.get().strip()
            address = entry_4.get().strip()
            phone = entry_5.get().strip()
            email = entry_6.get().strip()
            dob = entry_7.get().strip()

            if not validate_name(name):
                messagebox.showerror("Error", "അസാധുവായ പേര്")
            elif not validate_account_type(account_type):
                messagebox.showerror("Error", "അസാധുവായ അക്കൗണ്ട് തരം")
            elif not validate_aadhar(aadhar):
                messagebox.showerror("Error", "അസാധുവായ ആധാർ നമ്പർ")
            elif not validate_address(address):
                messagebox.showerror("Error", "അസാധുവായ വിലാസം")
            elif not validate_phone(phone):
                messagebox.showerror("Error", "അസാധുവായ ഫോൺ നമ്പർ")
            elif not validate_email(email):
                messagebox.showerror("Error", "അസാധുവായ ഇമെയിൽ")
            elif not validate_dob(dob):
                messagebox.showerror("Error", "അസാധുവായ ജനന തിയതി")
            else:
                # If all validations pass, proceed with submission
                entry_1.delete(0, tk.END)
                entry_2.delete(0, tk.END)
                entry_3.delete(0, tk.END)
                entry_4.delete(0, tk.END)
                entry_5.delete(0, tk.END)
                entry_6.delete(0, tk.END)
                entry_7.delete(0, tk.END)
                entry_8.delete(0, tk.END)
                # Delete other entry fields and submit details
                messagebox.showinfo("Success", "വിവരങ്ങൾ വിജയകരമായി സമർപ്പിച്ചു")
                canvas.destroy()
                home_page()
        button_submit = Button(
        image=button_images["button_submit_malayalam"],
        borderwidth=0,
        highlightthickness=0,
        command=submit_details,
        relief="flat",
        cursor="hand2"
        )

        button_submit.place(
        x=450.0,
        y=486.0,
        width=123.587890625,
        height=21.0
        ) 
    
    def back_createpage_to_accountpage():
        canvas.delete("create_account_text")
        button_submit.destroy()
        locked_text_label.destroy()
        entry_1.destroy()
        entry_2.destroy()
        entry_3.destroy()
        entry_4.destroy()
        entry_5.destroy()
        entry_6.destroy()
        entry_7.destroy()
        entry_8.destroy()
        account_page()

    button_back.config(command=back_createpage_to_accountpage)


def close_account_page():
    button_viewacc.destroy()
    button_createacc.destroy()
    button_closeacc.destroy()
    button_mergeacc.destroy()

    if current_language=="english":
        canvas.create_text(
        174.0,
        173.0,
        anchor="nw",
        text="REASON FOR CLOSING:",
        fill="#631313",
        font=("RobotoRoman SemiBold", 15 * -1),
        tags="close_account_text"
        )

        selected_reason = IntVar()

        radio_button_style = Style()
        radio_button_style.configure(
            'TRadiobutton',
            background='#FFFFFF',
            foreground='#000000',
            padding=(10, 5),
            font=('Helvetica', 12)
        )

        def handle_other_selection():
            if selected_reason.get() == 4:
                text_description.config(state='normal', bg='#EFEFEF')
            else:
                text_description.config(state='disabled', bg='#D9D9D9')



        radio_button_1 = Radiobutton(
            window,
            text="Unsatisfied",
            value=1,
            variable=selected_reason,
            style='TRadiobutton',
            command=handle_other_selection,
            cursor="hand2"
        )
        radio_button_1.place(x=355, y=167)

        radio_button_2 = Radiobutton(
            window,
            text="Procedures are difficult",
            value=2,
            variable=selected_reason,
            style='TRadiobutton',
            command=handle_other_selection,
            cursor="hand2"
        )
        radio_button_2.place(x=355, y=207)

        radio_button_3 = Radiobutton(
            window,
            text="Bank is crowded",
            value=3,
            variable=selected_reason,
            style='TRadiobutton',
            command=handle_other_selection,
            cursor="hand2"
        )
        radio_button_3.place(x=355, y=247)

        radio_button_4 = Radiobutton(
            window,
            text="Other(Please Specify:)",
            value=4,
            variable=selected_reason,
            style='TRadiobutton',
            command=handle_other_selection,
            cursor="hand2"
        )
        radio_button_4.place(x=355, y=287)

        text_description = Text(window,height=2, width=30, wrap='word',state='disabled',bg='#D9D9D9')
        text_description.place(x=385, y=317)

        def submit_close():
            if selected_reason.get() == 0:
                messagebox.showerror("Error", "Please select a reason for closing.")
            elif selected_reason.get() == 4 and len(text_description.get("1.0", "end-1c")) == 0:
                messagebox.showerror("Error", "Please specify the reason for closing.")    
            else:
                messagebox.showinfo("Success", "Request for Closing Submitted")
                canvas.delete("close_account_text")
                radio_button_1.destroy()
                radio_button_2.destroy()
                radio_button_3.destroy()
                radio_button_4.destroy()
                text_description.destroy()
                home_page()

        button_submit = Button(
            image=button_images["button_submit"],
            borderwidth=0,
            highlightthickness=0,
            command=submit_close,
            relief="flat",
            cursor="hand2"
        )

        button_submit.place(x=450.0,
                            y=370.0,
                            width=87.02251434326172,
                            height=21.0
                            )
    else:
        canvas.create_text(
        174.0,
        173.0,
        anchor="nw",
        text="എന്താണ് കാരണം:",
        fill="#631313",
        font=("RobotoRoman SemiBold", 15 * -1),
        tags="close_account_text"
        )

        selected_reason = IntVar()

        radio_button_style = Style()
        radio_button_style.configure(
            'TRadiobutton',
            background='#FFFFFF',
            foreground='#000000',
            padding=(10, 5),
            font=('Helvetica', 12)
        )

        def handle_other_selection():
            if selected_reason.get() == 4:  #
                text_description.config(state='normal', bg='#EFEFEF')
            else:
                text_description.config(state='disabled', bg='#D9D9D9')

        radio_button_1 = Radiobutton(
            window,
            text="അസംതൃപ്തികരമായിരിക്കുന്നു",
            value=1,
            variable=selected_reason,
            style='TRadiobutton',
            command=handle_other_selection,
            cursor="hand2"
        )
        radio_button_1.place(x=355, y=167)

        radio_button_2 = Radiobutton(
            window,
            text="നിയമനങ്ങൾ കഠിനമാണ്",
            value=2,
            variable=selected_reason,
            style='TRadiobutton',
            command=handle_other_selection,
            cursor="hand2"
        )
        radio_button_2.place(x=355, y=207)

        radio_button_3 = Radiobutton(
            window,
            text="ബാങ്ക് സന്ദർശിക്കാൻ വലിയ പ്രശ്നം",
            value=3,
            variable=selected_reason,
            style='TRadiobutton',
            command=handle_other_selection,
            cursor="hand2"
        )
        radio_button_3.place(x=355, y=247)

        radio_button_4 = Radiobutton(
            window,
            text="മറ്റ് (ദയവായി വിശദീകരിക്കുക:)",
            value=4,
            variable=selected_reason,
            style='TRadiobutton',
            command=handle_other_selection,
            cursor="hand2"
        )
        radio_button_4.place(x=355, y=287)

        text_description = Text(window,height=2, width=30, wrap='word',state='disabled',bg='#D9D9D9')
        text_description.place(x=385, y=317)

        def submit_close():
            if selected_reason.get() == 0:
                messagebox.showerror("Error", "അക്കൗണ്ട് അടയ്ക്കാൻ ഒരു കാരണം തിരഞ്ഞെടുക്കുക.")
            elif selected_reason.get() == 4 and len(text_description.get("1.0", "end-1c")) == 0:
                messagebox.showerror("Error", "അക്കൗണ്ട് അടയ്ക്കൽക്കാരണം നിരവധിക്കുകുക.")
            else:
                messagebox.showinfo("Success", "അടയ്ക്കൽക്കാരണം അഭ്യർത്ഥിച്ചു")
                canvas.delete("close_account_text")
                radio_button_1.destroy()
                radio_button_2.destroy()
                radio_button_3.destroy()
                radio_button_4.destroy()
                text_description.destroy()
                home_page()


        button_submit = Button(
            image=button_images["button_submit_malayalam"],
            borderwidth=0,
            highlightthickness=0,
            command=submit_close,
            relief="flat",
            cursor="hand2"
        )

        button_submit.place( x=450.0,
        y=370.0,
        width=123.587890625,
        height=21.0
        )

    def back_to_account_close():
        canvas.delete("close_account_text")
        radio_button_1.destroy()
        radio_button_2.destroy()
        radio_button_3.destroy()
        radio_button_4.destroy()
        text_description.destroy()
        button_submit.destroy()
        account_page()

    button_back.config(command=back_to_account_close)

def merge_account_page():
    button_viewacc.destroy()
    button_createacc.destroy()
    button_closeacc.destroy()
    button_mergeacc.destroy()

    if current_language=="english":
        canvas.create_text(
        184.0,
        158.0,
        anchor="nw",
        text="CHOOSE ACCOUNT 1:",
        fill="#631313",
        font=("RobotoRoman SemiBold", 15 * -1),
        tags="merge_account_text"
        )

        canvas.create_text(
        184.0,
        245.0,
        anchor="nw",
        text="CHOOSE ACCOUNT 2:",
        fill="#631313",
        font=("RobotoRoman SemiBold", 15 * -1),
        tags="merge_account_text"
        )

        account_options = ["Account 1", "Account 2", "Account 3"]

        account_1_dropdown = Combobox(window,values=account_options, state="readonly",cursor="hand2")
        account_1_dropdown.place(x=360.0, y=155.0, width=170.0, height=25.0)
        account_1_dropdown.set("Select Account")  # Set a default value

        account_2_dropdown = Combobox(window,values=account_options, state="readonly",cursor="hand2")
        account_2_dropdown.place(x=360.0, y=240.0, width=170.0, height=25.0)
        account_2_dropdown.set("Select Account")  # Set a default value

        def submit_merge():
            account_1 = account_1_dropdown.get()
            account_2 = account_2_dropdown.get()

            if account_1 == "Select Account" or account_2 == "Select Account":
                messagebox.showerror("Error", "Please select both accounts.")
            else:
                messagebox.showinfo("Success", "Accounts Merged Successfully")
                canvas.delete("merge_account_text")
                account_1_dropdown.destroy()
                account_2_dropdown.destroy()
                home_page()

        button_submit = Button(
        image=button_images["button_submit"],
        borderwidth=0,
        highlightthickness=0,
        command=submit_merge,
        relief="flat",
        cursor="hand2"
        )

        
        button_submit.place(
        x=400.0,
        y=289.0,
        width=87.02251434326172,
        height=21.0
        )

    else:
        canvas.create_text(
        184.0,
        158.0,
        anchor="nw",
        text="അക്കൗണ്ട് 1 :",
        fill="#631313",
        font=("RobotoRoman SemiBold", 15 * -1),
        tags="merge_account_text"
        )

        canvas.create_text(
            184.0,
            245.0,
            anchor="nw",
            text="അക്കൗണ്ട് 2 :",
            fill="#631313",
            font=("RobotoRoman SemiBold", 15 * -1),
            tags="merge_account_text"
        )

        account_options = ["അക്കൗണ്ട് 1", "അക്കൗണ്ട് 2", "അക്കൗണ്ട് 3"]

        account_1_dropdown = Combobox(window, values=account_options, state="readonly", cursor="hand2")
        account_1_dropdown.place(x=360.0, y=155.0, width=285.0, height=25.0)
        account_1_dropdown.set("അക്കൗണ്ട് തിരഞ്ഞെടുക്കുക")  # ഒരു ഡിഫോൾട്ട് മൂല്യം സജ്ജീകരിക്കുക

        account_2_dropdown = Combobox(window, values=account_options, state="readonly", cursor="hand2")
        account_2_dropdown.place(x=360.0, y=240.0, width=285.0, height=25.0)
        account_2_dropdown.set("അക്കൗണ്ട് തിരഞ്ഞെടുക്കുക")  # ഒരു ഡിഫോൾട്ട് മൂല്യം സജ്ജീകരിക്കുക

        def submit_merge():
            account_1 = account_1_dropdown.get()
            account_2 = account_2_dropdown.get()

            if account_1 == "അക്കൗണ്ട് തിരഞ്ഞെടുക്കുക" or account_2 == "അക്കൗണ്ട് തിരഞ്ഞെടുക്കുക":
                messagebox.showerror("Error", "ദയവായി രണ്ടു അക്കൗണ്ടുകൾ തിരഞ്ഞെടുക്കുക.")
            else:
                messagebox.showinfo("Success", "അക്കൗണ്ടുകൾ വിജയകരമായി ഒപ്പം ചേർത്തു")
                canvas.delete("merge_account_text")
                account_1_dropdown.destroy()
                account_2_dropdown.destroy()
                home_page()
        button_submit = Button(
        image=button_images["button_submit_malayalam"],
        borderwidth=0,
        highlightthickness=0,
        command=submit_merge,
        relief="flat",
        cursor="hand2"
        )

        
        button_submit.place(
        x=400.0,
        y=289.0,
        width=123.587890625,
        height=21.0
        )

    def back_mergepage_to_accpage():
        canvas.delete("merge_account_text")
        account_1_dropdown.destroy()
        account_2_dropdown.destroy()
        button_submit.destroy()
        account_page()

    button_back.config(command=back_mergepage_to_accpage)

def card_page():
    button_account.destroy()
    button_card.destroy()
    button_faq.destroy()
    button_moneytransfer.destroy()
    button_notifications.destroy()
    button_signout.place(x=454.0, y=30.0, width=122.14286041259766, height=20.0)

    def back_card_to_home():
        canvas.delete("card_text")
        account_dropdown.destroy()
        card_dropdown.destroy()
        button_submit.destroy()
        home_page()

    if current_language=="english":
        canvas.create_text(
        194.0,
        187.0,
        anchor="nw",
        text="SELECT YOUR ACCOUNT:",
        fill="#631313",
        font=("RobotoRoman SemiBold", 15 * -1),
        tags="card_text"
        )

        canvas.create_text(
            194.0,
            233.0,
            anchor="nw",
            text="CHOOSE TYPE OF CARD:",
            fill="#631313",
            font=("RobotoRoman SemiBold", 15 * -1),
            tags="card_text"
        )

        account_options = ["Account 1", "Account 2", "Account 3"]
        card_options = ["Debit", "Credit"]

        account_dropdown = Combobox(window,values=account_options, state="readonly",cursor="hand2")
        account_dropdown.place(x=390.0, y=183.0, width=170.0, height=25.0)
        account_dropdown.set("Select Account")


        card_dropdown = Combobox(window,values=card_options, state="readonly",cursor="hand2")
        card_dropdown.place(x=390.0, y=230.0, width=170.0, height=25.0)
        card_dropdown.set("Select Type of Card")

        def submit_card():
            account = account_dropdown.get()
            card_type = card_dropdown.get()

            if account == "Select Account" or card_type == "Select Type of Card":
                messagebox.showerror("Error", "Please select both account and card type.")
            else:
                messagebox.showinfo("Success", "Request For ATM Card Submitted")
                canvas.delete("card_text")
                account_dropdown.destroy()
                card_dropdown.destroy()
                button_submit.destroy()
                home_page()

        button_submit = Button(
        image=button_images["button_submit"],
        borderwidth=0,
        highlightthickness=0,
        command=submit_card,
        relief="flat",
        cursor="hand2"
        )
        button_submit.place(
        x=422.0,
        y=275.0,
        width=87.02251434326172,
        height=21.0
        )

        button_back = Button(
        image=button_images["button_back"],
        borderwidth=0,
        highlightthickness=0,
        command=back_card_to_home,
        relief="flat",
        cursor="hand2"
        )  
        button_back.place(
        x=63.11627197265625,
        y=100.0,
        width=72.5931396484375,
        height=21.0
        )
        button_malayalam.place_forget() 
    else:
        canvas.create_text(
        194.0,
        187.0,
        anchor="nw",
        text="നിങ്ങളുടെ അക്കൗണ്ട്:",
        fill="#631313",
        font=("RobotoRoman SemiBold", 15 * -1),
        tags="card_text"
        )

        canvas.create_text(
            194.0,
            233.0,
            anchor="nw",
            text="കാർഡിന്റെ തരം :",
            fill="#631313",
            font=("RobotoRoman SemiBold", 15 * -1),
            tags="card_text"
        )

        account_options = ["അക്കൗണ്ട് 1", "അക്കൗണ്ട് 2", "അക്കൗണ്ട് 3"]
        card_options = ["ഡെബിറ്റ്", "ക്രെഡിറ്റ്"]

        account_dropdown = Combobox(window, values=account_options, state="readonly", cursor="hand2")
        account_dropdown.place(x=390.0, y=183.0, width=280.0, height=25.0)
        account_dropdown.set("അക്കൗണ്ട് തിരഞ്ഞെടുക്കുക")


        card_dropdown = Combobox(window, values=card_options, state="readonly", cursor="hand2")
        card_dropdown.place(x=390.0, y=230.0, width=280.0, height=25.0)
        card_dropdown.set("കാർഡിന്റെ തരം തിരഞ്ഞെടുക്കുക")

        def submit_card():
            account = account_dropdown.get()
            card_type = card_dropdown.get()

            if account == "അക്കൗണ്ട് തിരഞ്ഞെടുക്കുക" or card_type == "കാർഡിന്റെ തരം തിരഞ്ഞെടുക്കുക":
                messagebox.showerror("Error", "ദയവായി അക്കൗണ്ടും കാർഡിന്റെ തരം രണ്ടും തിരഞ്ഞെടുക്കുക.")
            else:
                messagebox.showinfo("Success", "എട്ടിഎം കാർഡിന് അഭ്യർത്ഥന സമർപ്പിച്ചു")
                canvas.delete("card_text")
                account_dropdown.destroy()
                card_dropdown.destroy()
                button_submit.destroy()
                home_page()

        button_submit = Button(
            image=button_images["button_submit_malayalam"],
            borderwidth=0,
            highlightthickness=0,
            command=submit_card,
            relief="flat",
            cursor="hand2"
        )
        button_submit.place(
            x=422.0,
            y=275.0,
            width=123.587890625,
            height=21.0
        )
        button_back = Button(
        image=button_images["button_back_malayalam"],
        borderwidth=0,
        highlightthickness=0,
        command=back_card_to_home,
        relief="flat",
        cursor="hand2"
        )  
        button_back.place(
        x=45.0,
        y=100.0,
        width=102.09426879882812,
        height=21.0
        ) 
        button_english.place_forget()
def money_transfer_page():
    button_account.destroy()
    button_card.destroy()
    button_faq.destroy()
    button_moneytransfer.destroy()
    button_notifications.destroy()
    button_signout.place(x=454.0, y=30.0, width=122.14286041259766, height=20.0)

    def back_moneytransfer_to_home():
        canvas.delete("money_transfer_text")
        button_submit.destroy()
        entry_1.destroy()
        entry_2.destroy()
        entry_3.destroy()
        entry_4.destroy()
        entry_5.destroy()
        home_page()
    
    if current_language=="english":
        canvas.create_text(
        278.0,
        103.0,
        anchor="nw",
        text="ENTER RECIPIENT DETAILS",
        fill="#631313",
        font=("RobotoRoman SemiBold", 15 * -1)
        )

        canvas.create_text(
            181.0,
            161.0,
            anchor="nw",
            text="ACCOUNT NUMBER:",
            fill="#0B694D",
            font=("RobotoRoman Medium", 15 * -1),
            tags="money_transfer_text"
        )

        canvas.create_text(
            99.0,
            201.0,
            anchor="nw",
            text="RE-ENTER ACCOUNT NUMBER:",
            fill="#0B694D",
            font=("RobotoRoman Medium", 15 * -1),
            tags="money_transfer_text"
        )

        canvas.create_text(
            181.0,
            241.0,
            anchor="nw",
            text="IFSC CODE:",
            fill="#0B694D",
            font=("RobotoRoman Medium", 15 * -1),
            tags="money_transfer_text"
        )

        canvas.create_text(
            181.0,
            281.0,
            anchor="nw",
            text="RECIPIENT NAME:",
            fill="#0B694D",
            font=("RobotoRoman Medium", 15 * -1),
            tags="money_transfer_text"
        )

        canvas.create_text(
            181.0,
            320.0,
            anchor="nw",
            text="AMOUNT:",
            fill="#0B694D",
            font=("RobotoRoman Medium", 15 * -1),
            tags="money_transfer_text"
        )

        button_back = Button(
        image=button_images["button_back"],
        borderwidth=0,
        highlightthickness=0,
        command=back_moneytransfer_to_home,
        relief="flat",
        cursor="hand2"
        )  
        button_back.place(
        x=63.11627197265625,
        y=100.0,
        width=72.5931396484375,
        height=21.0
        )
        button_malayalam.place_forget()
    else:
        canvas.create_text(
        278.0,
        103.0,
        anchor="nw",
        text="സ്വീകരിക്കുന്നവരുടെ വിവരങ്ങൾ നൽകുക",
        fill="#631313",
        font=("RobotoRoman SemiBold", 15 * -1)
        )

        canvas.create_text(
            181.0,
            161.0,
            anchor="nw",
            text="അക്കൗണ്ട് നമ്പർ:",
            fill="#0B694D",
            font=("RobotoRoman Medium", 15 * -1),
            tags="money_transfer_text"
        )

        canvas.create_text(
            58.0,
            201.0,
            anchor="nw",
            text="അക്കൗണ്ട് നമ്പർ വീണ്ടും നൽകുക:",
            fill="#0B694D",
            font=("RobotoRoman Medium", 15 * -1),
            tags="money_transfer_text"
        )

        canvas.create_text(
            181.0,
            241.0,
            anchor="nw",
            text="IFSC കോഡ്:",
            fill="#0B694D",
            font=("RobotoRoman Medium", 15 * -1),
            tags="money_transfer_text"
        )

        canvas.create_text(
            118.0,
            281.0,
            anchor="nw",
            text="സ്വീകരിക്കുന്നവരുടെ പേര്:",
            fill="#0B694D",
            font=("RobotoRoman Medium", 15 * -1),
            tags="money_transfer_text"
        )

        canvas.create_text(
            181.0,
            320.0,
            anchor="nw",
            text="തുക:",
            fill="#0B694D",
            font=("RobotoRoman Medium", 15 * -1),
            tags="money_transfer_text"
        )

        button_back = Button(
            image=button_images["button_back_malayalam"],
            borderwidth=0,
            highlightthickness=0,
            command=back_moneytransfer_to_home,
            relief="flat",
            cursor="hand2"
        )  
        button_back.place(
            x=45.0,
            y=100.0,
            width=102.09426879882812,
            height=21.0
        )
        button_english.place_forget()


    entry_bg_1 = canvas.create_image(
    490.0,
    171.5,
    image=button_images["entry_image"],
    tags="money_transfer_text"
    )
    entry_1 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0,
        cursor="hand2"
    )
    entry_1.place(
        x=350.0,
        y=161.0,
        width=280.0,
        height=19.0
    )

    entry_bg_2 = canvas.create_image(
    490.0,
    211.5,
    image=button_images["entry_image"],
    tags="money_transfer_text"
    )
    entry_2 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0,
        cursor="hand2"
    )
    entry_2.place(
    x=350.0,
    y=201.0,
    width=280.0,
    height=19.0
    )

    entry_bg_3 = canvas.create_image(
    490.0,
    251.5,
    image=button_images["entry_image"],
    tags="money_transfer_text"
    )
    entry_3 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0,
        cursor="hand2"
    )
    entry_3.place(
    x=350.0,
    y=241.0,
    width=280.0,
    height=19.0
    )

    entry_bg_4 = canvas.create_image(
    490.0,
    291.5,
    image=button_images["entry_image"],
    tags="money_transfer_text"
    )
    entry_4 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0,
        cursor="hand2"
    )
    entry_4.place(
    x=350.0,
    y=281.0,
    width=280.0,
    height=19.0
    )

    entry_bg_5 = canvas.create_image(
    490.0,
    331.5,
    image=button_images["entry_image"],
    tags="money_transfer_text"
    )
    entry_5 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0,
        cursor="hand2"
    )
    entry_5.place(
    x=350.0,
    y=321.0,
    width=280.0,
    height=19.0
    )

    

    def validate_account_number(account_number):
    # Account number should be exactly 17 digits
        return re.match(r'^\d{17}$', account_number)

    def validate_ifsc_code(ifsc_code):
        # IFSC code should have 4 letters followed by 0, and then 6 digits
        return re.match(r'^[A-Z]{4}0\d{6}$', ifsc_code)

    def validate_recipient_name(recipient_name):
        # Recipient name should not be empty
        return len(recipient_name.strip()) > 0

    def validate_amount(amount):
        # Amount should be any positive number
        try:
            amount = float(amount)
            return amount > 0
        except ValueError:
            return False
        
    if current_language=="english":
        def submit_money_transfer():
            account_number = entry_1.get().strip()
            re_enter_account_number = entry_2.get().strip()
            ifsc_code = entry_3.get().strip()
            recipient_name = entry_4.get().strip()
            amount = entry_5.get().strip()

            if not validate_account_number(account_number):
                messagebox.showerror("Error", "Invalid Account Number")
            elif account_number != re_enter_account_number:
                messagebox.showerror("Error", "Account numbers do not match")
            elif not validate_ifsc_code(ifsc_code):
                messagebox.showerror("Error", "Invalid IFSC Code")
            elif not recipient_name:
                messagebox.showerror("Error", "Recipient name cannot be empty")
            elif not amount:
                messagebox.showerror("Error", "Amount cannot be empty")
            else:
                # If all validations pass, proceed with money transfer
                messagebox.showinfo("Success", "Money Transferred Successfully")
                canvas.delete("money_transfer_text")
                button_submit.destroy()
                entry_1.destroy()
                entry_2.destroy()
                entry_3.destroy()
                entry_4.destroy()
                entry_5.destroy()
                home_page()

        button_submit = Button(
        image=button_images["button_submit"],
        borderwidth=0,
        highlightthickness=0,
        command=submit_money_transfer,
        relief="flat",
        cursor="hand2"
        )
        button_submit.place(
        x=441.0,
        y=369.0,
        width=87.02251434326172,
        height=21.0
        )

    else:   
        def submit_money_transfer():
            account_number = entry_1.get().strip()
            re_enter_account_number = entry_2.get().strip()
            ifsc_code = entry_3.get().strip()
            recipient_name = entry_4.get().strip()
            amount = entry_5.get().strip()

            if not validate_account_number(account_number):
                messagebox.showerror("Error", "അസാധുവായ അക്കൗണ്ട് നമ്പർ")
            elif account_number != re_enter_account_number:
                messagebox.showerror("Error", "അക്കൗണ്ട് നമ്പർ തിരിച്ചു നൽകുന്നത് അസാധുവാകുന്നു")
            elif not validate_ifsc_code(ifsc_code):
                messagebox.showerror("Error", "അസാധുവായ IFSC കോഡ്")
            elif not recipient_name:
                messagebox.showerror("Error", "സ്വീകരിക്കുന്നവരുടെ പേര് ശൂന്യമാകരുത്")
            elif not amount:
                messagebox.showerror("Error", "തുക ശൂന്യമാകരുത്")
            else:
                # എല്ലാ പരിശോധനകൾക്കും പാസായാൽ, പണം അന്തരിപ്പിക്കൽ തുടങ്ങുക
                messagebox.showinfo("Success", "പണം വിജയകരമായി അന്തരിപ്പിക്കപ്പെട്ടു")
                canvas.delete("money_transfer_text")
                button_submit.destroy()
                entry_1.destroy()
                entry_2.destroy()
                entry_3.destroy()
                entry_4.destroy()
                entry_5.destroy()
                home_page()

        button_submit = Button(
            image=button_images["button_submit_malayalam"],
            borderwidth=0,
            highlightthickness=0,
            command=submit_money_transfer,
            relief="flat",
            cursor="hand2"
        )
        button_submit.place(
            x=441.0,
            y=369.0,
            width=123.587890625,
            height=21.0
        )

def faq_page():
    button_account.destroy()
    button_card.destroy()
    button_faq.destroy()
    button_moneytransfer.destroy()
    button_notifications.destroy()
    button_signout.place(x=454.0, y=30.0, width=122.14286041259766, height=20.0)

    def back_faq_to_home():
        canvas.delete("faq_text")
        home_page()

    if current_language=="english":
        canvas.create_text(
        87.0,
        176.0,
        anchor="nw",
        text="1.Is this a Shariah-complaint Bank?",
        fill="#0B694D",
        font=("RobotoRoman Medium", 16 * -1),
        tags="faq_text"
        )

        canvas.create_text(
        87.0,
        265.0,
        anchor="nw",
        text="2.Does this bank accept or give Interest?",
        fill="#0B694D",
        font=("RobotoRoman Medium", 16 * -1),
        tags="faq_text"
        )

        canvas.create_text(
        87.0,
        334.0,
        anchor="nw",
        text="3.Can I get a interest free loan?",
        fill="#0B694D",
        font=("RobotoRoman Medium", 16 * -1),
        tags="faq_text"
        )

        canvas.create_text(
        87.0,
        421.0,
        anchor="nw",
        text="4.Why all features of Sharia-Complaint bank are not available?",
        fill="#0B694D",
        font=("RobotoRoman Medium", 16 * -1),
        tags="faq_text"
        )

        canvas.create_text(
        87.0,
        203.0,
        anchor="nw",
        text="Ans:Yes, this is a Sharia-complaint bank, the bank operations are in accordance with",
        fill="#631313",
        font=("RobotoRoman Medium", 15 * -1),
        tags="faq_text"
        )

        canvas.create_text(
        117.0,
        227.0,
        anchor="nw",
        text="the principles of Shariah",
        fill="#631313",
        font=("RobotoRoman Medium", 15 * -1),
        tags="faq_text"
        )

        canvas.create_text(
        87.0,
        292.0,
        anchor="nw",
        text="Ans:No,we do not accept or give Interest.All operations are 100% interest free.",
        fill="#631313",
        font=("RobotoRoman Medium", 15 * -1),
        tags="faq_text"
        )

        canvas.create_text(
        87.0,
        361.0,
        anchor="nw",
        text="Ans:Yes you can get a interest free loan in bank,but that feature is currently unavailable",
        fill="#631313",
        font=("RobotoRoman Medium", 15 * -1),
        tags="faq_text"
        )

        canvas.create_text(
        117.0,
        385.0,
        anchor="nw",
        text="in this application",
        fill="#631313",
        font=("RobotoRoman Medium", 15 * -1),
        tags="faq_text"
        )

        canvas.create_text(
        87.0,
        448.0,
        anchor="nw",
        text="Ans:Full features will be added in the future.The basic features are available in this application",
        fill="#631313",
        font=("RobotoRoman Medium", 15 * -1),
        tags="faq_text"
        )

        canvas.create_text(
        237.0,
        104.0,
        anchor="nw",
        text="Frequently Asked Questions",
        fill="#631313",
        font=("RobotoRoman Medium", 20 * -1),
        tags="faq_text"
        )
        button_back = Button(
        image=button_images["button_back"],
        borderwidth=0,
        highlightthickness=0,
        command=back_faq_to_home,
        relief="flat",
        cursor="hand2"
        )  
        button_back.place(
        x=63.11627197265625,
        y=100.0,
        width=72.5931396484375,
        height=21.0
        ) 
        button_malayalam.place_forget()
    else:
        canvas.create_text(
        87.0,
        176.0,
        anchor="nw",
        text="1.Is this a Shariah-complaint Bank?",
        fill="#0B694D",
        font=("RobotoRoman Medium", 16 * -1),
        tags="faq_text"
        )
        canvas.create_text(
        87.0,
        265.0,
        anchor="nw",
        text="2.Does this bank accept or give Interest?",
        fill="#0B694D",
        font=("RobotoRoman Medium", 16 * -1),
        tags="faq_text"
        )

        canvas.create_text(
        87.0,
        334.0,
        anchor="nw",
        text="3.Can I get a interest free loan?",
        fill="#0B694D",
        font=("RobotoRoman Medium", 16 * -1),
        tags="faq_text"
        )

        canvas.create_text(
        87.0,
        421.0,
        anchor="nw",
        text="4.Why all features of Sharia-Complaint bank are not available?",
        fill="#0B694D",
        font=("RobotoRoman Medium", 16 * -1),
        tags="faq_text"
        )

        canvas.create_text(
        87.0,
        203.0,
        anchor="nw",
        text="Ans:Yes, this is a Sharia-complaint bank, the bank operations are in accordance with",
        fill="#631313",
        font=("RobotoRoman Medium", 15 * -1),
        tags="faq_text"
        )

        canvas.create_text(
        117.0,
        227.0,
        anchor="nw",
        text="the principles of Shariah",
        fill="#631313",
        font=("RobotoRoman Medium", 15 * -1),
        tags="faq_text"
        )

        canvas.create_text(
        87.0,
        292.0,
        anchor="nw",
        text="Ans:No,we do not accept or give Interest.All operations are 100% interest free.",
        fill="#631313",
        font=("RobotoRoman Medium", 15 * -1),
        tags="faq_text"
        )

        canvas.create_text(
        87.0,
        361.0,
        anchor="nw",
        text="Ans:Yes you can get a interest free loan in bank,but that feature is currently unavailable",
        fill="#631313",
        font=("RobotoRoman Medium", 15 * -1),
        tags="faq_text"
        )

        canvas.create_text(
        117.0,
        385.0,
        anchor="nw",
        text="in this application",
        fill="#631313",
        font=("RobotoRoman Medium", 15 * -1),
        tags="faq_text"
        )

        canvas.create_text(
        87.0,
        448.0,
        anchor="nw",
        text="Ans:Full features will be added in the future.The basic features are available in this application",
        fill="#631313",
        font=("RobotoRoman Medium", 15 * -1),
        tags="faq_text"
        )

        canvas.create_text(
        237.0,
        104.0,
        anchor="nw",
        text="പതിവായി ചോദിക്കുന്ന ചോദ്യങ്ങൾ",
        fill="#631313",
        font=("RobotoRoman Medium", 20 * -1),
        tags="faq_text"
        )
        button_back = Button(
        image=button_images["button_back_malayalam"],
        borderwidth=0,
        highlightthickness=0,
        command=back_faq_to_home,
        relief="flat",
        cursor="hand2"
        )  
        button_back.place(
        x=63.11627197265625,
        y=100.0,
        width=102.09426879882812,
        height=21.0
        )
        button_english.place_forget()

def notifications_page():
    button_account.destroy()
    button_card.destroy()
    button_faq.destroy()
    button_moneytransfer.destroy()
    button_notifications.destroy()
    button_signout.place(x=454.0, y=30.0, width=122.14286041259766, height=20.0)

    notification_image_1 = canvas.create_image(
    358.0,
    191.0,
    image=button_images["notifications_image"],
    tags="notifications_text"
    )

    notification_image_2 = canvas.create_image(
    356.0,
    284.0,
    image=button_images["notifications_image"],
    tags="notifications_text"
    )

    notification_image_3 = canvas.create_image(
    358.0,
    384.0,
    image=button_images["notifications_image"],
    tags="notifications_text"
    )

    notification_image_4 = canvas.create_image(
    356.0,
    486.0,
    image=button_images["notifications_image"],
    tags="notifications_text"
    )

    def back_notifications_to_home():
        canvas.delete("notifications_text")
        home_page()

    if current_language=="english":
        canvas.create_text(
        296.0,
        110.0,
        anchor="nw",
        text="Notifications",
        fill="#631313",
        font=("RobotoRoman Medium", 20 * -1)
        )

        canvas.create_text(
        210.0,
        169.0,
        anchor="nw",
        text="Please update your ID card details at Bank\n",
        fill="#0B694D",
        font=("RobotoRoman Medium", 16 * -1),
        tags="notifications_text"
        )

        canvas.create_text(
            299.0,
            261.0,
            anchor="nw",
            text="Loan Available",
            fill="#0B694D",
            font=("RobotoRoman Medium", 16 * -1),
            tags="notifications_text"
        )

        canvas.create_text(
            265.0,
            364.0,
            anchor="nw",
            text="Launch of new application",
            fill="#0B694D",
            font=("RobotoRoman Medium", 16 * -1),
            tags="notifications_text"
        )

        canvas.create_text(
            218.0,
            465.0,
            anchor="nw",
            text="Welcome to our Shariah-compliant bank",
            fill="#0B694D",
            font=("RobotoRoman Medium", 16 * -1),
            tags="notifications_text"
        )

        canvas.create_text(
            147.0,
            191.0,
            anchor="nw",
            text="Please update your ID card details soon in the Account section ",
            fill="#000000",
            font=("RobotoRoman Medium", 15 * -1),
            tags="notifications_text"
        )

        canvas.create_text(
            218.0,
            283.0,
            anchor="nw",
            text="Contact bank manager for more details",
            fill="#000000",
            font=("RobotoRoman Medium", 15 * -1),
            tags="notifications_text"
        )

        canvas.create_text(
            190.0,
            385.0,
            anchor="nw",
            text="New application has been launched for bank services",
            fill="#000000",
            font=("RobotoRoman Medium", 15 * -1),
            tags="notifications_text"
        )

        canvas.create_text(
            198.0,
            487.0,
            anchor="nw",
            text="We welcome you to our Shariah-compliant bank",
            fill="#000000",
            font=("RobotoRoman Medium", 15 * -1),
            tags="notifications_text"
        )
        button_back = Button(
        image=button_images["button_back"],
        borderwidth=0,
        highlightthickness=0,
        command=back_notifications_to_home,
        relief="flat",
        cursor="hand2"
        )  
        button_back.place(
        x=63.11627197265625,
        y=100.0,
        width=72.5931396484375,
        height=21.0
        )
        button_malayalam.place_forget()
    else:
        canvas.create_text(
        296.0,
        110.0,
        anchor="nw",
        text="അറിയിപ്പുകൾ",
        fill="#631313",
        font=("RobotoRoman Medium", 20 * -1)
        )

        canvas.create_text(
        210.0,
        169.0,
        anchor="nw",
        text="Please update your ID card details at Bank\n",
        fill="#0B694D",
        font=("RobotoRoman Medium", 16 * -1),
        tags="notifications_text"
        )

        canvas.create_text(
            299.0,
            261.0,
            anchor="nw",
            text="Loan Available",
            fill="#0B694D",
            font=("RobotoRoman Medium", 16 * -1),
            tags="notifications_text"
        )

        canvas.create_text(
            265.0,
            364.0,
            anchor="nw",
            text="Launch of new application",
            fill="#0B694D",
            font=("RobotoRoman Medium", 16 * -1),
            tags="notifications_text"
        )

        canvas.create_text(
            218.0,
            465.0,
            anchor="nw",
            text="Welcome to our Shariah-compliant bank",
            fill="#0B694D",
            font=("RobotoRoman Medium", 16 * -1),
            tags="notifications_text"
        )

        canvas.create_text(
            147.0,
            191.0,
            anchor="nw",
            text="Please update your ID card details soon in the Account section ",
            fill="#000000",
            font=("RobotoRoman Medium", 15 * -1),
            tags="notifications_text"
        )

        canvas.create_text(
            218.0,
            283.0,
            anchor="nw",
            text="Contact bank manager for more details",
            fill="#000000",
            font=("RobotoRoman Medium", 15 * -1),
            tags="notifications_text"
        )

        canvas.create_text(
            190.0,
            385.0,
            anchor="nw",
            text="New application has been launched for bank services",
            fill="#000000",
            font=("RobotoRoman Medium", 15 * -1),
            tags="notifications_text"
        )

        canvas.create_text(
            198.0,
            487.0,
            anchor="nw",
            text="We welcome you to our Shariah-compliant bank",
            fill="#000000",
            font=("RobotoRoman Medium", 15 * -1),
            tags="notifications_text"
        )
        button_back = Button(
        image=button_images["button_back_malayalam"],
        borderwidth=0,
        highlightthickness=0,
        command=back_notifications_to_home,
        relief="flat",
        cursor="hand2"
        )  
        button_back.place(
        x=63.11627197265625,
        y=100.0,
        width=102.09426879882812,
        height=21.0
        )
        button_english.place_forget()
   


def malayalam_page():
    global current_language
    current_language="malayalam"
    home_page()

def english_page():
    global current_language
    current_language="english"
    home_page()





welcome_page()
window.mainloop()



