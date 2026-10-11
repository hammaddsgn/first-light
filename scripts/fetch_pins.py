"""Download the pins listed in assets/pins.txt into assets/pins/{key}.jpg.
Runs on GitHub Actions, which can reach i.pinimg.com. Skips files already present."""
import pathlib, urllib.request, sys
root = pathlib.Path(__file__).resolve().parent.parent
out = root / "assets" / "pins"; out.mkdir(parents=True, exist_ok=True)
fail = 0
for line in (root / "assets" / "pins.txt").read_text().splitlines():
    if not line.strip() or line.startswith("#"): continue
    key, h = line.split()[:2]
    dest = out / f"{key}.jpg"
    if dest.exists() and dest.stat().st_size > 1000: continue
    url = f"https://i.pinimg.com/736x/{h[:2]}/{h[2:4]}/{h[4:6]}/{h}.jpg"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        data = urllib.request.urlopen(req, timeout=30).read()
        if data[:3] != b"\xff\xd8\xff": raise ValueError("not a jpeg")
        dest.write_bytes(data); print("ok", key, len(data))
    except Exception as e:
        fail += 1; print("FAILED", key, e)
sys.exit(1 if fail else 0)
