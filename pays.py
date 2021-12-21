import sys

def main(fl):
	pays_frontaliers = []
	
	with open(fl) as fp:
		for line in fp:
			if line != "\n":
				rendu = line.split()
				pays_frontaliers.append(tuple(rendu))
	fp.close()
	
	return pays_frontaliers

if __name__ == '__main__':
	assert len(sys.argv) > 1, 'il manque un argument'
	main(sys.argv[1])




