from tkinter import *


# 37. HOW TO INHERIT FROM A PYTHON TKINTER FRAME
# class RedFrame(Frame):
#     def __init__(self, the_window):
#         super().__init__()
#         self['height'] = 150
#         self['width'] = 150
#         self['relief'] = RAISED
#         self['bd'] = 8
#         self['bg'] = 'red'
#
#
# my_window = Tk()
#
# frame_a = RedFrame(my_window)
# frame_b = Frame(my_window, width=150, relief=RIDGE, height=150, bd=8)
# frame_c = RedFrame(my_window)
# frame_d = Frame(my_window, width=150, relief=RIDGE, height=150, bd=8)
# frame_a.grid(row=0, column=0)
# frame_b.grid(row=0, column=1)
# frame_c.grid(row=1, column=0)
# frame_d.grid(row=1, column=1)


# 38. THE IDENTITY AND TYPE OF A WIDGET THAT INHERITS FROM A PYTHON TKINTER FRAME
# class RedFrame(Frame):
#     def __init__(self, the_window):
#         super().__init__()
#         self['height'] = 150
#         self['width'] = 150
#         self['relief'] = RAISED
#         self['bd'] = 8
#         self['bg'] = 'red'
#
#
# my_window = Tk()
#
# frame_a = RedFrame(my_window)
# frame_a.grid(row=0, column=0)
# print('The id of frame_a is', id(frame_a))
# print('The type of frame_a is', type(frame_a))


# 39. THE NEED FOR THE INIT METHOD AND SELF PARAMETER WHEN INHERITING WITH TKINTER
class RedFrame(Frame):
    def __init__(self, the_window):
        super().__init__()
        print('The id of self id', id(self))
        self['height'] = 150
        self['width'] = 150
        self['relief'] = RAISED
        self['bd'] = 8
        self['bg'] = 'red'


my_window = Tk()

frame_a = RedFrame(my_window)
print('The id of frame_a id', id(frame_a))
frame_b = RedFrame(my_window)
print('The id of frame_b id', id(frame_b))
frame_a.grid(row=0, column=0)
frame_b.grid(row=0, column=1)


# frame_a = Frame(my_window, height=150, width=150, relief=RAISED, bd=8, bg='red')
# frame_b = Frame(my_window, height=150, width=150, relief=SUNKEN, bd=8, bg='green')
# frame_a.grid(row=0, column=0)
# frame_b.grid(row=0, column=1)

print(help(Frame))
my_window.mainloop()
