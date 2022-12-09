import time
from tkinter import *

def runTimer():
    global start_time, elapsed_time, prev_elapsed_time
    if (running):
        cur_time = time.time()
        time_diff = cur_time - start_time
        elapsed_time = time_diff + prev_elapsed_time
        timeText.configure(text="{:7.3f}".format(elapsed_time))
    window.after(10, runTimer)#tkinter에서 해당 밀리초 마다 계속 함수를 호출 함
    
def start():
    global running, start_time, elapsed_time, prev_elapsed_time
    if (running != True):
        running = True
        start_time = time.time()
        prev_elapsed_time = elapsed_time

def stop():
    global running, prev_elapsed_time, elapsed_time
    running = False
    prev_elapsed_time = elapsed_time

def reset():
    global running, elapsed_time, prev_elapsed_time
    running = False#running값을 false로 놔두면 runTimer 함수의 if문 값이 false로 함수가 실행되지 않는것과 같아짐
    elapsed_time = 0.000
    prev_elapsed_time = 0.000
    timeText.configure(text='0.000')

running = False
window = Tk()
timer = 0.000
start_time = time.time()
stop_time = time.time()
elapsed_time = 0.000
prev_elapsed_time = 0.000
window.title("My Simple Stop Watch")
timeText = Label(window, height = 5, text="0",font=("Arial 40 bold"))
timeText.pack(side = TOP)
startButton = Button(window, width=10, text="Start", bg="green", command=start)
startButton.pack(side = LEFT)
stopButton = Button(window, width=10, text="Pause", bg="red", command=stop)
stopButton.pack(side = LEFT)
resetButton = Button(window, width=10, text="Reset", bg="yellow", command=reset)
resetButton.pack(side = LEFT)

if __name__ == '__main__':
    reset()
    runTimer()
    window.mainloop()