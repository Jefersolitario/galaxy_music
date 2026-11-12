# galaxy_music

Beautiful galaxies dancing at the beat of music.

**Musica Universalis** draws galaxies, and a black hole, in 3D in your browser and moves them with the music. Two recordings come with it: Bach's Prelude in C major (BWV 846), which is calm water, and the storm that ends Vivaldi's *Summer*. You can also load a recording of your own.

## What's in it

Fourteen views, chosen from the strip above the play button:

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
- A black hole and its disk of gas (an imagined one)

Each galaxy is a likeness built from its known structure (bar, rings, arms, dust, tilt), not a copy of a photograph. Laniakea is a schematic, not a survey map.

**The black hole.** Gravity bends light near a black hole, so each pixel's line of sight is traced along the curved path light takes there. That is why the far side of the disk appears lifted over the top and folded underneath, with a thin ring of light at the edge of the shadow, and why stars behind it slide round it as the camera orbits. The gas coming towards you is brighter and whiter than the gas going away. It departs from a real one in three ways: the hole does not spin, that brightness contrast is softened so the dim side stays visible, and the stars use a simpler bending rule than the disk does. With the music, the gas orbits faster, the inner edge flares with the bass, and the disk tilts, which reshapes the whole bent image.

**How the music moves them.** The arm pattern turns at one rate while stars and gas orbit through it, faster near the centre, as in a real disk. The music sets the pace.

- **Bach.** Every note of the score was located in the recording, so the motion follows the pianist's actual timing and dynamics. Bass notes surge the spin and lean the disk, and new stars light up along the arms.
- **Vivaldi.** There is no score to follow, so the recording itself was analysed ahead of time: its onsets in the bass, middle and treble, each stroke of the full orchestra, and how hard it is playing ten times a second. The galaxy whirls faster as the orchestra builds and slows for the solos. Each big stroke throws the disk over, on the beat, with a flash through the core (never more than two a second). After a stroke the disk keeps wobbling round like a spun plate. In a silence it dims, slows and holds still until the storm breaks again.
- **Your own recording.** Its bass, middle and treble move the galaxy. A full, loud recording storms the way the Vivaldi does; a quiet one stays calm.

**Controls.** Drag to orbit, pinch or scroll to zoom, space to play or pause, left and right arrows to change galaxy. The row under the play button chooses the music.

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

Inside Streamlit the Bach recording is embedded in the page, so it is ready at once. The Vivaldi recording is fetched only when someone chooses it, from Streamlit's static file server (`enableStaticServing` in `.streamlit/config.toml`). If that cannot be reached, the page tries the copy on this repository's `main` branch instead. If you fork the repository, change `RAW` in `streamlit_app.py` to point at your own.

`index.html`, `prelude.mp3` and `static/summer-presto.mp3` also work on their own as a static site (GitHub Pages, for example), with no Python at all.

## Files

| File | What it is |
| --- | --- |
| `index.html` | The whole experience: one self-contained page (WebGL through three.js). |
| `prelude.mp3` | The Bach recording. |
| `static/summer-presto.mp3` | The Vivaldi recording. |
| `streamlit_app.py` | Serves the page full screen inside Streamlit. |
| `requirements.txt` | Streamlit, the only dependency. |
| `.streamlit/config.toml` | Dark theme, so there is no white flash on load, and static file serving. |

## Credits

- **Bach recording:** J. S. Bach, Prelude No. 1 in C major, BWV 846, played by Kimiko Ishizaka for the [Open Well-Tempered Clavier](https://welltemperedclavier.org) (2015), which she released into the public domain. One Wikimedia Commons upload of the same recording is tagged CC BY 3.0, so please keep this credit if you reuse the file.
- **Vivaldi recording:** A. Vivaldi, *The Four Seasons*, "Summer" (Concerto in G minor, RV 315), III. Presto. John Harrison, violin, with the Wichita State University Chamber Players, conducted by Robert Turizziani, recorded on 6 February 2000. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Source: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Vivaldi_-_Four_Seasons_2_Summer_mvt_3_Presto_-_John_Harrison_violin.oga). The MP3 here is a conversion of that file, copied from the [rauchg/vinyl](https://github.com/rauchg/vinyl) repository.
- **three.js** (MIT licence) is loaded from cdnjs. The fonts (Bodoni Moda, DM Mono, Instrument Sans) are loaded from Google Fonts.

## Licence

The code in this repository is released under CC0 1.0 (see `LICENSE`).

The recordings keep their own terms. The Vivaldi recording is **not** covered by CC0: it is CC BY-SA 4.0, so anyone who redistributes it must credit the performers and keep the same licence. That licence treats moving images synchronised to a recording as an adaptation, so the page played with this track may have to be shared under CC BY-SA 4.0 as well. This is a reading of the licence, not legal advice.
