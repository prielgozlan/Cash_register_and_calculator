import tkinter as tk

root = tk.Tk()
display = tk.Entry(root, width=0, font=('Arial', 20))
display.grid(row=0, column=0, columnspan=5, sticky='nsew')
list_of_product = {"פיצהL": 35, "מאפה": 20, "סלט": 35, "פלאפל": 25, "פיצהXL": 45, "פיצהXXL": 55, "טוסט": 20, "לאפה": 30,
                   "פיתה": 35}

sum_all = 0
root.title("Cash Register")



def add_product(key_1):
    global sum_all
    display.delete(0, tk.END)
    sum_all += list_of_product[key_1]
    print(list_of_product[key_1])


bun1 = tk.Button(root, text="פיצהL",
                 width=10, height=10, command=lambda: add_product("פיצהL"))
bun1.grid(row=1, column=0, sticky="nsew")
bun2 = tk.Button(root, text="מאפה",
                 width=10, height=10, command=lambda: add_product("מאפה"))
bun2.grid(row=2, column=0, sticky="nsew")
bun3 = tk.Button(root, text="סלט",
                 width=10, height=10, command=lambda: add_product("סלט"))
bun3.grid(row=3, column=0, sticky="nsew")
bun4 = tk.Button(root, text="פלאפל",
                 width=10, height=10, command=lambda: add_product("פלאפל"))
bun4.grid(row=2, column=1, sticky="nsew")
bun5 = tk.Button(root, text="פיצהXL",
                 width=10, height=10, command=lambda: add_product("פיצהXL"))
bun5.grid(row=1, column=1, sticky="nsew")
bun6 = tk.Button(root, text="פיצהXXL",
                 width=10, height=10, command=lambda: add_product("פיצהXXL"))
bun6.grid(row=1, column=2, sticky="nsew")
bun7 = tk.Button(root, text="טוסט",
                 width=10, height=10, command=lambda: add_product("טוסט"))
bun7.grid(row=3, column=1, sticky="nsew")
bun8 = tk.Button(root, text="לאפה",
                 width=10, height=10, command=lambda: add_product("לאפה"))
bun8.grid(row=3, column=2, sticky="nsew")
bun9 = tk.Button(root, text="פיתה",
                 width=10, height=10, command=lambda: add_product("פיתה"))
bun9.grid(row=2, column=2, sticky="nsew")
bun10 = tk.Button(root, text="סכום",
                  width=10, height=10, command=lambda: display_all_sum())
bun10.grid(row=3, column=3, sticky="nsew")


def display_all_sum():
    display.delete(0, tk.END)
    display.insert(tk.END, str(sum_all))


def delete_sum_all():
    global sum_all
    sum_all = 0
    display.delete(0, tk.END)


bun11 = tk.Button(root, text="איפוס",
                  width=10, height=10, command=lambda: delete_sum_all())
bun11.grid(row=2, column=3, sticky="nsew")
bun12 = tk.Button(root, text="הגדרות",
                  width=10, height=10)
bun12.grid(row=1, column=3, sticky="nsew")

print(sum_all)
root.mainloop()
