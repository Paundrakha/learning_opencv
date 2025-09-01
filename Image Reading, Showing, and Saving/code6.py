import cv2 as cv

def main():
    print("READING AND SHOWING IMAGE")
    gambar3 = cv.imread("yoona2.jpg")
    gambarCvt = cv.cvtColor(gambar3,cv.COLOR_BGR2GRAY)
    cv.imshow("ini gambar", gambar3)
    cv.imshow("gambar convert", gambarCvt)
    key = cv.waitKey(0)
    if key==115:
        cv.imwrite("gambar.png", gambarCvt)
        print("gambar tersimpan")
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()