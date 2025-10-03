import cv2 as cv

def main():
  print("Ekualisasi Histogram citra warna melalui ruang warna HLS")
  img=cv.imread("yoona2.jpg")
  imgHLS=cv.cvtColor(img,cv.COLOR_BGR2HLS)
  H=imgHLS[:,:,0]
  L=imgHLS[:,:,1]
  S=imgHLS[:,:,2]

  equalizeL=cv.equalizeHist(L)
  equalizedHLS=cv.merge([H,equalizeL,S])
  equalizedImg=cv.cvtColor(equalizedHLS,cv.COLOR_HLS2BGR)
  cv.imshow("Original Image", img)
  cv.imshow("Histogram Equalization", equalizedImg)
  cv.waitKey(0)
  cv.destroyAllWindows()

if __name__ == "__main__":
  main()