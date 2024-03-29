def signup():
    
    import tkinter as tk
    from tkinter import font
    import mysql.connector as sql
    from signup_new_user import user_record_entry

    #root app
    root = tk.Toplevel()
    root.title("Password Manager")
    root.configure(background = "#7c898b")
    root.minsize(height=982, width=700)

    #sql connection 
    con = sql.connect(host = 'localhost', user = 'root', password = 'erummeraj', database = 'pw-manager')
    cur = con.cursor(buffered=True)

    #button action
    def call_func():
        result = user_record_entry(entry_username.get(), entry_password.get(), entry_email.get(), cur, con)
        print(result)
        if result == 1:
            succ=tk.Label(root,text = "Successful !!!", font=("times new roman" , 24 , "bold") , fg = "black", bg = "#d9d9d9")
            succ.place(x=270 , y =850)
        elif result == 0:
            incomp=tk.Label(root,text = "Fill all details ", font=("times new roman" , 24 , "bold") , fg = "black", bg = "#d9d9d9")
            incomp.place(x=270 , y =850)
        else:
            failed=tk.Label(root,text = "Something went wrong ", font=("times new roman" , 24 , "bold") , fg = "black", bg = "#d9d9d9")
            failed.place(x=270 , y =850)



    #layout
    frame = tk.Frame(root, bg="#d9d9d9", bd=5)
    frame.place(x=115 , y = 170 , height = 630 , width =450)

    background_image= tk.PhotoImage(file=r'/Users/momeraj/Documents/erum/learning-python-master/12th/split_code my exp/Logo-removebg-preview.png')
    background_label = tk.Label(root, image=background_image, bg = "#d9d9d9")
    background_label.place(x=140, y=180, width=400, height=200)


    welcomeback=tk.Label(frame,text = "SIGN UP!", font=("times new roman" , 35 , "bold") , fg = "black", bg = "#d9d9d9")
    welcomeback.place(x=150 , y =250)

    username=tk.Label(frame,text = "Username", font=("times new roman" , 24 , "bold") , fg = "black", bg = "#d9d9d9")
    username.place(x= 80  , y =320)

    entry_username = tk.Entry(frame, font=('Bookman Old Style', 18), bg="white", fg="black")
    entry_username.place(x=80  , y =350 , width = 270)

    password=tk.Label(frame,text = "Password", font=("times new roman" , 24 , "bold") , fg = "black", bg = "#d9d9d9")
    password.place(x= 80  , y =500)

    bullet = "\u2022" 
    entry_password = tk.Entry(frame, font=('Bookman Old Style', 18), bg="white", fg="black", show=bullet)
    entry_password.place(x= 80  , y =530, width = 270)

    email=tk.Label(frame,text = "Email", font=("times new roman" , 24 , "bold") , fg = "black", bg = "#d9d9d9")
    email.place(x= 80  , y =410)

    bullet = "\u2022" 
    entry_email = tk.Entry(frame, font=('Bookman Old Style', 18), bg="white", fg="black")
    entry_email.place(x= 80  , y =440 , width = 270)

    button_login = tk.Button(frame, text="Sign Up", font=('Bookman Old Style', 14), bg='#ffffff', fg="black" , command = lambda: call_func())
    button_login.place(x=155,y=580, height=35, width=120)

    root.mainloop()
    return