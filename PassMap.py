import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mplsoccer.pitch import Pitch


class passMap:
    """This class draws a pass map, however in the future this class might be extended to draw
    other types of maps/graphs"""
    @staticmethod
    def draw_graph(location,minutes,outcome,end,team,opposition):
        """This method draws a pass map"""
        pitch = Pitch(line_color = "black")
        fig, ax = pitch.draw(figsize=(8, 5))
        yards_gained = []
        for x, empty in enumerate(location):
            if minutes[x] > 45:
                break
            if outcome[x] == 'Incomplete':
                pass_arrow=patches.Arrow(location[x][0], location[x][1], end[x][0]-location[x][0], end[x][1]-location[x][1],width=0.5,color="red")
                plt.scatter(location[x][0],location[x][1],color='red', s=2)
            else:
                pass_arrow=patches.Arrow(location[x][0], location[x][1], end[x][0]-location[x][0], end[x][1]-location[x][1],width=0.5,color="blue")
                plt.scatter(location[x][0],location[x][1],color='blue', s=2)
                yards_gained.append(end[x][0] - location[x][0])
            ax.add_patch(pass_arrow)
        print(sum(yards_gained) /len(yards_gained))
        plt.savefig(f'{team}vs{opposition}_at_euro2024.png', bbox_inches='tight')
        return fig
