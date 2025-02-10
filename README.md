# Auto-Flip-Image

termux-setup-storage
pkg update -y && pkg upgrade -y
pkg install python -y
pkg install python-pip
pkg install git -y 
pkg install libjpeg-turbo libpng freetype -y
pip install --no-cache-dir pillow
git clone https://github.com/CoderMisaki/Auto-Flip-Image/
cd Auto-Flip-Image
python image.py

