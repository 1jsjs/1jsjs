# Profile artwork

The selected direction is **Cutaway**: show the interaction and the part Jinsu implemented as an exploded software model. The three composition studies are in [DIRECTIONS.md](./DIRECTIONS.md).

## Production assets

- `assets/hero-{light,dark}.svg` and the corresponding `-ko.svg` headers contain exact, outlined English/Korean typography.
- `assets/cutaway/{thumbstap,sobi,speakup,vispresso}.png` are project-specific editorial illustrations generated with the built-in image generation tool. They are not screenshots or claimed product outputs.
- The final project illustrations are language-neutral apart from the product identifier SpeakUp and the file-format name MP4. Descriptions, role statements, alt text, and implementation links are localized in native Markdown.
- No runtime rendering service, workflow token, font request, tracking graphic, or scheduled regeneration is required.

## Sources and scope

| Project | Inspected revision | Visual basis | Jinsu's role |
| --- | --- | --- | --- |
| [Thumbstap](https://github.com/1jsjs/thumbstap/tree/178c9c6) | `178c9c6` | Native app grid, contact geometry, calibration, original app icon | Solo design, development, release |
| [Sobi Tribunal](https://github.com/1jsjs/sobi-tribunal/tree/c25efc3) | `c25efc3` | Original pig judge, courtroom art, upload/question/verdict flow, rules and explanation separation | Product planning, infrastructure, all v1/v2 code in a five-person team |
| [SpeakUp](https://github.com/eecczz/speech-coach/tree/007b080) | `007b080` | Report structure, light gray/plum colors, annotated replay and MP4 export | STT/LLM integration, coaching engine, report replay/export in a three-person team |
| [Vispresso](https://github.com/Me1e/jbnu_capstone_vispresso/tree/9a8ae50) | `9a8ae50` | Charcoal/red/teal review workbench, preview, trim ranges, timeline, original logo | Frontend in a four-person team |

Public source was inspected alongside the current career ledger and user corrections. The illustrations simplify the interfaces and do not attribute the rest of a team's work to Jinsu. The scenic video in the Vispresso illustration is generated placeholder imagery.

## Design system

- Surface `#E7EAED`; text `#17202A`; secondary text `#43515F`; structural outline `#A9B4BE`.
- Dark header `#222A32` with text `#F3F5F7`.
- Product colors come from the original projects rather than a universal accent color.
- Avenir Next and Apple SD Gothic Neo for the headers; GitHub's native typography for text.
- Header font glyphs are converted to SVG paths. Font binaries are never copied into the repository.
- Wide illustrations, no text embedded across languages, no tiny multi-column project descriptions.

## Generation and editing

Exact initial prompts are in [the prompt set](./prompts/2026-09-cutaway.json). The small corrective edits are in `prompts/corrections.json`. All image generation used the built-in tool, not an API-key/CLI fallback.

To regenerate the deterministic headers on a Mac with the listed fonts installed, install `fonttools` in a Python environment and run `python design/generate_artwork.py`.

English and Korean prose were revised using the public [Humanizer skill](https://github.com/blader/humanizer/blob/main/SKILL.md), with verified facts, names, links, and roles preserved. The skill was read for this edit; it was not installed as a global dependency.
