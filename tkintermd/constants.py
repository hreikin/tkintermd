"""Variables and constants to be used by tkintermd.

Args:
    cur_file (Path): Variable for tracking current open file.
    edit_warning (str): Warning message displayed to user when enabling edit 
        before export functionality.
    template_list (list): List of available template names.
    template_dict (dict): Dictionary containing lists of template values linked 
        with the appropriate name.
    BOLD_MD_SYNTAX (tuple): Markdown syntax for bold highlighting.
    BOLD_MD_IGNORE (tuple): Markdown syntax to ignore for bold highlighting.
    BOLD_MD_SPECIAL (tuple): Markdown syntax to ignore for bold highlighting 
        that requires special handling.
    ITALIC_MD_SYNTAX (tuple): Markdown syntax for italic highlighting.
    ITALIC_MD_IGNORE (tuple): Markdown syntax to ignore for italic highlighting.
    ITALIC_MD_SPECIAL (tuple): Markdown syntax to ignore for italic highlighting 
        that requires special handling.
    BOLD_ITALIC_MD_SYNTAX (tuple): Markdown syntax for bold-italic highlighting.
    BOLD_ITALIC_MD_IGNORE (tuple): Markdown syntax to ignore for bold-italic 
        highlighting.
    BOLD_ITALIC_MD_SPECIAL (tuple): Markdown syntax to ignore for bold-italic 
        highlighting that requires special handling.
    STRIKETHROUGH_MD_SYNTAX (tuple): Markdown syntax for strikethrough 
        highlighting.
    STRIKETHROUGH_MD_IGNORE (tuple): Markdown syntax to ignore for strikethrough 
        highlighting.
    DEFAULT_MD_STRING (str): Default string to show in the editor when it loads.
    DEFAULT_TEMPLATE_TOP (str): Default template, top portion.
    DEFAULT_TEMPLATE_MIDDLE (str): Default template, middle portion.
    DEFAULT_TEMPLATE_BOTTOM (str): Default template, bottom portion.
    CENTERED_TEMPLATE_TOP (str): Centered template, top portion.
    CENTERED_TEMPLATE_MIDDLE (str): Centered template, middle portion.
    CENTERED_TEMPLATE_BOTTOM (str): Centered template, bottom portion.
"""
from pathlib import Path
from pymdownx import emoji

editor_toolbar_menu_buttons = []
editor_toolbar_formatting_buttons = []
input_type = "markdown"
cur_file = Path()
cur_template_name = "default.html"
switch_editor_mode_message_shown = False
BOLD_MD_SYNTAX = ("**", "__")
BOLD_MD_IGNORE = (
    "- ", "> ", "# ", "`", 
    "--", ">> ", "## ",
    "***", "___", "---", ">>> ", "### ", "```", "===",
    "####", "#####", "######",
)
BOLD_MD_SPECIAL = ("*","***", "_", "___")
ITALIC_MD_SYNTAX = ("*", "_")
ITALIC_MD_IGNORE = (
    "- ", "> ", "# ", "`", 
    "**", "__", "--", ">> ", "## ",
    "***", "___", "---", ">>> ", "### ", "```", "===",
    "####", "#####", "######",
)
ITALIC_MD_SPECIAL = ("**","***", "__", "___")
BOLD_ITALIC_MD_SYNTAX = ("***", "___")
BOLD_ITALIC_MD_IGNORE = (
    "- ", "> ", "# ", "`", 
    "--", ">> ", "## ",
    "---", ">>> ", "### ", "```", "===",
    "####", "#####", "######",
)
BOLD_ITALIC_MD_SPECIAL = ("*","**", "_", "__")
STRIKETHROUGH_MD_SYNTAX = ("~~", "~~")
STRIKETHROUGH_MD_IGNORE = (
    "#", "##", "###", "####",
    "#####", "######", "======",
    "------", "- ", "* ", "> ", ">> ",
    "```", "`",
)
EXTENSIONS = [
    'markdown.extensions.codehilite',
    'markdown.extensions.tables',
    'pymdownx.magiclink',
    'pymdownx.betterem',
    'pymdownx.tilde',
    'pymdownx.emoji',
    'pymdownx.tasklist',
    'pymdownx.superfences',
    'pymdownx.saneheaders',
]
EXTENSION_CONFIGS = {
    "codehilite": {
        "linenums": True,
        "css_class": "highlight",
    },
    "pymdownx.magiclink": {
        "repo_url_shortener": True,
        "repo_url_shorthand": True,
        "provider": "github",
        "user": "facelessuser",
        "repo": "pymdown-extensions",
    },
    "pymdownx.tilde": {
        "subscript": False,
    },
    "pymdownx.emoji": {
        "emoji_index": emoji.gemoji,
        "emoji_generator": emoji.to_png,
        "alt": "short",
        "options": {
            "attributes": {
                "align": "absmiddle",
                "height": "20px",
                "width": "20px",
            },
            "image_path": "https://assets-cdn.github.com/images/icons/emoji/unicode/",
            "non_standard_image_path": "https://assets-cdn.github.com/images/icons/emoji/",
        }
    }
}
DEFAULT_MD_STRING = """# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6

Here is some normal text. Here is an `inline` code block. Here is some normal text.

``` python

# This is an untabbed, fenced code block with the language defined.
# There is a space after the start tag before the language and after the end tag.
def foo():
    print("Bar")

``` 

Here is some text.

``` 

# This is an untabbed, fenced code block without the language defined.
# There is a space after the start tag before the language and after the end tag.
def foo():
    print("Bar")

``` 

Here is some text.

``` python
	
	# This is a tabbed, fenced code block with the language defined.
    # There is a space after the start tag before the language and after the end tag.
	def foo():
	    print("Bar")
	
``` 

Here is some text.

``` 
	
	# This is a tabbed, fenced code block without the language defined.
   	# There is a space after the start tag before the language and after the end tag.
	def foo():
	    print("Bar")
	
``` 

Here is some normal text.

```python

# This is an untabbed, fenced code block with the language defined.
# There is no space after the tags.
def foo():
    print("Bar")

```

Here is some text.

```

# This is an untabbed, fenced code block without the language defined.
# There is no space after the tags.
def foo():
    print("Bar")

```

Here is some text.

```python
	
	# This is a tabbed, fenced code block with the language defined.
    # There is no space after the tags.
	def foo():
	    print("Bar")
	
```

Here is some text.

```
	
	# This is a tabbed, fenced code block without the language defined.
    # There is no space after the tags.
	def foo():
	    print("Bar")
	
```

Here is some normal text.   

Here is some normal text.  

Heading 1
=========

Heading 2
---------

Some paragraph text.
Line Breaks with two spaces on the end of the line.  
Line two.  
Line three.

- item one
- item two
    - item one
    - item two
- item three

Horizontal rule.
---

1. item one
2. item two
    1. item one
    2. item two
3. item three

*italic*
_Italic_
**bold**
__Bold__
***Bold Italic***
___Bold Italic___

> Blockquotes.
>
> Multiple paragraphs with a > symbol on the empty line.

> Blockquotes.
>
>> Nested paragraphs with a >> symbol.
> #### Using other elements
>
> - works with blockquotes
> - just like it would
>
>  *do* **normally**.

"""
DEFAULT_TEMPLATE_TOP = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>tkintermd - Default Template</title>
  <style>
    body {
        padding: 30px;  
        background-size: cover;  
        font-family: sans-serif;  
        align-items: center;
    }"""
DEFAULT_TEMPLATE_MIDDLE = """
  </style>
</head>
<Body>"""
DEFAULT_TEMPLATE_BOTTOM = """</Body>
</Html>"""
CENTERED_TEMPLATE_TOP = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>tkintermd - Default Template</title>
  <style>
    body {
        padding: 30px;  
        background-size: cover;  
        font-family: sans-serif;  
        align-items: center;
    }
    h1, h2, h3, h4, h5, h6 {
        text-align: center;
    }"""
CENTERED_TEMPLATE_MIDDLE = """
  </style>
</head>
<Body>"""
CENTERED_TEMPLATE_BOTTOM = """</Body>
</Html>"""
template_list = ["default", "centered"]
template_dict = {
    "default": [
        DEFAULT_TEMPLATE_TOP,
        DEFAULT_TEMPLATE_MIDDLE,
        DEFAULT_TEMPLATE_BOTTOM,
    ],
    "centered": [
        CENTERED_TEMPLATE_TOP,
        CENTERED_TEMPLATE_MIDDLE,
        CENTERED_TEMPLATE_BOTTOM,
    ]
}
edit_warning = """
Warning: Any edits made in the HTML code WILL NOT be reflected in the markdown \
editor.
        
Additionally, any changes to the markdown editor will reset the HTML and disable \
editing. Use this functionality just before exporting to make any required \
adjustments to the HTML.
"""