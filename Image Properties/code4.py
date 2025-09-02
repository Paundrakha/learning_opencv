import cv2 as cv

def main():
  print("Image Properties citra abu")
  img=cv.imread("yoona2.jpg")
  imgAbu=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
  print("resolusi citra=", imgAbu.shape)
  jmlBaris=imgAbu.shape[0]
  jmlKolom=imgAbu.shape[1]
  jmlPixel=imgAbu.size
  tipedata=imgAbu.dtype
  print("Jumlah baris pada citra=", jmlBaris)
  print("Jumlah kolom pada citra=", jmlKolom)
  print("Jumlah pixel pada citra=", jmlPixel)
  print("Tipe data pada pixel=", tipedata)
  cv.imshow("Citra", imgAbu)
  cv.waitKey(0)
  cv.destroyAllWindows()

if __name__ == "__main__":
  main()