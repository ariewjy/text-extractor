from email.mime import image
import cv2
import pytesseract
import pdf2image
import tabula
import streamlit as st
from PIL import Image
import numpy as np
from tempfile import NamedTemporaryFile
import tempfile

# ## characters detections

# st.write(pytesseract.image_to_boxes(img)) # printing height and width
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




# Title
st.title('Text-Extractor')

# importing data

st.subheader('Importing Files')
mode = st.radio(
    "Select file format",
    (
      'pdf', 
      # 'image'
      )
)

# converting pdf to images

if mode == 'pdf':
    file = st.file_uploader('Upload pdf file')
    # button = st.button('Extract PDF to Images')
    if file is not None:
      images = pdf2image.convert_from_bytes(file.read())
      st.subheader('Select Page')
      page_number = [z+1 for z in list(np.arange(len(images)))]
      page = (st.select_slider('Page Number', options=page_number)) - 1
      img=images[page]
      # st.image(img)

if mode == 'image':
    file = st.file_uploader('Upload image file')
    if file is not None:
      img=file
      st.subheader('Image Uploaded')
      # st.image(img)

# st.image(img)
# if img is not None:

if file:
  st.image(img)
  img = np.array(img)
  st.write(img.shape)
  st.subheader('Before')
  height_img, width_img, _ = img.shape #setting up height, width images
  
# word detections
  boxes = pytesseract.image_to_data(img)
  for x, box in enumerate (boxes.splitlines()):
    # st.write(box)
    if x>0: #first row is column name
      box = box.split()
      # print(box)
      if len(box) == 12:
        x, y, w, h = int(box[6]), int(box[7]), int(box[8]), int(box[9])
        img_pp = cv2.rectangle(img, (x, y), (w+x, h+y), (0,255, 0), 3)
        # img_pp = cv2.putText(img, box[11], (x, y+60), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

  st.subheader('After')
  st.image(img_pp)
  # img = images[page]
  text_from_image = pytesseract.image_to_string(images[page], lang='eng')
  st.subheader('Text Extracted')
  for index, text in enumerate (text_from_image.splitlines()):
    st.write(text)

# pdf_pp = pytesseract.image_to_pdf_or_hocr(images[page])
# st.download_button(data=pdf_pp)