#hacking v1

#my v1 was alot different then theres  they just used print statements i did more oop approach
#  debugging is a bool that is used for turning this notifation on or off
#   list a passwoirds is contanid for a loop trough print 
#   funtion for display all reader information up to the prompt to for the pasword an exit prompt and a failed notifaction 
from time import sleep

from uagame import Window
password_list = ['PROVIDE',
  'SETTING',
  'CANTINA',
  'CUTTING',
  'HUNTERS',
  'SURVIVE',
  'HEARING',
  'HUNTING',
  'REALIZE',
  'NOTHING',
  'OVERLAP',
  'FINDING',
  'PUTTING']
#start of program degug mode is indicated on the first line#
#create window
window = Window('Hacking',600,500)
window.set_font_name('couriernew')
window.set_font_size(18)
window.set_font_color('green')
window.set_bg_color('black')

#display header
line_y = 0
string_hieght = window.get_font_height()
window.draw_string('DEBUG MODE', 0,0)
window.update()
sleep(.3)
line_y = line_y +string_hieght


window.draw_string('1 ATTEPT(S) LEFT',0,line_y)
window.update()
sleep(.3)

window.draw_string('',0,line_y) 
window.update()
sleep(.3)

window.draw_string('',0,line_y)
window.update()
sleep(.3)
#display password list
for pw in password_list:
   line_yy = line_y+string_hieght
   window.draw_string(pw,0,line_yy)
   window.update()
   sleep(.3)    


#prompt for guess


#end game
   #clear window

#close window
window.close()

