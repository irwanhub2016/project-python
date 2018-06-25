import time
import os


def main():

	while True:

		hrs=int(time.strftime("%H"))
		sec=int(time.strftime("%S"))
		print(hrs)
		print(sec)

		if sec != '16':
			print('OKE')

		else:
			print('Not !')

		print('Done.')
		time.sleep(1)

if __name__ == "__main__":
    main()