import alsaaudio as audio
import time
import math

if __name__ == '__main__':
	print('nothing to run')

_alsa = False

def init_alsa(t=audio.PCM_CAPTURE, mode=audio.PCM_NORMAL, device='default', cardindex=-1):
	global _alsa
	try:
		_alsa = audio.PCM(t,mode,device,cardindex)
		_alsa.setchannels(1)
		_alsa.setformat(audio.PCM_FORMAT_U16_BE)
		_alsa.setperiodsize(1024)
	except ALSAAudioError:
		print('Exception occured while creating audio device.')
		print('Check your parameters and try to repeat.')
		return False
	return True

def set_alsa_blocksize(length):
	global _alsa
	_alsa.setperiodsize(length)

def set_alsa_freequency(freequency):
	global _alsa
	if str(type(_alsa)) == "<class 'alsaaudio.PCM'>":
		_alsa.setrate(freequency)
	else:
		print('ALSA is not initialized or exception occured. Try call init_alsa() first.')

def alsa_read_block(length,sensitivity=5):
	global _alsa
	block = []
	while len(block) < length:
		size, sound = _alsa.read()
		for i in range(size):
			#print(sound[i])
			if abs(sound[i]-127) > sensitivity:
				block.append(sound[i])
				print('listening',end='\r')
			else:
				print('             ',end='\r')
	return block

def alsa_read_raw_bylen(length):
	global _alsa
	block = []
	while len(block) < length:
		length ,sound = _alsa.read()
		block.extend(sound)
	return block

def alsa_read_raw_bytime(seconds):
	global _alsa
	block = []
	tm = time.time()
	while time.time() - tm < seconds:
		length ,sound = _alsa.read()
		block.extend(sound)
	return block

def alsa_get_speech_length(delay=5,sensitivity=5):
	global _alsa
	tm = math.floor(time.time())
	result = 0
	while time.time() - tm <= delay:
		size, sound = _alsa.read()
		for i in range(size):
			if abs(sound[i]-127) > sensitivity:
				tm = time.time()
				result += 1
				print('listening',end='\r')
			else:
				print('             ',end='\r')
	return result

def alsa_read_phrase(delay=1,sensitivity=5):
	global _alsa
	tm = time.time()
	data = []
	while time.time() - tm < delay:
		size, sound = _alsa.read()
		for i in range(size):
			if abs(sound[i] - 127) > sensitivity:
				data.append(sound[i])
				tm = time.time()
				print('listening',end='\r')
			else:
				print('             ',end='\r')
	return data

def get_alsa():
	global _alsa
	return _alsa
