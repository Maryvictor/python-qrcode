import qrcode

dado = "https://www.linkedin.com/in/maria-victor/"

img = qrcode.make(dado)
img.show()
img.save(f'img/img.png')
