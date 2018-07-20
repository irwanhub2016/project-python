import time
import os

x=9

def main():

	while True:

		hrs=int(time.strftime("%H"))
		min=int(time.strftime("%M"))
		sec=int(time.strftime("%S"))
		print(hrs)
		print(sec)
		print(min)

		if hrs == 18:
			print('Lampu ON')

		else:
			print('Lampu OFF')

		print('Done.')
		time.sleep

def irwan():

	while True:

		hrs=int(time.strftime("%H"))
		min=int(time.strftime("%M"))
		sec=int(time.strftime("%S"))
		print(hrs)
		print(sec)
		print(min)

		if hrs == 18:
			print('Lampu ON')

		else:
			print('Lampu OFF')

		print('Done.')
		time.sleep


if __name__ == "__main__":
    main()
	
     try:
  blink()
     except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
  	  destroy()