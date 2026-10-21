import subprocess, os, pytesseract
from PIL import Image

pdf = '/home/tapaswi/Mines_Geology/TEXT_BOOK/A text book of GEOLOGY by G.B.Mahapatra.pdf'

pages = [165, 168, 173, 186]
for p in pages:
    out = f"mahapatra_p{p}"
    subprocess.run(['pdftoppm', '-png', '-r', '150', '-f', str(p), '-l', str(p), pdf, out], check=True)
    fname = f"{out}-{p:03d}.png" if os.path.exists(f"{out}-{p:03d}.png") else f"{out}-{p:02d}.png"
    im = Image.open(fname)
    print(f"Mahapatra p{p} rendered. Size: {im.size}")
    txt = pytesseract.image_to_string(im)
    for l in txt.split('\n'):
        if any(w in l.upper() for w in ['VINDHYAN', 'SEMRI', 'KAIMUR', 'REWA', 'BHANDER', 'TALCHIR', 'BOULDER', 'MUTH', 'SPITI', 'CRETACEOUS', 'TRICHINOPOLY', 'UTTATUR', 'ARIYALUR', 'AMMONITE', 'SUTURE', 'FIG']):
            print(f"  [p{p}] {l.strip()[:90]}")

