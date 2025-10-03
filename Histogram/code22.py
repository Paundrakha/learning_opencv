import cv2 as cv

def main():
  print("Ekualisasi Histogram Citra Warna melalui HLS dengan CLAHE")
  img=cv.imread("yoona2.jpg")
  HLSImg=cv.cvtColor(img,cv.COLOR_BGR2HLS)

  H=HLSImg[:,:,0]
  L=HLSImg[:,:,1]
  S=HLSImg[:,:,2]

  clahe=cv.createCLAHE(clipLimit=10,tileGridSize=(8,8))
  equalizeL=clahe.apply(L)
  equalizedHLS=cv.merge([H,equalizeL,S])
  equalizeImage=cv.cvtColor(equalizedHLS,cv.COLOR_HLS2BGR)
  cv.imshow("Original Image", img)
  cv.imshow("Histogram Equalization", equalizeImage)
  cv.waitKey(0)
  cv.destroyAllWindows()

if __name__ == "__main__":
  main()