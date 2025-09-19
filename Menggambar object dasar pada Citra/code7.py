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

  cv.ellipse(citra,center=(xTengah,yTengah),axes=(100,50),angle=0,startAngle=0,endAngle=360,color=(255,0,0),thickness=5)

  cv.imshow("citra",citra)
  cv.waitKey(0)
  cv.destroyAllWindows()

if __name__ == "__main__":
  main()