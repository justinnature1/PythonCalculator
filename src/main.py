'''
CPSC-61200 Software Architecure
Week-3 Lab exercise: An implementation of a simple GUI-based
calculator using Model/View/Controller design pattern.
'''
import tkinter as Tk

class Model():
    '''Model class, abstracts the core data of the MVC pattern,
    Model maintains updates data based on events/calls it receives
    from Controller. Dependency should be one-way, Controller to Model,
    in otherwords, Model functions should NOT actively call methods of
    Controller or View
    '''
    def __init__(self):
        self.expr = ''

    def event(self, x):
        self.expr += x

    def calculate(self):
        try:
            self.expr = str(eval(self.expr))
        except:
            self.expr = ''

    def clear(self):
        self.expr = ''
    @property
    def value(self):
        return 0 if self.expr == '' else self.expr


class View():
    '''View in the MVC pattern assumes role of rendering user
    interface to the user, and maintaining an up to date view as
    it handles user interaction it receives from Controller.
    '''

    def _add_numbers_keypad(self, frame):
        # calculator display
        self.display = Tk.Label(frame, text=0, width=12, height=1)
        self.display.grid(row=0, column=0, columnspan=10, pady=5)

        #calculator numbers pad
        self.one = Tk.Button(frame, text="1")
        self.one.grid(row=1, column=0)

        self.two = Tk.Button(frame, text="2")
        self.two.grid(row=1, column=1)

        self.three = Tk.Button(frame, text="3")
        self.three.grid(row=1, column=2)

        self.four = Tk.Button(frame, text="4")
        self.four.grid(row=2, column=0)

        self.five = Tk.Button(frame, text="5")
        self.five.grid(row=2, column=1)

        self.six = Tk.Button(frame, text="6")
        self.six.grid(row=2, column=2)

        self.seven = Tk.Button(frame, text="7")
        self.seven.grid(row=3, column=0)

        self.eight = Tk.Button(frame, text="8")
        self.eight.grid(row=3, column=1)

        self.nine = Tk.Button(frame, text="9")
        self.nine.grid(row=3, column=2)

        self.zero = Tk.Button(frame, text="0")
        self.zero.grid(row=4, column=1)

    def _add_operations_keypad(self, frame):
        #operations pad
        self.clear = Tk.Button(frame, text="C")
        self.clear.grid(row=4, column=0)

        self.equal = Tk.Button(frame, text="=")
        self.equal.grid(row=4, column=2)

        self.add = Tk.Button(frame, text="+")
        self.add.grid(row=2, column=5)

        self.sub = Tk.Button(frame, text="-")
        self.sub.grid(row=3, column=5)

        self.mul = Tk.Button(frame, text="*")
        self.mul.grid(row=2, column=6)

        self.div = Tk.Button(frame, text="/")
        self.div.grid(row=3, column=6)

    def __init__(self):
        self.root = Tk.Tk()
        self.root.title("MVC example: Calculator")
        self.root.geometry()

        self._frame = Tk.Frame(self.root)
        self._frame.pack()
        self._add_numbers_keypad(self._frame)
        self._add_operations_keypad(self._frame)


    def refresh(self, value):
        self.display.config(text= value)

    def attach_keyboard(self, callback):
        self.root.bind("<Key>", callback)

    def start(self):
        self.root.mainloop()

class Controller():
    '''Controller is the primary coordinator in the MVC patter, it collects
    user input, ininitiates necessary changes to model (data), and refreshes
    view to reflect any changes that might have happened.'''

    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.view.one.bind("<Button>", lambda event, n=1: self.num_callback(n))
        self.view.two.bind("<Button>", lambda event, n=2: self.num_callback(n))
        self.view.three.bind("<Button>", lambda event, n=3: self.num_callback(n))
        self.view.four.bind("<Button>", lambda event, n=4: self.num_callback(n))
        self.view.five.bind("<Button>", lambda event, n=5: self.num_callback(n))
        self.view.six.bind("<Button>", lambda event, n=6: self.num_callback(n))
        self.view.seven.bind("<Button>", lambda event, n=7: self.num_callback(n))
        self.view.eight.bind("<Button>", lambda event, n=8: self.num_callback(n))
        self.view.nine.bind("<Button>", lambda event, n=9: self.num_callback(n))
        self.view.zero.bind("<Button>", lambda event, n=0: self.num_callback(n))
        self.view.add.bind("<Button>", lambda event, op='+': self.operation_callback(op))
        self.view.sub.bind("<Button>", lambda event, op='-': self.operation_callback(op))
        self.view.mul.bind("<Button>", lambda event, op='*': self.operation_callback(op))
        self.view.div.bind("<Button>", lambda event, op='/': self.operation_callback(op))
        self.view.equal.bind("<Button>", self.equal)
        self.view.clear.bind("<Button>", self.clear)


        self.view.attach_keyboard(self.keystroke_callback)

    def keystroke_callback(self, event):
        '''This is where you handle keystroke events from user,
        controller should invoke necessary methods on view and
        refresh view'''
        print('keystroke: {}'.format(event.keysym))

    def num_callback(self, num):
        self.model.event(str(num))
        self.view.refresh(self.model.value)
        print('number {} is clicked'.format(num))

    def operation_callback(self, operation):
        self.model.event(operation)
        self.view.refresh(self.model.value)
        print('operation: {}'.format(operation))

    def equal(self, event):
        self.model.calculate()
        self.view.refresh(self.model.value)
        print('equal pressed')

    def clear(self, event):
        self.model.clear()
        self.view.refresh(self.model.value)

    def run(self):
        self.view.start()

if __name__ == '__main__':
    ''' Main function, instantiate instances of Model, View and a Controller'''

    model = Model()
    view = View()

    controller = Controller(model=model, view=view)
    controller.run()