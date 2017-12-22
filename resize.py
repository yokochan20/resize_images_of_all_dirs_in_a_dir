'''
画像が格納されているディレクトリの集合のディレクトリの
パスを入力すると，画像を自動に順々に取得していき，
リサイズしてくれるスクリプトを書く
'''
import os
import numpy as np
import cv2

def get_image_paths(facedir):
    image_paths = []
    if os.path.isdir(facedir):
        images = os.listdir(facedir)
        image_paths = [os.path.join(facedir,img) for img in images]
    return image_paths

def get_image_paths_and_labels(dataset):
    image_paths_flat = []
    labels_flat = []
    for i in range(len(dataset)):
        image_paths_flat += dataset[i].image_paths
        labels_flat += [i] * len(dataset[i].image_paths)
    return image_paths_flat, labels_flat

def resize_dataset(path, has_class_directories=True):
    dataset = []
    #get path of directory / パスの取得
    path_exp = os.path.expanduser(path)
    #get directories' names in the directory / ディレクトリ内のディレクトリ名を取得
    classes = os.listdir(path_exp)
    #sort rectories by amount of images / 少ない順に並び替え
    classes.sort()
    #pop ".DS_store" from list when it exists / .DS_Storeがあったら，配列からpop
    if '.DS_Store' in classes :
        classes.remove('.DS_Store')
    else :
        pass
    #count how many classes/クラス数を数える
    nrof_classes = len(classes)
    for i in range(nrof_classes):
        class_name = classes[i]
        #get path / i番目のディレクトリのパス名を取得
        facedir = os.path.join(path_exp, class_name)
        #get images path/get_image_pathsを用いて，画像のパスを取得
        image_paths = get_image_paths(facedir)
        image_paths.sort()
        images = len(image_paths)
        for t in range(images) :
            #画像の読み込み
            p2img = image_paths[t]
            #img = '/'.join(img)
            i = cv2.imread(p2img)
            #resize images / リサイズを実行する
            resize_image = cv2.cvtColor(cv2.resize(i, (resize_width,resize_height)), cv2.COLOR_RGB2BGR)
            #保存
            cv2.imwrite(p2img,resize_image)
        #end / 何を返すのか，データセット
    return dataset

datadir = '/Users/SatoshiYokoyama/D-HACKS/abcd_test'
resize_width = 160
resize_height = 160

dataset = resize_dataset(datadir)
paths, labels = get_image_paths_and_labels(dataset)
print ("Number of classes: %d" % len(dataset))
print ("Number of images: %d" % len(paths))


