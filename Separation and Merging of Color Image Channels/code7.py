import cv2 as cv

def main():
  print("Pemisahan dan penggabungan kanal warna pada citra warna")
  img=cv.imread("yoona2.jpg")
  img=cv.cvtColor(img,cv.COLOR_BGR2HSV)
  hue,saturation,value=cv.split(img)
  cv.imshow("Kanal hue", hue)
  cv.imshow("Kanal saturation",saturation)
  cv.imshow("Kanal value", value)
  imgHSV=cv.merge([hue,saturation,value])
  cv.imshow("Pengabungan 3 kanal", imgHSV)
  cv.waitKey(0)
  cv.destroyAllWindows()


if __name__ == "__main__":
  main()