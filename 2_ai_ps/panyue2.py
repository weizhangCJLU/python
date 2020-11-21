import removebg
import os
import shutil

rmbg = removebg.RemoveBg("3EmmeEPcPRyRR41FPJ1se7H7", "error.log")

r = r"C:\Users\Lenovo\PycharmProjects\untitled1\project\ai_ps\raw_img2"

new_folder = os.path.join(r, "抠图")


def batch_removebg():
    fileList = os.listdir(r)
    for f in fileList:
        suffix = os.path.splitext(f)[-1]
        if suffix == ".png" or suffix == ".jpg":
            rmbg.remove_background_from_img_file(os.path.join(r, f))


def make_new_folder():
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)


def copy_new_pic():
    fileList = os.listdir(r)
    for f in fileList:
        if f.count("no_bg") > 0:
            print(os.path.join(r, f))
            shutil.move(os.path.join(r, f), new_folder)


make_new_folder()
batch_removebg()
copy_new_pic()

