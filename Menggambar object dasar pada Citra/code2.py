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

  cv.arrowedLine(citra,pt1=(xTengah,0),pt2=(xTengah,jmlBaris-1),color=(0,0,255),thickness=5)
  cv.arrowedLine(citra,pt1=(0,yTengah),pt2=(jmlKolom-1,yTengah),color=(255,0,0),thickness=5)
  cv.imshow("Citra",citra)
  cv.waitKey(0)
  cv.destroyAllWindows()

if __name__ == "__main__":
  main()