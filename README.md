# galaxy_music

Beautiful galaxies dancing at the beat of music.

**Musica Universalis** draws galaxies in 3D in your browser and moves them in time with a piano recording of Bach's Prelude in C major (BWV 846). You can also load a recording of your own.

## What's in it

Thirteen views, chosen from the strip above the play button:

- Grand-design spiral (an imagined galaxy)
- Andromeda Galaxy (M31), with M32 and M110
- Sombrero Galaxy (M104)
- Cigar Galaxy (M82)
- Messier 94 (NGC 4736)
- NGC 1097, NGC 1291, IC 342, IC 3639
- Hoag's Object
- Antennae Galaxies (NGC 4038 and NGC 4039)
- NGC 2207 and IC 2163
- Laniakea, our home supercluster

Each galaxy is a likeness built from its known structure (bar, rings, arms, dust, tilt), not a copy of a photograph. Laniakea is a schematic, not a survey map.

**How the music moves them.** Every note of the score was located in the recording, so the motion follows the pianist's actual timing and dynamics. The arm pattern turns at one rate while stars and gas orbit through it, faster near the centre, as in a real disk. The music sets the pace: bass notes surge the spin and lean the disk, and new stars light up along the arms.

**Controls.** Drag to orbit, pinch or scroll to zoom, space to play or pause, left and right arrows to change galaxy.

## Run it locally

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Deploy on Streamlit Community Cloud

1. Sign in at [share.streamlit.io](https://share.streamlit.io) with the GitHub account that owns this repository.
2. Create a new app from this repository and pick the branch to deploy.
3. Set the main file path to `streamlit_app.py` and deploy.

There are no secrets or data files to configure. All of the drawing and audio runs in the visitor's browser, which needs WebGL 2.

`index.html` and `prelude.mp3` also work on their own as a static site (GitHub Pages, for example), with no Python at all.

## Files

| File | What it is |
| --- | --- |
| `index.html` | The whole experience: one self-contained page (WebGL through three.js). |
| `prelude.mp3` | The piano recording. |
| `streamlit_app.py` | Serves the page full screen inside Streamlit. |
| `requirements.txt` | Streamlit, the only dependency. |
| `.streamlit/config.toml` | Dark theme, so there is no white flash on load. |

## Credits

- **Recording:** J. S. Bach, Prelude No. 1 in C major, BWV 846, played by Kimiko Ishizaka for the [Open Well-Tempered Clavier](https://welltemperedclavier.org) (2015), which she released into the public domain. One Wikimedia Commons upload of the same recording is tagged CC BY 3.0, so please keep this credit if you reuse the file.
- **three.js** (MIT licence) is loaded from cdnjs. The fonts (Bodoni Moda, DM Mono, Instrument Sans) are loaded from Google Fonts.

The code in this repository is released under CC0 1.0 (see `LICENSE`).
