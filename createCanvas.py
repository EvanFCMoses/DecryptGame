

import  Tkinter
top = Tkinter.Tk()

T = Tkinter.Text(top, height=5, width=100)
T.pack()
quote = """HAMLET: To be, or not to be--that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune
Or to take arms against a sea of troubles
And by opposing end them. To die, to sleep--
No more--and by a sleep to say we end
The heartache, and the thousand natural shocks
That flesh is heir to. 'Tis a consummation
Devoutly to be wished."""
T.insert(Tkinter.END, quote)


text2 = Tkinter.Text(top, height=20, width=50)
scroll = Tkinter.Scrollbar(top, command=text2.yview)
text2.configure(yscrollcommand=scroll.set)
text2.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
text2.tag_configure('big', font=('Verdana', 20, 'bold'))
text2.tag_configure('color', foreground='#476042', 
						font=('Tempus Sans ITC', 12, 'bold'))
text2.tag_bind('follow', '<1>', lambda e, t=text2: t.insert(Tkinter.END, "Not now, maybe later!"))
text2.insert(Tkinter.END,'\nWilliam Shakespeare\n', 'big')
quote = """
To be, or not to be that is the question:
Whether 'tis Nobler in the mind to suffer
The Slings and Arrows of outrageous Fortune,
Or to take Arms against a Sea of troubles,
"""
text2.insert(Tkinter.END, quote, 'color')
text2.insert(Tkinter.END, 'follow-up\n', 'follow')
text2.pack(side=Tkinter.LEFT)

text2.pack()

C = Tkinter.Canvas(top, bg="#b2c2c4", height=500, width=1000)

C.pack()

top.mainloop()
