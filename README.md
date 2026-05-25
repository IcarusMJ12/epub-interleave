# epub-interleave

A collection of python tools to generate a bilingual text as color-coded html
from a text and its translation.

Each sentence or group of sentences will display the inaccuracy of the
translation as a grey bar at the top right, extending all the way to the left
for translations whose accuracies are 0 or less (yes, this is possible XD ).


## Dependencies

`pip install -r requirements.txt` in your Python 3 virtual environment.

Outside of `requirements.txt` you'll need the `google/embeddinggemma-300m` from
huggingface.com or a similar embedding model (hardcoded for the time being).

If you're interleaving epubs you'll need to first convert them to raw text using
a tool like [epub2txt](https://github.com/kevinboone/epub2txt2.git).

If the resulting files have console escape codes, you may need to clean those up
manually or by using a tool such as npm-installed `ansi2html`.


## Usage

```bash
epub2txt a.epub > a.txt
epub2txt b.epub > b.txt  # if not text already

./sentencify.py < a.txt > a.sent.txt
./sentencify.py < b.txt > b.sent.txt

./align.py a.sent.txt b.sent.txt ab.pickle

./collate.py ab.pickle > ab.html

ansi2html -piu < ab.html > ab.fixed.html  # if necessary
./xmlcheck.py ab.fixed.html  # to check for invalid characters to edit out
```

Due to CSS implementation limitations of e-reader browsers, the grey alignment
mismatch bar doesn't span the content vertically.
