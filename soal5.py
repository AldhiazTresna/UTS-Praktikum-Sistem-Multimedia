from PIL import Image
import matplotlib.pyplot as plt

# (a) Membuka file gambar RGB
img_rgb = Image.open("sampel.jpg").convert("RGB")

# (b) Mengonversi gambar menjadi Grayscale ('L' = Luminance 8-bit)
img_gray = img_rgb.convert("L")

# (c) Menghitung histogram intensitas piksel (rentang 0 - 255)
histogram = img_gray.histogram()

# Menampilkan citra grayscale dan grafik histogram dengan Matplotlib
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.imshow(img_gray, cmap="gray", vmin=0, vmax=255)
plt.title("Citra Grayscale")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.plot(range(256), histogram, color="black")
plt.fill_between(range(256), histogram, color="gray", alpha=0.4)
plt.title("Histogram Intensitas Piksel")
plt.xlabel("Nilai Intensitas Piksel (0 = Hitam, 255 = Putih)")
plt.ylabel("Jumlah Piksel")
plt.xlim([0, 255])
plt.grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()
plt.show()