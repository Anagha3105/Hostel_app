from tkinter import *
import codecs
import webbrowser
d = [('Anagha', 'Rao'), ('Anushka', 'Jalori'), ('Tanu', 'R'), ('Netra', 'J')]
inp = []


def main():

    global d, inp

    def user():
        root = Tk()

        def butt():
            if inp == []:
                inp.append(e1.get())
                inp.append(e2.get())
            else:
                inp[0] = e1.get()
                inp[1] = e2.get()
            if tuple(inp) in d:
                root.destroy()
                eroot = Tk()
                succ = Label(eroot, text='You Have Successfully logged In', font=(
                    'calibre', 10, 'bold'))
                eroot.geometry("200x200")

                succ.pack()

            else:
                errl = Label(root, text='Sorry User/Pass does not exist',
                             font=('calibre', 10, 'bold'))
                errl.grid(row=4, column=0)

        e1 = Entry(root, width=40)
        e2 = Entry(root, width=40)
        l1 = Label(root, text='Username', font=('calibre', 10, 'bold'))
        l2 = Label(root, text='Password', font=('calibre', 10, 'bold'))
        b1 = Button(root, text='Login', font=(
            'calibre', 10, 'bold'), command=butt)
        root.geometry("700x100")
        e1.grid(row=0, column=0)
        e2.grid(row=0, column=2)
        l1.grid(row=1, column=0)
        l2.grid(row=1, column=2)
        b1.grid(row=2, column=1)
        mainloop()
    user()


main()
