import sys
import datetime
import imageio
import os, glob
import shutil
VALID_EXTENSIONS = ('png', 'jpg')


def create_gif(filenames, duration):
    images = []
    for filename in filenames:
        images.append(imageio.imread(filename))
    output_file = 'GIFs/avocado.gif'
    imageio.mimwrite(output_file, images, duration=duration)


def main():
    args = sys.argv
    script = args.pop(0)

    if len(args) < 1:
        print( 'Usage: python {} <frames per second> <path to folder>'.format(script))
        sys.exit(1)

    frames_per_second = int(args[0])
    duration = float(1/frames_per_second)
    input_dir = args[1]
    filenames = [os.path.join(input_dir, i )for i in os.listdir(input_dir)]

    if not all(f.lower().endswith(VALID_EXTENSIONS) for f in filenames):
        print('Only png and jpg files allowed')
        sys.exit(1)

    create_gif(filenames, duration)


if __name__ == "__main__":
    main()
    print("done")


