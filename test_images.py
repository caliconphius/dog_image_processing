from PIL import Image
img = Image.open('sample.webp').convert('RGB')
img.save('jpg_image.jpg', 'jpeg')
