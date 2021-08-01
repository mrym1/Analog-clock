import tkinter as Tkinter

import math
import time

class main(Tkinter.Tk):
	def __init__(self):
		Tkinter.Tk.__init__(self)
		self.x=190
		self.y=150
		self.length=60
		self.creating_all_function_trigger()

	# Creating Trigger For Other Functions
	def creating_all_function_trigger(self):
		self.create_canvas_for_shapes()
		self.creating_background_()
		self.creating_sticks()
		return

	# Creating Background
	def creating_background_(self):
		self.image=Tkinter.PhotoImage(file='clock.png')
		self.canvas.create_image(190,140, image=self.image)
		return

	# creating Canvas
	def create_canvas_for_shapes(self):
		self.canvas=Tkinter.Canvas(self, bg='pink')
		self.canvas.pack(expand='yes',fill='both')
		return

	# Creating Moving Sticks
	def creating_sticks(self):
		self.sticks=[]
		for i in range(3):
			store=self.canvas.create_line(self.x, self.y,self.x+self.length,self.y+self.length,width=4, fill='orange')
			self.sticks.append(store)
		return
# Function Need Regular Update
	def update_class(self):
		now=time.localtime()
		t = time.strptime(str(now.tm_hour), "%H")
		hour = int(time.strftime( "%I", t ))*5
		now=(hour,now.tm_min,now.tm_sec)
		# changing stick coordinates
		for n,i in enumerate(now):
			x,y=self.canvas.coords(self.sticks[n])[0:2]
			cr=[x,y]
			cr.append(self.length*math.cos(math.radians(i*6)-math.radians(90))+self.x)
			cr.append(self.length*math.sin(math.radians(i*6)-math.radians(90))+self.y)
			self.canvas.coords(self.sticks[n], tuple(cr))
		return

# main function trigger
if __name__ == '__main__':
	root=main()

	# Creating Main Loop
	while True:
		root.update()
		root.update_idletasks()
		root.update_class()
