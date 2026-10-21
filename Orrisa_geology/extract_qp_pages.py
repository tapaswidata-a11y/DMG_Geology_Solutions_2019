import subprocess, os, pytesseract
from PIL import Image

pdf = '/home/tapaswi/Mines_Geology/Orrisa_geology/Geology.pdf'

# Render pages 12 to 24
os.makedirs("qp_pages", exist_ok=True)
for p in range(12, 25):
    out = f"qp_pages/p{p:02d}"
    subprocess.run(['pdftoppm', '-png', '-r', '200', '-f', str(p), '-l', str(p), pdf, out], check=True)
    fnames = [os.path.join("qp_pages", f) for f in os.listdir("qp_pages") if f.startswith(f"p{p:02d}-")]
    if fnames:
        im = Image.open(fnames[0])
        # Two columns: left (x: 0 to width//2), right (x: width//2 to width)
        w, h = im.size
        # margin crop
        left_col = im.crop((50, 80, w//2 + 50, h - 80))
        right_col = im.crop((w//2 - 20, 80, w - 50, h - 80))
        
        txt_left = pytesseract.image_to_string(left_col)
        txt_right = pytesseract.image_to_string(right_col)
        
        with open(f"qp_pages/page_{p:02d}_left.txt", "w") as f:
            f.write(txt_left)
        with open(f"qp_pages/page_{p:02d}_right.txt", "w") as f:
            f.write(txt_right)
        with open(f"qp_pages/page_{p:02d}_combined.txt", "w") as f:
            f.write(f"=== PAGE {p} LEFT ===\n" + txt_left + f"\n=== PAGE {p} RIGHT ===\n" + txt_right)
        print(f"Page {p} extracted successfully.")

