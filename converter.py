def getText():
	return 'Git'

t = getText()
f = FontLoader().loadFOnt('fancyFont/')
d = TextDrawer()
d.setFont(f)
d.draw(t)

