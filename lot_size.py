from tkinter_project import Calculator
import customtkinter as ctk

entrys_name = ["Balance", "Risk", "SL Pips"]
class LotSize:
    def __init__(self, root):
        ctk.set_appearance_mode("dark")
        self.root = root
        self.root.title("Lot Size choice")
        
        self.calculater_tab = ctk.CTkTabview(self.root)
        self.calculater_tab.add("EUR/USD and GBP/USD")
        
        self.datail = {}
        self.tab(self.calculater_tab.tab("EUR/USD and GBP/USD"))
        
        self.button_press()

    def tab(self, master):
        self.entrys = []
        for i in range(3):
            self.create_entries(i, master)

        self.result_entry = ctk.CTkEntry(master)
        self.result_entry.grid(row=5, column=1, pady=10, padx=10)
        self.button = ctk.CTkButton(master, text="Calculate", command=self.lot_size)
        self.button.grid(row=5, column=0, pady=10, padx=10)
        self.calculater_tab.grid(row=0, column=0, pady=10, padx=10)
        self.calculater_button = ctk.CTkButton(master, text="do you want a normal colculater", command=self.calculator_win)
        self.calculater_button.grid(row=6, column=0)

        self.entrys_ = [(entry, i) for i, entry in enumerate(self.entrys)]
        
        self.set_cursor_position(self.result_entry)

    def set_cursor_position(self, entry, position="end"):
        entry.icursor(position)

    def button_press(self):
        self.root.bind("<Return>", self.enter_press)
        self.root.bind("<Up>", self.up_press)
        self.root.bind("<Down>", self.down_press)

    def enter_press(self, event):
        self.lot_size()

    def up_press(self, event):
        pass

    def down_press(self, event):
        pass

    def add_datail(self):
        self.datail = {}
        for i, key in enumerate(entrys_name):
            try:
                value = float(self.entrys[i].get().strip().replace(',', '.'))
            except ValueError:
                value = 0
            self.datail[key] = value
    
    def calculator_win(self):
        global calculator_app
        wn = ctk.CTk()
        calculator_app = Calculator(wn)
        wn.mainloop()

    def lot_size(self):
        self.add_datail()
        balance = self.datail["Balance"]
        risk = self.datail["Risk"]
        sl_pips = self.datail["SL Pips"]
        pip_value = 10
        if sl_pips <= 0:
            self.result_entry.delete(0, 'end')
            self.result_entry.insert(0, "SL pips must be greater than 0")
            return

        lot_size = (balance * (risk / 100)) / (sl_pips * pip_value)
        self.result_entry.delete(0, 'end')
        self.result_entry.insert(0, f"{lot_size:.2f}")

    def create_entries(self, i, master):
        self.label = ctk.CTkLabel(master, text=entrys_name[i])
        self.label.grid(row=i+1, column=0, pady=10, padx=10)
        self.entry = ctk.CTkEntry(master)
        self.entry.grid(row=i+1, column=1, pady=10, padx=20)
        self.entrys.append(self.entry)
        if entrys_name[i] == "Balance":
            self.entry.delete(0, 'end')
            self.entry.insert(0, "10000")
        elif entrys_name[i] == "Risk":
            self.entry.delete(0, 'end')
            self.entry.insert(0, "0.5")
if __name__ == "__main__":
    wn = ctk.CTk()
    calculator_app = LotSize(wn)
    wn.mainloop()
