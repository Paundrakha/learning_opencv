import cv2 as cv

def main():
  print("Menambahkan garis (line) pada sebuah citra")
  citra=cv.imread("yoona2.jpg")
  jmlBaris=citra.shape[0]
  jmlKolom=citra.shape[1]
  print("Jumlah baris pada citra\t=",jmlBaris)
  print("Jumlah kolom pada citra\t=",jmlKolom)
  xTengah=jmlKolom//2
  yTengah=jmlBaris//2

  cv.circle(citra,center=(xTengah,yTengah),radius=100,color=(100,100,100),thickness=cv.FILLED)

  cv.imshow("Citra",citra)
  cv.waitKey(0)
  cv.destroyAllWindows()

if __name__ == "__main__":
  main()