#Stored programm 0in github/checked the accuracy and efficiancy using CHATGPT at the end
#studentId:20230716
#Date:2023/11/19

from graphics import *
class User:#introdusing class we can add multiple users for this code
    def __init__(self,pass_cr=0,defer_cr=0,fail_cr=0):#changed userInputs to __init__ 
        self.pass_cr=pass_cr
        self.defer_cr=defer_cr
        self.fail_cr=fail_cr
        self.ListForUpdateExtend=[] #for use in updatelist
        self.Exclude_count,self.Trailer_count, self.Progress_count,self.Retrievr_count=0,0,0,0
        self.file = "progression_datasave.txt"
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
            self.VarForList="Exclude"
            self.Exclude_count+=1
        elif self.pass_cr==100 and 0 <= self.defer_cr <= 20 and 0 <= self.fail_cr <= 20 :
            print("Progress (module trailer)")
            self.VarForList="Progress (module trailer)"
            self.Trailer_count+=1
        elif self.pass_cr==120 :
            print("Progress")
            self.VarForList="Progress"
            self.Progress_count+=1 
        else:
            print("Do not Progress – module retriever")
            self.VarForList="Do not Progress – module retriever"
            self.Retrievr_count+=1  
    
    def UpdateList(self,pass_cr,defer_cr,fail_cr,VarForList):
        self.ListForUpdateExtend.append([VarForList, pass_cr, defer_cr, fail_cr])
        self.saveToFile(self) #save the file
        
    def histogram(self):
        data = {'Progress': self.Progress_count, 'Trailer': self.Trailer_count, 'Retrievr': self.Retrievr_count,
                'Exclude': self.Exclude_count}
        TotalOutcomes= self.Progress_count+self.Trailer_count+self.Retrievr_count+self.Exclude_count
        winWidth, winHeight, barWidth = 1000, 600, 100
        win = GraphWin("Histogram Results", winWidth, winHeight)
        
        MyHeading = Text(Point(200, 50), 'Histogram Results')#cordinates of histogramresults
        MyHeading.draw(win)
        MyHeading.setSize(25)
        MySubheading= Text(Point(200, 500),f"{TotalOutcomes} Outcomes in Total")
        MySubheading.setSize(20)
        MySubheading.draw(win) 
        
        totalWidth = len(data) * (barWidth + 20)
        start_x = (winWidth - totalWidth) / 2
        colors = ['red', 'green', 'blue', 'yellow']
        for i, (category, count) in enumerate(data.items()):
            
                x1 = start_x + i * (barWidth + 8 )#space between bars
                x2 = x1 + barWidth
                y1 = winHeight / 2 - count * 20 #getting center and /50 means growth of bars
                y2 = winHeight / 2 + count * 1   #make bar up

                rect = Rectangle(Point(x1, y1), Point(x2, y2))
                rect.setFill(colors[i])
                rect.draw(win)

                count_label = Text(Point((x1 + x2) / 2, y1 - 10), f"{count}")
                count_label.setTextColor("black")
                count_label.draw(win)

                category_label = Text(Point((x1 + x2) / 2, 350), f"{category}") #*****
                category_label.setTextColor("black")
                category_label.draw(win)
        total_count = sum(data.values())
        total_label = Text(Point(winWidth / 2, winHeight + 30), f"Total Count: {total_count}")
        total_label.setTextColor("black")
        total_label.draw(win)

        win.getMouse()
        win.close()

    def multipleoutcomes(self):
        try: 
            yorq=(input("Enter 'y' for yes or 'q' to quit and view results:")) 
            if yorq.lower()== 'y':
                self.UpdateList(self.pass_cr, self.defer_cr, self.fail_cr, self.VarForList)
                self.getInput()
            elif yorq.lower()== 'q':
                self.UpdateList(self.pass_cr, self.defer_cr, self.fail_cr, self.VarForList)
                self.PrintUpdateList()
                self.histogram()
                self.readFromFile(self)# read file by here !
            else:
                print("Input only 'y' or 'q' depending on your need")
                self.getInput()
                
        except Exception as e:
            print(f"faced error!  {e}")  

    def PrintUpdateList (self):#part 2
        print("Part 2 :")
        for i in range(0,len(self.ListForUpdateExtend)):
            print(f"{self.ListForUpdateExtend[i][0]} - {self.ListForUpdateExtend[i][1]}, {self.ListForUpdateExtend[i][2]}, {self.ListForUpdateExtend[i][3]}")

    def saveToFile(self,file):
        with open(self.file, 'w') as file:
            for item in self.ListForUpdateExtend:
                file.write(f"{item[0]}  - {item[1]}, {item[2]}, {item[3]} \n")

    def readFromFile(self,file): #part 3
        try:
            SavedData=[]
            with open(self.file, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    SavedData.append(tuple(line.strip().split("-")[1].split(" ,")))
            return("Part 3 :")
            return(SavedData)        
        except FileNotFoundError:
            print("No saved data found.")
if __name__ == '__main__':
    user3=User()
    user3.getInput() 