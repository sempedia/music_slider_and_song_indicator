from tkinter import (Tk, Frame, Button, Label, BOTH, LEFT)

class MyButton(Button):
    def __init__(self, parent=None, text='', width=5, height=None, cmd=None):
        self.text = text
        self.cmd = cmd
        Button.__init__(self, text=self.text, width=width, height=height, command=self.on_release)
        self.configure(bd=0)

    def on_release(self):
        if self.cmd:
            self.cmd(self, self.text)
            
class SimpleMusic(Tk):
    pos_x = 0
    current_width = 0
    def __init__(self):
        super().__init__()
        self.title('Music Slider & Song Indicator')
        self.config(bg='grey10')
        
        self.top_container = Frame(self)
        self.top_container.pack(fill=BOTH, expand=True)
        self.top_container.configure(bg='grey10')
        
        self.label = Label(self.top_container)
        self.label.pack()
        
        self.bottom = Frame(self, height=100)
        self.bottom.pack(fill=BOTH, expand=False)
        self.bottom.configure(bg='green')
        
        self.slider_holder = Frame(self, height=10)
        self.slider_holder.pack(fill=BOTH)
        self.slider_holder.configure(bg='grey10')
        
        self.slider = Label(self.slider_holder, width=5, height=5)
        self.slider.place(x=0)
        self.slider.configure(bg='green')
        
        self.buttons = Frame(self.bottom)
        self.buttons.pack(fill=BOTH)
        self.button_1 = MyButton(self.buttons, text='Song 1', cmd=self.navigation_command)
        self.button_2 = MyButton(self.buttons, text='Song 2', cmd=self.navigation_command)
        self.button_3 = MyButton(self.buttons, text='Song 3', cmd=self.navigation_command)
        self.button_4 = MyButton(self.buttons, text='Song 4', cmd=self.navigation_command)
        self.button_5 = MyButton(self.buttons, text='Song 5', cmd=self.navigation_command)
        self.button_1.pack(side=LEFT, expand=True)
        self.button_2.pack(side=LEFT, expand=True)
        self.button_3.pack(side=LEFT, expand=True)
        self.button_4.pack(side=LEFT, expand=True)
        self.button_5.pack(side=LEFT, expand=True)
        
        self.calculate_width_pos_x(self.button_1)
        self.slide()

    def navigation_command(self, *args):
        button = args[0]
        text = args[1]
        self.calculate_width_pos_x(button)
        self.slide()
    
    def slide(self):
        current_x = self.slider.winfo_x()
        if current_x > self.pos_x:
            position_range = current_x - self.pos_x
            for i in range(position_range + 1):
                self.slider.place(x=current_x - i)
                self.slider.update()
        elif current_x < self.pos_x:
            for k in range(self.pos_x - current_x):
                self.slider.place(x=current_x + k)
                self.slider.update()
            self.slider.place(x=self.pos_x)
            self.slider.configure(width=self.current_width)
   
    def calculate_width_pos_x(self, button):
        self.pos_x = button.winfo_x() - 1
        self.current_width = int(button.winfo_width() / 34.5) + 4  # button width is 5 and 1 is same as 34.5 in units of a Label
        self.label['text'] = 'Now singing: '+ button['text']

SimpleMusic().mainloop()
