import cv2 as cv

def main():
  print("Cara mengetahui nilai pixel pada citra warna")
  img=cv.imread("yoona2.jpg")
  nilaipixelBlue=img[0,0,0]
  nilaipixelGreen=img[0,0,1]
  nilaipixelRed=img[0,0,2]
  print("Nilai pixel koordinat (0,0) pada kanal biru=",nilaipixelBlue)
  print("Nilai pixel koordinat (0,0) pada kanal hijau=",nilaipixelGreen)
  print("Nilai pixel koordinat (0,0) pada kanal merah=",nilaipixelRed)
  cv.imshow("Citra", img)
  cv.waitKey(0)
  cv.destroyAllWindows()

if __name__ == "__main__":
  main()