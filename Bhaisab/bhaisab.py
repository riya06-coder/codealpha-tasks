
import tkinter as tk
from tkinter import messagebox

def save_data():
    data = {
        "Name":entry_name.get(),
        "Address":entry_address.get(),
        "Site": entry_site.get(),
        "Mode": entry_mode.get(),
        "Type of Material":entry_material.get(),
        "Size":entry_size.get(),
        "EGM":entry_egm.get(),
        "Quantity(CFT)":entry_quantity.get()
        
    }
    messagebox.showinfo("Saved",f"Data Saved\n{data}")

# create the main window
root = tk.Tk()
root.title("Construction Material Entry")


    # Labels and inputs
tk.Label(root,text="Name").grid(row=0,column=0)
entry_name=tk.Entry(root)
entry_name.grid(row=0,column=1)

tk.Label(root,text="Address").grid(row=1,column=0)
entry_address=tk.Entry(root)
entry_address.grid(row=1,column=1)

tk.Label(root,text="Site").grid(row=2,column=0)
entry_site=tk.Entry(root)
entry_site.grid(row=2,column=1)

tk.Label(root,text="Mode").grid(row=3,column=0)
entry_mode=tk.Entry(root)
entry_mode.grid(row=3,column=1)

tk.Label(root,text="Type of Material").grid(row=4,column=0)
entry_material=tk.Entry(root)
entry_material.grid(row=4,column=1)

tk.Label(root,text="Size").grid(row=5,column=0)
entry_size=tk.Entry(root)
entry_size.grid(row=5,column=1)


tk.Label(root,text="EGM").grid(row=6,column=0)
entry_egm=tk.Entry(root)
entry_egm.grid(row=6,column=1)


tk.Label(root,text="M.Sand").grid(row=7,column=0)
entry_msand=tk.Entry(root)
entry_msand.grid(row=7,column=1)

tk.Label(root,text="Dust").grid(row=8,column=0)
entry_dust=tk.Entry(root)
entry_dust.grid(row=8,column=1)




tk.Label(root,text="Quantity (CFT)").grid(row=9,column=0)
entry_quantity=tk.Entry(root)
entry_quantity.grid(row=9,column=1)

#Save button
tk.Button(root, text="Save Entry", command=save_data).grid(row=10, column=0, columnspan=2)

root.mainloop()
