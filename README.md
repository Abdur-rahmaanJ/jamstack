# jamstack

![](https://img.shields.io/pypi/v/jamstack)

Install

```bash
python -m pip install jamstack
```

Create basic project

```bash
jamstack plain <foldername>
```

`jamstack plain myproject`


with available templates

```bash
jamstack t <template> <foldername>
```

The only available template is 'html5up/massively' (`jamstack t html5up/massively myproject`)

Use the --existing flag if you want the project to be created in an existing folder (`jamstack t html5up/massively myproject --existing`)

Run project:

```bash
python static.py
```


# stites using the package:

- [https://deliciouspy.github.io/](https://deliciouspy.github.io/)

Use the --server flag if you want to start livewatch
