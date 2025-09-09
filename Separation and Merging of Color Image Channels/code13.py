import cv2 as cv

def main():
  print("Pemisahan dan penggabungan kanal warna pada citra warna")
  img=cv.imread("yoona2.jpg")
  img=cv.cvtColor(img,cv.COLOR_BGR2YCrCb)
  luminasi,Cr,Cb=cv.split(img)
  cv.imshow("Kanal luminasi", luminasi)
  cv.imshow("Kanal Cr", Cr)
  cv.imshow("Kanal Cb", Cb)
  imgYCrCb=cv.merge([luminasi,Cr,Cb])
  cv.imshow("Pengabungan 3 kanal", imgYCrCb)
  cv.waitKey(0)
  cv.destroyAllWindows()


if __name__ == "__main__":
  main()