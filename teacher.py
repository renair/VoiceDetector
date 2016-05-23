from neuro import *
from audiocore import *

MAINFILE = 'key.neu'
if init_alsa():
	print('alsa inited')
cons = read_consciousness(MAINFILE)
if cons:
	print('consciousness loaded')
#print('say something:')
#ln = alsa_get_speech_length(2,4)
print('repeat phrase')
cons = teach_neuron(alsa_read_phrase(1.5,3),cons)
print(len(cons))
print('repeat phrase')
cons = teach_neuron(alsa_read_phrase(1.5,3),cons)
print(len(cons))
print('repeat phrase')
cons = teach_neuron(alsa_read_phrase(1.5,3),cons)
print(len(cons))
print('repeat phrase')
cons = teach_neuron(alsa_read_phrase(1.5,3),cons)
print(len(cons))
print('repeat phrase')
cons = teach_neuron(alsa_read_phrase(1.5,3),cons)
print(len(cons))
print(cons)
write_consciousness(cons,MAINFILE)
