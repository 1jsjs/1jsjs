# Profile artwork

A profile for Jinsu Park's AI applications and native tools. The visual theme is the transition from an idea to a usable interface.

- Palette: porcelain `#EEF2F6`, ink `#142C42`, cobalt `#2356F6`, slate `#566B7D`, periwinkle `#DFDEF4`, sage `#E1EBE8`.
- Type: Avenir Next Bold for display, Regular for support. Artwork text is outlined so it does not rely on installed fonts or remote font loading. Body text uses GitHub's native typography.
- Layout: one wide hero, a quiet contact line, four project covers in a two-column gallery, then concise contribution and technology notes.
- Hero concept: a wireframe becomes an interface. Covers use each project's interaction: receipt, speech playback, video cropping, and trackpad gestures.
- Covers are editorial illustrations, not product screenshots. No usage numbers, charts with claimed metrics, or fabricated product output.
- Dark and light hero variants follow the viewer's color preference. Project covers have opaque backgrounds and work in either theme.
- Rejected from the earlier design: third-party banners, badge collections, decorative project numbers and activity counters.

The README needs no service, workflow, token, or scheduled job. All graphics are committed SVGs with titles, descriptions and native Markdown alternatives.

To regenerate on a Mac with Avenir Next installed: install `fonttools` in a Python environment and run `python design/generate_artwork.py`. Do not commit font binaries.
