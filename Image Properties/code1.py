import cv2 as cv

def main():
  print("Image Properties citra abu abu")
  img=cv.imread("yoona2.jpg")
  img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
  print("resolusi citra=", img.shape)
  jmlBaris=img.shape[0]
  jmlKolom=img.shape[1]
  print("Jumlah baris pada citra=", jmlBaris)
  print("Jumlah kolom pada citra=", jmlKolom)
  cv.imshow("Citra", img)
  cv.waitKey(0)
  cv.destroyAllWindows()

if __name__ == "__main__":
  main()