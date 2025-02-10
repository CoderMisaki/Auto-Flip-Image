from PIL import Image, ImageStat
import os

print("Program dimulai. Silakan masukkan path gambar.")  # Debugging awal

def get_brightness(image):
    stat = ImageStat.Stat(image)
    return sum(stat.mean) / len(stat.mean)

def calculate_threshold(brightness_left, brightness_right):
    average_brightness = (brightness_left + brightness_right) / 2
    return max(5.0, average_brightness * 0.1)

try:
    image_path = input("Masukkan path gambar: ").strip()
    print(f"Path gambar yang dimasukkan: {image_path}")  # Debugging

    if not os.path.isfile(image_path):
        print("File gambar tidak ditemukan.")
        exit()

    img = Image.open(image_path)
    width, height = img.size
    print(f"Ukuran gambar: {width}x{height}")  # Debugging

    left_part = img.crop((0, 0, width // 10, height))
    right_part = img.crop((width - width // 10, 0, width, height))

    brightness_left = get_brightness(left_part)
    brightness_right = get_brightness(right_part)
    print(f"Kecerahan kiri: {brightness_left}, Kecerahan kanan: {brightness_right}")  # Debugging

    THRESHOLD = calculate_threshold(brightness_left, brightness_right)
    print(f"Threshold: {THRESHOLD}")  # Debugging

    if abs(brightness_left - brightness_right) > THRESHOLD:
        img_flipped = img.transpose(Image.FLIP_LEFT_RIGHT)
        base_name, ext = os.path.splitext(image_path)
        output_path = f"{base_name}_flipped{ext}"
        img_flipped.save(output_path)
        print(f"Gambar dibalik, disimpan di {output_path}")
    else:
        print("Tidak ada perubahan arah gambar.")

except Exception as e:
    print(f"Terjadi kesalahan: {e}")