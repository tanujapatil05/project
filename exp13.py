import tkinter as tk

#Create main application window
root =tk.Tk()
root.title("Tkinter GUI")
root.geometry("300x200")

#Create a Label
label =tk.Label (root, text="Hello, IT Students!", font=("Arial", 14))
label.pack(pady=20)

#Create a button
button =tk.Button(root, text="Click Me", command=lambda: print("Button Clicked!"))
button.pack()
root.mainloop()