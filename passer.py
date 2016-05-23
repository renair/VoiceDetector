from neuro import *
from audiocore import *

MAINFILE = 'key.neu'
if init_alsa():
	print('alsa inited')
cons = read_consciousness(MAINFILE)
if cons:
	print('consciousness loaded')
#data = read_consciousness('test1')
#data = alsa_read_phrase(2,2)
#print(0)
#data2 = alsa_read_phrase(2,2)
if(compare_phrase()):
	print('done!')
exit(1)
data = read_consciousness('test2')
if(compare_phrase(data,cons)):
	print('done!')

data = read_consciousness('test3')
if(compare_phrase(data,cons)):
	print('done!')

data = read_consciousness('test4')
if(compare_phrase(data,cons)):
	print('done!')

data = read_consciousness('test5')
if(compare_phrase(data,cons)):
	print('done!')

data = read_consciousness('test6')
if(compare_phrase(data,cons)):
	print('done!')

