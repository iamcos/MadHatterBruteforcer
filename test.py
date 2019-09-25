import numpy as np
import pandas as pd

things = [1,2,3,4,5]
bzings = [0,1,10,20,30,40]

def loopy(things, bzings):
	i = 0
	for i in things:
		print('things',i)
		for b in bzings:
			print(b,'bzings')
	

loopy(things, bzings)