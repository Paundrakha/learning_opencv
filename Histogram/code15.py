import cv2 as cv

def main():
  print("Ekualisasi Histogram citra warna melalui ruang warna LUV")
  img=cv.imread("yoona2.jpg")
  imgLUV=cv.cvtColor(img,cv.COLOR_BGR2LUV)
  L=imgLUV[:,:,0]
  U=imgLUV[:,:,1]
  V=imgLUV[:,:,2]

  equalizeL=cv.equalizeHist(L)
  equalizedLUV=cv.merge([equalizeL,U,V])
  equalizedImg=cv.cvtColor(equalizedLUV,cv.COLOR_LUV2BGR)
  cv.imshow("Original Image", img)
  cv.imshow("Histogram Equalization", equalizedImg)
  cv.waitKey(0)
  cv.destroyAllWindows()

if __name__ == "__main__":
  main()