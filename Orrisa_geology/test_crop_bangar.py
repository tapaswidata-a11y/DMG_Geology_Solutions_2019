import subprocess, os
from PIL import Image

pdf = '/home/tapaswi/Mines_Geology/TEXT_BOOK/ Principle of Engieneering Geology by K M BANGAR.pdf'

# Bangar p. 23 (Pedestal Rock)
subprocess.run(['pdftoppm', '-png', '-r', '200', '-f', '23', '-l', '23', pdf, 'bangar_p23'], check=True)
fname = 'bangar_p23-23.png' if os.path.exists('bangar_p23-23.png') else 'bangar_p23-023.png'
im = Image.open(fname)
print(f"Bangar p23 size: {im.size}")

# Bangar p. 28 (Drainage patterns)
subprocess.run(['pdftoppm', '-png', '-r', '200', '-f', '28', '-l', '28', pdf, 'bangar_p28'], check=True)
fname2 = 'bangar_p28-28.png' if os.path.exists('bangar_p28-28.png') else 'bangar_p28-028.png'
im2 = Image.open(fname2)
print(f"Bangar p28 size: {im2.size}")

