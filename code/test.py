# encoding: utf-8

import time, sys

def main():
	f = open('out.txt', 'a')
	for i in range(0, 50):
		print("[Training] step: " + str(i) + " accuracy: " + str(i + 30))
		#f = open("out.txt", "a")
		str1 = "[Training] step: " + str(i) + " accuracy: " + str(i + 30)
		print >>f, str1
		sys.stdout.flush()
		#f.close()

		print("[Validation] step: " + str(i) + " accuracy: " + str(i + 50))
		#f = open("out.txt", "a")
		str2 = "[Validation] step: " + str(i) + " accuracy: " + str(i + 50)
		print >>f, str2
		sys.stdout.flush()
		#f.close()

		i += 1
		time.sleep(0.3)
	f.close()
if __name__ == "__main__":
	main()