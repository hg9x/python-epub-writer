# epubwriter

Generates valid EPuB 3.0 files with Python 3.

# Usage

```
from epubwriter import EPuB

metadata = {
    'title': 'Alice in Wonderland'
    ...
}

content = [
    {
        'title': 'Chapter 1',
        'html': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse diam odio, dapibus a laoreet quis...'
    },
    ...
]

epub = EPuB(metadata, content)
current_dir = Path.cwd()

epub.compile(current_dir, current_dir)

```python

The EPuB class takes in two parameters: metadata, and contents

`metadata` : dictionary

* title
* author
* publisher
* cover - URL of an online image, which will be used for the cover image. If none is supplied, a default one will be used.
* filename - filename of the outputed epub. If none is supplied, the title will be used

`contents` : list

Each entry of the list is a dictionary with the format

* title
* html - html string

Any `img` tags in the html will be downloaded

The `compile` method takes in two inputs

* output_dir - Python pathlib Path that represents where the epub will be saved in the end
* tmp_dir - Python pathlib Path that represents where the temmporary directory where files will be stored 

It is mostly important that the application has write permissions to whatever directories you supply.



