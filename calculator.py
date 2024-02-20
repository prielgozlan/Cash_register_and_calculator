import tkinter as tk
import tkinter.font


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
size = tkinter.font.Font(root, family='Arial', size=100,weight='bold')
txt_display = tk.Entry(root)
txt_display.grid(row=0, column=0, columnspan=5, sticky='NEWS')
bun1 = tk.Button(root, text="1",
                 command=lambda: txt_display.insert(tk.END, "1"))
bun1.grid(row=3, column=0, sticky='NEWS')
bun2 = tk.Button(root, text="2",
                 command=lambda: txt_display.insert(tk.END, "2"))
bun2.grid(row=3, column=1, sticky='NEWS')
bun3 = tk.Button(root, text="3",
                 command=lambda: txt_display.insert(tk.END, "3"))
bun3.grid(row=3, column=2, sticky='NEWS')
bun4 = tk.Button(root, text="4",
                 command=lambda: txt_display.insert(tk.END, "4"))
bun4.grid(row=2, column=0, sticky='NEWS')
bun5 = tk.Button(root, text="5",
                 command=lambda: txt_display.insert(tk.END, "5"))
bun5.grid(row=2, column=1, sticky='NEWS')
bun6 = tk.Button(root, text="6",
                 command=lambda: txt_display.insert(tk.END, "6"))
bun6.grid(row=2, column=2, sticky='NEWS')
bun7 = tk.Button(root, text="7",
                 command=lambda: txt_display.insert(tk.END, "7"))
bun7.grid(row=1, column=0, sticky='NEWS')
bun8 = tk.Button(root, text="8",
                 command=lambda: txt_display.insert(tk.END, "8"))
bun8.grid(row=1, column=1, sticky='NEWS')
bun9 = tk.Button(root, text="9",
                 command=lambda: txt_display.insert(tk.END, "9"))
bun9.grid(row=1, column=2, sticky='NEWS')
bun0 = tk.Button(root, text="0",
                 command=lambda: txt_display.insert(tk.END, "0"))
bun0.grid(row=4, column=0, columnspan=2, sticky='NEWS')
bun_ = tk.Button(root, text=".",
                 command=lambda: txt_display.insert(tk.END, "."))
bun_.grid(row=4, column=2, sticky='NEWS')
bun__ = tk.Button(root, text="+",
                  command=lambda: txt_display.insert(tk.END, "+"))
bun__.grid(row=4, column=3, sticky='NEWS')
bun11 = tk.Button(root, text="-",
                  command=lambda: txt_display.insert(tk.END, "-"))
bun11.grid(row=3, column=3, sticky='NEWS')
bun12 = tk.Button(root, text="/",
                  command=lambda: txt_display.insert(tk.END, "/"))
bun12.grid(row=2, column=3, sticky='NEWS')
bun13 = tk.Button(root, text="*",
                  command=lambda: txt_display.insert(tk.END, "*"))
bun13.grid(row=1, column=3, sticky='NEWS')
bun14 = tk.Button(root, text="AC",
                  command=lambda: txt_display.delete(0, tk.END))
bun14.grid(row=1, column=4, sticky='NEWS')
bun15 = tk.Button(root, text="=",
                  command=display_result)
bun15.grid(row=2, column=4,rowspan=3, sticky='NEWS')

root.mainloop()
