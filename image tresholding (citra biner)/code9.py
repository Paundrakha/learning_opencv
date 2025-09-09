import cv2 as cv

def main():
  print("Global Image Tresholding dengan threshold truncated")
  img=cv.imread("yoona2.jpg")

  imgGrey=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
  jmlBaris = imgGrey.shape[0]
  jmlKolom = imgGrey.shape[1]

  threshold=125

  for i in range(jmlBaris):
    for j in range(jmlKolom):
      if imgGrey[i,j]>threshold:
        imgGrey[i,j]=threshold
      else:
        imgGrey[i,j]=imgGrey[i,j]

  cv.imshow("Original image", img)
  cv.imshow("Image Thresholding", imgGrey)
  cv.waitKey(0)
  cv.destroyAllWindows()

if __name__ == "__main__":
  main()
