import tkinter as tk
root=tk.Tk()
root.geometry("300x200")

def increase_count():
    value=int(main_label.cget('text'))    
    value=value+1
    main_label.config(text=value)

def decrease_count():
    value=int(main_label.cget('text'))    
    value=value-1
    main_label.config(text=value)


main_label=tk.Label(root,text=0)
main_label.pack(pady=10)

increase_btn=tk.Button(root,text="Increase",command=increase_count)
increase_btn.pack(pady=10)
decrease_btn=tk.Button(root,text="Decrease",command=decrease_count)
decrease_btn.pack()

tk.mainloop()