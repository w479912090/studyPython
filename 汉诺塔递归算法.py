def move(n, a, b, c):
	if n == 1:
		print('move', a, '->', c)
	else:
		move(n-1, a, c, b)
		move(1, a, b, c)
		move(n-1, b, a, c)

move(3, 'A', 'B', 'C')

'''
要从a到b 那c就是缓冲 move(n-1,a,c,b)
要从a到c 那b就是缓冲 move(1,a,b,c)
要从b到c 那a就是缓冲 move(n-1,b,a,c)
'''