from statsbombpy import sb
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mplsoccer.pitch import Pitch
class passMap:
    @staticmethod
    def chooseMatch(id):
        events = sb.events(match_id=id)
        events = events[events['team'] == 'Netherlands']
        events = events[events['type']=='Pass']
        return events
    @staticmethod
    def collectData(events):
        location= []
        end = []
        minutes = []
        outcome = []
        for event in events['pass_outcome']:
            outcome.append(event)
        for event in events['location']:
            location.append(event)
        for event in events['pass_end_location']:
            end.append(event)
        for event in events['minute']:
            minutes.append(event)
        return outcome, location, end, minutes
    
    def drawGraph(self, location,minutes,outcome,end):
        pitch = Pitch(line_color = "black")
        fig, ax = pitch.draw(figsize=(8, 5))
        yardsGained = []
        for x in range(len(location)):
            if minutes[x] > 45:
                break
            if outcome[x] == 'Incomplete':
                passArrow=patches.Arrow(location[x][0], location[x][1], end[x][0]-location[x][0], end[x][1]-location[x][1],width=0.5,color="red")
                plt.scatter(location[x][0],location[x][1],color='red', s=2)
            else:
                passArrow=patches.Arrow(location[x][0], location[x][1], end[x][0]-location[x][0], end[x][1]-location[x][1],width=0.5,color="blue")
                plt.scatter(location[x][0],location[x][1],color='blue', s=2)
                yardsGained.append(end[x][0] - location[x][0])
            ax.add_patch(passArrow)
        print(sum(yardsGained) /len(yardsGained))
        return fig
