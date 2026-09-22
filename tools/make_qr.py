#!/usr/bin/env python3
"""Generate the conference QR code for the RoCarp-CHM-AGB landing page.

Produces a vector SVG for print and a high-resolution PNG as a fallback.
The QR uses error-correction level H (30 % recoverable), which survives a
fingerprint, a fold or a poorly printed edge.

    pip install segno
    python tools/make_qr.py https://mihnea13.github.io/rocarp-chm-agb/

Print guidance: at 3 cm the module size of this code is around 0.7 mm, which
every current phone camera resolves at arm's length. Do not go below 2.5 cm,
and leave the white quiet zone around the code intact.
"""
import sys
import pathlib

try:
    import segno
except ImportError:
    sys.exit("segno is not installed - run: pip install segno")

DEFAULT_URL = "https://mihnea13.github.io/rocarp-chm-agb/"


def main() -> None:
    url = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_URL

    out = pathlib.Path(__file__).resolve().parent.parent / "qr"
    out.mkdir(exist_ok=True)

    qr = segno.make(url, error="h")

    # Vector, for the poster file. scale sets the module size in SVG user units.
    qr.save(out / "rocarp-qr.svg", scale=10, border=4, dark="#000000", light="#ffffff")

    # Raster fallback: 720 px across, i.e. ~30 mm at 600 dpi.
    qr.save(out / "rocarp-qr.png", scale=16, border=4, dark="#000000", light="#ffffff")

    print(f"encoded : {url}")
    print(f"version : {qr.version}  (modules per side: {qr.symbol_size(scale=1, border=0)[0]})")
    print(f"written : {out / 'rocarp-qr.svg'}")
    print(f"          {out / 'rocarp-qr.png'}")
    print("\nPrint the URL in readable text underneath the code - people")
    print("photograph posters instead of scanning them.")


if __name__ == "__main__":
    main()
