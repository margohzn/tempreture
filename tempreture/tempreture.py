from tkinter import *


def convert():
    temp_celcius = celcius.get()
    if temp_celcius.replace(".", "", 1).isdigit():
        error_message.grid_forget()
        temp_fahrenheit = (float(temp_celcius)*9/5)+32
        output.config(text = "tempreture in farinheit: " +str(temp_fahrenheit))
    else:
        error_message.grid(row = 2, column = 1)



window = Tk()
window.geometry("700x400")
window.title("Celcius to Fahrinheit")
window.configure(background = "pink")

heading = Label(text = "Celsius → Fahenfeit", fg = "black",bg = "white", font = ("times", 40)).grid(row = 0, column = 0)

frame = Frame(window).grid(row = 1, column = 0)
text = Label(frame, text = "Enter tempreture in celcius: ", fg = "blue", bg = "white", font = ("times", 20)).grid(row = 1, column = 0, pady = 20)
celcius = Entry(frame, bg = "white", fg = "black").grid(row = 1, column = 1) 
error_message = Label(frame, text = "Enter a valid input...", fg = "red", bg = "white")#.grid(row = 2, column = 1)
output = Label(frame, text = "Tempreture in Fahrinheit: ",bg = "navy", fg = "white",  font = ("times", 30)).grid(row = 3, column = 0, pady = 10, padx = 60)
covert = Button(frame, text = "Convert").grid(row = 4, column = 0, command = convert)


window.mainloop()
