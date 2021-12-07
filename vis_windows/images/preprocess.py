import base64


def pic2py(picture_name):
    open_pic = open("%s" % picture_name, 'rb')
    b64str = base64.b64encode(open_pic.read())
    open_pic.close()
    f = open("whu_ico.py", 'w+')
    f.write("imgs = '%s'" % b64str.decode())
    f.close()


if __name__ == '__main__':
    pics = "whu.ico"
    pic2py(pics)
