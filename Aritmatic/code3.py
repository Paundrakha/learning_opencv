import cv2 as cv

def main():
  print("Image Addition with weight")
  img1=cv.imread("baboon.jpg")
  img2=cv.imread("lena.jpg")

  hasilA=cv.addWeighted(src1=img1,alpha=0.5,src2=img2,beta=0.5,gamma=0)
  hasilB=cv.addWeighted(src1=img1,alpha=0.7,src2=img2,beta=0.3,gamma=0)
  hasilC=cv.addWeighted(src1=img1,alpha=0.3,src2=img2,beta=0.7,gamma=0)

  cv.imshow("Hasil A",hasilA)
  cv.imshow("Hasil B",hasilB)
  cv.imshow("Hasil C",hasilC)
  cv.waitKey(0)
  cv.destroyAllWindows()

if __name__ == "__main__":
  main()