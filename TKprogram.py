import tkinter as tk
# 1} create tkinter window
root=tk.Tk()

# 2} set size of window
root.geometry("500x300")

# 6} Create a function
def fact():
    # Take value entered in input text box
    value=int(entry.get())
    res=1
    for i in range(1,value+1):
        res*=i
    # update label and show result using "config" 
    label.config(text=f"Output is: {res}")

# 3} Create input text box and pack it
entry=tk.Entry(root)
entry.pack()

# 4} label to shoe result and pack it
label=tk.Label(root, text="Output is: ")
label.pack()

# 5} Button to trigger function and pack it
btn=tk.Button(root, text="calculate", command=fact)
btn.pack()

# 7} 
# used to keep window in running state
tk.mainloop()