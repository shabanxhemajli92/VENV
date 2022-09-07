from tkinter import *
root = Tk()
root.title('Image viewer')
root.geometry("220x220")
my_menu = Menu(root)
root.config(menu=my_menu)
# Click command
def our_command1():
    my_label = Label(root, text="the image").pack()
def our_command2():
    my_label = Label(root, text="This is an integrated jpg").pack()
def our_command3():
    my_label=Label(root,text="This is made to show a jpg file").pack()    
# Create a menu item
file_menu = Menu(my_menu)
my_menu.add_cascade(label="Menu", menu =file_menu)
file_menu.add_command(label="1", command = our_command1)
file_menu.add_separator()
file_menu.add_command(label="2", command = our_command2)
file_menu.add_separator()
file_menu.add_command(label="3",command=our_command3)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
root.mainloop()















