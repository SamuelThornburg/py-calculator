import tkinter as tk

class CalculatorApp(tk.Tk):
	def __init__(self):
		super().__init__()

		self.title("Calculator")
		self.geometry("300x400")
		
		self.display = tk.Entry(self, font=("Arial", 24), justify="right")
		self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=10, ipady=10)

		buttons = [
		     ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
		     ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
		     ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
		     ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
			]

		for (text, row, col) in buttons:
			button = tk.Button(self, text=text, font=("Arial", 18), command=lambda t=text: self.on_button_click(t))
			button.grid(row=row, column=col, padx=5, pady=5, ipadx=10, ipady=10)

	def on_button_click(self, button_text):
		if button_text == "=":
			try:
				result = eval(self.display.get())
				self.display.delete(0, tk.END)
				self.display.insert(tk.END, str(result))
			except Exception as e:
				self.display.delete(0, tk.END)
				self.display.insert(tk.END, "Error")
		else:
			self.display.insert(tk.END, button_text)

if __name__ == "__main__":
	app = CalculatorApp()
	app.mainloop()
