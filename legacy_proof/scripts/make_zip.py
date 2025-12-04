#!/usr/bin/env python3
import os, zipfile
def zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        for f in files:
            fp = os.path.join(root, f)
            rel = os.path.relpath(fp, path)
            ziph.write(fp, rel)
if __name__ == "__main__":
    out = "beal-pipeline.zip"
    with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as z:
        zipdir(".", z)
    print(f"Created {out}")
