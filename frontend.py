from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from views import *


LARGE_FONT=("Verdana",24)
MED_FONT=("Verdana",18)

class Polling(Tk):
	def __init__(self,*args,**kwargs):
		Tk.__init__(self,*args,**kwargs)


		self.container=Frame(self)
		self.container.grid()
		self.container.grid_rowconfigure(0,weight=1)
		self.container.grid_columnconfigure(0,weight=1)

		self.geometry("750x480")
		self.show_frame(Main)


	def show_frame(self, cont):
 		frame=cont(parent=self.container, controller=self)
 		frame.grid(row=0,column=0,sticky="nsew")
 		frame.tkraise()


class Main(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent) 	
		self.controller=controller
		
		heading_label = Label(self,text="Polling App",font=LARGE_FONT)
		
		congress_label = Label(self,text='Congress')
		
		bjp_label = Label(self,text='BJP')
		
		jds_label = Label(self,text='JDS')

		result_label = Label(self,text='Result')



		
		vote_btn1 = Button(self,text='Vote_congress',command=self.vote_congress)
		vote_btn2 = Button(self,text='Vote_bjp',command=self.vote_bjp)
		vote_btn3 = Button(self,text='Vote_jds',command=self.vote_jds)
		result_btn = Button(self,text='Result',command=self.result)
		

		heading_label.grid(row=2, column=5, padx=120,pady=30)

		congress_label.grid(row=6, column=5, padx=120,pady=10)
		bjp_label.grid(row=7,column=5,padx=120,pady=10)
		jds_label.grid(row=8,column=5,padx=120,pady=10)
		vote_btn1.grid(row=6, column=7, pady=30)
		vote_btn2.grid(row=7, column=7, pady=30)
		vote_btn3.grid(row=8, column=7, pady=30)
		result_btn.grid(row=9,column=7,pady=30)
	
	def vote_congress(self):
		add_vote_congress()
		
	def vote_bjp(self):
		add_vote_bjp()

	def vote_jds(self):
		add_vote_jds()
	
	def result(self):
		result=get_result()	
		print(result)
		congress=int(result[0])
		bjp=int(result[1])
		jds=int(result[2])


			
		messagebox.showinfo('results',"congress {}".format(congress))
		messagebox.showinfo('results',"bjp{}".format(bjp))
		messagebox.showinfo('results',"jds{}".format(jds))







app=Polling()
app.mainloop()					    
        
        


		
			