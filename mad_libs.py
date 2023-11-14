from tkinter import *

root = Tk()
root.geometry('300x300')
root.title('DataFlair-Mad Libs Generator')
Label(root, text= 'Mad Libs Generator \n Have Fun!' , font = 'arial 20 bold').pack()
Label(root, text = 'Click Any One :', font = 'arial 15 bold').place(x=40, y=80)

def madlib1():

     animals = input('enter a animal name : ')
     profession = input('enter a profession name: ')
     cloth = input('enter a piece of cloth name: ')
     things = input('enter a thing name: ')
     name= input('enter a name: ')
     place = input('enter a place name: ')
     verb = input('enter a verb in ing form: ')
     food = input('food name: ')
     print('say ' + food + ', the photographer said as the camera flashed! ' + name + ' and I had gone to ' + place +' to get our photos taken on my birthday. The first photo we really wanted was a picture of us dressed as ' + animals + ' pretending to be a ' + profession + '. when we saw the second photo, it was exactly what I wanted. We both looked like ' + things + ' wearing ' + cloth + ' and ' + verb + ' –exactly what I had in mind')

def madlib2():

     adjective = input('enter adjective : ')
     color = input('enter a color name : ')
     thing = input('enter a thing name :')
     place = input('enter a place name : ')
     person= input('enter a person name : ')
     adjactive1 = input('enter a adjactive : ')
     insect= input('enter a insect name : ')
     food = input('enter a food name : ')
     verb = input('enter a verb name : ')

     print('Last night I dreamed I was a ' +adjective+ ' butterfly with ' + color+ ' splocthes that looked like '+thing+ ' .I flew to ' + place+ ' with my bestfriend and '+person+ ' who was a '+adjactive1+ ' ' +insect +' .We ate some ' +food+ ' when we got there and then decided to '+verb+ ' and the dream ended when I said– lets ' +verb+ '.')

Button(root, text= 'The Photographer', font ='arial 15', command= madlib1, bg = 'ghost white').place(x=60, y=120)
Button(root, text= 'The Butterfly', font ='arial 15', command = madlib2, bg = 'ghost white').place(x=80, y=240)

root.mainloop()