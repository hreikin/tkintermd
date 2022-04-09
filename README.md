# `tkintermd`

<!-- PROJECT SHIELDS -->
![Commits](https://img.shields.io/github/commit-activity/m/hreikin/tkintermd?style=for-the-badge)
![Contributors](https://img.shields.io/github/contributors/hreikin/tkintermd.svg?style=for-the-badge)
![Forks](https://img.shields.io/github/forks/hreikin/tkintermd.svg?style=for-the-badge)
![Stargazers](https://img.shields.io/github/stars/hreikin/tkintermd.svg?style=for-the-badge)
![PyPI - Downloads](https://img.shields.io/pypi/dm/tkintermd?style=for-the-badge)
![Issues](https://img.shields.io/github/issues/hreikin/tkintermd.svg?style=for-the-badge)
![MIT License](https://img.shields.io/github/license/hreikin/tkintermd.svg?style=for-the-badge)

A Markdown editor with HTML preview for use in tkinter projects.

- [Explore the docs](https://hreikin.github.io/tkintermd)
- [Download the docs](https://hreikin.github.io/tkintermd/pdf/tkintermd-documentation-LATEST.pdf)
- [PyPi](https://pypi.org/project/tkintermd/)
- [Issues](https://github.com/hreikin/tkintermd/issues)

<!-- ABOUT THE PROJECT -->
## About The Project

An embeddable tkinter based Markdown editor with HTML preview. The editor has
syntax highlighting provided by `Pygments` and the HTML preview window is
provided by `tkinterweb`.

- Github v0.1.0 Project: [Github Project - tkintermd v0.1.0](https://github.com/users/hreikin/projects/1/)  
- Github Discussion: [Github Discussions](https://github.com/hreikin/tkintermd/discussions)  
- PyPi Link: [https://pypi.org/project/tkintermd/](https://pypi.org/project/tkintermd/)  
- PDF Documentation: [https://hreikin.github.io/tkintermd/pdf/tkintermd-documentation-LATEST.pdf](https://hreikin.github.io/tkintermd/pdf/tkintermd-documentation-LATEST.pdf)

### Built With

- [Pygments](https://github.com/pygments/pygments)
- [Python](https://www.python.org/)
- [Python Markdown](https://github.com/Python-Markdown/markdown)
- [tkinter](https://docs.python.org/3/library/tkinter.html)
- [tkinterweb](https://github.com/Andereoo/TkinterWeb)

<!-- GETTING STARTED -->
## Getting Started

### Installation

To get a local copy up and running choose one of the below install instructions
and follow the steps provided.

#### Install With PIP

The simplest way to install `tkintermd` is to use `pip`:

```sh
pip install tkintermd
```

#### Install From Source

Alternatively you can install from source by following the steps below:

1. Clone the repo:

   ```sh
   git clone https://github.com/hreikin/tkintermd.git
   cd tkintermd/
   ```

2. Create and source a Python virtual environment:

   ```sh
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install requirements with `pip`:

   ```sh
   pip install -r requirements.txt
   ```

<!-- USAGE EXAMPLES -->
## Usage

### Embedded

To use the `TkintermdFrame` in one of your own python scripts:

```python
from tkintermd.frame import TkintermdFrame

import tkinter as tk
from tkinter.constants import *

root = tk.Tk()
app = TkintermdFrame(root)
app.pack(fill="both", expand=1)
app.mainloop()
```

_For more examples, please refer to the [Documentation](https://hreikin.github.io/tkintermd)_

<!-- ROADMAP -->
## Roadmap

Check out the [Github Project - tkintermd v0.1.0](https://github.com/users/hreikin/projects/1/)
for an overview of the work being done towards the release. See the [open issues](https://github.com/hreikin/tkintermd/issues)
for a full list of proposed features (and known issues).

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<!-- CONTACT -->
## Contact

Github Link: [https://github.com/hreikin/tkintermd](https://github.com/hreikin/tkintermd)  
PyPi Link: [https://pypi.org/project/tkintermd/](https://pypi.org/project/tkintermd/)  
Documentation: [https://hreikin.github.io/tkintermd/](https://hreikin.github.io/tkintermd/)

<!-- ACKNOWLEDGMENTS -->
<!-- ## Acknowledgments -->

<!-- - []() -->
<!-- - []() -->
<!-- - []() -->
