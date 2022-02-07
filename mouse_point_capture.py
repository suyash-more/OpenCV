import os
import cv2 as cv

def click_event(event, x, y, flags, params):

	if event == cv.EVENT_LBUTTONDOWN:
		print('X-Cord = {0}, Y-Cord = {1}'.format(x,y))
		font = cv.FONT_HERSHEY_SIMPLEX
		cv.putText(img, str(x) + ',' +
					str(y), (x,y), font,
					1, (255, 0, 0), 2)
		cv.imshow('image', img)

	if event==cv.EVENT_RBUTTONDOWN:
		print('X-Cord = {0}, Y-Cord = {1}'.format(x,y))
		font = cv.FONT_HERSHEY_SIMPLEX
		b = img[y, x, 0]
		g = img[y, x, 1]
		r = img[y, x, 2]
		cv.putText(img, str(b) + ',' +
					str(g) + ',' + str(r),
					(x,y), font, 1,
					(255, 255, 0), 2)
		cv.imshow('image', img)

if __name__=="__main__":
  path_to_image = os.path.join(os.path.dirname(__file__), "images", "warp.jpeg")
  img = cv.imread(path_to_image, 1)
  cv.imshow('image', img)
  cv.setMouseCallback('image', click_event)
  cv.waitKey(0)
  cv.destroyAllWindows()
