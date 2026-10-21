import urllib.request
import re
import glob

base_url = "http://localhost:8085"

# 1. Test index.html modal images
print("--- 1. Testing modal images from index.html ---")
req = urllib.request.urlopen(f"{base_url}/index.html")
html = req.read().decode('utf-8')
modal_imgs = re.findall(r'<img[^>]+src=[\'\"]([^\'\"]+)[\'\"]', html)
print(f"Total modal image tags in index.html: {len(modal_imgs)}")

modal_errors = []
for src in set(modal_imgs):
    img_url = f"{base_url}/{src}"
    try:
        r = urllib.request.urlopen(img_url)
        if r.status != 200:
            modal_errors.append((img_url, r.status))
    except Exception as e:
        modal_errors.append((img_url, str(e)))

print(f"Modal images tested: {len(set(modal_imgs))}, Errors: {len(modal_errors)}")
if modal_errors:
    for e in modal_errors:
        print("  ERROR:", e)

# 2. Test standalone guide images
print("\n--- 2. Testing standalone guide images ---")
guide_files = sorted(glob.glob("solutions/geology_2021/Q*.html"))
print(f"Total standalone guides found: {len(guide_files)}")

guide_errors = []
total_guide_imgs = set()

for gf in guide_files:
    url = f"{base_url}/{gf}"
    req = urllib.request.urlopen(url)
    g_html = req.read().decode('utf-8')
    imgs = re.findall(r'<img[^>]+src=[\'\"]([^\'\"]+)[\'\"]', g_html)
    for src in imgs:
        # resolve relative to solutions/geology_2021/
        # if src is ../../figures_Q01/abc.png -> base_url/figures_Q01/abc.png
        resolved = src.replace("../../", "")
        img_url = f"{base_url}/{resolved}"
        if img_url in total_guide_imgs:
            continue
        total_guide_imgs.add(img_url)
        try:
            r = urllib.request.urlopen(img_url)
            if r.status != 200:
                guide_errors.append((gf, img_url, r.status))
        except Exception as e:
            guide_errors.append((gf, img_url, str(e)))

print(f"Standalone unique images tested: {len(total_guide_imgs)}, Errors: {len(guide_errors)}")
if guide_errors:
    for e in guide_errors:
        print("  ERROR:", e)

if not modal_errors and not guide_errors:
    print("\n>>> ALL CHECKS PASSED: 100% 200 OK for every single figure across all 150 questions! <<<")
else:
    print("\n>>> THERE WERE ERRORS! <<<")

