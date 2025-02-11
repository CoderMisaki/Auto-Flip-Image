from PIL import Image, ImageStat
import os

def get_brightness(image):
    if image.mode != 'L':
        image = image.convert('L')
    stat = ImageStat.Stat(image)
    return stat.mean[0]

def get_contrast(image):
    if image.mode != 'L':
        image = image.convert('L')
    stat = ImageStat.Stat(image)
    return stat.stddev[0]

def calculate_histogram_difference(left_image, right_image):
    left_hist = left_image.histogram()
    right_hist = right_image.histogram()
    hist_diff = sum(abs(l - r) for l, r in zip(left_hist, right_hist))
    return hist_diff

def calculate_threshold(brightness_left, brightness_right, contrast_left, contrast_right, hist_diff):
    brightness_diff = abs(brightness_left - brightness_right)
    contrast_diff = abs(contrast_left - contrast_right)
    return max(0.5, (brightness_diff + contrast_diff + hist_diff * 0.001))

try:
    image_path = input("Masukkan path gambar: ").strip()
    if not os.path.isfile(image_path):
        print("File gambar tidak ditemukan.")
        exit()

    img = Image.open(image_path)
    width, height = img.size

    left_part = img.crop((0, 0, width // 10, height))
    right_part = img.crop((width - width // 10, 0, width, height))

    brightness_left = get_brightness(left_part)
    brightness_right = get_brightness(right_part)

    contrast_left = get_contrast(left_part)
    contrast_right = get_contrast(right_part)

    hist_diff = calculate_histogram_difference(left_part, right_part)

    THRESHOLD = calculate_threshold(brightness_left, brightness_right, contrast_left, contrast_right, hist_diff)

    print(f"Kecerahan kiri: {brightness_left}, Kecerahan kanan: {brightness_right}")
    print(f"Kontras kiri: {contrast_left}, Kontras kanan: {contrast_right}")
    print(f"Histogram Difference: {hist_diff}")
    print(f"Threshold: {THRESHOLD}")

    if abs(brightness_left - brightness_right) > THRESHOLD or abs(contrast_left - contrast_right) > THRESHOLD or hist_diff > 1000:
        img_flipped = img.transpose(Image.FLIP_LEFT_RIGHT)
        base_name, ext = os.path.splitext(image_path)
        output_path = f"{base_name}_flipped{ext}"
        img_flipped.save(output_path)
        print(f"Gambar dibalik, disimpan di {output_path}")
    else:
        print("Tidak ada perubahan arah gambar.")

except Exception as e:
    print(f"Terjadi kesalahan: {e}")
