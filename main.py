import tkinter as tk

root = tk.Tk()
root.geometry('800x600')
root.title('Canvas Demo - Rectangle')

canvas = tk.Canvas(root, width=600, height=400, bg='white')
canvas.pack(anchor=tk.CENTER, expand=True)

def from_rgb(rgb):
  r, g, b = rgb
  return f'#{r:02x}{g:02x}{b:02x}'
  
canvas.create_rectangle((0, 20), (20, 40), fill=from_rgb((255,0,0)))#red
canvas.create_rectangle((0, 0), (20, 20), fill=from_rgb((0,255,0)))#green
canvas.create_rectangle((0, 20), (20, 40), fill=from_rgb((0,0,255)))#blue

colors = [from_rgb((255,0,0)), from_rgb((125,17,45)), from_rgb((187,45,214)), from_rgb((2,25,91)), from_rgb((0,255,0)), from_rgb((0,0,255))]

#create one square or pixel. This should be a helper function. That is it only gets called within another function
def pixel(top_left_x, top_left_y, color):
  pass #delete this line when you start to build this

#creates multiple pixels of the same color in a row. You will need to use a for, while or do loop. 
def color_row(row, column_start, column_end, color):
  pass #delete this line when you start to build this

#creates character 1
def character_1(colors):
  pass #delete this line when you start to build this

#creates character 2
def character_2(colors):
  pass #delete this line when you start to build this










#don't forget to call your character creating functions


root.mainloop()