from graphics import *
class User:#introdusing class we can add multiple users for this code
    def __init__(self,pass_cr=0,defer_cr=0,fail_cr=0):#changed userInputs to __init__ 
        self.pass_cr=pass_cr
        self.defer_cr=defer_cr
        self.fail_cr=fail_cr
        self.Exclude_count,self.Trailer_count, self.Progress_count,self.Retrievr_count=0,0,0,0
        #because faced error in when processing counts           
    def getInput(self):      
        while True:    
            try:
                self.pass_cr=int(input("Enter your total PASS credits:"))
                if self.checkRange(self.pass_cr,self.defer_cr,self.fail_cr):
                    self.defer_cr=int(input("Enter your total defrer credits:"))
                    if self.checkRange(self.pass_cr,self.defer_cr,self.fail_cr):
                        self.fail_cr=int(input("Enter your total fail credits:"))
                        if self.checkRange(self.pass_cr,self.defer_cr,self.fail_cr):
                            self.inputRange(self.pass_cr,self.defer_cr,self.fail_cr)#send user data to the user input function
                            break 
                
            except ValueError:
                print("Integer required")
    
    def checkRange(self, pass_cr, defer_cr, fail_cr):
        rangelist = [0, 20, 40, 60, 80, 100, 120]
        if pass_cr not in rangelist or defer_cr not in rangelist or fail_cr not in rangelist:
            print("Out of range.")
            return False  
        else:
            return True  

    def inputRange(self,pass_cr,defer_cr,fail_cr):
        sum1=pass_cr+defer_cr+fail_cr
        if sum1 > 120:
            print("Total incorrect.")
            self.getInput()
        else:
            self.main()
            self.multipleoutcomes()
            
    def main(self):
        if 0 <= self.pass_cr <= 40 and 0 <= self.defer_cr <= 40 and 80 <= self.fail_cr <= 120 :
            print("Exclude")
            self.Exclude_count+=1
        elif self.pass_cr==100 and 0 <= self.defer_cr <= 20 and 0 <= self.fail_cr <= 20 :
            print("Progress (module trailer)")
            self.Trailer_count+=1
        elif self.pass_cr==120 :
            print("Progress")
            self.Progress_count+=1 
        else:
            print("Do not Progress – module retriever")
            self.Retrievr_count+=1  
    
    def updateinputs(self, pass_cr, defer_cr, fail_cr):
        self.templist1=[pass_cr,defer_cr,fail_cr]
        self.permelist1=[self.templist1]
        print(self.permlist1)

    def histogram(self):
        data = {'Progress': self.Progress_count, 'Trailer': self.Trailer_count, 'Retrievr': self.Retrievr_count,
                'Exclude': self.Exclude_count}

        win_width, win_height, bar_width = 1000, 600, 100
        win = GraphWin("Histogram Results", win_width, win_height)
        total_width = len(data) * (bar_width + 20)
        start_x = (win_width - total_width) / 2
        colors = ['red', 'green', 'blue', 'yellow']   #add some colour codes to match the code
        for i, (category, count) in enumerate(data.items()):
            
                x1 = start_x + i * (bar_width + 20)
                x2 = x1 + bar_width
                y1 = win_height - count * 10 
                y2 = win_height

                rect = Rectangle(Point(x1, y1), Point(x2, y2))
                rect.setFill(colors[i])
                rect.draw(win)

                count_label = Text(Point((x1 + x2) / 2, y1 - 10), f"{count}")
                count_label.setTextColor("black")
                count_label.draw(win)

                category_label = Text(Point((x1 + x2) / 2, y2 + 10), f"{category}")
                category_label.setTextColor("black")
                category_label.draw(win)
        total_count = sum(data.values())
        total_label = Text(Point(win_width / 2, win_height + 30), f"Total Count: {total_count}")
        total_label.setTextColor("black")
        total_label.draw(win)

        win.getMouse()
        win.close()

    def multipleoutcomes(self):
        try: 
            yorq=(input("Enter 'y' for yes or 'q' to quit and view results:")) 
            if yorq.lower()== 'y':
                self.getInput()
            elif yorq.lower()== 'q':
                self.updateinputs()#new implimented 101
                self.histogram()
            else:
                print("Input only 'y' or 'q' depending on your need")
                
        except Exception as e:
            print(f"faced error!  {e}")

user2=User()
user2.getInput() 