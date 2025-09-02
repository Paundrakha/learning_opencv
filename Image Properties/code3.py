import cv2 as cv

def main():
  print("Image Properties citra warna")
  img=cv.imread("yoona2.jpg")
  print("resolusi citra=", img.shape)
  jmlBaris=img.shape[0]
  jmlKolom=img.shape[1]
  jmlKanal=img.shape[2]
  jmlPixel=img.size
  tipedata=img.dtype
  print("Jumlah baris pada citra=", jmlBaris)
  print("Jumlah kolom pada citra=", jmlKolom)
  print("Jumlah kanal pada citra=", jmlKanal)
  print("Jumlah pixel pada citra=", jmlPixel)
  print("Tipe data pada pixel=", tipedata)
  cv.imshow("Citra", img)
  cv.waitKey(0)
  cv.destroyAllWindows()

if __name__ == "__main__":
  main()