from tkinter import Tk, Label, Button

time_running = False  # запущен ли
default_seconds = 300  # всего
time_seconds = default_seconds  # текущее время

def time_start_pause():
    global time_running
    time_running = not time_running  # пауза или нет
    if time_running:  # нет
        timer_tick()

def time_tick():
    if time_running and time_seconds:
        label.after(1000, timer_tick)  # уменьшить время
        global time_seconds
        time_seconds -= 1
        show_time()

def show_time():
    m = time_seconds//60
    s = time_seconds-m*60
    label['text'] = (m, s)

if __name__ == '__main__':
    root = Tk()
    label = Label(root)
    label.pack()
    Button(root, text='pause', command=time_start_pause).pack()  # пауза


    time_reset()
    root.mainloop()