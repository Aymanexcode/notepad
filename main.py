import tkinter as tk
from tkinter import filedialog, messagebox, ttk

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Notepad")
        self.root.geometry("700x500")

        # Style:
        self.style = ttk.Style(self.root)
        self.style.configure('TButton', font=('Arial', 10, 'bold'), background='#4CAF50', fontground='white')
        self.style.configure('TFrame', background='#F0F0F0')
        self.style.configure('TLabel', background='#F0F0F0', font=('Arial', 10, 'bold'))

        # Text:
        self.text_area = tk.Text(self.root, font=('Arial', 12), bg='#f9f9f9', fg='#333333', insertbackground='#000000')
        self.text_area.pack(expand=True, fill='both', padx=10, pady=10)

        # Menu bar:
        self.menu_bar = tk.Menu(self.root, bg='#4CAF50', fg='white', font=('Arial', 10, 'bold'))
        self.root.config(menu=self.menu_bar)

        # File Menu:
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0, bg='#4CAF50', fg='white', font=('Arial', 10))
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit_app)

        # Edit Menu:
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0, bg='#4CAF50', fg='white', font=('Arial', 10))
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Cut", command=self.cut_text)
        self.edit_menu.add_command(label="Copy", command=self.copy_text)
        self.edit_menu.add_command(label="Paste", command=self.paste_text)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Select All", command=self.select_all)
        self.edit_menu.add_command(label="Clear All", command=self.clear_all)

    def new_file(self):
        self.text_area.delete(1.0, tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt",
                                               filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, file.read())

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                               filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))
            messagebox.showinfo("File Saved", "Your file has been saved successfully!")

    def exit_app(self):
        self.root.quit()

    def cut_text(self):
        self.text_area.event_generate("<<Cut>>")

    def copy_text(self):
        self.text_area.event_generate("<<Copy>>")
    
    def paste_text(self):
        self.text_area.event_generate("<<Paste>>")

    def select_all(self):
        self.text_area.tag_add(tk.SEL, "1.0", tk.END)
        self.text_area.mark_set(tk.INSERT, "1.0")
        self.text_area.see(tk.INSERT)


    def clear_all(self):
        self.text_area.delete(1.0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    notepad = Notepad(root)
    root.mainloop()

