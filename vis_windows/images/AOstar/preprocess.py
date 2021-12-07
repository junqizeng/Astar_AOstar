import base64


def pic2py(picture_names):
    write_data = []
    for name in picture_names:
        open_pic = open("%s" % name, 'rb')
        b64str = base64.b64encode(open_pic.read())
        open_pic.close()
        write_data.append("%s" % b64str.decode())
    f = open("AO_images.py", 'w+')
    f.write("imgs = "+str(write_data))
    f.close()


if __name__ == '__main__':
    pics = ["-1.png", "0.png", "1.png", "2.png", "3.png", "4.png"]
    pic2py(pics)
