import requests
from tkinter import *

target_url = "https://pokeapi.co/api/v2/pokemon"
limit = {'limit':100}

response = requests.get(target_url,params=limit)

def PokeGuide():
    if response.status_code == 200:
        poke_data = response.json()
        for pokemon in poke_data['results']:
            print(pokemon['name'], pokemon['url'])

my_window = Tk()
my_window.config(padx=100,pady=100)
my_window.title("Pokemon Guide")

my_label = Label()
my_label.config(width=20,text="Press for pokemon guide")
my_label.pack()

my_button = Button()
my_button.config(text="Pokemon Guide",command=PokeGuide)
my_button.pack()

my_label_2 = Label()
my_label_2.pack()

my_window.mainloop()