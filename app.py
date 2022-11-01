import cv2
import pytesseract
import pdf2image
import tabula

## extracting image from pdf

# images = pdf2image.convert_from_path('./data/finalreport.pdf')
# print("Converting Images from PDF")
# for page in range(len(images)):
#     images[page].save('page'+ str(page+1) +'.jpg', 'JPEG')

# print("Converting Done")

## pre-processing image page13

img = cv2.imread('./page13.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# ## characters detections

# # print(pytesseract.image_to_boxes(img)) # printing height and width
# # print(img.shape)
# height_img, width_img, _ = img.shape #setting up height, width images

# ### setting up the boxes
# boxes = pytesseract.image_to_boxes(img)
# for box in boxes.splitlines():
#   # print(box)
#   box = box.split(' ')
#   # print(box)
#   x, y, w, h = int(box[1]), int(box[2]), int(box[3]), int(box[4])
#   cv2.rectangle(img, (x, height_img-y), (w, height_img-h), (0,255, 0), 2)
#   cv2.putText(img, box[0], (x, height_img-y+40), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

# cv2.imshow('Page-13', img)
# cv2.waitKey(0)

# word detections

# print(pytesseract.image_to_boxes(img)) # printing height and width
# print(img.shape)
height_img, width_img, _ = img.shape #setting up height, width images

### setting up the boxes
boxes = pytesseract.image_to_data(img)
for x, box in enumerate (boxes.splitlines()):
  # print(box)
  if x>0: #first row is column name
    box = box.split()
    print(box)
    if len(box) == 12:
      x, y, w, h = int(box[6]), int(box[7]), int(box[8]), int(box[9])
      cv2.rectangle(img, (x, y), (w+x, h+y), (0,255, 0), 3)
      # cv2.putText(img, box[11], (x, y+60), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

cv2.imshow('Page-13', img)
cv2.waitKey(0)