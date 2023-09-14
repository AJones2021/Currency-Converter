# Anna Jones
# 09/12/2023
# Python Currency converter


from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import json
import requests

# Colors
color4 = '#FFFFFF'
color3 = '#E6F8FF'
color1 = "#e7f2fb"
color2 = "#333333"
color5 = "#9eccf5"

root = Tk()
root.geometry('300x300')
root.title('Currency Converter')
root.configure(bg=color1)

top = Frame(root, width=300, height=60, bg=color5)
top.grid(row=0, column=0)

main = Frame(root, width=300, height=200, bg=color1)
main.grid(row=1, column=0)

def converter_api():

    url = "https://currency-converter-by-api-ninjas.p.rapidapi.com/v1/convertcurrency"

    from_currency = from_box.get()
    to_currency = to_box.get()
    amount = value.get()
    money_sign = '$'
    querystring = {"from": from_currency, "to": to_currency, "amount": amount}



    if to_currency == 'USD':
        money_sign = '$'
    elif to_currency == 'UAH':
        money_sign = '₴'
    elif to_currency == 'EUR':
        money_sign = '€'
    elif to_currency == 'CAD':
        money_sign = 'C$'
    elif to_currency == 'AUD':
        money_sign = 'A$'
    elif to_currency == 'SBD':
        money_sign = 'SI$'
    elif to_currency == 'NOK':
        money_sign = 'kr'
    elif to_currency == 'DKK':
        money_sign = 'kr'
    elif to_currency == 'GBP':
        money_sign = '£'
    elif to_currency == 'PLN':
        money_sign = 'zł'
    elif to_currency == 'RUB':
        money_sign = '₽'
    else:
        money_sign = "$"

    headers = {
        "X-RapidAPI-Key": "f7b873b383mshf919bb732781e22p19d747jsneb32b8d4cb32",
        "X-RapidAPI-Host": "currency-converter-by-api-ninjas.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    print(response.json())

    data = json.loads(response.text)
    amount_converted = data["result"]["convertedAmount"]
    format_two_decimal = money_sign + "{:,.2f}".format(amount_converted)

    result['text'] = format_two_decimal
    print(amount_converted, format_two_decimal)


# Image one
icon = Image.open('moneyconvert.png')
icon = icon.resize((43, 43))
icon = ImageTk.PhotoImage(icon)


title = Label(top, image=icon, compound=LEFT, text="Currency Converter", height=2, padx=15
                 , pady=35, anchor=CENTER, font=('arial 15 bold'), bg=color5)
title.place(x=0, y=0)


currency = ['UAH','RUB','EUR', 'CAD', 'USD', 'AUD','SBD', 'NOK', 'DKK','GBP','PLN']

from_label = Label(main, text="From", width=10, height=0, pady=0, padx=0, relief="flat", anchor=NW, font=('Helvetica 10'), bg=color1, fg=color5)
from_label.place(x=48, y=30)
entry_text1 = StringVar()
from_box = ttk.Combobox(main, textvariable=entry_text1, width=9, justify=CENTER, font=("Helvetica 10"))
entry_text1.set( "Select one..." )
from_box['values'] = (currency)
from_box.place(x=50, y=50)

to_label = Label(main, text="To", width=10, height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Helvetica 10'), bg=color1, fg=color5)
to_label.place(x=48, y=80)
entry_text2 = StringVar()
to_box = ttk.Combobox(main, textvariable=entry_text2, width=9, justify=CENTER, font=("Helvetica 10"))
entry_text2.set( "Select one..." )
to_box['values'] = (currency)
to_box.place(x=48, y=100)

# Function to check valid input from user
def check_number():

    try:
        if float(value.get()):
            converter_api()
    except ValueError:
        messagebox.showerror("error", "enter number to convert.")

value_label = Label(main, text="Amount", width=10, height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Helvetica 10'), bg=color1, fg=color5)
value_label.place(x=155, y=29)
value = Entry(main, width=12, justify=CENTER, font=("Helvetica 10"), relief="groove")
value.place(x=158, y=50)

result = Label(main, text=" ", width=11, height=1,padx=0, pady=0, relief="ridge", anchor=CENTER, font=('Helvetica 10 '), bg=color4, fg=color2)
result.place(x=155, y=100)

# Button calls validation function
# if correct proceed to converter_api function
button = Button(main, text="Convert", width=15, padx=10, height=1, bg=color5, fg=color1, relief="ridge", justify=CENTER, font=("Helvetica 12"), command=check_number)
button.place(x=65, y=150)

root.mainloop()
