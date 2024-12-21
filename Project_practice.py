from tkinter import Tk, Entry, Button, Label, StringVar

from creating_desktop_app import entry_text, result_label, search

window = Tk()
window.geometry("800x400")

window.title("Japanese Dictionary.")


entry_text=Entry(window)

entry_text.pack()


result = StringVar()
result_label=Label(window,textvariable=result)
result_label.pack()


japanese_dictionary = {'Aikido': 'A Japanese martial art.',
                       'Anime': 'A Japanese animation.' ,
                       'Bento': 'A Japanese boxed lunch.' ,
                       'Bonsai': 'A Japanese art of growing miniature trees in tiny pots.' ,
                       'Bushido': 'The code of the Samuri' ,
                       'Chanoyu': 'The Japanese tea ceremony' ,
                       'Chirashi': 'A Japanese sushi dish.' ,
                       'Chopsticks': 'Tapered sticks used for eating.' ,
                       'Dojo': 'A Japanese martial arts training hall.' ,
                       'Furoshiki': 'A Japanese wrapping cloth' ,
                       'Geisha': 'A Japanese female entertainer.' ,
                       'Gyoza': "Japanese pan-fried dumplings" ,
                       'Hara kiri': 'Ritual suicide by disembowelment' ,
                       'Iaijutsu': 'The japanese art of drawing and cutting with a sword' ,
                       'Ikrbana': 'The Japanese art of flower arrangement' ,
                       'Izakaya': 'A Japanese pub' ,
                       'Judo': 'A Japanese martial arts that emphasises throwing and grappling techmiques.' ,
                       'kabuki': 'A classicak japanese dance-drama' ,
                       'Karaoke': 'A Japanese singing competition.' ,
                       'Kimono': 'A traditional Japanese robe.' ,
                       'Kintsugi': 'the Japanese afrt of repairing broken pottery with gold.' ,
                       'Konnichiwa': 'Hello in Japanese.' ,
                       'Manga': 'Japanese comics' ,
                       'Origami': 'The Japanese art of paper folding.' ,
                       'Ramen': 'A Japanese noodle soop.' ,
                       'Samuri': 'A Japanese warrior' ,
                       'Sensei': 'A Japanese teacher.' ,
                       'Sushi': 'A Japanese dish of rice topped with vegetable or seafood' ,
                       'Tatami': 'A Japanese floor covering made of woven straw.' ,
                       'Zen': 'A Japanese school of Buddhism that emphasizes meditation.' ,
                       }

def search_word(word):
    if word in japanese_dictionary:
        result.set(japanese_dictionary[word])
        print(japanese_dictionary[word])

    else:
        result.set("Not found")
        print("Not Found.")


from creating_desktop_app import search

search_btn = Button(window, text='Search', command=lambda:search(entry_text.get()))
search_btn.pack()
window.mainloop()






