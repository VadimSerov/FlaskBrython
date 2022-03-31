from browser import *
	
body = document.select('body')
spisok = html.UL()
spisok <= html.LI('From Python')
spisok <= html.LI('with love')
body[0] <= spisok
