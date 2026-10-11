# First Light

Daily morning briefing email, sent at 07:48 UK time by a scheduled Claude task.

- `email/build_email.py` builds the weekday and weekend email layouts (design kit).
- `assets/pins/` holds pictures from the notetoself Pinterest board, served to Gmail through raw.githubusercontent.com.
- `assets/gif/` holds small animated GIFs.
- `assets/pins.txt` lists the pins (key and Pinterest hash). `scripts/fetch_pins.py` downloads them on GitHub Actions.
- Content tables (Seerah, Quran words, ayah pool, Instagram ideas) and the control panel live in Google Drive.

Picture URL pattern: `https://raw.githubusercontent.com/hammaddsgn/first-light/main/assets/pins/{key}.jpg`
