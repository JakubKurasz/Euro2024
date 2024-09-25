from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import PassMap
import DataCollector


def main():
    """
    gives the user the choice to either create an image, or run the application
    """
    while True:
        choice = input("type 1 to create image, type 2 to run app")
        if choice == '1':
            create_image()
        elif choice == '2':
            run_app()
        else:
            break
            
def create_image():
    """
    Creates an image
    """
    d = DataCollector.DataCollector()
    p = PassMap.PassMap()

    events = d.choose_match(3938637,'Netherlands', 'Pass')
    outcome, location, end, minutes = d.collect_data(events)
    p.draw_graph(location,minutes,outcome,end,'Netherlands', 'Poland')

def run_app():
    """
    runs the application
    """
    root = Tk()
    #root.geometry("800x800+300+000")
    image1 = Image.open('NetherlandsvsPoland_at_euro2024.png')  # Replace with your image file
    image1 = image1.resize((800, 600))
    photo = ImageTk.PhotoImage(image1)
    label = ttk.Label(root, image=photo)
    label.grid(row = 2, columnspan = 2)
    fact = StringVar()
    fact.set("Netherlands Vs Poland passmap")
    t = Label(root, textvariable=fact)
    t.grid(row = 1, columnspan=2)

    root.mainloop()
if __name__ == '__main__':
    main()