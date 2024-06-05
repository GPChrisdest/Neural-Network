import tkinter as tk

def create_main_window():
    # Δημιουργία του κύριου παραθύρου
    root = tk.Tk()
    root.title("My App")
   
    # Ορισμός του χρώματος φόντου
    root.configure(bg='#00CED1')  # Γαλαζοπράσινο χρώμα
   
    # Ορισμός ελάχιστου μεγέθους παραθύρου
    root.minsize(300, 100)
   
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=1)
    root.grid_rowconfigure(0, weight=1)
   
    # Δημιουργία κουμπιών με padding για να περιοριστεί το μέγιστο μέγεθος
    train_button = tk.Button(root, text="Train")
    check_button = tk.Button(root, text="Check")
    exit_button = tk.Button(root, text="Exit")
   
    train_button.grid(row=0, column=0, sticky='nsew', padx=10, pady=10, ipadx=10, ipady=10)
    check_button.grid(row=0, column=1, sticky='nsew', padx=10, pady=10, ipadx=10, ipady=10)
    exit_button.grid(row=0, column=2, sticky='nsew', padx=10, pady=10, ipadx=10, ipady=10)
   
    return root

if __name__ == "__main__":
    main_window = create_main_window()
    main_window.mainloop()
