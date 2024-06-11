import Tkinter 
import tkMessageBox
import pkl_viewer as pk


def create_main_window():
    # Dhmioyrgia kyrioy para8yrou
    root = Tkinter.Tk()
    root.title("My App")

    # Orismos xrwmatos
    root.configure(bg='#2E3944')

    # Orismos ellaxistoy mege8ous para8yrou
    root.minsize(600, 400)

    def train():
        return 0

    def check():
        root.destroy()
        pk.view()
        check_root =Tkinter.Tk() 
        check_root.title("Second Window")
        yes_button = Tkinter.Button(check_root, text = "Select this photo", command = train)
        no_button = Tkinter.Button(check_root, text = "Move to next photo", command = check)

        yes_button.pack()
        no_button.pack()

    def exit():
        return 0

    image=Tkinter.PhotoImage(file="C:\Users\georg\Downloads\LogoVersionEN.gif")
    label=Tkinter.Label(root, image=image, width=350, height=170)
    label.grid(row=0, column=0, padx=5, pady=5, sticky="nw")
    label.image=image
    
    # Dhmiourgia koumpiwn me padding gia na perioristei to megisto mege8os
    train_button = Tkinter.Button(root, text = "Train", command = train, width=15, height=2, bg="#D3D9D4", font=("Helvetica",10,"bold"))
    check_button = Tkinter.Button(root, text = "Find hand\nwritten number", command = check, width=15, height=5, bg="#D3D9D4", font=("Helvetica",10,"bold"))
    exit_button = Tkinter.Button(root, text = "Exit", command = exit, width=15, height=2, bg="#D3D9D4", font=("Helvetica",10,"bold"))

    train_button.pack()
    check_button.pack()
    exit_button.pack()

    train_button.grid(row=1, column=0, pady=(0,10))
    check_button.grid(row=2, column=0, pady=(0,10))
    exit_button.grid(row=3, column=0,  pady=(0,10))
    root.grid_columnconfigure(0,weight=1)

    return root
        

if __name__ == "__main__":
    main_window = create_main_window()
    main_window.mainloop()
    