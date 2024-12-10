import tkinter as tk
from tkinter import PhotoImage, ttk
import tkinter.font as font
from tkinter import StringVar
from forex_python.converter import CurrencyRates

window = tk.Tk()
window.title("Currency Exchange")
window.geometry('931x524')

background = PhotoImage(file='bg.png')
bg = tk.Label(image=background)
bg.pack()

font1 = font.Font(family='helvetica', size='15')


def selected():
    a = int(amount.get())
    c = CurrencyRates()
    result = c.convert(from_currency, to_currency,a)
    print(result)
    answer.configure(text=result)

def from_func(event):
    global from_currency
    from_currency = event.widget.get()
    print(from_currency)

def to_func(event):
    global to_currency
    to_currency = event.widget.get()
    print(to_currency)

n = StringVar()
fromdd = ttk.Combobox(window,textvariable=n,width='30')
fromdd['value']=('USD',
                 'INR',
                 'EUR',
                 'GBP',
                 'JPY',
                 'AUD',
                 'CAD',
                 'CNY',
                 'KRW',
                 'BRL')

fromdd.current()
fromdd.bind('<<ComboboxSelected>>',from_func)
fromdd.place(relx='0.5', rely='0.33')

m = StringVar()
todd = ttk.Combobox(window,width='30', textvariable=m)
todd['value']=('USD',
               'INR',
               'EUR',
               'GBP',
               'JPY',
               'AUD',
               'CAD',
               'CNY',
               'KRW',
               'BRL')

todd.current()
todd.bind('<<ComboboxSelected>>', to_func)
todd.place(relx='0.5', rely='0.5')


amount = tk.Entry(window,width='20')
amount.place(relx='0.5', rely='0.7')


enter = tk.Button(window, text='Enter', command=selected,width='10',height='2')
enter.place(relx='0.43',rely='0.8')

answer = tk.Label(window,text='',width='50',height='2')
answer['font'] = font1
answer.place(relx='0.24', rely='0.9')



window.mainloop()