from tkinter import *

def drawboard(core_array,chip_array,color = 'orange'):
    board = [core_array[0]*chip_array[0],core_array[1]*chip_array[1]]
    core_nums = board[0] * board[1]
    startx = starty = cellwidth = 900/2/core_array[1]/chip_array[1]
    #startx = starty = cellwidth = 15
    width=2*startx+board[0]*cellwidth*2+cellwidth*(chip_array[0]-1) - cellwidth
    height=2*starty+board[1]*cellwidth*2+cellwidth*(chip_array[1]-1) - cellwidth
    #print('width',width,'height',height)
    canvas.config(width=width,height=height)
    chx = 0
    chy = 0

    for m in range(chip_array[0]):
        for n in range(chip_array[1]):
            chip_x0 = chx + cellwidth / 2 + core_array[0] * 2 * cellwidth * m
            chip_y0 = chy + cellwidth / 2 + core_array[1] * 2 * cellwidth * n
            chip_x1 = chx + cellwidth / 2 + 2 * core_array[0] * cellwidth * (m + 1)
            chip_y1 = chy + cellwidth / 2 + core_array[1] * 2 * cellwidth * (n + 1)
            canvas.create_rectangle(chip_x0, chip_y0, chip_x1, chip_y1, fill='bisque', outline="blue", width=3)

            if not m == chip_array[0] - 1:
                canvas.create_line(chip_x1, (chip_y0 + chip_y1) / 2, chip_x1 + cellwidth, (chip_y0 + chip_y1) / 2,
                                   fill='black', width=5)
            if not n == chip_array[1] - 1:
                canvas.create_line((chip_x0 + chip_x1) / 2, chip_y1, (chip_x0 + chip_x1) / 2, chip_y1 + cellwidth,
                                   fill='black', width=5)

            chy = chy + cellwidth

            for i in range(core_array[0]):
                if i == 0:
                    cellx = cellwidth + (core_array[0]*2+1)*m*cellwidth
                else:
                    cellx = cellx + cellwidth*2
                celly = 0
                for j in range(core_array[1]):
                    if j == 0:
                        celly = cellwidth + (core_array[1]*2+1)*n*cellwidth
                    else:
                        celly = celly + cellwidth*2

                    canvas.create_rectangle(cellx, celly, cellx + cellwidth, celly + cellwidth, fill=color,
                                            outline="black")
                    if not j == core_array[1] - 1:
                        canvas.create_line(cellx + cellwidth / 2, celly + cellwidth, cellx + cellwidth / 2,
                                           celly + 2 * cellwidth, fill='red', width=2)
                    if not i == core_array[0] - 1:
                        canvas.create_line(cellx + cellwidth, celly + cellwidth / 2, cellx + 2 * cellwidth,
                                           celly + cellwidth / 2, fill='red', width=2)
                    #print(cellx, celly, cellx + cellwidth, celly + cellwidth)
        chy = 0
        chx = chx + cellwidth
    canvas.update()

root=Tk()
canvas=Canvas(root,bg="white")
canvas.pack(expand='yes')
#canvas.pack()
core_array=[4,4]
chip_array=[2,2]
drawboard(core_array,chip_array)
root.mainloop()