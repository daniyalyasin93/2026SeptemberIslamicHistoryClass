# -*- coding: utf-8 -*-
"""
Builds Lecture1.pptx — the WHOLE muqaddima in one ~43-min session.
Part A: how do we know? (method) · Part B: who saved it + the great books (trimmed).
All Urdu is in Urdu script (no Roman Urdu). Bilingual. 16:9.
Run:  python build_lecture1.py
References trace to the OCR'd Tareekh-e-Ummat muqaddima or established primary sources.
"""
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn

INK=RGBColor(0x1C,0x23,0x21); TEAL=RGBColor(0x10,0x4A,0x43); TEAL_D=RGBColor(0x0A,0x32,0x2E)
GOLD=RGBColor(0xC4,0x9A,0x45); CREAM=RGBColor(0xFA,0xF7,0xF0); CREAM_D=RGBColor(0xEF,0xE9,0xDB)
GREY=RGBColor(0x8C,0x8C,0x86); WHITE=RGBColor(0xFF,0xFF,0xFF); MAROON=RGBColor(0x7A,0x2E,0x2E)
AR="Traditional Arabic"; UR="Jameel Noori Nastaleeq"; EN="Georgia"; SANS="Segoe UI"

prs=Presentation(); prs.slide_width=Inches(13.333); prs.slide_height=Inches(7.5)
SW,SH=prs.slide_width,prs.slide_height; BLANK=prs.slide_layouts[6]

def slide(): return prs.slides.add_slide(BLANK)
def bg(s,c=CREAM):
    s.background.fill.solid(); s.background.fill.fore_color.rgb=c
def rect(s,x,y,w,h,fill=None,line=None,lw=1.0,shape=MSO_SHAPE.RECTANGLE):
    sp=s.shapes.add_shape(shape,x,y,w,h)
    if fill is None: sp.fill.background()
    else: sp.fill.solid(); sp.fill.fore_color.rgb=fill
    if line is None: sp.line.fill.background()
    else: sp.line.color.rgb=line; sp.line.width=Pt(lw)
    sp.shadow.inherit=False; return sp
def set_cs(run,name):
    rPr=run._r.get_or_add_rPr(); cs=rPr.find(qn('a:cs'))
    if cs is None: cs=rPr.makeelement(qn('a:cs'),{}); rPr.append(cs)
    cs.set('typeface',name)
def rtl(p): p._p.get_or_add_pPr().set('rtl','1')
def tb(s,x,y,w,h,anchor=MSO_ANCHOR.TOP):
    box=s.shapes.add_textbox(x,y,w,h); tf=box.text_frame
    tf.word_wrap=True; tf.vertical_anchor=anchor
    tf.margin_left=tf.margin_right=Pt(4); tf.margin_top=tf.margin_bottom=Pt(2)
    return box,tf
def para(tf,text,size=20,color=INK,bold=False,font=SANS,align=PP_ALIGN.LEFT,first=False,
         space_after=6,italic=False,arabic=False,cs=None):
    p=tf.paragraphs[0] if first and tf.paragraphs[0].text=="" else tf.add_paragraph()
    p.alignment=align; p.space_after=Pt(space_after)
    r=p.add_run(); r.text=text; f=r.font
    f.size=Pt(size); f.bold=bold; f.italic=italic; f.color.rgb=color; f.name=font
    set_cs(r, cs or UR)          # Urdu/Arabic glyphs → Jameel Noori Nastaleeq unless overridden
    if arabic: rtl(p)
    return p,r
def aside(tf, urdu, size=18):
    """The speaker's own voice — a casual Urdu-script line in gold (Nastaliq)."""
    para(tf, urdu, size=size, color=GOLD, italic=False, font=UR, arabic=True, space_after=6)
def kicker(s,text,color=GOLD):
    _,tf=tb(s,Inches(0.7),Inches(0.45),Inches(11.9),Inches(0.5))
    para(tf,text,size=14,color=color,bold=True,font=SANS,first=True,space_after=0)
def goldbar(s,x=0.7,y=0.86,w=1.6): rect(s,Inches(x),Inches(y),Inches(w),Pt(3),fill=GOLD)
def headline(s,text,y=0.98,size=33,color=TEAL_D):
    _,tf=tb(s,Inches(0.7),Inches(y),Inches(11.9),Inches(1.2))
    para(tf,text,size=size,color=color,bold=True,font=EN,first=True,space_after=0)
def notes(s,t):
    # Mixed Eng+Urdu garbles in an LTR paragraph. Fix: put the English citation on its own
    # line, and give every Urdu-bearing line an RTL base direction so it reads cleanly.
    t=t.replace("  "," ").replace(" Ref:", "\nRef:").replace(" EXTRA:", "\nEXTRA:")
    tf=s.notes_slide.notes_text_frame; tf.text=t
    for p in tf.paragraphs:
        txt="".join(r.text for r in p.runs)
        for r in p.runs: set_cs(r, UR)        # Urdu in notes → Nastaliq
        if any('؀'<=c<='ۿ' for c in txt):     # Urdu-bearing line → RTL base direction
            rtl(p)
def footer(s,n):
    _,tf=tb(s,Inches(11.2),Inches(7.0),Inches(1.9),Inches(0.4))
    para(tf,f"Lesson 1 · {n}",size=10,color=GREY,align=PP_ALIGN.RIGHT,first=True,space_after=0)
def section(title,sub_ar,urdu=None):
    s=slide(); bg(s,TEAL_D)
    rect(s,Inches(0.7),Inches(2.9),Inches(2.0),Pt(4),fill=GOLD)
    _,tf=tb(s,Inches(0.7),Inches(3.1),Inches(12),Inches(2.4))
    para(tf,title,size=42,color=WHITE,bold=True,font=EN,first=True,space_after=8)
    para(tf,sub_ar,size=24,color=GOLD,font=AR,arabic=True,space_after=6)
    if urdu: para(tf,urdu,size=18,color=CREAM,font=AR,arabic=True,space_after=0)
    return s
def card_row(s,items,y,h=2.3,accent=TEAL,title_size=19,desc_size=15):
    n=len(items); margin=0.7; gap=0.3; total=13.333-2*margin; w=(total-gap*(n-1))/n; x=margin
    for (name,sub,desc) in items:
        rect(s,Inches(x),Inches(y),Inches(w),Inches(h),fill=CREAM_D,line=accent,lw=1.0)
        rect(s,Inches(x),Inches(y),Inches(w),Pt(5),fill=GOLD)
        _,tf=tb(s,Inches(x+0.18),Inches(y+0.16),Inches(w-0.36),Inches(h-0.3))
        para(tf,name,size=title_size,bold=True,color=TEAL_D,first=True,space_after=2)
        if sub:
            _ar=any('؀'<=c<='ۿ' for c in sub)
            para(tf,sub,size=13,color=GOLD,bold=True,space_after=6,font=(UR if _ar else SANS),arabic=_ar)
        para(tf,desc,size=desc_size,color=INK,space_after=0)
        x+=w+gap

import os
from PIL import Image as _PILImg
def add_map(s, path, x, y, w, h):
    iw,ih=_PILImg.open(path).size
    bw,bh=Inches(w),Inches(h); sc=min(bw/iw,bh/ih)
    pw,ph=int(iw*sc),int(ih*sc)
    s.shapes.add_picture(path,int(Inches(x)+(bw-pw)/2),int(Inches(y)+(bh-ph)/2),width=pw,height=ph)
MAP_IMG=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','maps','world_632_kandg.png')

# ===== 1 TITLE
s=slide(); bg(s,TEAL_D)
rect(s,0,Inches(3.05),SW,Inches(1.4),fill=TEAL); rect(s,Inches(0.7),Inches(2.78),Inches(2.2),Pt(4),fill=GOLD)
_,tf=tb(s,Inches(0.7),Inches(1.5),Inches(12),Inches(1.2))
para(tf,"LESSONS FROM HISTORY · LESSON 1",size=18,color=GOLD,bold=True,font=SANS,first=True,space_after=2)
para(tf,"تاریخ سے سبق",size=20,color=CREAM,font=AR,arabic=True,space_after=0)
_,tf=tb(s,Inches(0.7),Inches(3.15),Inches(12),Inches(1.25),anchor=MSO_ANCHOR.MIDDLE)
para(tf,"How do we even know what really happened?",size=40,color=WHITE,bold=True,font=EN,first=True,space_after=0)
_,tf=tb(s,Inches(0.7),Inches(4.7),Inches(12),Inches(1))
para(tf,"ہمیں کیسے پتا کہ اصل میں ہوا کیا تھا؟",size=26,color=CREAM,font=AR,arabic=True,first=True,space_after=4)
para(tf,"The whole muqaddima, in one sitting",size=16,color=GOLD,font=SANS,space_after=0)
notes(s,"سلام۔ گرم جوشی سے شروع کریں۔ تعریف سے شروع *مت* کریں۔ کہیں: ”آج صرف ایک تعارف ہے — لیکن وعدہ ہے، "
        "میں بور نہیں کروں گا۔ تعریف کے بجائے ایک کہانی سے شروع کرتے ہیں۔ چلیں بغداد — آج سے ہزار سال پیچھے۔“ "
        "پھر cold open پر جائیں۔")
footer(s,"Title")

# ===== 2 FORGED DOC setup
s=slide(); bg(s); kicker(s,"Baghdad · about a thousand years ago")
goldbar(s); headline(s,"An old document shows up in court",size=31)
_,tf=tb(s,Inches(0.7),Inches(2.15),Inches(11.9),Inches(4.3))
para(tf,"The Jews of Baghdad bring an old, worn-out paper to the authorities.",size=24,first=True,space_after=12)
para(tf,"The claim: after Khaybar, the Prophet ﷺ freed them from jizya — for good.",size=24,space_after=12)
para(tf,"The signatures on it:  ʿAlī · Saʿd ibn Muʿādh · Muʿāwiyah",size=24,bold=True,color=TEAL,space_after=12)
aside(tf,"کاغذ واقعی پرانا لگتا ہے۔ سب ماننے کو تیار ہیں…",size=22)
notes(s,"آرام سے، تھیٹر کی طرح سنائیں — یہ آپ کا سب سے مضبوط آغاز ہے، جلدی مت کریں۔\n"
        "«آج سے تقریباً ہزار سال پہلے، بغداد۔ شہر کے یہود کا ایک وفد دربار میں آتا ہے۔ اُن کے ہاتھ میں ایک بہت "
        "پرانا، گھسا پٹا کاغذ ہے۔ دعویٰ یہ ہے کہ فتحِ خیبر کے بعد رسول اللہ ﷺ نے انہیں ہمیشہ کے لیے جزیہ سے معاف "
        "کر دیا تھا۔ اور اِس دستاویز پر دستخط کس کے ہیں؟ سیدنا علی، سیدنا سعد بن معاذ، اور سیدنا معاویہ ؓ۔ کاغذ "
        "دیکھنے میں واقعی صدیوں پرانا لگتا ہے۔ مسلمان تقریباً مان ہی لینے والے ہیں کہ چلو جزیہ معاف کر دیتے ہیں…»\n"
        "— یہاں رکیں، آواز دھیمی کریں —\n"
        "«لیکن آخری فیصلے سے پہلے یہ کاغذ ایک عالم کو دکھایا جاتا ہے — امام الخطیب البغدادی۔» (پھر اگلی slide)\n"
        "اگر اٹک جائیں: بس اتنا یاد رکھیں — پرانی دستاویز، تین صحابہؓ کے دستخط، سب ماننے کو تیار، پھر ایک عالم کو دکھائی گئی۔\n"
        "Ref: muqaddima p.57-58 (al-Muntazam, Ibn al-Jawzi).")
footer(s,"The story")

# ===== 3 REVEAL
s=slide(); bg(s,TEAL_D); kicker(s,"One look was enough")
_,tf=tb(s,Inches(0.7),Inches(1.0),Inches(11.9),Inches(1.0))
para(tf,"Imam al-Khatib: “This is a fake.”",size=34,color=WHITE,bold=True,font=EN,first=True,space_after=0)
rect(s,Inches(0.7),Inches(2.45),Inches(5.7),Inches(3.2),fill=TEAL,line=GOLD,lw=1.5)
rect(s,Inches(6.9),Inches(2.45),Inches(5.7),Inches(3.2),fill=TEAL,line=GOLD,lw=1.5)
_,tf=tb(s,Inches(1.0),Inches(2.7),Inches(5.1),Inches(2.7))
para(tf,"PROBLEM 1",size=15,color=GOLD,bold=True,first=True,space_after=8)
para(tf,"Muʿāwiyah became Muslim AFTER Khaybar.",size=22,color=CREAM,space_after=6)
para(tf,"So how did he sign a Khaybar deal?",size=20,color=WHITE,italic=True,space_after=0)
_,tf=tb(s,Inches(7.2),Inches(2.7),Inches(5.1),Inches(2.7))
para(tf,"PROBLEM 2",size=15,color=GOLD,bold=True,first=True,space_after=8)
para(tf,"Saʿd ibn Muʿādh had died years before, at Khandaq.",size=22,color=CREAM,space_after=6)
para(tf,"A dead man, signing?",size=20,color=WHITE,italic=True,space_after=0)
_,tf=tb(s,Inches(0.7),Inches(5.9),Inches(11.9),Inches(1.0))
para(tf,"The dates gave the whole thing away.",size=23,color=GOLD,bold=True,first=True,space_after=0)
notes(s,"دونوں نکتے مزے لے کر، ایک ایک کر کے بولیں:\n"
        "«ایک ہی نظر۔ امام الخطیب فرماتے ہیں: یہ جعلی ہے۔ کیسے؟ دو باتیں۔»\n"
        "«پہلی بات: سیدنا معاویہ ؓ تو خیبر کے بعد مسلمان ہوئے — وہ خیبر کے معاہدے پر دستخط کر ہی نہیں سکتے تھے۔»\n"
        "«دوسری بات: سیدنا سعد بن معاذ ؓ تو اِس سے برسوں پہلے غزوۂ خندق میں شہید ہو چکے تھے — ایک فوت شدہ شخص بھلا دستخط کیسے کرے گا؟»\n"
        "«ایک غیر مسلم اور ایک فوت شدہ، دونوں کے دستخط ایک ہی معاہدے پر — تاریخوں نے جھوٹ کھول دیا۔»\n"
        "پھر سامعین سے پوچھیں: «سوچیے، ایک نظر میں کیسے پکڑ لیا؟ کیونکہ اُن کے پاس تاریخ تھی۔»\n"
        "پُل (آج کے موضوع کی طرف): «یہی آج کا موضوع ہے — وہ علم جس سے ہم سچ اور جھوٹ الگ کرتے ہیں۔»\n"
        "اگر اٹک جائیں: دو نکتے کافی ہیں — معاویہؓ بعد میں مسلمان ہوئے؛ سعد بن معاذؓ پہلے شہید ہو چکے تھے۔")
footer(s,"The catch")

# ===== 4 THESIS
s=slide(); bg(s,GOLD)
_,tf=tb(s,Inches(1.2),Inches(2.4),Inches(10.9),Inches(2.7),anchor=MSO_ANCHOR.MIDDLE)
para(tf,"History isn't just the nice stories we like.",size=34,color=TEAL_D,bold=True,font=EN,first=True,space_after=16,align=PP_ALIGN.CENTER)
para(tf,"There's a way to check it. So — who has that 'way'?",size=30,color=INK,font=EN,align=PP_ALIGN.CENTER,space_after=0)
notes(s,"اِس slide کو ٹھہرنے دیں۔ تین سیکنڈ رک کر آگے جائیں۔ یہی پوری lecture کا نقطہ ہے۔")
footer(s,"The point")

# ===== 4b WHAT IS HISTORY (light)
s=slide(); bg(s); kicker(s,"Quick — what even counts as 'history'?")
goldbar(s); headline(s,"It comes down to time-order",size=30)
card_row(s,[
 ("In a poem","شاعری","told to move you, to give a lesson"),
 ("In a hadith book","حدیث","sorted by chains and rulings"),
 ("In a tārīkh","تاریخ","sorted by TIME — first things first"),
], y=2.7, h=2.5, title_size=20, desc_size=17)
_,tf=tb(s,Inches(0.7),Inches(5.5),Inches(11.9),Inches(0.9))
para(tf,"Same event, three books. Only the tārīkh puts it in time-order.",size=20,italic=True,color=TEAL,first=True,space_after=2)
para(tf,"یہی ترتیبِ زمانی تاریخ کو تاریخ بناتی ہے۔",size=19,color=TEAL,font=AR,arabic=True,space_after=0)
notes(s,"LIGHT slide ~1.5 min — مگر یہاں تفصیل موجود ہے اگر کھولنا ہو۔ ابنِ خلدون کی تعریف: ”گزری ہوئی قوموں، "
        "حکومتوں اور لوگوں کی خبر۔“ علامہ سخاوی: موضوع = الإنسان والزمان — تاریخ کا اصل موضوع انسان اور زمانہ ہے: "
        "کس دور میں انسان کو کیا پیش آیا۔ ایک اور بات: تاریخ عام طور پر صرف *غیر معمولی* لوگ (بادشاہ، وزراء، علماء، "
        "فاتحین) کا ذکر کرتی ہے؛ اِسی لیے کہتے ہیں تاریخ ”مشاہیر کے احوال کا علم“ ہے۔ Ref: muqaddima p.32-33.")
footer(s,"What is history")

# ===== 5 TWO WAYS (single compare)
s=slide(); bg(s); kicker(s,"Two ways to know the past · ماضی جاننے کے دو طریقے")
goldbar(s); headline(s,"Two ways to know the past",size=30)
rect(s,Inches(0.7),Inches(2.0),Inches(5.9),Inches(4.5),fill=CREAM_D,line=MAROON,lw=1.5)
rect(s,Inches(6.75),Inches(2.0),Inches(5.85),Inches(4.5),fill=CREAM_D,line=TEAL,lw=1.5)
_,tf=tb(s,Inches(1.0),Inches(2.2),Inches(5.3),Inches(4.1))
para(tf,"THE MODERN / WESTERN WAY",size=15,color=MAROON,bold=True,first=True,space_after=10)
for t in ["Mostly digging, guessing, joining the dots.","No chain of who-said-what.",
          "No fixed rule to accept or drop a report.","Yet they still trust the Old Testament and Ramayana as top sources."]:
    para(tf,"•  "+t,size=18,space_after=9)
_,tf=tb(s,Inches(7.05),Inches(2.2),Inches(5.3),Inches(4.1))
para(tf,"THE ISLAMIC WAY",size=15,color=TEAL,bold=True,first=True,space_after=10)
for t in ["Every report carries a chain — back to the eyewitness.",
          "We keep a file on every narrator (ʿilm asmā' al-rijāl).","So we can actually grade a report.",
          "We'll drop even Wāqidī, a judge of Baghdad, if the rule says so."]:
    para(tf,"•  "+t,size=18,space_after=9)
_,tf=tb(s,Inches(0.7),Inches(6.65),Inches(11.9),Inches(0.7))
para(tf,"So “no historical basis” often just means: “it doesn't fit our guess.”",size=19,bold=True,color=TEAL_D,first=True,space_after=0)
notes(s,"انصاف سے بولیں، مذاق نہیں۔ ”یہ لوگ محنتی ہیں — لیکن اِن کے پاس سند کا نظام نہیں۔“ پھر ہمارا طریقہ: "
        "”ہم پوچھتے ہیں — یہ کس نے کہا؟ وہ کون تھا؟ وہاں موجود بھی تھا؟“ اصل فرق: ہم نے روایت پر *درایت* (عقل سے "
        "پرکھنا) بھی شامل کی۔ Ref: muqaddima p.43-44, 48-49.")
footer(s,"Two ways")

# ===== 6 QUOTE bridge
s=slide(); bg(s,TEAL)
rect(s,Inches(0.7),Inches(1.7),Pt(5),Inches(4.1),fill=GOLD)
_,tf=tb(s,Inches(1.3),Inches(1.9),Inches(11.2),Inches(3.7),anchor=MSO_ANCHOR.MIDDLE)
para(tf,"لَمَّا اسْتَعْمَلَ الرُّوَاةُ الْكَذِبَ اسْتَعْمَلْنَاهُمُ التَّارِيخَ",size=32,color=WHITE,bold=True,font=AR,arabic=True,cs=AR,first=True,space_after=16)
para(tf,"“When people started forging reports, we caught them with dates.”",size=25,color=CREAM,italic=True,font=EN,space_after=8)
para(tf,"— Sufyān al-Thawrī",size=19,color=GOLD,bold=True,space_after=14)
para(tf,"اگر تاریخیں اتنی اہم ہیں… تو ہم خود وقت میں کہاں کھڑے ہیں؟",size=20,color=WHITE,font=AR,arabic=True,space_after=0)
notes(s,"یہ quote timeline کا پُل ہے۔ بولیں: ”تاریخ — یعنی وقت کا علم — وہ ہتھیار ہے جس سے جھوٹ پکڑا جاتا ہے۔ "
        "اور اگر وقت اتنا اہم ہے، تو سوال یہ ہے — ہم خود کہاں کھڑے ہیں؟“ Ref: muqaddima p.57.")
footer(s,"Bridge")

# ===== timeline helper
def draw_timeline(s,pegs,title,highlight=None):
    kicker(s,"The timeline we build every week · ہماری ٹائم لائن")
    goldbar(s); headline(s,title,size=28)
    axis_y=Inches(4.2); x0,x1=Inches(0.9),Inches(12.4)
    rect(s,x0,axis_y,x1-x0,Pt(3),fill=TEAL)
    n=len(pegs); span=(x1-x0)
    for i,(top,bot,grey) in enumerate(pegs):
        cx=x0+int(span*(i/(n-1))) if n>1 else (x0+x1)//2
        col=GREY if grey else (GOLD if highlight==i else TEAL_D)
        d=Inches(0.16); rect(s,cx-d//2,axis_y-d//2+Emu(int(Pt(1.5))),d,d,fill=col,shape=MSO_SHAPE.OVAL)
        above=(i%2==0); ty=Inches(2.7) if above else Inches(4.7)
        _,tf=tb(s,cx-Inches(1.1),ty,Inches(2.2),Inches(1.4),anchor=MSO_ANCHOR.BOTTOM if above else MSO_ANCHOR.TOP)
        para(tf,top,size=15,bold=True,color=col,align=PP_ALIGN.CENTER,first=True,space_after=2)
        if bot: para(tf,bot,size=12,color=GREY if grey else INK,align=PP_ALIGN.CENTER,space_after=0)

PEGS_P=[("Ādam → ʿĪsā ﷺ","prophets\n(not our topic)",True),("The Prophet ﷺ","Hijra = 1 AH\n622 CE",False),("…","",True)]
PEGS_F=[("Ādam → ʿĪsā ﷺ","(not our topic)",True),("Prophet ﷺ","1 AH · 622",False),("Rāshidūn","11–40 AH",False),
        ("Umayyads","41–132 AH",False),("Abbasids","132–656 AH",False),("Mongols take\nBaghdad","656 · 1258",False),
        ("Ottomans","→ 1924",False),("Today","1447 · 2026",False)]

# ===== 7 timeline partial
s=slide(); bg(s); draw_timeline(s,PEGS_P,"First, just two points",highlight=1)
_,tf=tb(s,Inches(0.7),Inches(6.05),Inches(11.9),Inches(0.9))
para(tf,"سب کچھ یہیں سے شروع — ہجرت سے — اور آگے چلتا ہے۔",size=20,color=TEAL,font=AR,arabic=True,first=True,space_after=0)
notes(s,"صرف دو peg لگائیں: لمبا دھندلا ”پہلے“ (مت سمجھائیں)، اور ہجرت ہمارا صفر۔ پوچھیں: ”اندازہ لگائیے — "
        "ہجرت کو کتنے سال ہو گئے؟“ اندازہ کروائیں، پھر اگلی slide. (جواب: تقریباً ۱۴۴۷)")
footer(s,"Timeline")

# ===== 8 timeline full
s=slide(); bg(s); draw_timeline(s,PEGS_F,"And here's the whole journey — our 10 weeks")
notes(s,"اب پوری لکیر دکھائیں، ہاتھ سے trace کریں۔ ”ہم اِس پوری لکیر پر چلیں گے — ابوبکرؓ سے آج تک۔“ "
        "یہ نکتہ اٹھائیں کہ ہم کتنے *حالیہ* ہیں — یہ سب صرف پچھلے ۱۴۰۰ سال، انسانی تاریخ کا ایک پتلا سا ٹکڑا۔")
footer(s,"Timeline")

# ===== 9 calendar
s=slide(); bg(s); kicker(s,"Why do we even count from the Hijra?")
goldbar(s); headline(s,"A letter dated just “Shaʿbān”",size=30)
_,tf=tb(s,Inches(0.7),Inches(2.1),Inches(11.9),Inches(4.4))
para(tf,"A letter reaches ʿUmar ؓ, dated only “Shaʿbān.” He asks: which year's Shaʿbān?",size=23,first=True,space_after=12)
para(tf,"The state has grown huge. Papers everywhere. Nobody can tell which file is from which year.",size=23,space_after=12)
para(tf,"They sit together: count from the Prophet's ﷺ birth? his passing? the Hijra?",size=23,space_after=12)
para(tf,"ʿUmar ؓ picks the HIJRA — “it's the thing that separated truth from falsehood.”",size=23,bold=True,color=TEAL,space_after=10)
aside(tf,"اور اِسی طرح ہمارا کیلنڈر — اور اِس لکیر کا صفر — بنا۔",size=21)
notes(s,"پیاری، انسانی کہانی — گرم جوشی سے، تفصیل سے سنائیں:\n"
        "«سیدنا عمر ؓ کے دور میں سلطنت بہت پھیل چکی تھی، سرکاری خطوں اور دستاویزات کا انبار لگ گیا۔ ایک دن آپؓ کے "
        "پاس ایک خط آیا جس پر صرف ’شعبان‘ لکھا تھا۔ آپؓ نے پوچھا: یہ کس سال کا شعبان ہے؟ کسی کو پتا نہ چلے کہ کون "
        "سی تحریر کس سال کی ہے۔»\n"
        "«صحابہؓ نے مشورہ کیا۔ کسی نے کہا رومیوں کا کیلنڈر لے لیں — عمرؓ نے فرمایا وہ بہت طویل ہے۔ کسی نے کہا فارس "
        "کا — فرمایا اُن کے ہاں ہر بادشاہ پر گنتی نئے سرے سے شروع ہوتی ہے۔ آخر طے ہوا کہ اپنی الگ تقویم ہو۔»\n"
        "«اب سوال: کہاں سے گنیں؟ تین تجاویز آئیں — نبی ﷺ کی ولادت سے، ہجرت سے، یا وفات سے۔ عمرؓ نے ہجرت چنی — "
        "’کیونکہ اِسی نے حق اور باطل میں فرق کیا۔‘»\n"
        "«اور اِسی طرح ہمارا ہجری کیلنڈر بنا — اور اِسی لیے ہماری ٹائم لائن کا صفر ہجرت ہے۔»\n"
        "EXTRA: مہینے کا آغاز محرم سے رکھنے کا مشورہ حضرت عثمانؓ کا تھا؛ سیوطیؒ کے مطابق خود نبی ﷺ نے ایک تحریر پر ’سن ۵‘ لکھوایا تھا۔\n"
        "Ref: muqaddima p.36-37.")
footer(s,"Calendar")

# ===== 9b NASI (light slide, rich notes)
s=slide(); bg(s); kicker(s,"A twist: the calendar someone had tampered with")
goldbar(s); headline(s,"النسیء — shifting the months",size=29)
_,tf=tb(s,Inches(0.7),Inches(2.1),Inches(11.9),Inches(4.5))
para(tf,"Before Islam, the mushrikūn used to shuffle the months — to keep Hajj sitting in the same trading season.",
     size=23,first=True,space_after=13)
para(tf,"They'd slip in an extra 13th month when it suited them, so the four “sacred months” drifted off their real place.",
     size=23,space_after=13)
para(tf,"At the Farewell Hajj the Prophet ﷺ ended it for good: “Time has come back round to how Allah made it the day He created the heavens and the earth.”",
     size=22,bold=True,color=TEAL,space_after=10)
aside(tf,"اِسی لیے سیرت کی کچھ تاریخوں میں فرق ہے — یہ اُس کی ایک بڑی وجہ ہے۔",size=20)
notes(s,"یہ slide ہلکی رکھ سکتے ہیں، لیکن نیچے پوری کہانی موجود ہے اگر کھولنا ہو:\n"
        "«اسلام سے پہلے ایک دلچسپ گڑبڑ تھی۔ قمری سال شمسی سال سے تقریباً ۱۱ دن چھوٹا ہوتا ہے، اِس لیے قمری مہینے "
        "تقریباً ۳۳ سال میں سارے موسموں سے گزر جاتے ہیں — کبھی حج گرمی میں، کبھی سردی میں۔»\n"
        "«مشرکین چاہتے تھے کہ حج ہمیشہ گرمی اور تجارت کے موسم میں رہے، کیونکہ تب کھجوریں اور مویشی بکتے تھے۔ تو بنو "
        "کنانہ کا ایک سردار ہر حج پر اعلان کرتا کہ اگلا سال ۱۲ مہینے کا ہوگا یا ۱۳ — یعنی جب چاہتے ایک تیرہواں مہینہ بڑھا دیتے۔»\n"
        "«اِس ہیر پھیر سے چار ’اشہرِ حرم‘ اپنی اصل جگہ سے ہٹ گئے۔ قرآن نے اِسے ’النسیء‘ کہا — ’زیادۃ فی الکفر‘ (التوبہ ۹:۳۷)۔»\n"
        "«حجۃ الوداع پر نبی ﷺ نے فرمایا: ’ان الزمان قد استدار…‘ — زمانہ گھوم کر پھر اُسی حالت پر آ گیا جیسا اللہ نے "
        "بنایا تھا — اور یہ گڑبڑ ہمیشہ کے لیے ختم کر دی۔»\n"
        "اگر اٹک جائیں: مشرکین مہینے آگے پیچھے کرتے تھے تاکہ حج تجارت کے موسم میں رہے؛ نبی ﷺ نے حجۃ الوداع پر بند کر دیا۔ "
        "یہی سیرت کی کچھ تاریخوں میں فرق کی ایک وجہ ہے۔\n"
        "Ref: muqaddima p.38-40; al-Tawba 9:37; Bukhari (farewell-hajj hadith).")
footer(s,"Nasī'")

# ===== 10 MAP
s=slide(); bg(s); kicker(s,"First, a bit of geography")
goldbar(s)
if os.path.exists(MAP_IMG):
    add_map(s, MAP_IMG, 0.7, 1.5, 8.4, 5.0)
    _,tf=tb(s,Inches(0.7),Inches(6.55),Inches(8.4),Inches(0.4))
    para(tf,"Map: Kings & Generals — “Early Muslim Expansion” (video frame)",size=11,color=GREY,first=True,space_after=0)
else:
    rect(s,Inches(0.7),Inches(1.5),Inches(8.4),Inches(5.4),fill=CREAM_D,line=TEAL,lw=1.5)
    _,tf=tb(s,Inches(1.0),Inches(3.7),Inches(7.8),Inches(1.2),anchor=MSO_ANCHOR.MIDDLE)
    para(tf,"◣  MAP GOES HERE  ◢",size=20,color=GREY,bold=True,align=PP_ALIGN.CENTER,first=True,space_after=6)
    para(tf,"World ~11 AH / 632 CE — Byzantine Rome, Sasanian Persia, and the Hijaz in between.",size=15,color=GREY,align=PP_ALIGN.CENTER,space_after=0)
_,tf=tb(s,Inches(9.4),Inches(1.7),Inches(3.4),Inches(5.0))
para(tf,"POINT AT:",size=15,color=GOLD,bold=True,first=True,space_after=10)
for t in ["Makkah & Madina","Rome (Byzantium): Sham, Egypt","Persia (Sasanians): Iraq, Iran",
          "The road the conquests take:","Hijaz → Sham → Iraq → Egypt → Persia"]:
    para(tf,"•  "+t,size=17,color=INK,space_after=10)
notes(s,"نقشہ embed ہو چکا ہے (Kings & Generals frame)۔ یہاں تھوڑا وقت دیں — جغرافیہ ٹھیک کریں: روم/بازنطین "
        "شمال مغرب، فارس/ساسانی مشرق، عرب قبائل بیچ میں۔ Point کریں کربلا، دمشق، کوفہ، قرطبہ آگے کہاں ہوں گے۔ "
        "پورا term فائدہ دے گا۔")
footer(s,"Map")

# ===== 11 WHY + RULES
s=slide(); bg(s); kicker(s,"Why read history at all? Not for fun — for ʿibrah")
goldbar(s)
_,tf=tb(s,Inches(0.7),Inches(1.5),Inches(11.9),Inches(1.4))
para(tf,"لَقَدْ كَانَ فِي قَصَصِهِمْ عِبْرَةٌ لِأُولِي الْأَلْبَابِ",size=29,color=TEAL,bold=True,font=AR,arabic=True,cs=AR,first=True,space_after=6)
para(tf,"“In their stories is a lesson for people who think.”  (Yūsuf 12:111)",size=18,italic=True,color=INK,space_after=0)
rect(s,Inches(0.7),Inches(3.1),Inches(11.93),Inches(3.5),fill=CREAM_D,line=GOLD,lw=1.5)
_,tf=tb(s,Inches(1.0),Inches(3.35),Inches(11.3),Inches(3.1))
para(tf,"OUR RULES FOR THIS COURSE",size=16,color=MAROON,bold=True,first=True,space_after=10)
para(tf,"• ہر بات کا کوئی ماخذ ہو۔ ”میں نے سنا تھا“ نہیں چلے گا — ہم سند کی پیروی کریں گے۔",size=19,color=INK,font=AR,arabic=True,space_after=11)
para(tf,"• صحابہؓ کے بارے میں حُسنِ ظن۔ بلا ضرورت، یا عقیدے کو نقصان پہنچانے والے انداز میں اُن کے اختلافات (مشاجرات) پڑھنا ہماری فقہ میں مکروہ ہے۔",size=19,color=INK,font=AR,arabic=True,space_after=11)
para(tf,"• جب ہم اُن واقعات تک پہنچیں گے (سبق ۵ اور ۷)، پورے ادب کے ساتھ۔",size=19,color=INK,font=AR,arabic=True,space_after=0)
notes(s,"یہ slide management کے لیے اہم ہے۔ Guardrail *ابھی*، آرام سے بولیں — کسی حساس چیز سے پہلے۔ EXTRA: فقہاء "
        "نے تاریخ کے *پڑھنے* کا حکم بھی بیان کیا — کچھ فرضِ عین (اتنی سیرت کہ اپنے نبی ﷺ کو پہچانیں)، کچھ فرضِ کفایہ، "
        "نیچے مکروہ (فضول قصے) اور حرام (بے حیائی کی حکایات)۔ Ref: muqaddima p.52-53; Yusuf 12:111.")
footer(s,"Why + rules")

# ===== 11b MUSLIMS NOT THE RELIGION
s=slide(); bg(s); kicker(s,"One thing to be clear about from day one")
goldbar(s); headline(s,"This is the history of the Muslims",size=29)
_,tf=tb(s,Inches(0.7),Inches(2.1),Inches(11.9),Inches(4.4))
para(tf,"“Tārīkh al-Islām” really means Tārīkh al-Muslimīn — the history of the MUSLIMS, not of the religion itself.",
     size=24,bold=True,color=TEAL,first=True,space_after=14)
para(tf,"The religion is perfect. The Muslims are people — there are highs and lows, just caliphs and also unjust kings, closeness to the dīn and sometimes distance from it.",
     size=22,space_after=12)
aside(tf,"تو جب کوئی برا واقعہ آئے — اُسے اسلام کے کھاتے میں مت ڈالو۔ یہ انسانوں کی کہانی ہے، دین کی نہیں۔",size=20)
notes(s,"اہم framing — یہ سیدھا مشاجرات کے لیے بنیاد ہے (management کا concern بھی)۔ بولیں: ”سیرت اور صحابہؓ کا "
        "دور تو دین کی بھی تاریخ ہے۔ لیکن بعد کے بادشاہوں کی آپس کی جنگیں، خاندانی جھگڑے — یہ *مسلمانوں* کی تاریخ ہے، "
        "اسلام کی نہیں۔ طبری، البدایہ، الکامل — اِنہیں قوم کی تاریخ کی طرح پڑھیں، مذہب کی تاریخ کی طرح نہیں۔“ Ref: muqaddima p.61.")
footer(s,"Muslims, not the dīn")

# ===== 12 SECTION B
section("So who saved all this?","یہ سب بچایا کس نے؟","چودہ سو سال بعد بھی ہمیں پتا ہے — کیسے؟")
notes(prs.slides[-1],"Part B شروع۔ Energy بدلیں — اب heroes سے مل رہے ہیں۔ ”یہ سب سینوں میں یا کاغذ پر کیسے بچ گیا؟ "
                     "کچھ لوگوں نے اپنی زندگیاں لگا دیں۔“")
footer(prs.slides[-1],"Part B")

# ===== 13 PILLARS
s=slide(); bg(s); kicker(s,"It all stands on two things — both from hadith")
goldbar(s); headline(s,"Two pillars",size=30)
card_row(s,[
 ("Seerah-nigārī","سیرت و مغازی","Writing the Prophet's ﷺ life in proper time-order. This is the root of all our history-writing."),
 ("Fann al-Rijāl","علم اسماء الرجال","A full file on every narrator. Built to protect hadith and history — so any liar gets caught."),
], y=2.6, h=2.9, title_size=23, desc_size=19)
notes(s,"آرام سے: ”دو بنیادیں۔ ایک — سیرت نگاری۔ دوسری — فنِ رجال، یعنی ہر راوی کا پورا حساب۔“ Ref: muqaddima p.43-44.")
footer(s,"Pillars")

# ===== 13b FOUR STAGES (light)
s=slide(); bg(s); kicker(s,"How any science gets built — in four steps")
goldbar(s); headline(s,"Building the house",size=30)
stages=[("1 · TĀSĪS","تاسیس","lay the foundation",GREY),
        ("2 · TADWĪN","تدوین","raise the walls (gather)",TEAL),
        ("3 · TANQĪH","تنقیح","plaster & clean (sift)",TEAL_D),
        ("4 · TAKMĪL","تکمیل","paint & furnish (perfect)",GOLD)]
_m=0.7; _g=0.25; _n=4; _t=13.333-2*_m; _w=(_t-_g*(_n-1))/_n; _x=_m
for (t,ar,d,col) in stages:
    rect(s,Inches(_x),Inches(2.5),Inches(_w),Inches(2.9),fill=CREAM_D,line=col,lw=1.5)
    rect(s,Inches(_x),Inches(2.5),Inches(_w),Inches(0.55),fill=col)
    _,tf=tb(s,Inches(_x+0.15),Inches(2.56),Inches(_w-0.3),Inches(0.5))
    para(tf,t,size=15,bold=True,color=WHITE,first=True,space_after=0)
    _,tf=tb(s,Inches(_x+0.15),Inches(3.2),Inches(_w-0.3),Inches(2.1))
    para(tf,ar,size=22,bold=True,color=col,font=AR,arabic=True,first=True,space_after=8)
    para(tf,d,size=15,color=INK,space_after=0)
    _x+=_w+_g
_,tf=tb(s,Inches(0.7),Inches(5.7),Inches(11.9),Inches(1.0))
para(tf,"History-WRITING began before Islam (Greeks, Romans…). Muslims turned it into a real science — gathered it (2nd–4th c. AH), sifted it (7th), perfected it (8th, Ibn Khaldūn).",
     size=17,italic=True,color=TEAL,first=True,space_after=0)
notes(s,"LIGHT ~1 min.\n"
        "«یہ چار مرحلے ہر علم کے ہوتے ہیں، بالکل گھر بنانے کی طرح — بنیاد (تاسیس)، دیواریں اور مال جمع (تدوین)، "
        "پلستر اور صفائی یعنی کمزور مال نکالنا (تنقیح)، اور رنگ روغن یعنی بہتر و آسان بنانا (تکمیل)۔»\n"
        "خاص نکتہ (کوئی پوچھے تو): «تاریخ نگاری، یعنی یہ فن، کی *تاسیس* اسلام سے پہلے یونان و روم میں ہو چکی تھی، مگر "
        "بغیر سند کے۔ مسلمانوں نے اِسے سند اور اصول کے ساتھ ایک باقاعدہ *علم* بنایا۔»\n"
        "«تاریخ کی تدوین ۲-۳-۴ ہجری؛ تنقیح ۷ویں صدی (ذہبی ’تاریخ الاسلام‘، ابن کثیر ’البدایہ‘)؛ تہذیب کا عروج ۸ویں صدی (ابن خلدون)۔»\n"
        "Ref: muqaddima p.41-42, 45.")
footer(s,"4 stages")

# ===== 14 GIANTS (condensed)
s=slide(); bg(s); kicker(s,"The people who actually wrote it down")
goldbar(s); headline(s,"Meet the giants",size=30)
_,tf=tb(s,Inches(0.7),Inches(2.05),Inches(11.9),Inches(4.6))
for n,t in [
 ("Ibn Isḥāq (d.151) → Ibn Hishām (d.213):","the seerah we still read most — Sīrat Ibn Hishām."),
 ("Wāqidī (d.207) & his student Ibn Saʿd (d.230):","one vivid but loose, one careful. Ibn Saʿd's Ṭabaqāt is a treasury of the Companions."),
 ("Balādhurī (d.279):","the conquests, city by city — Futūḥ al-Buldān."),
 ("⚠ Yaʿqūbī & Masʿūdī (d.346):","were Shīʿa — parts tilt against the Companions. We read them aware."),
]:
    p,_=para(tf,n+" ",size=20,bold=True,color=TEAL,first=(n.startswith("Ibn Isḥ")),space_after=12)
    r=p.add_run(); r.text=t; r.font.size=Pt(20); r.font.color.rgb=INK; r.font.name=SANS
notes(s,"تیزی سے، نام رٹنے کی ضرورت نہیں — slide خود carry کر رہی ہے۔ مختصر تعارف:\n"
        "«پہلے سیرت سینوں میں تھی۔ زہریؒ نے پہلی مغازی کی کتاب لکھی؛ ابن اسحاقؒ نے سب جمع کیا؛ ابن ہشامؒ نے اُسے صاف "
        "کر کے وہ سیرت دی جو آج بھی سب سے مشہور ہے۔»\n"
        "«واقدیؒ بہت رنگین اور تفصیل والے تھے مگر روایت میں ذرا بے احتیاط؛ اُن کے شاگرد ابن سعدؒ زیادہ محتاط نکلے — "
        "اُن کی ’طبقات‘ صحابہؓ کے حالات کا خزانہ ہے۔ بلاذریؒ نے شہر بہ شہر فتوحات لکھیں۔»\n"
        "سب سے اہم نکتہ (ضرور کہیں): «یعقوبی اور مسعودی شیعہ مؤرخ تھے — اُن کے بعض حصے صحابہؓ کے خلاف جھکتے ہیں۔ "
        "اِس لیے ہمیشہ پوچھیں: یہ لکھا کس نے؟»\n"
        "Ref: muqaddima p.43-46.")
footer(s,"Giants")

# ===== 15 BOOKS (shelf) + Tabari namesake box
s=slide(); bg(s); kicker(s,"Five books. Almost everything else comes from these.")
goldbar(s); headline(s,"The five big ones",size=30)
card_row(s,[
 ("Tārīkh al-Ṭabarī","d.310","The big well: every report with its chain."),
 ("Al-Kāmil","Ibn al-Athīr d.630","Year by year, cleaned up."),
 ("Tārīkh al-Islām","Dhahabī d.748","The most careful sieve."),
 ("Al-Bidāya","Ibn Kathīr d.774","Chains + reason; easiest read."),
 ("Ibn Khaldūn","d.808","Its Muqaddima started social science."),
], y=2.5, h=2.5, title_size=16, desc_size=14)
rect(s,Inches(0.7),Inches(5.25),Inches(11.93),Inches(1.5),fill=CREAM_D,line=GOLD,lw=1.5)
_,tf=tb(s,Inches(1.0),Inches(5.4),Inches(11.3),Inches(1.2))
para(tf,"🎯  Fun fact — two men, same name:",size=16,bold=True,color=TEAL,first=True,space_after=4)
para(tf,"There were TWO Ṭabarīs with the exact same name. Ours (grandson of Yazīd) is the Sunnī imam; the other "
        "(from Rustam) was Shīʿa. The mix-up has fooled people into calling our Ṭabarī a Shīʿa. He wasn't.",
     size=16,color=INK,space_after=0)
notes(s,"کتابوں کو ایک ’شیلف‘ کی طرح پیش کریں:\n"
        "«پانچ بڑی ماں کتابیں ہیں، باقی سب اِنہی سے نکلتی ہیں۔ طبری — کچا کنواں، ہر روایت سند کے ساتھ۔ ابن اثیر کی "
        "’الکامل‘ — سال بہ سال، نچوڑ کر۔ ذہبی کی ’تاریخ الاسلام‘ — سب سے سخت چھان بین۔ ابن کثیر کی ’البدایہ‘ — سند "
        "اور عقل دونوں، پڑھنے میں سب سے آسان۔ اور ابن خلدون — جن کے مقدمے نے عمرانیات (سوشیالوجی) کی بنیاد رکھی۔»\n"
        "مزیدار بات (اعتراض کا توڑ): «دو طبری تھے، بالکل ایک ہی نام! ہمارے والے، یزید کے پوتے، سنی امام؛ دوسرے، رستم "
        "کی نسل سے، شیعہ۔ اِسی نام کی مشابہت سے لوگوں نے ہمارے طبری کو بھی شیعہ سمجھ لیا — حالانکہ وہ نہیں تھے، حافظ "
        "ذہبیؒ نے خود اِس الزام کی تردید کی۔»\n"
        "EXTRA: دو چھپے جواہر بھی — المنتظم (ابن جوزی) اور مرآۃ الزمان (اُن کے نواسے)۔\n"
        "Ref: muqaddima p.69-78.")
footer(s,"The books")

# ===== 16 FUN STORY wine
s=slide(); bg(s); kicker(s,"How the rules catch a fake story")
goldbar(s); headline(s,"The “wine cup” story",size=30)
_,tf=tb(s,Inches(0.7),Inches(2.1),Inches(11.9),Inches(4.5))
para(tf,"A story went around: Maʾmūn al-Rashīd tested Imām al-Shāfiʿī with enough wine to floor any man, and it did nothing to him.",
     size=22,first=True,space_after=14)
para(tf,"Ḥāfiẓ Ibn Ḥajar took it apart in two lines:",size=22,bold=True,color=TEAL,space_after=10)
para(tf,"•  History: al-Shāfiʿī meeting Maʾmūn isn't even proven. The chain fails.",size=21,space_after=8)
para(tf,"•  Common sense: al-Shāfiʿī said he'd skip even cold water if it dulled his mind. A wine cup?!",size=21,space_after=0)
notes(s,"«ایک اور مثال کہ یہ اصول جعلی کہانی کیسے پکڑتے ہیں۔ ایک قصہ مشہور ہوا کہ مامون الرشید نے امام شافعیؒ کو "
        "آزمانے کے لیے اتنی شراب پلائی جو کسی عام آدمی کو گرا دے — مگر امام صاحب پر کوئی اثر نہ ہوا۔»\n"
        "«حافظ ابن حجرؒ نے ’لسان المیزان‘ میں دو ہی باتوں سے اِسے جعلی ثابت کر دیا۔ ایک — تاریخی طور پر امام شافعیؒ "
        "کا مامون سے ملنا ہی ثابت نہیں، تو سند ہی ٹوٹ گئی۔ دوسری — عقل: امام شافعیؒ تو وہ ہستی ہیں جو فرماتے تھے کہ "
        "اگر مجھے خدشہ ہو کہ ٹھنڈا پانی بھی میری سمجھ بوجھ پر اثر ڈالے گا تو میں عمر بھر گرم پانی پیوں — ایسی شخصیت کے "
        "بارے میں شراب کی کہانی؟!»\n"
        "اگر اٹک جائیں: سند ٹوٹی (شافعیؒ مامون سے ملے ہی نہیں)؛ اور عقل کہتی ہے — جو ٹھنڈا پانی چھوڑ دے، وہ شراب پیے گا؟\n"
        "[skippable اگر وقت کم ہو]\n"
        "Ref: muqaddima p.57 (Lisan al-Mizan, Ibn Hajar).")
footer(s,"Detective")

# ===== 17 CLOSE
s=slide(); bg(s,TEAL_D)
rect(s,Inches(0.7),Inches(1.2),Inches(2.0),Pt(4),fill=GOLD)
_,tf=tb(s,Inches(0.7),Inches(1.4),Inches(11.9),Inches(2.2))
para(tf,"Next week",size=18,color=GOLD,bold=True,first=True,space_after=8)
para(tf,"The story begins — Abu Bakr ؓ",size=38,color=WHITE,bold=True,font=EN,space_after=6)
para(tf,"خلافتِ راشدہ اور سیدنا ابوبکر صدیق ؓ",size=26,color=CREAM,font=AR,arabic=True,space_after=0)
_,tf=tb(s,Inches(0.7),Inches(4.3),Inches(11.9),Inches(2.6))
para(tf,"We start exactly where the seerah ended, and put our first bright peg on the timeline.",
     size=22,color=CREAM,first=True,space_after=16)
para(tf,"گھر لے جانے والا سوال: کوئی تاریخ کی ”بات“ سنائے — تو اب آپ سب سے پہلے *کیا* پوچھیں گے؟",
     size=21,color=GOLD,bold=True,font=AR,arabic=True,space_after=0)
notes(s,"Take-home سوال پر ختم کریں (جواب: ”کس نے کہا؟ ماخذ کیا ہے؟“)۔ Banner لگا رہنے دیں۔ وقت ہو تو ایک دو "
        "ہلکے سوال لیں؛ گرم موضوع کو مسکرا کر سبق ۵ پر ٹال دیں۔")
footer(s,"Close")

# ===== 18 SOURCES
s=slide(); bg(s); kicker(s,"Where this comes from"); goldbar(s); headline(s,"Sources",size=28)
_,tf=tb(s,Inches(0.7),Inches(2.1),Inches(11.9),Inches(4.6))
for t in [
 "Course text — Tareekh-e-Ummat, Maulana Muhammad Ismail Rehan, Vol. 1 (the muqaddima).",
 "The forged document — al-Muntaẓam, Ibn al-Jawzī (muqaddima p.57–58).",
 "Method, isnād, the giants & books — muqaddima p.43–49, 69–78.",
 "Hijri calendar & Nasī' — al-Shamārīkh, al-Suyūṭī; Tarīkh al-Ṭabarī; al-Tawba 9:37 (muqaddima p.35–40).",
 "Fiqh of studying history — muqaddima p.52–53. ʿibrah āyah — Yūsuf 12:111.",
 "The 'wine' story — Lisān al-Mīzān, Ibn Ḥajar (muqaddima p.57).",
 "Map (slide 12) — frame from Kings & Generals, “Early Muslim Expansion” (YouTube).",
]:
    para(tf,"•  "+t,size=17,first=(t.startswith("Course")),space_after=10)
notes(s,"اپنی credibility / handout کے لیے۔ Live دکھانے کی ضرورت نہیں جب تک کوئی پوچھے نہیں۔ سارے dates "
        "established ہیں اور source سے مطابقت رکھتے ہیں۔")
footer(s,"Sources")

out=os.path.join(os.path.dirname(os.path.abspath(__file__)),"Lecture1.pptx")
try:
    prs.save(out)
except PermissionError:
    out=out.replace(".pptx","_NEW.pptx"); prs.save(out)
    print("NOTE: Lecture1.pptx was open/locked — saved as", out, "(close PowerPoint, then rename).")
print("Saved:",out,"·",len(prs.slides._sldIdLst),"slides")
