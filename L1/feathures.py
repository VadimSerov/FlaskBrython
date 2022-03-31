from browser import *
	
items = document.select('.item')

def change_text(event):
	text_in_field = document['for-input'].select('input')[0].value
	items[0].text = text_in_field

def change_style_class(event):
	if 'colored' in items[1].classList :
		items[1].classList.remove('colored')
		items[1].classList.add('colored1')
	elif 'colored1' in items[1].classList :
		items[1].classList.remove('colored1')
		items[1].classList.add('colored')
	else:
		items[1].classList.add('colored')

document['btn-1'].bind('click',change_text)
document['btn-2'].bind('click',change_style_class)
