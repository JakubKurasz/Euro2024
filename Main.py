from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import PassMap
import DataCollector


def main():
    """
    runs the main logic of the application
    """
    while True:
        choice = input("type 1 to create image, type 2 to run app")
        if choice == '1':
            createImage()
        elif choice == '2':
            runApp()
        else:
            break
            
def createImage():
    """
    Creates an image
    """
    d = DataCollector.DataCollector()
    p = PassMap.passMap()

    events = d.choose_match(3938637,'Netherlands', 'Pass')
    outcome, location, end, minutes = d.collect_data(events)
    p.draw_graph(location,minutes,outcome,end,'Netherlands', 'Poland')

def runApp():
    root = Tk()
    #root.geometry("800x800+300+000")
    image1 = Image.open('NetherlandsvsPoland_at_euro2024.png')  # Replace with your image file
    image1 = image1.resize((800, 600))
    photo = ImageTk.PhotoImage(image1)
    label = ttk.Label(root, image=photo)
    label.grid(row = 2, columnspan = 2)
    fact = 'dsd'
    t = Text(root, height = 10, width = 10)
    t.grid(row = 4, columnspan=4)
    t.insert(END, fact)

    root.mainloop()
if __name__ == '__main__':
    main()