import tkinter as tk
root=tk.Tk()

def isPalindrome():
    value=entry.get()
    temp=int(value)
    result=int(value[::-1])
    if result==temp:
        result_label.config(text="THE NUMBER IS: PALINDROME")
    else:
        result_label.config(text="THE NUMBER IS: NOT PALINDROME")
    

root.geometry("500x300")    *9
heading=tk.Label(root,text="ENTER ANY NUMBER HERE")
heading.pack(pady=10)
entry=tk.Entry(root)
entry.pack()
result_label=tk.Label(root,text="THE NUMBER IS: ")
result_label.pack(pady=10)
button=tk.Button(root,text="Find", command=isPalindrome)
button.pack(pady=5)


tk.mainloop()