import Tkinter 
import tkMessageBox
import pkl_viewer as pk
import network as nt


def create_main_window():
    # Dhmioyrgia kyrioy para8yrou
    root = Tkinter.Tk()
    root.title("Hand written numbers ditector")

    # Orismos xrwmatos
    root.configure(bg="#2E3944")

    # Orismos ellaxistoy mege8ous para8yrou
    root.minsize(350, 200)

    def train():
        root.destroy()
        nt.start()

    def check():
        root.destroy()
        pk.view()
        check_root =Tkinter.Tk() 
        check_root.title("Hand written numbers ditector")
        check_root.configure(bg='#2E3944')
        check_root.minsize(350, 300)
        text=Tkinter.Label(check_root, text="Do you want to select this photo?",bg="#2E3944" ,font=("Helvetica",15,"bold"))
        yes_button=Tkinter.Button(check_root, text="Select this photo", command=train, width=15, height=4, bg="#D3D9D4", font=("Helvetica",10,"bold"))
        no_button=Tkinter.Button(check_root, text="Move to next photo", command=check, width=15, height=4, bg="#D3D9D4", font=("Helvetica",10,"bold"))
        exit1_button=Tkinter.Button(check_root, text="Exit", command=lambda: exit(check_root), width=15, height=4, bg="#D3D9D4", font=("Helvetica",10,"bold"))

        text.pack()
        yes_button.pack()
        no_button.pack()
        exit1_button.pack()

        text.grid(row=1, column=0,pady=(0,10))
        yes_button.grid(row=2, column=0, pady=(0,10))
        no_button.grid(row=3, column=0, pady=(0,10))
        exit1_button.grid(row=4, column=0, pady=(0,10))
        check_root.grid_columnconfigure(0,weight=1)

        return check_root

    def exit(name):
        name.destroy()
    #photo layaout
    image=Tkinter.PhotoImage(file="C:\Users\georg\Downloads\LogoVersionEN.gif")
    label=Tkinter.Label(root, image=image, width=350, height=170)
    label.grid(row=0, column=0, padx=5, pady=5, sticky="nw")
    label.image=image
    
    
    train_button=Tkinter.Button(root, text="Train", command = train, width=15, height=2, bg="#D3D9D4", font=("Helvetica",10,"bold"))
    check_button=Tkinter.Button(root, text="Find hand\nwritten number", command = check, width=15, height=5, bg="#D3D9D4", font=("Helvetica",10,"bold"))
    exit_button=Tkinter.Button(root, text="Exit", command=lambda: exit(root), width=15, height=2, bg="#D3D9D4", font=("Helvetica",10,"bold"))

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
    