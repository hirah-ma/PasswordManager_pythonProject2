from tkinter import *
from tkinter import messagebox
import pyperclip
from random import choice, randint, shuffle
# ---------------------------- CONSTANTS ------------------------------- #
WHITE = "#FEFBF6"
RED = "#e7305b"
BLUE = "#41C9E2"
LBLUE="#DFF5FF"
YELLOW = "#f7f5dd"
FONT_NAME = "Arial 20"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#pyperclip to automatically copy the password on user's clipboard
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


    messagebox.showinfo("Congratulations",
                        "The generated password was copied to your clipboard.\nYou shall now paste it on your website.")


# ---------------------------- SAVE PASSWORD ------------------------------- #
#message boxes from messageboxes module in tkinter
def save():
    website= website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(website)==0 or len(email)==0 or len(password)==0:
        messagebox.showinfo("oops", message="fill all the fields")
    else:
        if messagebox.askokcancel("confirm", message= f"The details are \nwebsite: {website} \nemail: {email}\npassword: {password}\ndo you wish to save this details?"):
            with open("my_password_data", "a") as data_file:
                data_file.write(f"{website}  |  {email}  |  {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window =Tk()
window.title("KEEPPASS")
window.config(padx=100 , pady= 100, bg=LBLUE)

#label, entry and button
label1= Label(text= "Website:" , font= (FONT_NAME, 14, "italic"),bg=LBLUE)
label1.grid(row= 1, column = 0)

website_entry = Entry(width = 53)
website_entry.grid(row = 1 , column= 1 , columnspan = 2)
website_entry.focus()

label2= Label(text= "Email/Username:" , font= (FONT_NAME, 14, "italic"), bg=LBLUE)
label2.grid(row= 2, column = 0)

email_entry= Entry(width = 53,)
email_entry.grid(row =2, column= 1 , columnspan = 2)
email_entry.insert(0, "hirah@gmail.com")

label3= Label(text= "Password:" , font= (FONT_NAME, 14, "italic"), bg=LBLUE)
label3.grid(row= 3, column = 0)

password_entry= Entry(width = 36)
password_entry.grid(row =3, column= 1 )

label4 = Button(text= "Generate Password", command = generate_password, bg=BLUE, font=("Arial",8))
label4.grid(row=3, column= 2)

label5 = Button(text= "Add", width= 47 , command = save, bg=WHITE)
label5.grid(row=4, column= 1, columnspan= 2)

logo= PhotoImage(file = "logo.png")

canvas = Canvas(width=228, height=224, highlightthickness=0, bg=LBLUE)
canvas.create_image(110, 112, image= logo )
canvas.grid(row= 0, column = 1)
window.mainloop()

