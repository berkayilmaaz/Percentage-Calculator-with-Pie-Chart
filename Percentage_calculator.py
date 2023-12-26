import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import webbrowser

def calculate_percentage_and_plot():
    try:
        total = float(entry_total.get())
        part = float(entry_part.get())
        if total <= 0:
            messagebox.showerror("Error", "Total must be greater than zero.")
            return

        percentage = (part * 100) / total
        label_result.config(text=f"{part} is {percentage:.2f}% of {total}")

      
        sizes = [part, total - part]
        labels = [f'Part: {part}', f'Remaining: {total - part}']
        colors = ['#ff9999','#66b3ff']

    
        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  

     
        canvas = FigureCanvasTkAgg(fig, master=window)  
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack()

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

def close_window():
    window.destroy()

def open_github():
    webbrowser.open_new("https://github.com/berkayilmaaz")

window = tk.Tk()
window.title("Percentage Calculator with Pie Chart")

label_total = tk.Label(window, text="Enter total number:")
label_total.pack()

entry_total = tk.Entry(window)
entry_total.pack()

label_part = tk.Label(window, text="Enter part number:")
label_part.pack()

entry_part = tk.Entry(window)
entry_part.pack()

calculate_button = tk.Button(window, text="Calculate", command=calculate_percentage_and_plot)
calculate_button.pack()

label_result = tk.Label(window, text="")
label_result.pack()

github_label = tk.Label(window, text="github.com/berkayilmaaz", fg="blue", cursor="hand2")
github_label.pack()
github_label.bind("<Button-1>", lambda e: open_github())

exit_button = tk.Button(window, text="Exit", command=close_window)
exit_button.pack()

window.mainloop()
