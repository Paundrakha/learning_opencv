import cv2 as cv

def main():
  print("Cara mengetahui nilai pixel pada citra abu abu")
  img=cv.imread("yoona2.jpg",cv.IMREAD_GRAYSCALE)
  nilaipixel=img[1:5,1:5]
  #Nilai pixel dari baris 1-5 dan kolom 1-5
  print("Nilai pixel=",nilaipixel)
  cv.imshow("Citra", img)
  cv.waitKey(0)
  cv.destroyAllWindows()

if __name__ == "__main__":
  main()