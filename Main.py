from statsbombpy import sb
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
from tkinter import ttk
import PassMap

p = PassMap.passMap()
events = p.chooseMatch(3938637)
outcome, location, end, minutes = p.collectData(events)
fig = p.drawGraph(location,minutes,outcome,end)
root = Tk()
root.geometry("800x800+300+000")


canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=LEFT)

root.mainloop()	