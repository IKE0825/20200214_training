import sklearn.datasets
import sklearn.svm
import PIL.Image
import numpy
import pdb

def imageToData(filename):
    grayImage = PIL.Image.open(filename).convert("L") #Imageモード　L : 8bitグレイスケール
    grayImage = grayImage.resize((8,8),PIL.Image.ANTIALIAS) #画像サイズの縮小、アンチエアリアス処理
    numImage = numpy.asarray(grayImage,dtype = float)
    print(numImage)
    numImage = numpy.floor(16 - 16 * (numImage / 256)) #floor 切り捨て
    print(numImage)
    numImage = numImage.flatten() # リストの平坦化
    print(numImage)
    return numImage

def predictDigits(data):
    digits = sklearn.datasets.load_digits()
    clf = sklearn.svm.SVC(gamma = 0.001,C=100) #機械学習用マシン
    clf.fit(digits.data,digits.target) 
    n = clf.predict([data])
    print("予測は= " , n)

data = imageToData("2.png")
predictDigits(data)