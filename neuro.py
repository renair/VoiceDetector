import os, os.path
import pickle

if __name__ == '__main__':
	print('nothing to run')

def read_consciousness(filemem):
	consciousness = []
	if not os.path.exists(filemem):
		try:
			filemem = open(filemem,'wb+')
			consciousness = [127 for i in range(1000)]
			pickle.dump(consciousness,filemem)
			filemem.close()
		except Exception:
			return False
	else:
		try:
			filemem = open(filemem,'rb')
			consciousness = pickle.load(filemem)
			filemem.close()
		except Exception:
			return False
	return consciousness

def write_consciousness(consciousness,filemem):
	if consciousness:
		filemem = open(filemem,'wb+')
		pickle.dump(consciousness,filemem)
		filemem.close()
		
def teach_neuron(data,neuron):
	if len(neuron) >= len(data):
		for i in range(len(data)):
			neuron[i] = (data[i] + neuron[i])/2
		for i in range(len(data),len(neuron),2):
			neuron.pop()
	else:
		for i in range(len(neuron)):
			neuron[i] = (data[i] + neuron[i])/2
		for i in range(len(neuron),len(data)//2):
			neuron.append(data[i])
	return neuron

def compare_phrase(data,consciousness,accuracy=0.5):
	num = 0
	if len(data) >= len(consciousness):
		for i in range(len(consciousness)):
			num += abs(consciousness[i] - data[i])
		print(num/len(consciousness))
		if num/len(consciousness) < accuracy:
			return True
	else:
		for i in range(len(data)):
			num += abs(consciousness[i] - data[i])
		print(num/len(data))
		if num/len(data) < accuracy:
			return True
	return False
