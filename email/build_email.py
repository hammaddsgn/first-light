#!/usr/bin/env python3
"""First Light email builder (preview). Component kit mirrors what the scheduled task uses."""
import html, sys

INK="#17231D"; BODY="#43524A"; MUTED="#6B7A71"; LINE="#D8E0DA"; GREEN="#1F3D2F"
CORAL="#D9583B"; LINK="#B8432A"; CARD="#FBFCFA"; OUTER="#E9EEE9"; TINT="#FFF1E8"
SERIF="Georgia,'Times New Roman',serif"
AR="'Amiri','Scheherazade New','Traditional Arabic','Geeza Pro','Noto Naskh Arabic',serif"

RAW="https://raw.githubusercontent.com/hammaddsgn/first-light/main/assets/pins/"
GIF="https://raw.githubusercontent.com/hammaddsgn/first-light/main/assets/gif/"
BAND=""
TITLE="First Light"
def band(name,alt,h): return f'<tr><td style="padding:40px 0 0;font-size:0;line-height:0"><img src="{GIF}{name}.gif" width="620" height="{h}" alt="{alt}" style="display:block;width:100%;height:auto;border:0"></td></tr>'
ALIAS={"clouds66":"cbacfca311de95817bc618ac1afcaaea","clouds61":"60f54910db70fa6346438c2e5d8a376f","mist36":"e2dd4744aeda04723df16f4cc382ff8e","sky52":"885f7ca31b0d3ad3e3f2fae7d19f52d5","ducks17":"9a3fad2479527ae6b54c6f8c2c89f143","timing30":"65d3d5f43611445a8afcfdd0cdb25444","future33":"7b320d9ee0829ba51b26800381d2688b","godwins32":"95ef4c9b2af0850a7d4322f2ceb13c24","man38":"361307d5fb2f3164609156cc00760c31"}
def pin(x): return f"{RAW}{ALIAS.get(x,x)}.jpg"
class _P(dict):
    def __missing__(self,k): return pin(k)
PINS=_P()
e=html.escape

def p(t, size=16, color=BODY, mb=14):
    return f'<p style="margin:0 0 {mb}px;font:400 {size}px/1.65 {SERIF};color:{color}">{t}</p>'
def a(href,t): return f'<a href="{e(href)}" style="color:{LINK};text-decoration:underline">{t}</a>'
def h2(t, sub=None):
    r=f'<h2 style="margin:0 0 18px;font:400 26px/1.2 {SERIF};letter-spacing:-0.01em;color:{INK}">{t}</h2>'
    if sub: r+=f'<div style="margin:-10px 0 18px;font:italic 400 15px/1.4 {SERIF};color:{MUTED}">{sub}</div>'
    return r
def section(inner):
    return (f'<tr><td style="padding:0 40px"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">'
            f'<tr><td style="padding:44px 0 0;border-top:1px solid {LINE}"></td></tr>'
            f'<tr><td>{inner}</td></tr></table></td></tr>')
def crop(key, h, shift, alt, radius=14):
    return (f'<div style="height:{h}px;overflow:hidden;border-radius:{radius}px;background:#C9D6CD">'
            f'<img src="{PINS[key]}" width="540" alt="{e(alt)}" style="display:block;width:100%;height:auto;margin-top:-{shift}px;border:0"></div>')
def poster(key, alt, w=300, cap="From your notetoself board"):
    return (f'<div style="text-align:center"><img src="{PINS[key]}" width="{w}" alt="{e(alt)}" '
            f'style="display:inline-block;width:{w}px;max-width:100%;height:auto;border-radius:14px;border:0">'
            f'<div style="margin-top:10px;font:italic 400 13px/1.4 {SERIF};color:{MUTED}">{cap}</div></div>')
def poster_pair(k1,a1,k2,a2):
    cell=lambda k,al: (f'<td width="50%" valign="top" style="padding:0 6px;text-align:center"><img src="{PINS[k]}" width="260" alt="{e(al)}" '
                       f'style="width:100%;max-width:260px;height:auto;border-radius:14px;border:0;display:inline-block"></td>')
    return (f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>{cell(k1,a1)}{cell(k2,a2)}</tr></table>'
            f'<div style="margin-top:10px;text-align:center;font:italic 400 13px/1.4 {SERIF};color:{MUTED}">From your notetoself board</div>')
def note(t):
    return (f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>'
            f'<td style="background:{TINT};border-left:4px solid {CORAL};border-radius:0 14px 14px 0;padding:20px 22px">'
            f'<div style="font:italic 400 17px/1.6 {SERIF};color:{INK}">{t}</div></td></tr></table>')
def card(inner):
    return (f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin:0 0 14px"><tr>'
            f'<td style="border:1px solid {LINE};border-radius:14px;padding:20px 22px;background:#fff">{inner}</td></tr></table>')
def item(tag, title, href, blurb, src):
    return (f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin:0 0 22px"><tr><td>'
            f'<div style="font:400 13px/1.4 {SERIF};color:{MUTED};margin-bottom:4px">{tag}</div>'
            f'<div style="font:400 19px/1.35 {SERIF};color:{INK};margin-bottom:6px">{a(href,title)}</div>'
            f'<div style="font:400 15px/1.6 {SERIF};color:{BODY}">{blurb} <span style="color:{MUTED}">{src}</span></div></td></tr></table>')
def arabic(t, size=32):
    return (f'<div dir="rtl" lang="ar" style="font:400 {size}px/2 {AR};color:{GREEN};text-align:right;margin:0 0 14px">{t}</div>')

def page(subject, preheader, date_line, hero_inner, sections, footer_note):
    body="".join(sections)
    return f'''<!doctype html>
<html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="color-scheme" content="light only"><meta name="supported-color-schemes" content="light only">
<title>{e(subject)}</title>
<style>@media (max-width:640px){{.w{{width:100%!important}}.px{{padding-left:22px!important;padding-right:22px!important}}}}</style></head>
<body style="margin:0;padding:0;background:{OUTER}">
<div style="display:none;max-height:0;overflow:hidden;opacity:0;font-size:1px;line-height:1px;color:{OUTER}">{e(preheader)}&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:{OUTER}"><tr><td align="center" style="padding:28px 12px 40px">
<table role="presentation" class="w" width="620" cellpadding="0" cellspacing="0" border="0" style="width:620px;max-width:100%;background:{CARD};border-radius:20px">
<tr><td style="padding:40px 40px 0">
 <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>
  <td style="font:italic 400 34px/1 {SERIF};letter-spacing:-0.02em;color:{GREEN}">{TITLE}</td>
  <td align="right" style="font:400 14px/1.3 {SERIF};color:{MUTED}">{date_line}</td></tr></table>
</td></tr>
<tr><td style="padding:28px 40px 0">{hero_inner}</td></tr>
{body}
{BAND}<tr><td style="padding:48px 40px 40px"><div style="border-top:1px solid {LINE};padding-top:22px;font:400 13px/1.6 {SERIF};color:{MUTED}">{footer_note}</div></td></tr>
</table></td></tr></table></body></html>'''

# ---------------- WEEKDAY SAMPLE (Monday 12 October 2026) ----------------
def weekday():
    subject="Two UX roles you can apply to this week, and a prayer for interview nerves"
    pre="Capgemini's graduate scheme closes on 30 October. Moses' prayer for a calm start. Five things worth your time."
    hero=(crop("clouds66",230,110,"Soft golden clouds in an old oil painting")
          +f'<h1 style="margin:26px 0 12px;font:400 36px/1.12 {SERIF};letter-spacing:-0.025em;color:{INK}">Good morning, Hammad. Two junior UX roles are live.</h1>'
          +p("The Capgemini graduate programme closes on 30 October, and a junior designer role went up on Saturday. Both are below, with what they ask for, then the rest of your Monday.",17,BODY,0))
    S=[]
    S.append(section(h2("Before you start")+note("Both Capgemini roles ask for security clearance, which needs five years of continuous UK residence. Check that first, so you do not spend an evening on an application you cannot complete.")+'<div style="height:22px"></div>'+poster("timing30","Quote poster: I am not behind. I am on Allah's timing.")))
    S.append(section(h2("Today's ayah","Surah Ta-Ha, 20:25 to 20:28")
        +arabic("قَالَ رَبِّ ٱشْرَحْ لِى صَدْرِى وَيَسِّرْ لِىٓ أَمْرِى وَٱحْلُلْ عُقْدَةً مِّن لِّسَانِى يَفْقَهُوا۟ قَوْلِى",30)
        +p("Moses prayed, “My Lord! Uplift my heart for me, and make my task easy, and remove the impediment from my tongue so people may understand my speech,”",19,INK,8)
        +f'<div style="font:400 13px/1.5 {SERIF};color:{MUTED};margin-bottom:18px">Dr Mustafa Khattab, The Clear Quran. {a("https://quran.com/20:25","Read it on Quran.com")}</div>'
        +p("This is a prayer you can use before an interview or a call you have been putting off. It asks for an open heart, an easier task and clear speech, in that order.",16,BODY,0)))
    S.append(section(h2("Roles worth a look","Checked this morning")
        +card(f'<div style="font:400 19px/1.35 {SERIF};color:{INK}">{a("https://targetjobs.co.uk/jobs/graduate-ux-programme-2027-248355","Graduate UX Programme 2027")}</div>'
              +f'<div style="font:400 14px/1.5 {SERIF};color:{MUTED};margin:2px 0 10px">Capgemini UK, Hove, hybrid with up to three office days a week. Apply by 30 October, start 1 April 2027.</div>'
              +p("Joins a Scrum team on a large public sector service, with user research, interaction design and content design. It asks for a degree in a related field and SC clearance. Hove is a long way from Wolverhampton, so it would mean moving.",15,BODY,0))
        +card(f'<div style="font:400 19px/1.35 {SERIF};color:{INK}">{a("https://careers.capgemini.com/job/London-Junior-UX-Designer-%28SC-Cleared-SC-Eligible%29-Associate-Consultant-Digital-Excellence/1436342133/","Junior UX Designer (SC Cleared or SC Eligible)")}</div>'
              +f'<div style="font:400 14px/1.5 {SERIF};color:{MUTED};margin:2px 0 10px">Capgemini Invent, AI and Digital Factory. London, Manchester, Glasgow, Newcastle or Bristol, hybrid. Posted 10 October.</div>'
              +p("Covers user research, prototyping, accessibility and Agile delivery. It asks for at least a year in a UX or design-focused role, so it is a stretch. Worth applying if your freelance work counts toward that year.",15,BODY,0))
        +p("Indeed showed nothing new for junior or graduate UX in the last seven days. Fresh entry-level adverts are scarce at the moment, so two live ones in a morning is a good day.",15,MUTED,0)))
    S.append(section(h2("Worth reading and watching")
        +item("Article, Nielsen Norman Group","Context Libraries: How AI Power Users Manage Context Engineering","https://www.nngroup.com/articles/context-libraries/","People who use AI agents heavily spend more time maintaining the files that feed them than writing prompts, and often lose track of those files.","Published 9 October.")
        +item("Medium","My UX Portfolio Did Everything Right and Still Got Rejected.","https://medium.com/@MannDesigner/my-ux-portfolio-did-everything-right-and-still-got-rejected-61884c40c1ef","Nick Mann spoke to hiring managers and recruiters about why a clear process section does not settle the decision. Useful while your own portfolio is being rebuilt.","Published 11 October.")
        +item("Substack, Lenny's Newsletter","How OpenAI uses ChatGPT Sites, with Kath Korevec","https://www.lennysnewsletter.com/p/how-openai-uses-chatgpt-sites-live","A product lead at OpenAI shows how the company builds small internal tools that pull in Slack, Notion and calendar data.","Podcast episode, 5 October.")
        +item("Video, three minutes","Why Your Research Findings Aren't Landing","https://www.nngroup.com/videos/why-your-research-findings-arent-landing/","A short Nielsen Norman Group video on getting research findings noticed by the people who decide.","Published 5 October.")
        +item("Reflection, Muslim Matters","When a Place Teaches You What Softness Is Not","https://muslimmatters.org/2026/10/10/when-a-place-teaches-you-what-softness-is-not/","Dania Damrah writes about how a busy, pressured place can harden people, and about wanting a sincere community.","Published 10 October.")))
    S.append(section(h2("Seerah, day 8 of 60","The first revelation")
        +crop("sky52",170,60,"A pale, painted sky")+'<div style="height:18px"></div>'
        +p(f"Sahih al-Bukhari 3 gives this account through Aisha, the Prophet's ﷺ wife. He was in the cave of Hira when an angel came and told him to read. He answered that he could not read. This happened three times, with the angel pressing him each time, until the first verses of Surah al-Alaq were revealed ({a('https://quran.com/96:1','96:1')}).",16,BODY,12)
        +p(f"Shaken, he went back to Khadijah, who covered him and reassured him. She then took him to her cousin Waraqa ibn Nawfal, who recognised the angel as the one sent to Moses. Read it in full at {a('https://sunnah.com/bukhari:3','Sunnah.com, Bukhari 3')}.",16,BODY,12)
        +f'<div style="font:italic 400 14px/1.5 {SERIF};color:{MUTED}">Narration level: a hadith in Sahih al-Bukhari, narrated by Aisha. This is a summary in my own words, not a translation.</div>'))
    S.append(section(h2("Quran word of the week","ٱللَّه · Allāh · Allah")
        +arabic("قُلْ هُوَ ٱللَّهُ أَحَدٌ",30)
        +p(f"Allah is among the most frequent words in the Quran, with 2,699 occurrences in the Quranic Arabic Corpus. This week's ayah is {a('https://quran.com/112:1','Surah al-Ikhlas, 112:1')}. Open it on Quran.com for the Khattab English beside the Arabic. A new word arrives every Monday.",16,BODY,0)))
    S.append(section(h2("Three post ideas for LinkedIn")
        +p("<span style=\"color:#17231D\">What a junior UX advert asks for that a portfolio does not show.</span> Both Capgemini adverts mention Agile delivery and accessibility. Take one of your diploma projects and map it to those two words, using your own details.",16,BODY,12)
        +p("<span style=\"color:#17231D\">Your own context files.</span> Nielsen Norman Group's piece on context libraries could sit beside a short tour of how you set up Claude for design work, with a screenshot of one file.",16,BODY,12)
        +p("<span style=\"color:#17231D\">A time findings did not land.</span> Pick one real project where the research was sound and the team did nothing. Say what you changed in how you presented it.",16,BODY,0)))
    S.append(section(h2("Design skill of the day")
        +card(f'<div style="font:400 19px/1.35 {SERIF};color:{INK}">{a("https://github.com/pbakaus/impeccable","pbakaus/impeccable")}</div>'
              +f'<div style="font:400 14px/1.5 {SERIF};color:{MUTED};margin:2px 0 10px">About 79,800 stars on GitHub. Apache 2.0 licence. Updated 11 October.</div>'
              +p("A set of design instructions you add to an AI coding tool so it critiques and polishes interfaces with better judgement. It installs with a single npx command.",15,BODY,10)
              +f'<div style="font:400 13px/1.55 {SERIF};color:{MUTED}">Before you install anything, read its SKILL.md and scripts, check what it is allowed to run, and commit your work first.</div>')))
    S.append(section(h2("A UX word and one small thing")
        +p("<i>Progressive disclosure.</i> Showing people only what they need at each step and revealing more when they ask for it. A long form split into short steps is the common example.",16,BODY,14)
        +p("Today, open one screen from a portfolio project and write down every decision it asks the user to make. If there is more than one, try splitting it.",16,BODY,0)))
    S.append(section(crop("mist36",190,360,"Mist over still water at dawn")+'<div style="height:22px"></div>'
        +p("The Capgemini graduate deadline is 30 October. Everything else on this page can wait until the first application is in.",17,INK,0)))
    foot=("First Light daily briefing, sent at 07:48 on weekdays and weekends. This is a design preview with sample content. "
          "To add, remove or reorder sections, edit the First Light control panel in Google Drive, or tell Claude what to change.")
    global BAND
    BAND=band("waves","Soft green waves gently moving",40)
    return subject, pre, page(subject,pre,"Monday 12 October 2026",hero,S,foot)

# ---------------- WEEKEND PREVIEW (Sunday) ----------------
def weekend():
    subject="Sunday reset: the story of Abu Bakr steadying the community, and one word worth keeping"
    pre="Ease after hardship, a word for knowledge, and three Instagram ideas for the weekend."
    hero=(crop("ducks17",230,250,"Ducks resting by a dark pond, with a short quote about the company you keep")
          +f'<h1 style="margin:26px 0 12px;font:400 36px/1.12 {SERIF};letter-spacing:-0.025em;color:{INK}">Sunday, slowly. A story, a word and an ayah about ease.</h1>'
          +p("No job hunting today. This edition is about the Seerah, the Quran and a few ideas for your Instagram, with one design read at the end.",17,BODY,0))
    S=[]
    S.append(section(h2("Ayah of the day","Surah ash-Sharh, 94:6")
        +arabic("إِنَّ مَعَ ٱلْعُسْرِ يُسْرًا",34)
        +p("Surely with ˹that˺ hardship comes ˹more˺ ease.",20,INK,8)
        +f'<div style="font:400 13px/1.5 {SERIF};color:{MUTED};margin-bottom:18px">Dr Mustafa Khattab, The Clear Quran. {a("https://quran.com/94:6","Read it on Quran.com")}</div>'
        +poster_pair("future33","Quote poster: Do it for your future self.","godwins32","Quote poster: God wants me to win.")))
    S.append(section(h2("Seerah, day 60 of 60","Abu Bakr steadies the community")
        +p(f"Sahih al-Bukhari 3668 records what happened after the Prophet's ﷺ death, narrated by Aisha. Abu Bakr praised Allah and told the people that whoever worshipped Muhammad ﷺ should know he had died, and that whoever worshipped Allah should know Allah is alive and never dies.",16,BODY,12)
        +p(f"He then recited two ayat, {a('https://quran.com/39:30','Surah az-Zumar 39:30')} and {a('https://quran.com/3:144','Surah Al Imran 3:144')}, which remind the listeners that messengers come and go. Read the hadith at {a('https://sunnah.com/bukhari:3668','Sunnah.com, Bukhari 3668')}.",16,BODY,12)
        +f'<div style="font:italic 400 14px/1.5 {SERIF};color:{MUTED}">Narration level: a hadith in Sahih al-Bukhari, narrated by Aisha. This is a summary in my own words, not a translation.</div>'))
    S.append(section(h2("Quran word of the week","عِلْم · ʿilm · knowledge")
        +arabic("عَلَّمَ ٱلْإِنسَـٰنَ مَا لَمْ يَعْلَمْ",30)
        +p("taught humanity what they knew not.",19,INK,8)
        +f'<div style="font:400 13px/1.5 {SERIF};color:{MUTED};margin-bottom:14px">Surah al-Alaq, 96:5. Dr Mustafa Khattab, The Clear Quran. {a("https://quran.com/96:5","Read it on Quran.com")}</div>'
        +p("ʿIlm appears 105 times in the Quranic Arabic Corpus. It is the word at the end of the first revelation, which connects to this week's Seerah story.",16,BODY,0)))
    S.append(section(h2("Worth reading")
        +item("Reflection, Muslim Matters","Maryam: The Story of the Muslim ‘Virgin’ Mary","https://muslimmatters.org/2026/10/02/maryam-the-story-of-the-muslim-virgin-mary/","Janis Mahnure retells Maryam's story from the Quran, from her mother's vow to her life in the sanctuary, with reflections on trusting Allah.","Published 2 October.")
        +item("Podcast, Muslim Matters","Wait, Muslims Have Been Here HOW Long?!, with Hassam Munir","https://muslimmatters.org/2026/10/05/podcast-wait-muslims-have-been-how-long-hassam-munir/","Hassam Munir talks about Canadian Muslim history and how to organise a local Islamic History Month event. Canada is on your list of places to think about.","Published 5 October.")
        +item("Article, Nielsen Norman Group","Empathy Mapping: The First Step in Design Thinking","https://www.nngroup.com/articles/empathy-mapping/","A shared visual tool for capturing what a team knows about users and spotting where more research is needed.","Published 2 October.")))
    S.append(section(h2("Three Instagram ideas","For @thehammadakhtar")
        +p("<span style=\"color:#17231D\">Quran word of the week, a still.</span> ʿIlm in clean Arabic typography with its root, its count of 105 and 96:5 beneath it, with the translator named.",16,BODY,12)
        +p("<span style=\"color:#17231D\">Arabic type in interfaces, a carousel.</span> How Naskh and Uthmani script differ on screen, and what line height stops diacritics colliding.",16,BODY,12)
        +p("<span style=\"color:#17231D\">A job-search day built around salah, a reel.</span> Time-block applications, portfolio work and prayers, and leave in the parts that did not go to plan.",16,BODY,0)))
    S.append(section(h2("A UX word")
        +p("<i>Affordance.</i> A visual hint about how something can be used. A button that looks pressable is one, and a flat label that looks like a button is a false one.",16,BODY,0)))
    S.append(section(crop("mist36",190,360,"Mist over still water at dawn")+'<div style="height:22px"></div>'
        +p("Monday's email brings the jobs back.",17,INK,0)))
    foot=("First Light daily briefing, weekend edition. This is a design preview with sample content. "
          "To add, remove or reorder sections, edit the First Light control panel in Google Drive, or tell Claude what to change.")
    global BAND
    BAND=band("night","A crescent moon over a dark green night sky, with stars slowly twinkling",60)
    return subject, pre, page(subject,pre,"Sunday 11 October 2026",hero,S,foot)

if __name__=="__main__":
    out=sys.argv[1]
    for name,fn in (("weekday",weekday),("weekend",weekend)):
        s,pre,h=fn()
        open(f"{out}/{name}.html","w").write(h)
        open(f"{out}/{name}.subject.txt","w").write(s)
        print(name,len(h.encode()),"bytes", "em-dashes:",h.count("—"),h.count("–"))
