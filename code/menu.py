import Tkinter 
import tkMessageBox

def create_main_window():
    # Dhmioyrgia kyrioy para8yrou
    root = Tkinter.Tk()
    root.title("My App")
   
    # Orismos xrwmatos
    root.configure(bg='#00CED1')
   
    # Orismos ellaxistoy mege8ous para8yrou
    root.minsize(300, 100)
   
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=1)
    root.grid_rowconfigure(0, weight=1)

    def train():
        return 0

    def check():
        return 0

    def exit():
        return 0
       
    # Dhmiourgia koumpiwn me padding gia na perioristei to megisto mege8os
    train_button = Tkinter.Button(root, text = "Train", command = train)
    check_button = Tkinter.Button(root, text = "Check", command = check)
    exit_button = Tkinter.Button(root, text = "Exit", command = exit)

    train_button.pack()
    check_button.pack()
    exit_button.pack()
   
    train_button.grid(row=0, column=0, sticky='nsew', padx=10, pady=10, ipadx=10, ipady=10)
    check_button.grid(row=0, column=1, sticky='nsew', padx=10, pady=10, ipadx=10, ipady=10)
    exit_button.grid(row=0, column=2, sticky='nsew', padx=10, pady=10, ipadx=10, ipady=10)

    exit_button.grid(row=0, column=2, sticky='nsew', padx=10, pady=10, ipadx=10, ipady=10)
   
    return root

if __name__ == "__main__":
    main_window = create_main_window()
    main_window.mainloop()
    