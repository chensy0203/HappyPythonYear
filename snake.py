from tkinter import *
import random
class snake(Frame):
        def __init__(self, master=None):
                Frame.__init__(self, master)
                self.h=[[1,0,0,0,1,0],[1,0,0,0,1,0],[1,1,1,1,1,0],[1,0,0,0,1,0],[1,0,0,0,1,0],[1,0,0,0,1,0]]
                self.a=[[0,0,1,0,0,0],[0,1,0,1,0,0],[1,0,0,0,1,0],[1,1,1,1,1,0],[1,0,0,0,1,0],[1,0,0,0,1,0]]
                self.p=[[1,1,1,1,1,0],[1,0,0,0,1,0],[1,0,0,0,1,0],[1,1,1,1,1,0],[1,0,0,0,0,0],[1,0,0,0,0,0]]
                self.y=[[1,0,0,0,1,0],[0,1,0,1,0,0],[0,0,1,0,0,0],[0,0,1,0,0,0],[0,0,1,0,0,0],[0,0,1,0,0,0]]
                self.n=[[1,0,0,0,1,0],[1,1,0,0,1,0],[1,0,1,0,1,0],[1,0,0,1,1,0],[1,0,0,0,1,0],[1,0,0,0,1,0]]
                self.e=[[1,1,1,1,1,0],[1,0,0,0,0,0],[1,1,1,1,1,0],[1,0,0,0,0,0],[1,0,0,0,0,0],[1,1,1,1,1,0]]
                self.w=[[1,0,0,0,1,0],[1,0,1,0,1,0],[1,0,1,0,1,0],[1,1,0,1,1,0],[1,1,0,1,1,0],[1,0,0,0,1,0]]
                self.r=[[1,1,1,1,1,0],[1,0,0,0,1,0],[1,1,1,1,1,0],[1,1,1,0,0,0],[1,0,0,1,0,0],[1,0,0,0,1,0]]
                self.empty=[0,0,0,0,0,0]
                self.happyNewYear=[]
                for i in range(6):
                        self.happyNewYear.append(self.h[i]+self.a[i]+self.p[i]+self.p[i]+self.y[i])
                self.happyNewYear.append(self.empty+self.empty+self.empty+self.empty+self.empty)
                for i in range(6):
                        self.happyNewYear.append(self.n[i]+self.e[i]+self.w[i]+self.empty+self.empty)
                self.happyNewYear.append(self.empty+self.empty+self.empty)
                for i in range(6):
                        self.happyNewYear.append(self.y[i]+self.e[i]+self.a[i]+self.r[i]+self.empty)
                self.happyNewYear.append(self.empty+self.empty+self.empty+self.empty)
               
                self.body = [(0,0)]
                self.bodyid = []
                self.food = [ -1, -1 ]
                self.foodid = -1
                self.gridcount = 30 
                self.size = 600
                self.di = 3
                self.speed = 300

                self.top = self.winfo_toplevel()
                self.top.resizable(False, False)
                self.grid()
                self.canvas = Canvas(self)
                self.canvas.grid()
                self.canvas.config(width=self.size, height=self.size,relief=RIDGE)

                self.happyNewYearXY=[]
                self.drawHappyNewYear()

                self.drawgrid()
                s = self.size/self.gridcount
                id = self.canvas.create_rectangle(self.body[0][0]*s,self.body[0][1]*s,(self.body[0][0]+1)*s, (self.body[0][1]+1)*s, fill="blue")
                self.bodyid.insert(0, id)
                self.bind_all("<KeyRelease>", self.keyrelease)
                
                self.drawfood()
                self.after(self.speed, self.drawsnake)
                
        def drawgrid(self):
                s = self.size/self.gridcount
                for i in range(0, self.gridcount+1):
                        self.canvas.create_line(i*s, 0, i*s, self.size)
                        self.canvas.create_line(0, i*s, self.size, i*s)
                        
        def drawsnake(self):
                s = self.size/self.gridcount
                head = self.body[0]
                new = [head[0], head[1]] 
                if self.di == 1:
                        new[1] = (head[1]-1) % self.gridcount
                elif self.di == 2:
                        new[0] = (head[0]+1) % self.gridcount
                elif self.di == 3:
                        new[1] = (head[1]+1) % self.gridcount
                else:
                        new[0] = (head[0]-1) % self.gridcount
                next = ( new[0], new[1] )
                if next in self.body:
                        exit()
                elif next == (self.food[0], self.food[1]):
                        self.body.insert(0, next)
                        self.bodyid.insert(0, self.foodid)
                        self.canvas.create_rectangle(self.food[0]*s,self.food[1]*s,(self.food[0]+1)*s,(self.food[1]+1)*s, fill="red")
                        self.drawfood()
                else:
                        tail = self.body.pop()
                        id = self.bodyid.pop()
                        self.canvas.move(id, (next[0]-tail[0])*s, (next[1]-tail[1])*s)
                        self.body.insert(0, next)
                        self.bodyid.insert(0, id)
                self.after(self.speed, self.drawsnake)

        def drawHappyNewYear(self):
             s = self.size/self.gridcount
             for i in range(len(self.happyNewYear)):
                    for j in range(len(self.happyNewYear[i])):
                        if(self.happyNewYear[i][j] == 1):
                                #reverse
                                self.happyNewYearXY.append((j,i))
                                #self.canvas.create_rectangle(  j*s, i*s,(j+1)*s,(i+1)*s,fill="green")
                            
        def getNextFood(self):
                i=random.randrange(0,len(self.happyNewYearXY))
                self.food[0]=self.happyNewYearXY[i][0]
                self.food[1]=self.happyNewYearXY[i][1]
                del self.happyNewYearXY[i]
                            
        def drawfood(self):
                s = self.size/self.gridcount
                self.getNextFood()
                x=self.food[0]
                y=self.food[1]
                id = self.canvas.create_rectangle(x*s,y*s,(x+1)*s, (y+1)*s, fill="blue")
                #reverse
                self.happyNewYear[y][x]=0
                self.foodid = id
                
        def keyrelease(self, event):
                if event.keysym == "Up" and self.di != 3:
                        self.di = 1
                elif event.keysym == "Right" and self.di !=4:
                        self.di = 2
                elif event.keysym == "Down" and self.di != 1:
                        self.di = 3
                elif event.keysym == "Left" and self.di != 2:
                        self.di = 4

app = snake()
app.master.title("Happy New Year")
app.mainloop()
