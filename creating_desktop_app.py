from tkinter import Tk, Entry, Button, Label, StringVar

#creating a window...

window = Tk()

#width and length of window.
window.geometry("600x250")

window.title("Hausa Dictionary")

#creating an entry space


entry_text = Entry(window)

entry_text.pack()

result=StringVar()
result_label=Label(window,textvariable=result)
result_label.pack()






hausa_dictionary = {'gida': 'house' ,
              'hanu': 'hand' ,
              'kasa': 'floor' ,
              'tala': 'advertisment' ,
              'doke': 'horse'  ,
              'rago': 'ram' ,
              'ruwa': 'water' ,
              'abinci': 'food' ,
              }





def search(word):
    if word in hausa_dictionary:
        result.set(hausa_dictionary[word])
        print(hausa_dictionary[word])


    else:
        result.set("Not found")
        print("Not Found")


search_btn = Button(window, text="Search", command=lambda:search(entry_text.get()))
search_btn.pack()
window.mainloop()

