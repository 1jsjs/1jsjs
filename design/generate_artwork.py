"""Generate bilingual outlined headers; final project art is in assets/cutaway.
Requires fonttools and the system fonts below. Never copies font binaries.
"""
from pathlib import Path
from html import escape
from fontTools.ttLib import TTCollection
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

OUT = Path(__file__).resolve().parents[1] / 'assets'
EN = TTCollection('/System/Library/Fonts/Avenir Next.ttc').fonts
KO = TTCollection('/System/Library/Fonts/AppleSDGothicNeo.ttc').fonts

def text_path(text, x, y, size, font, fill, stroke=None):
    scale = size / font['head'].unitsPerEm
    glyphs = font.getGlyphSet()
    cmap = font.getBestCmap()
    pen = SVGPathPen(glyphs)
    for c in text:
        glyph = cmap[ord(c)]
        glyphs[glyph].draw(TransformPen(pen, (scale, 0, 0, -scale, x, y)))
        x += font['hmtx'][glyph][0] * scale
    outline = f' stroke="{stroke}" stroke-width="0.9"' if stroke else ''
    return f'<path fill="{fill}"{outline} d="{pen.getCommands()}"/>'

for lang in ('en', 'ko'):
    name = 'Jinsu Park' if lang == 'en' else '박진수'
    subtitle = 'Web apps and macOS tools' if lang == 'en' else '웹 서비스와 macOS 앱을 만듭니다'
    font, size = (EN[0], 133) if lang == 'en' else (KO[6], 145)
    for theme in ('light', 'dark'):
        bg, fg, muted, outline = ('#E7EAED','#17202A','#43515F','#A9B4BE') if theme == 'light' else ('#222A32','#F3F5F7','#C1CBD4','#526270')
        b = f'<rect width="960" height="300" fill="{bg}"/>'
        b += text_path('github.com/1jsjs', 42, 43, 17, EN[2], muted)
        b += text_path(name, 54, 194, size, font, 'none', outline)
        b += text_path(name, 48, 188, size, font, 'none', outline)
        b += text_path(name, 42, 182, size, font, fg)
        b += f'<path d="M42 225H918" stroke="{outline}"/>'
        b += text_path(subtitle, 42, 270, 24, EN[2] if lang=='en' else KO[0], fg)
        suffix = '-ko' if lang=='ko' else ''
        title = name + '. ' + subtitle + '.'
        (OUT / f'hero-{theme}{suffix}.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="960" height="300" viewBox="0 0 960 300" role="img" aria-labelledby="title"><title id="title">{escape(title)}</title>{b}</svg>')
print('Generated four bilingual theme-aware headers.')
