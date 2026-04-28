from tkinter import *
import pyperclip

root = Tk()
e=Entry(root, width = 50, borderwidth = 5)
e.pack()
root.title("Convert English and Arabic characters")

language = 0
x=" "
root.geometry("400x400")

def change():
    global language
    language +=1

    if language % 2 == 0:
        languageLabel = Label(root, text = "Input English characters, get Arabic characters" ).pack()
    if language % 2 == 1:
        languageLabel = Label(root, text = "Input Arabic characters, get English characters" ).pack()  


def myClick():
    global language
    global string
    string = e.get()

    print(language)
    if language % 2 == 0:
        x = string.replace("`", "ذ")
        x = x.replace("q", "ض")
        x = x.replace("w", "ص")
        x = x.replace("e", "ث")
        x = x.replace("r", "ق")
        x = x.replace("t", "ف")
        x = x.replace("y", "غ")
        x = x.replace("u", "ع")
        x = x.replace("i", "ه")
        x = x.replace("o", "خ")
        x = x.replace("p", "ح")
        x = x.replace("[", "ج")
        x = x.replace("]", "د")
        x = x.replace("a", "ش")
        x = x.replace("s", "س")
        x = x.replace("d", "ي")
        x = x.replace("f", "ب")
        x = x.replace("g", "ل")
        x = x.replace("h", "ا")
        x = x.replace("j", "ت")
        x = x.replace("k", "ن")
        x = x.replace("l", "م")
        x = x.replace(";", "ك")
        x = x.replace("'", "ط")
        x = x.replace("z", "ئ")
        x = x.replace("x", "ء")
        x = x.replace("c", "ؤ")
        x = x.replace("v", "ر")
        x = x.replace("n", "ى")
        x = x.replace("m", "ة")
        x = x.replace(",", "و")
        x = x.replace(".", "ز")
        x = x.replace("/", "ظ")
        x = x.replace("H", "أ")
        x = x.replace("N", "آ")
        x = x.replace("Y", "إ")
    elif language % 2 == 1:
        x = string.replace("`", "ذ")
        x = x.replace("ض", "q")
        x = x.replace("ص", "w")
        x = x.replace("ث", "e")
        x = x.replace("ق", "r")
        x = x.replace("ف", "t")
        x = x.replace("غ", "y")
        x = x.replace("ع", "u")
        x = x.replace("ه", "i")
        x = x.replace("خ", "o")
        x = x.replace("ح", "p")
        x = x.replace("ج", "[")
        x = x.replace("د", "]")
        x = x.replace("ش", "a")
        x = x.replace("س", "s")
        x = x.replace("ي", "d")
        x = x.replace("ب", "f")
        x = x.replace("ل", "g")
        x = x.replace("ا", "h")
        x = x.replace("ت", "j")
        x = x.replace("ن", "k")
        x = x.replace("م", "l")
        x = x.replace("ك", ";")
        x = x.replace("ط", "'")
        x = x.replace("ئ", "z")
        x = x.replace("ء", "x")
        x = x.replace("ؤ", "c")
        x = x.replace("ر", "v")
        x = x.replace("ى", "n")
        x = x.replace("ة", "m")
        x = x.replace("و", ",")
        x = x.replace("ز", ".")
        x = x.replace("ظ", "/")
        x = x.replace("أ", "H")
        x = x.replace("آ", "N")
        x = x.replace("إ", "Y")  

    myLabel = Label(root,text=x)
    myLabel.pack()
    myLabel2 = Label(root, text="Copied to User").pack()
    pyperclip.copy(x)


submitButton = Button(root, text = "Submit ", command = myClick).pack()
languageButton = Button(root, text = "Change Language", command = change).pack()

print("SUCCESS")


root.mainloop()