#!/usr/bin/env python
"""Zoom detrame sur le scan de l'image 9 de *The Secret*.

Le scan est une reproduction d'imprimerie : le papier porte une trame de
demi-teintes (rosettes CMJN). Un autocontrast applique directement dessus
amplifie les points de trame au lieu du dessin, et le crop devient illisible.
On noie donc la trame au flou gaussien -- rayon ~= le pas de la rosette --
AVANT d'etirer le contraste, puis on agrandit.

    python zoom.py col 980 1980 1080 560
    python zoom.py figure 1820 2440 260 240 --scale 6 --blur 1.6

Zones utiles reperees (x y largeur hauteur, pixels du fichier pleine qualite
3064 x 4878) :

    bandeau       900   960  1180  260
    cheveux_d    1980  1480   340  300
    col           980  1980  1080  560
    panneau_haut 1820  2210   260  220
    panneau_bas  1820  2440   260  240
    objet        1940  2560   100  100
    pendentif    1780  2650   340  250
    manchette_g   940  3130   360  430
    manchette_d  2020  3140   340  430
    manteau       200  2700  2750  2000
"""
import argparse
import os

import numpy as np
from PIL import Image, ImageFilter

SRC = r"C:\Users\misty\Claude\Secret\images\09_pleine_qualite.jpg"


def zoom(src, box, scale=3.0, blur=1.8, lo_pct=2.0, hi_pct=98.0, gray=True):
    im = Image.open(src).crop(box).filter(ImageFilter.GaussianBlur(blur))
    if gray:
        im = im.convert("L")
    a = np.asarray(im, dtype=np.float32)
    if a.ndim == 2:
        a = _stretch(a, lo_pct, hi_pct)
    else:
        for c in range(a.shape[2]):
            a[:, :, c] = _stretch(a[:, :, c], lo_pct, hi_pct)
    out = Image.fromarray(a.astype("uint8"))
    w, h = box[2] - box[0], box[3] - box[1]
    return out.resize((int(w * scale), int(h * scale)), Image.LANCZOS)


def _stretch(a, lo_pct, hi_pct):
    lo, hi = np.percentile(a, lo_pct), np.percentile(a, hi_pct)
    return np.clip((a - lo) / max(hi - lo, 1e-6), 0, 1) * 255


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("name")
    p.add_argument("x", type=int)
    p.add_argument("y", type=int)
    p.add_argument("w", type=int)
    p.add_argument("h", type=int)
    p.add_argument("--scale", type=float, default=3.0)
    p.add_argument("--blur", type=float, default=1.8,
                   help="rayon du flou anti-trame, en pixels natifs")
    p.add_argument("--color", action="store_true")
    p.add_argument("--src", default=SRC)
    p.add_argument("--out", default=".")
    a = p.parse_args()

    img = zoom(a.src, (a.x, a.y, a.x + a.w, a.y + a.h),
               scale=a.scale, blur=a.blur, gray=not a.color)
    path = os.path.join(a.out, a.name + ".png")
    img.save(path)
    print(path, img.size)


if __name__ == "__main__":
    main()
