# import tkinter as tk
#
# def on_resize(event):
#     # Function to handle window resizing
#     new_width = event.width
#     new_height = event.height
#     print(f"Window resized to {new_width}x{new_height}")
#
# root = tk.Tk()
# root.title("Responsive Screen Example")
#
# # Create widgets
# label1 = tk.Label(root, text="Label 1", bg="lightblue")
# label2 = tk.Label(root, text="Label 2", bg="lightgreen")
# entry = tk.Entry(root)
# button = tk.Button(root, text="Click me")
#
# # Use grid to place widgets
# label1.grid(row=0, column=0, sticky="nsew")
# label2.grid(row=0, column=1, sticky="nsew")
# entry.grid(row=1, column=0, columnspan=2, sticky="nsew")
# button.grid(row=2, column=0, columnspan=2, sticky="nsew")
#
# # Configure row and column weights to make the layout responsive
# root.columnconfigure(0, weight=1)
# root.columnconfigure(1, weight=1)
# root.rowconfigure(0, weight=1)
# root.rowconfigure(1, weight=1)
# root.rowconfigure(2, weight=1)
#
# # Bind the resize event to the on_resize function
# root.bind("<Configure>", on_resize)
#
# root.mainloop()


