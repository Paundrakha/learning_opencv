import cv2 as cv

def main():
    img = cv.imread("yoona2.jpg")
    print("resolusi citra", img.shape)
    imgChannelB = img[:,:,0]
    print("resolusi Biru", imgChannelB)
    imgChannelG = img[:,:,1]
    print("resolusi Hijau", imgChannelG)
    imgChannelR = img[:,:,2]
    print("resolusi Merah", imgChannelR)
    imgBGR = cv.merge([imgChannelB, imgChannelG,imgChannelR])
    print("resolosi gabungan 3 warna", imgBGR.shape)
    cv.imshow("Channel Blue", imgChannelB)
    cv.imshow("Channel Green", imgChannelG)
    cv.imshow("Channel Red", imgChannelR)
    cv.imshow("Channel 3 channel", imgBGR)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()

