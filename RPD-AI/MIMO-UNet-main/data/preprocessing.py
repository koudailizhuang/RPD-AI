import os
import argparse


def move(src, dst):

    if not os.path.exists(dst):
        os.mkdir(dst)
    if not os.path.exists(os.path.join(dst)):
        os.mkdir(os.path.join(dst, 'blur'))
    if not os.path.exists(os.path.join(dst)):
        os.mkdir(os.path.join(dst, 'sharp'))

    print(src)
    print(dst)
    folders = os.listdir(src)
    print(folders)
    cnt = 0

    for f in folders:
        image_name = os.listdir(os.path.join(src, f))
        img_path = os.path.join(src, f)
        print(img_path)
        print(image_name)
        for i in image_name:
            int_putpath=os.path.join(src, f,  i)
            ouy_putpath=os.path.join(dst,  f,  i)
            print(int_putpath)
            print(ouy_putpath)
            os.rename(os.path.join(src, f, i), os.path.join(dst,  f,  i))
            os.rename(os.path.join(src, f, i), os.path.join(dst,  f,  i))
            cnt += 1
    print('%d images are moved' % cnt)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    # Directories
    parser.add_argument('--root_src', default='E:\GOPRO1', type=str)
    parser.add_argument('--root_dst', default='E:\GOPRO_Large1', type=str)

    args = parser.parse_args()
    path=os.path.join(args.root_src, 'train')
    print(path)
    if not os.path.exists(args.root_dst):
        os.mkdir(args.root_dst)

    move(os.path.join(args.root_src, 'train'), os.path.join(args.root_dst, 'train'))
    #move(os.path.join(args.root_src, 'test'), os.path.join(args.root_dst, 'test'))
