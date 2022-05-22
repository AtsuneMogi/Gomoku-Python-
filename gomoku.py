# Atsune MOGI

import tkinter as tk
from PIL import Image, ImageTk

# the size of this game
SIZE = 13
# the number that the players need to win
WIN = 5
# boolian value that means the game is cleard
GAME = False
# now player
player = 1
# set board
B = [[0 for i in range(SIZE)] for j in range(SIZE)]
# main window
root = tk.Tk()
# the size of the window
root.geometry(str(50*SIZE+300)+'x'+str(50*SIZE)+'+0+0')
# game title
root.title('Gomoku')
# font size
fonts = ('', 40)
# the canvas to draw the images
canvas = tk.Canvas(
    root,
    bg='white',
    width=50*SIZE,
    height=50*SIZE
)
# set the canvas at the coordinates (x, y) = (0, 0)
canvas.place(
    x=0,
    y=0
)
# display the player
player_label = tk.Label(
    text='Black',
    font=fonts,
    foreground='black'
)
# place player label at the coordinates (x, y) = (50*SIZE, 100)
player_label.place(
    x=50*SIZE,
    y=100,
    width=300,
    height=50
)

# reset board
def reset():
    global B, player, GAME
    B = [[0 for i in range(SIZE)] for j in range(SIZE)]
    player = 2
    GAME = False
    switch_player()
    display_images()

# the button to reset board
def reset_button():
    button = tk.Button(
        root,
        text='Reset',
        font=fonts,
        command=reset
    )
    # place 'Reset' button at the coordinates (x, y) = (50*SIZE, 0)
    button.place(
        x=50*SIZE,
        y=0,
        width=300,
        height=100
    )

# display images
def display_images():
    global imgs
    # the list to maintain images
    imgs = []
    # delete all images on the canvas
    canvas.delete('all')
    for i in range(SIZE):
        for j in range(SIZE):
            # open the image with specified number
            img = Image.open('images/'+str(B[i][j])+'.png')
            img = ImageTk.PhotoImage(img)
            # append the image to the list
            imgs.append(img)
            # draw the image on the canvas
            img = canvas.create_image(
                j*50,
                i*50,
                image=img,
                anchor=tk.NW
            )

# switch the player
def switch_player():
    global player
    if player % 2:
        player = 2
        player_label.config(text='White', foreground='black')
        root.unbind('<1>')
        root.bind('<1>', click_2)
    else:
        player = 1
        player_label.config(text='Black', foreground='black')
        root.unbind('<1>')
        root.bind('<1>', click_1)

# set a black stone at clicked place
def click_1(event):
    global player, x, y
    x, y = event.x // 50, event.y // 50
    if not B[y][x]:    
        B[y][x] = 1
        display_images()
        switch_player()
        winner(1)
        if GAME:
            root.unbind('<1>')
            player_label.config(text='Black Win!', foreground='red')

# set a white stone at clicked place
def click_2(event):
    global player, x, y
    x, y = event.x // 50, event.y // 50
    if not B[y][x]:    
        B[y][x] = 2
        display_images()
        switch_player()
        winner(2)
        if GAME:
            root.unbind('<1>')
            player_label.config(text='White Win!', foreground='red')

# check if now player is winner
def winner(n):
    global x, y, GAME
    cnt = 1
    i, j = y - 1, x + 1 
    while i >= 0 and j < SIZE:
        if B[i][j] == n:
            cnt += 1
            i -= 1
            j += 1
        else:
            break
    i, j = y + 1, x - 1
    while i < SIZE and j >= 0:
        if B[i][j] == n:
            cnt += 1
            i += 1
            j -= 1
        else:
            break
    if cnt >= WIN:
        GAME = True
    else:
        cnt = 1
        i, j = y - 1, x - 1
        while i >= 0 and j >= 0:
            if B[i][j] == n:
                cnt += 1
                i -= 1
                j -= 1
            else:
                break
        i, j = y + 1, x + 1
        while i < SIZE and j < SIZE:
            if B[i][j] == n:
                cnt += 1
                i += 1
                j += 1
            else:
                break
        if cnt >= WIN:
            GAME = True
        else:
            cnt = 1
            i = y - 1
            while i >= 0:
                if B[i][x] == n:
                    cnt += 1
                    i -= 1
                else:
                    break
            i = y + 1
            while i < SIZE:
                if B[i][x] == n:
                    cnt += 1
                    i += 1
                else:
                    break
            if cnt >= WIN:
                GAME = True
            else:
                cnt = 1
                j = x - 1 
                while j >= 0:
                    if B[y][j] == n:
                        cnt += 1
                        j -= 1
                    else:
                        break
                j = x + 1
                while j < SIZE:
                    if B[y][j] == n:
                        cnt += 1
                        j += 1
                    else:
                        break
                if cnt >= WIN:
                    GAME = True

# main function
def main():
    display_images()
    reset_button()
    root.bind('<1>', click_1)
    root.mainloop()


if __name__ == '__main__':
    main()