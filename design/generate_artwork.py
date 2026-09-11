"""Generate self-contained profile artwork. Requires fonttools and Avenir Next on macOS.
No font binaries or third-party image services are used by the published README.
"""
from pathlib import Path
from html import escape
import math
import re
from fontTools.ttLib import TTCollection
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

OUT = Path(__file__).resolve().parents[1] / 'assets'
FONTS = TTCollection('/System/Library/Fonts/Avenir Next.ttc').fonts
INK, BLUE, PAPER, MUTED = '#142C42', '#2356F6', '#EEF2F6', '#566B7D'

def letters(s,x,y,size,color=INK,bold=False,tracking=0):
    f=FONTS[0 if bold else 2]; scale=size/f['head'].unitsPerEm
    gs=f.getGlyphSet(); cmap=f.getBestCmap(); pen=SVGPathPen(gs)
    for c in s:
        name=cmap[ord(c)]
        gs[name].draw(TransformPen(pen,(scale,0,0,-scale,x,y)))
        x+=f['hmtx'][name][0]*scale+tracking
    return f'<path fill="{color}" d="{pen.getCommands()}"/>'

def svg(name,w,h,body,title,desc):
    content=f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" fill="none" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>
{body}
</svg>'''
    content=re.sub(r'-?\d+\.\d{4,}', lambda m: str(round(float(m[0]), 3)), content)
    (OUT/f'{name}.svg').write_text(content)

def rect(x,y,w,h,fill,rx=0,stroke=None):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}"'+(f' stroke="{stroke}"' if stroke else '')+'/>'

# Design plan: cool porcelain, cobalt, slate, periwinkle, and muted coral.
# One expressive hero; the rest is a restrained gallery of project-specific art.
# Critique: removed badges, decorative counters, card numbers and generic gradients.
# Theme-specific hero keeps contrast; project art has its own opaque background.
for theme in ['light','dark']:
    bg,fg,sub,line = (PAPER,INK,MUTED,'#CED7E1') if theme=='light' else ('#152432','#F2F6FC','#ADC0D2','#384B5D')
    b=rect(0,0,960,432,bg,16)
    b+=letters('Jinsu Park',40,54,25,fg,True)+letters('From first sketch to working code.',526,52,17,sub)
    b+=f'<path d="M40 78H920" stroke="{line}"/>'
    b+=letters('Ideas into',36,179,92,fg,True,tracking=-3.5)
    b+=letters('interfaces.',36,272,92,fg,True,tracking=-3.5)
    b+=letters('AI applications, web & macOS.',40,330,23,sub)
    b+=letters('jinsu.build',40,390,19,fg,True)
    # Transformation from a wireframe to a usable interface. No fabricated UI metrics.
    b+='<g transform="translate(610 102)">'
    b+=rect(14,18,262,234,'none',18,line)
    b+='<path d="M14 69H276M92 18V252M198 18V252M14 160H276" stroke="'+line+'" stroke-dasharray="4 6"/>'
    b+='<g transform="rotate(-8 161 162)">'
    b+=rect(38,59,260,250,BLUE,20)
    b+=f'<path d="M58 103H278" stroke="#698AFC"/>'
    b+='<circle cx="61" cy="82" r="4" fill="#FFFFFF"/><circle cx="76" cy="82" r="4" fill="#9EB7FF"/><circle cx="91" cy="82" r="4" fill="#9EB7FF"/>'
    b+=rect(61,124,130,13,'#E7EFFF',6)+rect(61,149,85,8,'#A8C0FF',4)
    b+=rect(61,180,74,102,'#F2F5FE',10)
    b+='<path d="M79 244L93 220L106 235L119 205" stroke="#2356F6" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>'
    b+=rect(147,180,128,46,'#9EB7FF',10)+rect(147,238,128,44,'#466FF8',10)
    b+='</g>'
    b+='<path d="M254 206L245 285L267 266L285 301L303 291L283 258L311 256Z" fill="#FFFFFF" stroke="#142C42" stroke-width="4" stroke-linejoin="round"/>'
    b+='</g>'
    svg(f'hero-{theme}',960,432,b,'Jinsu Park. Ideas into interfaces.','AI applications, web and macOS. A wireframe becomes a working interface; jinsu.build.')

# Each cover interprets a real product interaction rather than posing as a screenshot.
b=rect(0,0,720,280,'#DCE7EF',14)
b+=letters('Sobi Tribunal',28,57,33,INK,True)
b+=letters('A second look at spending.',28,91,18,MUTED)
b+='<g transform="rotate(9 515 150)"><path d="M411 31H606V237L592 250L578 237L564 250L550 237L536 250L522 237L508 250L494 237L480 250L466 237L452 250L438 237L424 250L411 237Z" fill="#FFFFFF"/>'
b+=letters('Think twice.',431,79,23,INK,True)
b+='<path d="M431 103H581M431 128H539M431 151H581M431 177H518" stroke="#C5D3DF" stroke-width="6" stroke-linecap="round"/>'
b+=rect(430,196,152,26,BLUE,5)+letters('Reflect, then decide.',440,214,12,'#FFFFFF',True)+'</g>'
b+='<path d="M31 211H270M270 211L255 196M270 211L255 226" stroke="#2356F6" stroke-width="3" stroke-linecap="round"/>'
svg('sobi',720,280,b,'Sobi Tribunal','Project artwork: a receipt invites the user to reflect before deciding. Planning, infrastructure and full v1/v2 implementation.')

b=rect(0,0,720,280,'#254FD8',14)
b+=letters('SpeakUp',28,57,33,'#FFFFFF',True)
b+=letters('Find your voice. Play it back.',28,91,18,'#DCE5FF')
for i in range(43):
    x=32+i*15.5; h=14+72*math.exp(-((i-14)/7)**2)*abs(math.sin(i*1.47))+65*math.exp(-((i-33)/5)**2)*abs(math.sin(i*1.37))
    b+=rect(round(x,2),round(193-h/2,2),5,round(h,2),'#FFFFFF' if i<25 else '#93B9FF',2.5)
b+='<circle cx="434" cy="192" r="39" fill="#254FD8" stroke="#FFFFFF" stroke-width="2"/><path d="M425 175L450 192L425 209Z" fill="#FFFFFF"/>'
svg('speakup',720,280,b,'SpeakUp','Project artwork: speech waveforms and playback. Speech recognition, LLM coaching and report replay.')

b=rect(0,0,720,280,'#DFDEF4',14)
b+=letters('Vispresso',28,57,33,INK,True)
b+=letters('A clearer cut.',28,91,18,MUTED)
b+=rect(31,121,422,128,'#202F4C',10)
for x in [48,156,264,372]:
 b+=rect(x,135,67,99,'#485B80',5)
 b+=f'<path d="M{x} 211L{x+28} 157L{x+67} 203V234H{x}Z" fill="#A4B8D1"/>'
 b+=f'<circle cx="{x+47}" cy="160" r="11" fill="#D8E3F1"/>'
b+=rect(527,87,106,161,'#202F4C',8)
b+='<path d="M533 208L578 113L627 202V242H533Z" fill="#A4B8D1"/><circle cx="598" cy="125" r="16" fill="#D8E3F1"/>'
b+='<path d="M470 185H506M495 174L507 185L495 196" stroke="#2356F6" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'
b+='<path d="M514 104V76H539M621 76H646V104M514 230V259H539M621 259H646V230" stroke="#2356F6" stroke-width="3"/>'
svg('vispresso',720,280,b,'Vispresso','Project artwork: a filmstrip becomes a vertical edit. Frontend for video preview, timelines and review.')

b=rect(0,0,720,280,'#E1EBE8',14)
b+=letters('Thumbstap',28,57,33,INK,True)
b+=letters('One gesture. Everything in reach.',28,91,18,MUTED)
b+=rect(31,119,273,130,'#F3F7F5',15,'#BDCDC7')
b+='<ellipse cx="230" cy="193" rx="27" ry="34" transform="rotate(-28 230 193)" stroke="#2356F6" stroke-width="2"/><ellipse cx="230" cy="193" rx="12" ry="20" transform="rotate(-28 230 193)" fill="#2356F6"/>'
b+='<path d="M331 185H394M383 174L395 185L383 196" stroke="#2356F6" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'
for row in range(2):
 for col in range(4):
  color=['#2356F6','#8EA7C1','#89ACA4','#D6A697'][(row+col)%4]
  b+=rect(427+col*60,130+row*60,45,45,color,11)
svg('thumbstap',720,280,b,'Thumbstap','Project artwork: a thumb gesture on a trackpad opens an app grid. A Swift macOS utility.')
print('Generated', len(list(OUT.glob('*.svg'))), 'self-contained SVG assets')
