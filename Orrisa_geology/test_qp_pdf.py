import subprocess, os, pytesseract
from PIL import Image

pdf = '/home/tapaswi/Mines_Geology/Orrisa_geology/Geologist P_II.pdf'
subprocess.run(['pdftoppm', '-png', '-r', '150', '-f', '1', '-l', '2', pdf, 'qp_test'], check=True)
for f in sorted(os.listdir('.')):
    if f.startswith('qp_test'):
        txt = pytesseract.image_to_string(Image.open(f))
        print(f"=== {f} ===")
        print(txt[:400])
        os.remove(f)

