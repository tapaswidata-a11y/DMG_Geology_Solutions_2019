import subprocess, os, pytesseract
from PIL import Image

for pdf in ['Geology.pdf', 'Mining Officer Applied Geology P_II.pdf', '091819_Geology.pdf']:
    subprocess.run(['pdftoppm', '-png', '-r', '150', '-f', '1', '-l', '2', pdf, f'qp_{pdf[:4]}'], check=True)
    for f in sorted(os.listdir('.')):
        if f.startswith(f'qp_{pdf[:4]}'):
            txt = pytesseract.image_to_string(Image.open(f))
            print(f"=== {pdf} ({f}) ===")
            print(txt[:300])
            os.remove(f)

