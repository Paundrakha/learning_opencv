import cv2 as cv

def main():
    print("READING AND SHOWING IMAGE")
    gambar1 = cv.imread("yoona2.jpg")
    gambarCvt = cv.cvtColor(gambar1,cv.COLOR_BGR2GRAY)
    cv.imshow("ini gambar", gambar1)
    cv.imshow("gambar convert", gambarCvt)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()