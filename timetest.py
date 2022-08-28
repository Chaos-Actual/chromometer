# Terminal coloring
BLACK_BG = "\x1b[40m"
WHITE_FG = "\x1b[97m"
L_BLUE_FG = "\x1b[94m"
L_BLUE_BG = "\x1b[104m"
D_GRAY_FG = "\x1b[90m"
RST_COLORS = "\x1b[0m"

themes = [
    BLACK_BG,  # background
    WHITE_FG,  # text
    L_BLUE_FG,  # table borders
    L_BLUE_BG,  # text highlight
    D_GRAY_FG  # progress bar dim
]

def print_char(x,y,char):
    print("\033["+str(y)+";"+str(x)+"H"+char)


def reset_cursor():
    print("\033[0;0H", end="")


def move_cursor_down(n=1):
    print('\033[' + str(n) + 'B', end='')


def move_cursor_up(n=1):
    print('\033[' + str(n) + 'A', end='')


def draw_progress_bar(*, min=0, width, max, value):
    level = int((width + 1) * (value - min)/(max - min))
    return (chr(0x2550) * level + D_GRAY_FG + (chr(0x2500) * (width - level)))


print(draw_progress_bar(width=20,max=100,value=30))