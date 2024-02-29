import tkinter as tk

root = tk.Tk()
display = tk.Entry(root, width=0, font=('Arial', 20))
display.grid(row=0, column=0, columnspan=5, sticky='nsew')
list_of_product = {"פיצהL": 35, "מאפה": 20, "סלט": 35, "פלאפל": 25, "פיצהXL": 45, "פיצהXXL": 55, "טוסט": 20, "לאפה": 30,
                   "פיתה": 35}

sum_all = 0
root.title("Cash Register")

display.insert(0, str(0))

x = "add"


def add_product(key_1):
    global x
    global sum_all
    display.delete(0, tk.END)
    if x == "add":
        sum_all += list_of_product[key_1]
    elif x == "subtract":
        sum_all -= list_of_product[key_1]
        x = "add"
    display.insert(0, str(sum_all))
    print(list_of_product[key_1])


def delete_sum_all():
    global sum_all
    sum_all = 0
    display.delete(0, tk.END)
    display.insert(0, str(0))


def delete_subtract():
    global x
    if sum_all > 0:
        x = "subtract"


def open_new_window():
    for widget in root.winfo_children():
        widget.destroy()
    display = tk.Entry(root, width=0, font=('Arial', 20))
    display.grid(row=0, column=0, columnspan=5, sticky='nsew')
    con_1 = 1
    con_2 = 0
    con_3 = 0
    list_1 = ["פיצהL", "סלט", "מאפה", "פיצהXL", "טוסט", "פלאפל", "פיצהXXL", "לאפה", "פיתה"]
    for item in range(3):
        for item1 in range(3):
            bun1 = tk.Button(root, text=list_1[con_3],
                             width=10, height=10, command=lambda: change_price(list_1[con_3]))
            bun1.grid(row=con_1, column=con_2, sticky="nsew")
            con_1 += 1
            con_3 += 1
        con_2 += 1
        con_1 = 1
    but_1 = tk.Button(root, text="שינוי מחיר",
                      width=10, height=10, command=lambda: display.insert(0, "בחר מוצר :"))
    but_1.grid(row=3, column=3, sticky="nsew")
    but_2 = tk.Button(root, text=" חזור",
                      width=10, height=10, command=button)
    but_2.grid(row=1, column=3, sticky="nsew")
    but_3 = tk.Button(root, text="שינוי שם",
                      width=10, height=10)
    but_3.grid(row=2, column=3, sticky="nsew")

    def change_price(product):
        print(product)

        def on_enter(event):
            user_input = display.get()
            # print(user_input)
            for z in list_of_product.keys():
                if z == product:
                    list_of_product[item] = int(user_input)
                    print(list_of_product[item])
                else:
                    print("error")
                    print(product)

        display.delete(0, tk.END)
        display.bind("<Return>", on_enter)


def button():
    con_1 = 1
    con_2 = 0
    con_3 = 0
    list_1 = ["פיצהL", "סלט", "מאפה", "פיצהXL", "טוסט", "פלאפל", "פיצהXXL", "לאפה", "פיתה"]
    for item in range(3):
        for item1 in range(3):
            bun1 = tk.Button(root, text=list_1[con_3],
                             width=10, height=10, command=lambda: add_product(list_1[con_3]))
            bun1.grid(row=con_1, column=con_2, sticky="nsew")
            con_1 += 1
            con_3 += 1
        con_2 += 1
        con_1 = 1

    bun10 = tk.Button(root, text="חשבון חדש",
                      width=10, height=10, command=lambda: delete_sum_all())
    bun10.grid(row=3, column=3, sticky="nsew")

    bun11 = tk.Button(root, text="חיסור מוצר",
                      width=10, height=10, command=lambda: delete_subtract())
    bun11.grid(row=2, column=3, sticky="nsew")
    bun12 = tk.Button(root, text="הגדרות",
                      width=10, height=10, command=lambda: open_new_window())
    bun12.grid(row=1, column=3, sticky="nsew")


button()

root.mainloop()

# לחצים גירסה א'
# bun1 = tk.Button(root, text="פיצהL",
#                  width=10, height=10, command=lambda: add_product("פיצהL"))
# bun1.grid(row=1, column=0, sticky="nsew")
# bun2 = tk.Button(root, text="מאפה",
#                  width=10, height=10, command=lambda: add_product("מאפה"))
# bun2.grid(row=2, column=0, sticky="nsew")
# bun3 = tk.Button(root, text="סלט",
#                  width=10, height=10, command=lambda: add_product("סלט"))
# bun3.grid(row=3, column=0, sticky="nsew")
# bun4 = tk.Button(root, text="פיצהXL",
#                  width=10, height=10, command=lambda: add_product("פיצהXL"))
# bun4.grid(row=1, column=1, sticky="nsew")
# bun5 = tk.Button(root, text="טוסט",
#                  width=10, height=10, command=lambda: add_product("טוסט"))
# bun5.grid(row=2, column=1, sticky="nsew")
# bun6 = tk.Button(root, text="פלאפל",
#                  width=10, height=10, command=lambda: add_product("פלאפל"))
# bun6.grid(row=3, column=1, sticky="nsew")
# bun7 = tk.Button(root, text="פיצהXXL",
#                  width=10, height=10, command=lambda: add_product("פיצהXXL"))
# bun7.grid(row=1, column=2, sticky="nsew")
# bun8 = tk.Button(root, text="לאפה",
#                  width=10, height=10, command=lambda: add_product("לאפה"))
# bun8.grid(row=2, column=2, sticky="nsew")
# bun9 = tk.Button(root, text="פיתה",
#                  width=10, height=10, command=lambda: add_product("פיתה"))
# bun9.grid(row=3, column=2, sticky="nsew")


# bun1 = tk.Button(root, text="פיצהL",
#                  width=10, height=10, command=lambda: change_price("פיצהL"))
# bun1.grid(row=1, column=0, sticky="nsew")
# bun2 = tk.Button(root, text="מאפה",
#                  width=10, height=10, command=lambda: change_price("מאפה"))
# bun2.grid(row=2, column=0, sticky="nsew")
# bun3 = tk.Button(root, text="סלט",
#                  width=10, height=10, command=lambda: change_price("סלט"))
# bun3.grid(row=3, column=0, sticky="nsew")
# bun4 = tk.Button(root, text="פלאפל",
#                  width=10, height=10, command=lambda: change_price("פלאפל"))
# bun4.grid(row=2, column=1, sticky="nsew")
# bun5 = tk.Button(root, text="פיצהXL",
#                  width=10, height=10, command=lambda: change_price("פיצהXL"))
# bun5.grid(row=1, column=1, sticky="nsew")
# bun6 = tk.Button(root, text="פיצהXXL",
#                  width=10, height=10, command=lambda: change_price("פיצהXXL"))
# bun6.grid(row=1, column=2, sticky="nsew")
# bun7 = tk.Button(root, text="טוסט",
#                  width=10, height=10, command=lambda: change_price("טוסט"))
# bun7.grid(row=3, column=1, sticky="nsew")
# bun8 = tk.Button(root, text="לאפה",
#                  width=10, height=10, command=lambda: change_price("לאפה"))
# bun8.grid(row=3, column=2, sticky="nsew")
# bun9 = tk.Button(root, text="פיתה",
#                  width=10, height=10, command=lambda: change_price("פיתה"))
# bun9.grid(row=2, column=2, sticky="nsew")
