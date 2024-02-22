import tkinter
from tkinter import *


def add_digit(count):
    count = int(calc.get())
    # print(count)
    # fl = tkinter.Entry(win, font='Arial 15', width=5).grid(row=3, column=0, columnspan=1, stick='we', padx=10,
    #                                                        pady=5)
    tkinter.Label(win, bg='CornflowerBlue', text='Фланец, мм', font='Arial 13',
                  width=10).grid(row=3, column=1, columnspan=1, padx=10, pady=10)

    entries = []
    fl = tkinter.Entry(win, font='Arial 15', width=5)

    fl.grid(row=3, column=0, columnspan=1, stick='we', padx=10,
            pady=5)

    for i in range(1, count + 1):
        entry = tkinter.Entry(win, font='Arial 15', width=5)

        entries.append(entry)
        # print(*entries)

        entry.grid(row=i + 3, column=0, columnspan=1, stick='we', padx=10,
                   pady=5)
        # entry.insert(0, f'Lсек{i}')

        tkinter.Label(win, bg='CornflowerBlue', text=f'Lсек {i}', font='Arial 13',
                      width=10).grid(row=i + 3, column=1, columnspan=1, padx=10, pady=10)

    canvas = Canvas(bg='white', width=1250, height=550)
    canvas.grid(row=2, column=5, columnspan=10, rowspan=20, stick='we', padx=105, pady=5)

    canvas.create_text(600, 30, font='Arial 14', text=f'Фланцевая вставка {count} секций')

    def add_flange(flange):
        canvas.create_rectangle(55, 100, 80, 440, width=4)
        canvas.create_line(80, 100, 100, 120, width=4, arrowshape='5 10 5', )
        canvas.create_line(80, 440, 100, 420, width=4, arrowshape='5 10 5', )

        canvas.create_line(55, 100, 55, 70, width=1, arrowshape='5 10 5', )
        canvas.create_line(100, 120, 100, 70, width=1, arrowshape='5 10 5', )
        canvas.create_line(55, 80, 100, 80, width=1, arrow=FIRST, arrowshape='5 10 5', )
        canvas.create_line(55, 80, 100, 80, width=1, arrow=LAST, arrowshape='5 10 5', )
        canvas.create_text(75, 70, font='Arial 12', text=f'{flange}')

        canvas.create_rectangle(1120, 100, 1145, 440, width=4)
        canvas.create_line(1100, 120, 1120, 100, width=4, arrowshape='5 10 5', )
        canvas.create_line(1100, 420, 1120, 440, width=4, arrowshape='5 10 5', )

        canvas.create_line(1145, 100, 1145, 70, width=1, arrowshape='5 10 5', )
        canvas.create_line(1100, 120, 1100, 70, width=1, arrowshape='5 10 5', )
        canvas.create_line(1100, 80, 1145, 80, width=1, arrow=FIRST, arrowshape='5 10 5', )
        canvas.create_line(1100, 80, 1145, 80, width=1, arrow=LAST, arrowshape='5 10 5', )
        canvas.create_text(1120, 70, font='Arial 12', text=f'{flange}')

    def create_line(l, lfv): # Общий размер фв
        canvas.create_line(55, 470, 1145, 470, width=1, arrow=LAST, arrowshape='5 10 5', )
        canvas.create_line(55, 470, 1145, 470, width=1, arrow=FIRST, arrowshape='5 10 5', )

        canvas.create_line(55, 420, 55, 480, width=1)
        canvas.create_line(1145, 420, 1145, 480, width=1)
        canvas.create_text(600, 460, font='Arial 12', text=lfv)

    def create_line2(l):
        x1, y1, x2, y2 = 100, 120, 1100, 420
        for i in l:
            canvas.create_line(x1, 80, x2, 80, width=1, arrow=FIRST, arrowshape='5 10 5', )  # размер общий
            canvas.create_line(x1, 80, x2, 80, width=1, arrow=LAST, arrowshape='5 10 5', )  # размер общий
            x2 = 100 + (l[0] * 1000) / 8200
            canvas.create_line(x2, 80, 1100, 80, width=1, arrow=FIRST, arrowshape='5 10 5', )  # размер 1 секции

            canvas.create_line(x2, 70, x2, 120, width=1, arrowshape='5 10 5', )  # разделитель 1 и 2 секции

            canvas.create_text((x1 + x2) / 2, 70, font='Arial 12', text=f'{l[0]}')

            canvas.create_text((1100 - x2) / 2 + x2, 70, font='Arial 12', text=f'{l[1]}')

            # canvas.create_text((l[1] * 1000) / 8200, 415, font='Arial 12', text='секция 2')

    def create_line3(l, count):
        x1, y1, x2, y2 = 100, 100, 1100, 400

        for i in range(0, count):
            canvas.create_line(x1, 80, x2, 80, width=1, arrow=FIRST, arrowshape='5 10 5', )  # размер общий 
            canvas.create_line(x1, 80, x2, 80, width=1, arrow=LAST, arrowshape='5 10 5', )  # размер общий
            canvas.create_line(x1, 70, x1, 120, width=1, arrowshape='5 10 5', )

            # canvas.create_text((1100 - x2) / 2 + x2, 70, font='Arial 12', text=f'{l[1]}')
            x1 = x1 + (l[i] * 1000) / 8200

            canvas.create_text(x1 - ((l[i] * 1000) / 8200)/2, 70, font='Arial 12', text=f'{l[i]} ')

    def get_param():
        l = []
        flange = (int(fl.get()))
        print(flange)
        for i in entries:
            l.append(int(i.get()))
        lfv = (sum(l) + flange)
        x1, y1, x2, y2 = 100, 120, 1100, 420

        create_line(l, lfv)

        if count == 1:
            canvas.create_rectangle(x1, y1, x2, y2, width=4)
            add_flange(flange)
            canvas.create_line(x1, 80, x2, 80, width=1, arrow=FIRST, arrowshape='5 10 5', )  # размер общий
            canvas.create_line(x1, 80, x2, 80, width=1, arrow=LAST, arrowshape='5 10 5', )  # размер общий
            canvas.create_text(600, 70, font='Arial 12', text=f'{l[0]}')

        elif count == 2:
            create_line2(l)
            canvas.create_rectangle(x1, y1, x2, y2, width=4)
            x1 = x1 + (l[0] * 1000) / 8200
            canvas.create_rectangle(x1, y1, 1100, y2, width=4)
            add_flange(flange)

        else:
            create_line3(l, count)
            for i in range(0, count):
                canvas.create_rectangle(x1, y1, x2, y2, width=4)
                x1 = x1 + (l[i] * 1000) / 8200
            add_flange(flange)
            # create_line(l)

    tkinter.Button(text='Get', width=10, bd=5, font='Arial 14', command=get_param).grid(row=2, column=0,
                                                                                        stick='we',
                                                                                        padx=5, pady=5)


def make_digit_button(count):
    return tkinter.Button(text=count, bd=5, font='Arial 14',
                          command=lambda: add_digit(count))


win = tkinter.Tk()
win.geometry(f'1920x1080+0+0')
win['bg'] = 'CornflowerBlue'
win.title('Scheme')

calc = tkinter.Entry(win, justify=tkinter.RIGHT, font='Arial 15', width=10)
calc.insert(1, '1')
calc.grid(row=0, column=0, columnspan=1, stick='we', padx=5, pady=5)

tkinter.Label(win, bg='CornflowerBlue', text='Количество секций', justify=tkinter.LEFT, font='Arial 15', width=15).grid(
    row=0, column=1,
    columnspan=1,
    stick='we', padx=5,
    pady=5)

make_digit_button('Ввод').grid(row=1, column=0, stick='wens', padx=5, pady=5)

win.mainloop()
