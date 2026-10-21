import urllib.request
import re
import os

base_url = "http://localhost:8085"

print("1. Checking index.html...")
req = urllib.request.urlopen(f"{base_url}/index.html")
print(f"index.html status: {req.status}")
html = req.read().decode('utf-8')

# Find all guide links
guide_links = set(re.findall(r'solutions/geology_2021/Q[^\"]+\.html', html))
print(f"Found {len(guide_links)} guide links in index.html")

failed_guides = []
failed_images = []
tested_images = set()

for gl in sorted(guide_links):
    url = f"{base_url}/{gl}"
    try:
        g_req = urllib.request.urlopen(url)
        if g_req.status != 200:
            failed_guides.append((url, g_req.status))
        g_html = g_req.read().decode('utf-8')
        # find all images in this guide
        imgs = re.findall(r'<img[^>]+src=[\'\"]([^\'\"]+)[\'\"]', g_html)
        for img in imgs:
            if img in tested_images:
                continue
            tested_images.add(img)
            # resolve relative path
            if img.startswith('figures_'):
                img_url = f"{base_url}/solutions/geology_2021/{img}"
                # wait, let's see how the img src is written: is it relative to root or relative to guide?
                # In standalone guides in solutions/geology_2021/, if src="figures_QXX/...", 
                # let's check how the browser resolves it!
            else:
                img_url = f"{base_url}/{img}"
    except Exception as e:
        failed_guides.append((url, str(e)))

print(f"Tested {len(guide_links)} guides: {len(failed_guides)} failed")
