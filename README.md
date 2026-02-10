# Python_lectures
Here are all the lecture materials used in the 1. and 2. semester of Python programming for mathematicians, based on [How to Design Programs book](https://htdp.org/) and other notes by my colleague ([1.semester](http://mj.ucw.cz/vyuka/2021/p1m/), [2.semester](http://mj.ucw.cz/vyuka/2021/p2m/)). As taught on MFF UK 2023-2025 by me.

Additional recommendations for learning Python:
- [Khan Academy: Introduction to Python fundamentals](https://www.khanacademy.org/computing/intro-to-python-fundamentals)
- And some reading for evenings: [A layman's guide to thinking like the self-aware smol brained](https://grugbrain.dev/)

Link to my lecture sites here: [ipnp.cz/strelecek](https://ipnp.cz/strelecek).

## Structure
- The materials are organized into two main directories, `1.semester` and `2.semester`, each containing lecture notes, exercises, and additional resources for the respective semesters. Homeworks are linked to ReCodEx, appologies for outsiders which do not have access to it.
- `Website template`: I offer a template for website organization. GPTs can write the same in a few minutes (indeed it is mostly vibecoded), but as an inspiration this might help you to organize your own materials.
- `Conversion Scripts`: serve for converting Jupyter notebooks to html sites, so students don't have to download the notebook when browsing your webpage.


## Converting notebooks to html
Install [nbconvert](https://nbconvert.readthedocs.io/en/latest/) and run the deploy/convert_notebooks.sh script.
```bash
pip install jupyterlab nbconvert
```

On MacOS, templates should be located at
```bash
/opt/homebrew/share/jupyter/nbconvert/templates
```

## Inserting images
I did not follow this in the 1.semester, but it is better to directly embed images to markdown cells as
```markdown
<div style="text-align: center;">
    <img src="data:image/png;base64,YOUR_BASE64_STRING_HERE" alt="GPT logo" width="300" />
</div>
```
where `YOUR_BASE64_STRING_HERE` can be obtained by running `base64 -i image.png | pbcopy`