from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox
import secrets
import time

root = Tk()
root.minsize(700, 660)
wid = 600
can = Canvas(root, width=wid, height=wid)

col = 'pink'


def vic():
    global root
    root.iconbitmap("icon_victory.ico")
    root.update()


def tt():
    global root
    root.iconbitmap("icon_tic_tac_toe.ico")
    root.update()


def check(l: list):
    if l[0][0] == l[1][1] == l[2][2] != "" and type(l[0][0]) == type(l[1][1]) == type(l[2][2]) == type('x'):
        x = l[0][0]
        return True, x

    elif l[0][2] == l[1][1] == l[2][0] != "" and type(l[0][2]) == type(l[1][1]) == type(l[2][0]) == type('x'):
        x = l[0][2]
        return True, x

    for i in range(0, 3):
        if l[i][0] == l[i][1] == l[i][2] != "" and type(l[i][0]) == type(l[i][1]) == type(l[i][2]) == type('x'):
            x = l[i][0]
            return True, x

        elif l[0][i] == l[1][i] == l[2][i] != "" and type(l[0][i]) == type(l[1][i]) == type(l[2][i]) == type('x'):
            x = l[0][i]
            return True, x


def human_vs_human(xname, oname):
    global can, root
    tt()
    root.minsize(468, 500)
    root.title(f'Tic Tac Toe\\{xname} vs {oname}')
    root.update()
    can.place(x=0, y=0)
    l = [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""]
    ]
    ll = [""]

    def imh(r, c, btn: Button):
        rr = int(btn.grid_info()['row'])
        cc = int(btn.grid_info()['column'])
        y = [b00, b01, b02, b10, b11, b12, b20, b21, b22]
        lb = Label(can, bg='pink')
        if check(l):
            btn['state'] = DISABLED
        else:
            btn['state'] = DISABLED
            imx = ImageTk.PhotoImage(Image.open('imgx.png'))
            imo = ImageTk.PhotoImage(Image.open('imgo.png'))
            if ll[-1] == 'x':
                ll.append('o')
                l[rr][cc] = 'o'
                im = imo
            else:
                ll.append('x')
                l[rr][cc] = 'x'
                im = imx

            lb.image = im
            lb.configure(image=im)
            lb.grid(row=r, column=c)
            lb.update()

            def drw():
                yn = []
                for i in y:
                    if i['state'] == DISABLED:
                        yn.append(True)
                if len(yn) == 9 and all(yn):
                    return True

            if check(l):
                for i in y:
                    i['state'] = DISABLED
                nm = check(l)[1].capitalize()
                if nm == 'X':
                    msg = 'Winner : ' + xname + '\nPlay Again'
                else:
                    msg = 'Winner : ' + oname + '\nPlay Again'
                vic()
                chh = tkinter.messagebox.askyesno('Winner', msg)
                if chh:
                    tt()
                    human_vs_human(oname, xname)
                else:
                    close()
            elif drw():
                vic()
                chh = tkinter.messagebox.askyesno('Tie', "Match tie\nPlay Again")
                if chh:
                    tt()
                    human_vs_human(oname, xname)
                else:
                    close()

    b00 = Button(can, bg=col, width=20, height=10, relief="groove", borderwidth=5, command=lambda: imh(0, 0, b00))
    b00.grid(row=0, column=0)
    b01 = Button(can, relief="groove", bg=col, width=20, height=10, borderwidth=5, command=lambda: imh(0, 1, b01))
    b01.grid(row=0, column=1)
    b02 = Button(can, bg=col, relief="groove", width=20, height=10, borderwidth=5, command=lambda: imh(0, 2, b02))
    b02.grid(row=0, column=2)
    b10 = Button(can, bg=col, width=20, relief="groove", height=10, borderwidth=5, command=lambda: imh(1, 0, b10))
    b10.grid(row=1, column=0)
    b11 = Button(can, bg=col, width=20, relief="groove", height=10, borderwidth=5, command=lambda: imh(1, 1, b11))
    b11.grid(row=1, column=1)
    b12 = Button(can, bg=col, width=20, height=10, relief="groove", borderwidth=5, command=lambda: imh(1, 2, b12))
    b12.grid(row=1, column=2)
    b20 = Button(can, relief="groove", bg=col, width=20, height=10, borderwidth=5, command=lambda: imh(2, 0, b20))
    b20.grid(row=2, column=0)
    b21 = Button(can, bg=col, relief="groove", width=20, height=10, borderwidth=5, command=lambda: imh(2, 1, b21))
    b21.grid(row=2, column=1)
    b22 = Button(can, bg=col, width=20, relief="groove", height=10, borderwidth=5, command=lambda: imh(2, 2, b22))
    b22.grid(row=2, column=2)

    def all_key(val):
        sq = (b00, b01, b02, b10, b11, b12, b20, b21, b22)
        var = val.keycode
        if 97 <= int(var) <= 105:
            idx = int(var) - 97
            a = sq[idx]
            r, c = a.grid_info()['row'], a.grid_info()['column']
            if a['state'] != DISABLED:
                imh(r, c, a)
        elif 49 <= int(var) <= 57:
            idx = int(var) - 49
            a = sq[idx]
            r, c = a.grid_info()['row'], a.grid_info()['column']
            if a['state'] != DISABLED:
                imh(r, c, a)

    root.bind('<Key>', all_key)


def human_vs_john(xname, oname):
    global can, root
    tt()
    root.minsize(468, 500)
    root.title(f'Tic Tac Toe\\{xname} vs {oname}')
    root.update()
    can.place(x=0, y=0)
    lst = [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""]
    ]

    def imx(btn):
        r, c = int(btn.grid_info()['row']), int(btn.grid_info()['column'])
        lst[r][c] = 'x'
        btn['state'] = DISABLED
        im = ImageTk.PhotoImage(Image.open('imgx.png'))
        l = Label(can, bg='pink', )
        l.image = im
        l.configure(image=im)
        l.grid(row=r, column=c)
        l.update()
        john()

    def imo(btn):
        time.sleep(0.1)
        r, c = int(btn.grid_info()['row']), int(btn.grid_info()['column'])
        lst[r][c] = 'o'
        btn['state'] = DISABLED
        im = ImageTk.PhotoImage(Image.open('imgo.png'))
        l = Label(can, bg='pink', )
        l.image = im
        l.configure(image=im)
        l.grid(row=r, column=c)
        l.update()

    def john():

        btns = [b00, b01, b02, b10, b11, b12, b20, b21, b22]
        y = [b00, b01, b02, b10, b11, b12, b20, b21, b22]

        def drw():
            if not check(lst):
                yn = []
                for i in y:
                    if i['state'] == DISABLED:
                        yn.append(True)
                if len(yn) == 9 and all(yn):
                    return True

        if check(lst):
            for i in btns:
                i['state'] = DISABLED
            nm = check(lst)[1].capitalize()
            if nm == 'X':
                msg = 'Winner : ' + xname + "\nPlay Again"
            else:
                msg = 'Winner : ' + oname + "\nPlay Again"
            vic()
            chh = tkinter.messagebox.askyesno('Winner', msg)
            if chh:
                tt()
                human_vs_john(xname, oname)
            else:
                close()
        elif drw():
            vic()
            chh = tkinter.messagebox.askyesno('Tie', "Match tie\nPlay Again")
            if chh:
                tt()
                human_vs_john(xname, oname)
            else:
                close()
        else:
            while True:
                try:
                    ch = secrets.choice(btns)
                except IndexError:
                    break
                if ch['state'] != DISABLED:
                    btns.remove(ch)
                    imo(ch)
                    break
                else:
                    btns.remove(ch)
            if check(lst):
                for i in btns:
                    i['state'] = DISABLED
                nm = check(lst)[1].capitalize()
                if nm == 'X':
                    msg = 'Winner : ' + xname + "\nPlay Again"
                else:
                    msg = 'Winner : ' + oname + "\nPlay Again"
                vic()
                chh = tkinter.messagebox.askyesno('Winner', msg)
                if chh:
                    tt()
                    human_vs_john(xname, oname)
                else:
                    close()
            elif drw():
                vic()
                chh = tkinter.messagebox.askyesno('Tie', "Match tie\nPlay Again")
                if chh:
                    tt()
                    human_vs_john(xname, oname)
                else:
                    close()

    col = 'pink'
    b00 = Button(can, bg=col, width=20, height=10, relief="groove", borderwidth=5, command=lambda: imx(b00))
    b00.grid(row=0, column=0)
    b01 = Button(can, bg=col, width=20, height=10, relief="groove", borderwidth=5, command=lambda: imx(b01))
    b01.grid(row=0, column=1)
    b02 = Button(can, bg=col, width=20, height=10, relief="groove", borderwidth=5, command=lambda: imx(b02))
    b02.grid(row=0, column=2)
    b10 = Button(can, bg=col, width=20, height=10, relief="groove", borderwidth=5, command=lambda: imx(b10))
    b10.grid(row=1, column=0)
    b11 = Button(can, bg=col, width=20, height=10, relief="groove", borderwidth=5, command=lambda: imx(b11))
    b11.grid(row=1, column=1)
    b12 = Button(can, bg=col, width=20, height=10, relief="groove", borderwidth=5, command=lambda: imx(b12))
    b12.grid(row=1, column=2)
    b20 = Button(can, bg=col, width=20, height=10, relief="groove", borderwidth=5, command=lambda: imx(b20))
    b20.grid(row=2, column=0)
    b21 = Button(can, bg=col, width=20, height=10, relief="groove", borderwidth=5, command=lambda: imx(b21))
    b21.grid(row=2, column=1)
    b22 = Button(can, bg=col, width=20, height=10, relief="groove", borderwidth=5, command=lambda: imx(b22))
    b22.grid(row=2, column=2)

    def all_key(val):
        sq = (b00, b01, b02, b10, b11, b12, b20, b21, b22)
        var = val.keycode
        if 97 <= int(var) <= 105:
            idx = int(var) - 97
            a = sq[idx]
            if a['state'] != DISABLED:
                imx(a)
        elif 49 <= int(var) <= 57:
            idx = int(var) - 49
            a = sq[idx]
            if a['state'] != DISABLED:
                imx(a)

    root.bind('<Key>', all_key)


def human_vs_shivang(xname, oname):
    global can, root
    tt()
    root.minsize(468, 500)
    root.title(f'Tic Tac Toe\\{xname} vs {oname}')
    root.update()
    can.place(x=0, y=0)
    lst = [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""]
    ]
    res = []

    def imx(btn):
        r, c = int(btn.grid_info()['row']), int(btn.grid_info()['column'])
        lst[r][c] = 'x'
        btn['state'] = DISABLED
        im = ImageTk.PhotoImage(Image.open('imgx.png'))
        l = Label(can, bg='pink', )
        l.image = im
        l.configure(image=im)
        l.grid(row=r, column=c)
        l.update()
        shivang(btn)

    def imo(btn):
        time.sleep(0.1)
        r, c = int(btn.grid_info()['row']), int(btn.grid_info()['column'])
        lst[r][c] = 'o'
        btn['state'] = DISABLED
        im = ImageTk.PhotoImage(Image.open('imgo.png'))
        l = Label(can, bg='pink', )
        l.image = im
        l.configure(image=im)
        l.grid(row=r, column=c)
        l.update()

    def play(y, btnn):
        res.append(y.index(btnn) + 1)
        b1 = b00
        b2 = b01
        b3 = b02
        b4 = b10
        b5 = b11
        b6 = b12
        b7 = b20
        b8 = b21
        b9 = b22
        try:
            if res[0] == 1:
                imo(b5)
                if res[1] == 2:
                    imo(b3)
                    if res[2] == 7:
                        imo(b4)
                        if res[3] == 6:
                            imo(b8)
                        else:
                            imo(b6)
                    else:
                        imo(b7)

                elif res[1] == 3:
                    imo(b2)
                    if res[2] == 8:
                        imo(b4)
                        if res[3] == 6:
                            imo(b9)
                        else:
                            imo(b6)

                    else:
                        imo(b8)

                elif res[1] == 4:
                    imo(b7)
                    if res[2] == 3:
                        imo(b2)
                        if res[3] == 8:
                            imo(b6)
                        else:
                            imo(b8)

                    else:
                        imo(b3)

                elif res[1] == 6:
                    imo(b2)
                    if res[2] == 8:
                        imo(b9)
                        if res[3] == 4:
                            imo(b7)
                        else:
                            imo(b4)

                    else:
                        imo(b8)

                elif res[1] == 7:
                    imo(b4)
                    if res[2] == 6:
                        imo(b3)
                        if res[3] == 8:
                            imo(b9)
                        else:
                            imo(b8)

                    else:
                        imo(b6)

                elif res[1] == 8:
                    imo(b7)
                    if res[2] == 3:
                        imo(b2)
                        if res[3] == 6:
                            imo(b9)
                        else:
                            imo(b6)

                    else:
                        imo(b3)

                elif res[1] == 9:
                    imo(b2)
                    if res[2] == 8:
                        imo(b7)
                        if res[3] == 3:
                            imo(b6)
                        else:
                            imo(b3)
                    else:
                        imo(b8)

            elif res[0] == 2:
                imo(b5)
                if res[1] == 1:
                    imo(b3)
                    if res[2] == 7:
                        imo(b4)
                        if res[3] == 6:
                            imo(b9)
                        else:
                            imo(b6)

                    else:
                        imo(b7)
                elif res[1] == 3:
                    imo(b1)
                    if res[2] == 9:
                        imo(b6)
                        if res[3] == 4:
                            imo(b7)
                        else:
                            imo(b4)
                    else:
                        imo(b9)
                elif res[1] == 4:
                    imo(b1)
                    if res[2] == 9:
                        imo(b7)
                        if res[3] == 3:
                            imo(b6)
                        else:
                            imo(b3)
                    else:
                        imo(b9)
                elif res[1] == 6:
                    imo(b3)
                    if res[2] == 7:
                        imo(b1)
                        if res[3] == 9:
                            imo(b8)
                        else:
                            imo(b9)
                    else:
                        imo(b7)
                elif res[1] == 7:
                    imo(b4)
                    if res[2] == 6:
                        imo(b9)
                        if res[3] == 1:
                            imo(b3)
                        else:
                            imo(b1)
                    else:
                        imo(b6)
                elif res[1] == 8:
                    imo(b4)
                    if res[2] == 6:
                        imo(b1)
                        if res[3] == 7:
                            imo(b9)
                        else:
                            imo(b7)
                    else:
                        imo(b6)
                elif res[1] == 9:
                    imo(b3)
                    if res[2] == 7:
                        imo(b8)
                        if res[3] == 1:
                            imo(b4)
                        else:
                            imo(b1)
                    else:
                        imo(b7)
            elif res[0] == 3:
                imo(b5)
                if res[1] == 1:
                    imo(b2)
                    if res[2] == 8:
                        imo(b4)
                        if res[3] == 6:
                            imo(b9)
                        else:
                            imo(b6)
                    else:
                        imo(b8)
                elif res[1] == 2:
                    imo(b1)
                    if res[2] == 9:
                        imo(b6)
                        if res[3] == 4:
                            imo(b7)
                        else:
                            imo(b4)
                    else:
                        imo(b9)
                elif res[1] == 4:
                    imo(b1)
                    if res[2] == 9:
                        imo(b6)
                        if res[3] == 7:
                            imo(b8)
                        else:
                            imo(b7)
                    else:
                        imo(b9)
                elif res[1] == 6:
                    imo(b9)
                    if res[2] == 1:
                        imo(b2)
                        if res[3] == 8:
                            imo(b4)
                        else:
                            imo(b8)
                    else:
                        imo(b1)
                elif res[1] == 7:
                    imo(b2)
                    if res[2] == 8:
                        imo(b9)
                        if res[3] == 1:
                            imo(b4)
                        else:
                            imo(b1)
                    else:
                        imo(b8)
                elif res[1] == 8:
                    imo(b6)
                    if res[2] == 4:
                        imo(b1)
                        if res[3] == 9:
                            imo(b7)
                        else:
                            imo(b9)
                    else:
                        imo(b4)
                elif res[1] == 9:
                    imo(b6)
                    if res[2] == 4:
                        imo(b2)
                        if res[3] == 8:
                            imo(b7)
                        else:
                            imo(b8)
                    else:
                        imo(b4)
            elif res[0] == 4:
                imo(b5)
                if res[1] == 1:
                    imo(b7)
                    if res[2] == 3:
                        imo(b2)
                        if res[3] == 8:
                            imo(b9)
                        else:
                            imo(b8)
                    else:
                        imo(b3)
                elif res[1] == 2:
                    imo(b1)
                    if res[2] == 9:
                        imo(b3)
                        if res[3] == 7:
                            imo(b8)
                        else:
                            imo(b7)
                    else:
                        imo(b9)
                elif res[1] == 3:
                    imo(b1)
                    if res[2] == 9:
                        imo(b6)
                        if res[3] == 8:
                            imo(b7)
                        else:
                            imo(b8)
                    else:
                        imo(b9)
                elif res[1] == 6:
                    imo(b2)
                    if res[2] == 8:
                        imo(b1)
                        if res[3] == 3:
                            imo(b9)
                        else:
                            imo(b3)
                    else:
                        imo(b8)
                elif res[1] == 7:
                    imo(b1)
                    if res[2] == 9:
                        imo(b8)
                        if res[3] == 2:
                            imo(b3)
                        else:
                            imo(b2)
                    else:
                        imo(b9)
                elif res[1] == 8:
                    imo(b7)
                    if res[2] == 3:
                        imo(b1)
                        if res[3] == 9:
                            imo(b6)
                        else:
                            imo(b9)
                    else:
                        imo(b3)
                elif res[1] == 9:
                    imo(b7)
                    if res[2] == 3:
                        imo(b6)
                        if res[3] == 2:
                            imo(b1)
                        else:
                            imo(b2)
                    else:
                        imo(b3)
            elif res[0] == 5:
                imo(b1)
                if res[1] == 2:
                    imo(b8)
                    if res[2] == 3:
                        imo(b7)
                        if res[3] == 4:
                            imo(b9)
                        else:
                            imo(b4)
                    elif res[2] == 4:
                        imo(b6)
                        if res[3] == 3:
                            imo(b7)
                        else:
                            imo(b3)
                    elif res[2] == 6:
                        imo(b4)
                        if res[3] == 7:
                            imo(b3)
                        else:
                            imo(b7)
                    elif res[2] == 7:
                        imo(b3)
                        if res[3] == 4:
                            imo(b6)
                        else:
                            imo(b4)
                    elif res[2] == 9:
                        imo(b7)
                        if res[3] == 4:
                            imo(b6)
                        else:
                            imo(b4)
                elif res[1] == 3:
                    imo(b7)
                    if res[2] == 4:
                        imo(b6)
                        if res[3] == 2:
                            imo(b8)
                        else:
                            imo(b2)
                    else:
                        imo(b4)
                elif res[1] == 4:
                    imo(b6)
                    if res[2] == 2:
                        imo(b8)
                        if res[3] == 3:
                            imo(b7)
                        else:
                            imo(b3)
                    elif res[2] == 3:
                        imo(b7)
                        if res[3] == 8:
                            imo(b2)
                        else:
                            imo(b8)
                    elif res[2] == 7:
                        imo(b3)
                        if res[3] == 2:
                            imo(b9)
                        else:
                            imo(b2)
                    elif res[2] == 8:
                        imo(b2)
                        if res[3] == 3:
                            imo(b7)
                        else:
                            imo(b3)
                    elif res[2] == 9:
                        imo(b8)
                        if res[3] == 3:
                            imo(b7)
                        else:
                            imo(b3)
                elif res[1] == 6:
                    imo(b4)
                    if res[2] == 7:
                        imo(b3)
                        if res[3] == 2:
                            imo(b8)
                        else:
                            imo(b2)
                    else:
                        imo(b7)
                elif res[1] == 7:
                    imo(b3)
                    if res[2] == 2:
                        imo(b8)
                        if res[3] == 6:
                            imo(b4)
                        else:
                            imo(b6)
                    else:
                        imo(b2)
                elif res[1] == 8:
                    imo(b2)
                    if res[2] == 3:
                        imo(b7)
                        if res[3] == 4:
                            imo(b6)
                        else:
                            imo(b4)
                    else:
                        imo(b3)
                elif res[1] == 9:
                    imo(b3)
                    if res[2] == 2:
                        imo(b8)
                        if res[3] == 4:
                            imo(b6)
                        else:
                            imo(b4)
                    else:
                        imo(b2)
            elif res[0] == 6:
                imo(b5)
                if res[1] == 1:
                    imo(b2)
                    if res[2] == 8:
                        imo(b7)
                        if res[3] == 3:
                            imo(b9)
                        else:
                            imo(b3)
                    else:
                        imo(b8)
                elif res[1] == 2:
                    imo(b3)
                    if res[2] == 7:
                        imo(b1)
                        if res[3] == 9:
                            imo(b8)
                        else:
                            imo(b9)
                    else:
                        imo(b7)
                elif res[1] == 3:
                    imo(b9)
                    if res[2] == 1:
                        imo(b2)
                        if res[3] == 8:
                            imo(b4)
                        else:
                            imo(b8)
                    else:
                        imo(b1)
                elif res[1] == 4:
                    imo(b2)
                    if res[2] == 8:
                        imo(b1)
                        if res[3] == 3:
                            imo(b9)
                        else:
                            imo(b3)
                    else:
                        imo(b8)
                elif res[1] == 7:
                    imo(b8)
                    if res[2] == 2:
                        imo(b1)
                        if res[3] == 9:
                            imo(b3)
                        else:
                            imo(b9)
                    else:
                        imo(b2)
                elif res[1] == 8:
                    imo(b9)
                    if res[2] == 1:
                        imo(b3)
                        if res[3] == 7:
                            imo(b4)
                        else:
                            imo(b7)
                    else:
                        imo(b1)
                elif res[1] == 9:
                    imo(b3)
                    if res[2] == 7:
                        imo(b8)
                        if res[3] == 2:
                            imo(b4)
                        else:
                            imo(b2)
                    else:
                        imo(b7)
            elif res[0] == 7:
                imo(b5)
                if res[1] == 1:
                    imo(b4)
                    if res[2] == 6:
                        imo(b2)
                        if res[3] == 8:
                            imo(b9)
                        else:
                            imo(b8)
                    else:
                        imo(b6)
                elif res[1] == 2:
                    imo(b1)
                    if res[2] == 9:
                        imo(b8)
                        if res[3] == 6:
                            imo(b3)
                        else:
                            imo(b6)
                    else:
                        imo(b9)

                elif res[1] == 3:
                    imo(b2)
                    if res[2] == 8:
                        imo(b9)
                        if res[3] == 1:
                            imo(b4)
                        else:
                            imo(b1)
                    else:
                        imo(b8)
                elif res[1] == 4:
                    imo(b1)
                    if res[2] == 9:
                        imo(b8)
                        if res[3] == 2:
                            imo(b3)
                        else:
                            imo(b2)
                    else:
                        imo(b9)
                elif res[1] == 6:
                    imo(b9)
                    if res[2] == 1:
                        imo(b4)
                        if res[3] == 2:
                            imo(b3)
                        else:
                            imo(b2)
                    else:
                        imo(b1)
                elif res[1] == 8:
                    imo(b9)
                    if res[2] == 1:
                        imo(b4)
                        if res[3] == 6:
                            imo(b2)
                        else:
                            imo(b6)
                    else:
                        imo(b1)
                elif res[1] == 9:
                    imo(b8)
                    if res[2] == 2:
                        imo(b4)
                        if res[3] == 6:
                            imo(b3)
                        else:
                            imo(b6)
                    else:
                        imo(b2)
            elif res[0] == 8:
                imo(b5)
                if res[1] == 1:
                    imo(b4)
                    if res[2] == 6:
                        imo(b3)
                        if res[3] == 7:
                            imo(b9)
                        else:
                            imo(b7)
                    else:
                        imo(b6)
                elif res[1] == 2:
                    imo(b4)
                    if res[2] == 6:
                        imo(b1)
                        if res[3] == 7:
                            imo(b9)
                        else:
                            imo(b7)
                    else:
                        imo(b6)
                elif res[1] == 3:
                    imo(b6)
                    if res[2] == 4:
                        imo(b1)
                        if res[3] == 9:
                            imo(b7)
                        else:
                            imo(b9)
                    else:
                        imo(b4)
                elif res[1] == 4:
                    imo(b7)
                    if res[2] == 3:
                        imo(b1)
                        if res[3] == 9:
                            imo(b6)
                        else:
                            imo(b9)
                    else:
                        imo(b3)
                elif res[1] == 6:
                    imo(b9)
                    if res[2] == 1:
                        imo(b3)
                        if res[3] == 7:
                            imo(b4)
                        else:
                            imo(b7)
                    else:
                        imo(b1)
                elif res[1] == 7:
                    imo(b9)
                    if res[2] == 1:
                        imo(b4)
                        if res[3] == 6:
                            imo(b3)
                        else:
                            imo(b6)
                    else:
                        imo(b1)
                elif res[1] == 9:
                    imo(b7)
                    if res[2] == 3:
                        imo(b6)
                        if res[3] == 4:
                            imo(b2)
                        else:
                            imo(b4)
                    else:
                        imo(b3)
            elif res[0] == 9:
                imo(b5)
                if res[1] == 1:
                    imo(b2)
                    if res[2] == 8:
                        imo(b7)
                        if res[3] == 3:
                            imo(b6)
                        else:
                            imo(b3)
                    else:
                        imo(b8)
                elif res[1] == 2:
                    imo(b3)
                    if res[2] == 7:
                        imo(b8)
                        if res[3] == 1:
                            imo(b4)
                        else:
                            imo(b1)
                    else:
                        imo(b7)
                elif res[1] == 3:
                    imo(b6)
                    if res[2] == 4:
                        imo(b2)
                        if res[3] == 8:
                            imo(b7)
                        else:
                            imo(b8)
                    else:
                        imo(b4)
                elif res[1] == 4:
                    imo(b7)
                    if res[2] == 3:
                        imo(b6)
                        if res[3] == 1:
                            imo(b2)
                        else:
                            imo(b1)
                    else:
                        imo(b3)
                elif res[1] == 6:
                    imo(b3)
                    if res[2] == 7:
                        imo(b8)
                        if res[3] == 2:
                            imo(b1)
                        else:
                            imo(b2)
                    else:
                        imo(b7)
                elif res[1] == 7:
                    imo(b8)
                    if res[2] == 2:
                        imo(b4)
                        if res[3] == 6:
                            imo(b3)
                        else:
                            imo(b6)
                    else:
                        imo(b2)
                elif res[1] == 8:
                    imo(b7)
                    if res[2] == 3:
                        imo(b6)
                        if res[3] == 4:
                            imo(b1)
                        else:
                            imo(b4)
                    else:
                        imo(b3)
        except IndexError:
            pass

    def shivang(btnn):

        btns = [b00, b01, b02, b10, b11, b12, b20, b21, b22]
        y = [b00, b01, b02, b10, b11, b12, b20, b21, b22]

        def drw():
            if not check(lst):
                yn = []
                for i in y:
                    if i['state'] == DISABLED:
                        yn.append(True)
                if len(yn) == 9 and all(yn):
                    return True

        if check(lst):
            for i in btns:
                i['state'] = DISABLED
            nm = check(lst)[1].capitalize()
            if nm == 'X':
                msg = 'Winner : ' + xname + '\nPlay Again'
            else:
                msg = 'Winner : ' + oname + '\nPlay Again'
            vic()
            chh = tkinter.messagebox.askyesno('Winner', msg)
            if chh:
                tt()
                human_vs_shivang(xname, oname)
            else:
                close()

        elif drw():
            vic()
            chh = tkinter.messagebox.askyesno('Tie', "Match tie\nPlay Again")
            if chh:
                tt()
                human_vs_shivang(xname, oname)
            else:
                close()
        else:
            play(y, btnn)

            if check(lst):
                for i in btns:
                    i['state'] = DISABLED
                nm = check(lst)[1].capitalize()
                if nm == 'X':
                    msg = 'Winner : ' + xname + '\nPlay Again'
                else:
                    msg = 'Winner : ' + oname + '\nPlay Again'
                vic()
                chh = tkinter.messagebox.askyesno('Winner', msg)
                if chh:
                    tt()
                    human_vs_shivang(xname, oname)
                else:
                    close()

            elif drw():
                vic()
                chh = tkinter.messagebox.askyesno('Tie', "Match tie\nPlay Again")
                if chh:
                    tt()
                    human_vs_shivang(xname, oname)
                else:
                    close()

    col = 'pink'
    b00 = Button(can, bg=col, width=20, height=10, relief="groove", borderwidth=5, command=lambda: imx(b00))
    b00.grid(row=0, column=0)
    b01 = Button(can, bg=col, width=20, height=10, relief="groove", borderwidth=5, command=lambda: imx(b01))
    b01.grid(row=0, column=1)
    b02 = Button(can, bg=col, width=20, height=10, relief="groove", borderwidth=5, command=lambda: imx(b02))
    b02.grid(row=0, column=2)
    b10 = Button(can, bg=col, width=20, height=10, relief="groove", borderwidth=5, command=lambda: imx(b10))
    b10.grid(row=1, column=0)
    b11 = Button(can, bg=col, width=20, height=10, relief="groove", borderwidth=5, command=lambda: imx(b11))
    b11.grid(row=1, column=1)
    b12 = Button(can, bg=col, width=20, height=10, relief="groove", borderwidth=5, command=lambda: imx(b12))
    b12.grid(row=1, column=2)
    b20 = Button(can, bg=col, width=20, height=10, relief="groove", borderwidth=5, command=lambda: imx(b20))
    b20.grid(row=2, column=0)
    b21 = Button(can, bg=col, width=20, height=10, relief="groove", borderwidth=5, command=lambda: imx(b21))
    b21.grid(row=2, column=1)
    b22 = Button(can, bg=col, width=20, height=10, relief="groove", borderwidth=5, command=lambda: imx(b22))
    b22.grid(row=2, column=2)

    def all_key(val):
        sq = (b00, b01, b02, b10, b11, b12, b20, b21, b22)
        var = val.keycode
        if 97 <= int(var) <= 105:
            idx = int(var) - 97
            a = sq[idx]
            if a['state'] != DISABLED:
                imx(a)
        elif 49 <= int(var) <= 57:
            idx = int(var) - 49
            a = sq[idx]
            if a['state'] != DISABLED:
                imx(a)

    root.bind('<Key>', all_key)


canvas = Canvas(root, bg='cyan', width=700, height=660)
canvas.place(x=0, y=0)
canvas.create_line(233, 0, 233, 660, fill='red', width=5)
canvas.create_line(466, 0, 466, 660, fill='red', width=5)
canvas.create_line(0, 190, 700, 190, fill='red', width=5)
canvas.create_line(0, 440, 700, 440, fill='red', width=5)
ximg = ImageTk.PhotoImage(Image.open('imgxcy.png'))
Label(canvas, image=ximg, borderwidth=0).place(x=39, y=500)
oimg = ImageTk.PhotoImage(Image.open('imgocy.png'))
Label(canvas, image=oimg, borderwidth=0).place(x=520, y=500)
root.maxsize(700, 660)


def play_cmd():
    global play, Help, Quit, root
    tt()
    play.destroy()
    Help.destroy()
    Quit.destroy()
    root.title("Menu\\Play --Select Mode")
    root.update()

    def h_vs_h():
        global root, canvas
        root.title("Tic Tac Toe\\Menu\\Play --Player name")
        root.update()
        canvas.destroy()
        cann = Canvas(root, bg='cyan', width=400, height=300)
        cann.grid(row=0, column=0)
        root.minsize(400, 140)
        root.maxsize(400, 320)
        root.update()
        pxx = StringVar()
        poo = StringVar()
        Label(cann, text="Player Name (X):", font=('arial', 20, 'bold'), bg="cyan").grid(row=1, column=0)
        px = Entry(cann, textvariable=pxx, bg='pink', width=11, font=('arial', 20, 'bold'), justify=LEFT)
        px.grid(row=1, column=1)
        Label(cann, text="Player Name (0):", font=('arial', 20, 'bold'), bg="cyan").grid(row=2, column=0)
        po = Entry(cann, textvariable=poo, bg='pink', width=11, font=('arial', 20, 'bold'), justify=LEFT)
        po.grid(row=2, column=1)
        Button(cann, text='Submit', bg='red', command=lambda: submit(), font=('Arial', 20, 'bold')).grid(row=3,
                                                                                                         column=1)

        def submit():
            global root
            x_name = str(px.get()).title()
            o_name = str(po.get()).title()
            cann.destroy()
            root.title(f"Tic Tac Toe\\{x_name} vs {o_name}")
            human_vs_human(x_name, o_name)

    def h_vs_c():
        def h_vs_john():
            global root, canvas
            root.title("Tic Tac Toe\\Menu\\Play --Player name")
            root.update()
            canvas.destroy()
            cann = Canvas(root, bg='cyan', width=400, height=300)
            cann.grid(row=0, column=0)
            root.minsize(400, 140)
            root.maxsize(400, 320)
            root.update()
            pxx = StringVar()
            poo = StringVar()
            Label(cann, text="Player Name (X):", font=('arial', 20, 'bold'), bg="cyan").grid(row=1, column=0)
            px = Entry(cann, textvariable=pxx, bg='pink', width=11, font=('arial', 20, 'bold'), justify=LEFT)
            px.grid(row=1, column=1)
            Label(cann, text="Player Name (0):", font=('arial', 20, 'bold'), bg="cyan").grid(row=2, column=0)
            poo.set("John")
            po = Entry(cann, textvariable=poo, bg='pink', width=11, font=('arial', 20, 'bold'), justify=LEFT)
            po.grid(row=2, column=1)
            po['state'] = DISABLED
            Button(cann, text='Submit', bg='red', command=lambda: submit(), font=('Arial', 20, 'bold')).grid(row=3,
                                                                                                             column=1)

            def submit():
                global root
                x_name = str(px.get()).title()
                o_name = str(po.get()).title()
                cann.destroy()
                root.title(f"Tic Tac Toe\\{x_name} vs {o_name}")
                human_vs_john(x_name, o_name)

        def h_vs_shivang():
            global root, canvas
            root.title("Tic Tac Toe\\Menu\\Play --Player name")
            root.update()
            canvas.destroy()
            cann = Canvas(root, bg='cyan', width=400, height=300)
            cann.grid(row=0, column=0)
            root.minsize(400, 140)
            root.maxsize(400, 320)
            root.update()
            pxx = StringVar()
            poo = StringVar()
            Label(cann, text="Player Name (X):", font=('arial', 20, 'bold'), bg="cyan").grid(row=1, column=0)
            px = Entry(cann, textvariable=pxx, bg='pink', width=11, font=('arial', 20, 'bold'), justify=LEFT)
            px.grid(row=1, column=1)
            Label(cann, text="Player Name (0):", font=('arial', 20, 'bold'), bg="cyan").grid(row=2, column=0)
            poo.set("Shivang")
            po = Entry(cann, textvariable=poo, bg='pink', width=11, font=('arial', 20, 'bold'), justify=LEFT)
            po.grid(row=2, column=1)
            po['state'] = DISABLED
            Button(cann, text='Submit', bg='red', command=lambda: submit(), font=('Arial', 20, 'bold')).grid(row=3,
                                                                                                             column=1)

            def submit():
                global root
                x_name = str(px.get()).title()
                o_name = str(po.get()).title()
                cann.destroy()
                root.title(f"Tic Tac Toe\\{x_name} vs {o_name}")
                human_vs_shivang(x_name, o_name)

        ply_h_vs_h.destroy()
        ply_h_vs_c.destroy()
        Button(canvas, text='Human V/s John', fg='blue', bg='cyan', font=('Arial', 40, 'bold', 'italic'),
               activebackground='cyan', activeforeground='blue', borderwidth=0,
               command=lambda: h_vs_john()).place(relx=0.2, rely=0.2)
        Button(canvas, text='Human V/s Shivang', fg='blue', bg='cyan', font=('Arial', 40, 'bold', 'italic'),
               activebackground='cyan', activeforeground='blue', borderwidth=0,
               command=lambda: h_vs_shivang()).place(relx=0.15, rely=0.4)

    ply_h_vs_h = Button(canvas, text='Human V/s Human', fg='blue', bg='cyan', font=('Arial', 40, 'bold', 'italic'),
                        activebackground='cyan', activeforeground='blue', borderwidth=0, command=lambda: h_vs_h())
    ply_h_vs_h.place(relx=0.15, rely=0.1)
    ply_h_vs_c = Button(canvas, text='Human V/s Computer', fg='blue', bg='cyan', font=('Arial', 40, 'bold', 'italic'),
                        activebackground='cyan', activeforeground='blue', borderwidth=0, command=lambda: h_vs_c())
    ply_h_vs_c.place(relx=0.1, rely=0.4)


def close():
    root.quit()


def help_cmd():
    hotkeys = "F1=Go to Help; F5= Go to Play; Esc=Quit game"
    rule = "The game is played on a grid that's 3 squares by 3 squares.\nYou are X, your friend (or\n" \
           "the computer in this case) is O. Players take turns putting\ntheir marks in empty squares. " \
           "The first player to get 3 of\nher/his marks in a row (up, down, across, or diagonally) is the\n" \
           "winner.When all 9 squares are full, the game is over and draw."
    gameplay = "Click on box to fill your grid with your mark or press key (1-9)\n1=Upper left corner;" \
               "2=Central up box;3=Upper right corner;\n4=Central left box;5=Center;6=Central right box;7=Lower left " \
               "corner;8=Down box;\n9=Lower right corner. To play with easy level you choose 'Human V/s John'.\nFor " \
               "difficult level choose 'Human V/s Shivang'"
    dev = "Developed By Shivang Srivastava"
    ms = Toplevel(root)
    ms.title("HELP")
    ms.iconbitmap('icon_help.ico')
    Label(ms, text="-:HELP WINDOW:-", font=('Arial', 30, 'bold', 'italic'), fg='red').pack()
    Label(ms, text="RULE", font=('Arial', 20, 'bold', 'italic'), fg='red').pack()
    Label(ms, text=rule, font=('Arial', 20, 'bold', 'italic'), fg='blue').pack()
    Label(ms, text="GAMEPLAY", font=('Arial', 20, 'bold', 'italic'), fg='red').pack()
    Label(ms, text=gameplay, font=('Arial', 20, 'bold', 'italic'), fg='blue').pack()
    Label(ms, text="HOTKEYS", font=('Arial', 20, 'bold', 'italic'), fg='red').pack()
    Label(ms, text=hotkeys, font=('Arial', 20, 'bold', 'italic'), fg='blue').pack()
    Label(ms, text=dev.title(), font=('Arial', 17, 'bold', 'italic'), fg='black', bg='light grey').pack()
    Button(ms, text="Close Help Window", font=('Arial', 20, 'bold', 'italic'), fg='orange',
           command=lambda: cls()).pack()

    def cls():
        ms.destroy()

    def key__bind(val):
        if val.keycode == 81:
            cls()

    ms.bind('<Key>', key__bind)
    ms.mainloop()


play = Button(canvas, text='Play', fg='blue', bg='cyan', font=('Arial', 40, 'bold', 'italic'), activebackground='cyan',
              activeforeground='blue', borderwidth=0, command=lambda: play_cmd())
Help = Button(canvas, text='Help', fg='blue', bg='cyan', font=('Arial', 40, 'bold', 'italic'), activebackground='cyan',
              activeforeground='blue', borderwidth=0, command=lambda: help_cmd())
Quit = Button(canvas, text='Quit', fg='blue', bg='cyan', font=('Arial', 40, 'bold', 'italic'), activebackground='cyan',
              activeforeground='blue', borderwidth=0, command=lambda: close())


def run(x=0.4):
    global play, Help, Quit, root
    tt()
    root.title("Tic Tac Toe\\Menu")
    root.update()
    play.place(relx=x, rely=0.2)
    Help.place(relx=x, rely=0.4)
    Quit.place(relx=x, rely=0.6)


run()


def key_bind(var):
    val = var.keysym
    if val.lower() == 'f1':
        help_cmd()
    elif val.lower() == 'f5':
        try:
            play_cmd()
        except EXCEPTION:
            pass


root.bind('<Key>', key_bind)
root.bind('<Escape>', lambda a: close())
root.mainloop()
