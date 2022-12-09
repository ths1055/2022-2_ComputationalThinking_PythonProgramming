import tkinter as tk

LC=tk.Tk()
LC.title("Lenght Converter")
LC.geometry("450x100+450+155")

def convert_Kilo():
    E1_val_flo = float(E1_val.get())    
    mile=round(E1_val_flo/1.60934, 3)
    Entry2.delete(0,tk.END)
    Entry2.insert(tk.END,mile)
def convert_Mile():
    E2_val_flo=float(E2_val.get())
    km = round(E2_val_flo*1.60934, 3)
    Entry1.delete(0, tk.END)
    Entry1.insert(tk.END,km)

E1_val = tk.DoubleVar()
E2_val = tk.DoubleVar()

Entry1 = tk.Entry(LC, textvariable = E1_val)
Entry1.grid(row = 0, column = 1,pady=10,padx=10)
Entry2 = tk.Entry(LC, textvariable = E2_val)
Entry2.grid(row = 0, column = 3,pady=10,padx=10)

tk.Label(LC, text = 'km').grid(row = 0, column = 2,pady=10,padx=10)
tk.Label(LC, text = 'mile').grid(row = 0, column = 4,pady=10,padx=10)

tk.Button(LC, text = "KM -> MILE", command = convert_Kilo).grid(row = 1, column = 1,padx=10,pady=10)
tk.Button(LC, text = "MILE -> KM", command = convert_Mile).grid(row = 1, column = 3,padx=10,pady=10)
tk.Button(LC, text="Exit", command=LC.destroy).place(x=450,y=255)

LC.mainloop()