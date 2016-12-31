#!/usr/bin/python

# ---------------- READ ME ---------------------------------------------
# This Script is Created Only For Practise And Educational Purpose Only
# This is an Example Of Tkinter Canvas Graphics
# This Script Is Created For https://hackworldwithssb.blogspot.in
# This Script is Written By
__author__='''

######################################################
                By S.S.B Group                          
######################################################

    Suraj Singh
    Admin
    S.S.B Group
    surajsinghbisht054@gmail.com
    https://hackworldwithssb.blogspot.in

    Note: We Feel Proud To Be Indian
######################################################
'''
print __author__
# ============ CONFIGURATIONS =====================

NUMBER_OF_BALLS=15
TIME_LAP=0.01
CIRCLE_WIDTH=200
CIRCLE_HEIGHT=200
BACKGROUND='black'
TRANSPARENCY_LEVEL=0.5

# =================================================

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ===================== Scripts Starts From Here =============================+
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# *************** Importing Module ****************
try:
    import Tkinter, random, time
except:
    import tkinter as Tkinter, random, time
    
# *************************************************

# ======================== Ball Configurations =====================================
class BouncingBall:
    def __init__(self, canvas):
        self.canvas=canvas
        self.widthlimit=self.canvas.winfo_reqwidth()
        self.heightlimit=self.canvas.winfo_reqheight()
        randomwidth=random.randrange(0, self.widthlimit)
        randomheight=random.randrange(0, self.heightlimit)
        x1=randomwidth-CIRCLE_WIDTH
        y1=randomheight-CIRCLE_HEIGHT
        color=random.choice(['lightgreen','powderblue', 'skyblue', 'yellow', 'grey','VioletRed4','wheat','SpringGreen3','SteelBlue','SandyBrown','seagreen','MintCream',
'mistyrose',])
        self.ball=Tkinter.Canvas.create_oval(self.canvas, x1,y1,randomwidth,randomheight, fill=color)
        self.xvelocity=1
        self.yvelocity=0.5
        
        
    def update(self):
        x1,y1,x2,y2=self.canvas.coords(self.ball)
        if x1<=0:
            self.xvelocity=random.choice([0.7,0.9,1.1,1.3,1.5,1.7,1.9])
            self.canvas.move(self.ball,self.xvelocity,0)
        elif y2>=self.heightlimit:
            self.yvelocity=random.choice([-0.7,-0.9,-1.1,-1.3])
            self.canvas.move(self.ball, 0, self.yvelocity)
        elif x2>=self.widthlimit:
            self.xvelocity=random.choice([-0.7,-0.9,-1.1,-1.3,-1.5,-1.7,-1.9])
            self.canvas.move(self.ball,self.xvelocity,0)
        elif y1<=0:
            self.yvelocity=random.choice([0.7,0.9,1.1,1.3,1.5,1.7,1.9])
            self.canvas.move(self.ball, 0, self.yvelocity)    
        else:
            self.canvas.move(self.ball, self.xvelocity, self.yvelocity)
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^                            
# =============================================== Main Tk WIndow =================================
class main:
    def __init__(self):
        self.root=Tkinter.Tk(className='Bouncing Balls')
        self.loop=Tkinter.IntVar()
        self.loop.set(1)
        w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.canvas=Tkinter.Canvas(self.root, background=BACKGROUND, width=w, height=h)
        self.canvas.pack(expand='yes', fill='both')
        self.root.wm_attributes("-topmost", True)
        #self.root.overrideredirect(1)
        balls=[]
        self.root.attributes('-fullscreen', True)
        self.transparency()
        for i in range(NUMBER_OF_BALLS):
            ball=BouncingBall(self.canvas)
            balls.append(ball)
        for seq in ('<Any-KeyPress>', '<Any-Button>', '<Motion>'):
            self.root.bind_all(seq, self.out)
        while self.loop.get()==1:
            try:
                for i in balls:
                    i.update()
                self.root.update_idletasks()
                self.root.update()
                time.sleep(TIME_LAP)
            except Exception as e:
                break
        self.root.destroy()
    def out(self, event):
        self.loop.set(0)
        return
    def transparency(self):
        x=1
        if x==1:
            #self.root.wait_visibility(self.root)
            self.root.wait_visibility(self.canvas)
            self.root.wm_attributes('-alpha',TRANSPARENCY_LEVEL)
            
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^        


#============ Trigger ========================  
if __name__=='__main__':
    main()
