def hori_line():
    print('+','-','-','-','-','+','-','-','-','-','+', end=' ' )
    print('-','-','-','-','+','-','-','-','-','+','-','-','-','-','+' )
    #draws the horizontal line



def column_no():
    print('|'+' '*9 +'|'+ ' '*9 +'|'+' '*9 +'|'+ ' '*9 +'|'+ ' '*9 +'|')
    #draws 1/4th of the columns
        
def draw_row():
    column_no()
    column_no()
    column_no()
    column_no()
    hori_line()
    #draws one row with one line under

def draw_grid():
    hori_line()
    draw_row()
    draw_row()
    draw_row()
    draw_row()
    draw_row()
    draw_row()
    draw_row()
    #draws the grid


    
draw_grid()
