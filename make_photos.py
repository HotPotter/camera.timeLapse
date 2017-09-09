from picamera import PiCamera
import sys
import time
import os

def take_photo(output_dir):
    with PiCamera() as picam:
        filename = '{}.jpg'.format(round(time.time()))
        output_path = os.path.join(output_dir, filename)
        picam.capture(output_path, format='jpeg', rotation=180)

def main(args):
    script = args.pop(0)

    if len(args) < 2:
        print('Usage: python {} <photo_every_x_seconds> <output_dir>'.format(script))
        exit(1)

    interval = int(args[0])
    output_dir = args[1]

    while True:
       take_photo(output_dir)
       time.sleep(interval)


if __name__ == '__main__':
    main(sys.argv)
