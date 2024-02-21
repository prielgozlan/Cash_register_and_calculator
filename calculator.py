import tkinter as tk


def display_result():
    string = txt_display.get()

    try:

        result = eval(string)

    except:

        result = "ERROR"

    txt_display.delete(0, tk.END)

    txt_display.insert(0, str(result))


root = tk.Tk()
root.title("מחשבון פשוט")
root.geometry("200x260")
a = 4
b = 3


def on_resize(event):
    new_width = event.width
    new_height = event.height
    print(f"Window resized to {new_width}x{new_height}")


txt_display = tk.Entry(root, width=0, font=('Arial', 20))
txt_display.grid(row=0, column=0, columnspan=5, sticky='nsew')
bun1 = tk.Button(root, text="1",
                 command=lambda: txt_display.insert(tk.END, "1"), width=a, height=b)
bun1.grid(row=3, column=0, sticky='nsew')
bun2 = tk.Button(root, text="2",
                 command=lambda: txt_display.insert(tk.END, "2"), width=a, height=b)
bun2.grid(row=3, column=1, sticky='nsew')
bun3 = tk.Button(root, text="3",
                 command=lambda: txt_display.insert(tk.END, "3"), width=a, height=b)
bun3.grid(row=3, column=2, sticky='nsew')
bun4 = tk.Button(root, text="4",
                 command=lambda: txt_display.insert(tk.END, "4"), width=a, height=b)
bun4.grid(row=2, column=0, sticky='nsew')
bun5 = tk.Button(root, text="5",
                 command=lambda: txt_display.insert(tk.END, "5"), width=a, height=b)
bun5.grid(row=2, column=1, sticky='nsew')
bun6 = tk.Button(root, text="6",
                 command=lambda: txt_display.insert(tk.END, "6"), width=a, height=b)
bun6.grid(row=2, column=2, sticky='nsew')
bun7 = tk.Button(root, text="7",
                 command=lambda: txt_display.insert(tk.END, "7"), width=a, height=b)
bun7.grid(row=1, column=0, sticky='nsew')
bun8 = tk.Button(root, text="8",
                 command=lambda: txt_display.insert(tk.END, "8"), width=a, height=b)
bun8.grid(row=1, column=1, sticky='nsew')
bun9 = tk.Button(root, text="9",
                 command=lambda: txt_display.insert(tk.END, "9"), width=a, height=b)
bun9.grid(row=1, column=2, sticky='nsew')
bun0 = tk.Button(root, text="0",
                 command=lambda: txt_display.insert(tk.END, "0"), width=a, height=b)
bun0.grid(row=4, column=0, columnspan=2, sticky='nsew')
bun_ = tk.Button(root, text=".",
                 command=lambda: txt_display.insert(tk.END, "."), width=a, height=b)
bun_.grid(row=4, column=2, sticky='nsew')
bun__ = tk.Button(root, text="+",
                  command=lambda: txt_display.insert(tk.END, "+"), width=a, height=b)
bun__.grid(row=4, column=3, sticky='nsew')
bun11 = tk.Button(root, text="-",
                  command=lambda: txt_display.insert(tk.END, "-"), width=a, height=b)
bun11.grid(row=3, column=3, sticky='nsew')
bun12 = tk.Button(root, text="/",
                  command=lambda: txt_display.insert(tk.END, "/"), width=a, height=b)
bun12.grid(row=2, column=3, sticky='nsew')
bun13 = tk.Button(root, text="*",
                  command=lambda: txt_display.insert(tk.END, "*"), width=a, height=b)
bun13.grid(row=1, column=3, sticky='nsew')
bun14 = tk.Button(root, text="AC",
                  command=lambda: txt_display.delete(0, tk.END), width=6, height=b)
bun14.grid(row=1, column=4, sticky='nsew')
bun15 = tk.Button(root, text="=",
                  command=display_result)
bun15.grid(row=2, column=4, rowspan=3, sticky='nsew')

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)

root.bind("<Configure>", on_resize)

root.mainloop()
