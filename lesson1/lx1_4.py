import qrcode

url = "https://www.tongji.edu.cn/"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(url)
qr.make(fit=True)
# 创建二维码图片
img = qr.make_image(fill_color="black", back_color="white")

# 保存图片
img.save("tongji_qrcode.png")
print("已生成二维码图片：tongji_qrcode.png")

