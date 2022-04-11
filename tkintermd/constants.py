"""Variables and constants to be used by tkintermd.

Args:
    cur_file (Path): Variable for tracking current open file.
    bold_md_syntax (tuple): Markdown syntax for bold highlighting.
    bold_md_ignore (tuple): Markdown syntax to ignore for bold highlighting.
    bold_md_special (tuple): Markdown syntax to ignore for bold highlighting 
        that requires special handling.
    italic_md_syntax (tuple): Markdown syntax for italic highlighting.
    italic_md_ignore (tuple): Markdown syntax to ignore for italic highlighting.
    italic_md_special (tuple): Markdown syntax to ignore for italic highlighting 
        that requires special handling.
    bold_italic_md_syntax (tuple): Markdown syntax for bold-italic highlighting.
    bold_italic_md_ignore (tuple): Markdown syntax to ignore for bold-italic 
        highlighting.
    bold_italic_md_special (tuple): Markdown syntax to ignore for bold-italic 
        highlighting that requires special handling.
    strikethrough_md_syntax (tuple): Markdown syntax for strikethrough 
        highlighting.
    strikethrough_md_ignore (tuple): Markdown syntax to ignore for strikethrough 
        highlighting.
    default_md_string (str): Default string to show in the editor when it loads.
"""
from pathlib import Path
from pymdownx import emoji

cur_file = Path()
bold_md_syntax = ("**", "__")
bold_md_ignore = (
    "- ", "> ", "# ", "`", 
    "--", ">> ", "## ",
    "***", "___", "---", ">>> ", "### ", "```", "===",
    "####", "#####", "######",
)
bold_md_special = ("*","***", "_", "___")
italic_md_syntax = ("*", "_")
italic_md_ignore = (
    "- ", "> ", "# ", "`", 
    "**", "__", "--", ">> ", "## ",
    "***", "___", "---", ">>> ", "### ", "```", "===",
    "####", "#####", "######",
)
italic_md_special = ("**","***", "__", "___")
bold_italic_md_syntax = ("***", "___")
bold_italic_md_ignore = (
    "- ", "> ", "# ", "`", 
    "--", ">> ", "## ",
    "---", ">>> ", "### ", "```", "===",
    "####", "#####", "######",
)
bold_italic_md_special = ("*","**", "_", "__")
strikethrough_md_syntax = ("~~", "~~")
strikethrough_md_ignore = (
    "#", "##", "###", "####",
    "#####", "######", "======",
    "------", "- ", "* ", "> ", ">> ",
    "```", "`",
)
extensions = [
    'markdown.extensions.tables',
    'pymdownx.magiclink',
    'pymdownx.betterem',
    'pymdownx.tilde',
    'pymdownx.emoji',
    'pymdownx.tasklist',
    'pymdownx.superfences',
    'pymdownx.saneheaders'
]
extension_configs = {
    "pymdownx.magiclink": {
        "repo_url_shortener": True,
        "repo_url_shorthand": True,
        "provider": "github",
        "user": "facelessuser",
        "repo": "pymdown-extensions"
    },
    "pymdownx.tilde": {
        "subscript": False
    },
    "pymdownx.emoji": {
        "emoji_index": emoji.gemoji,
        "emoji_generator": emoji.to_png,
        "alt": "short",
        "options": {
            "attributes": {
                "align": "absmiddle",
                "height": "20px",
                "width": "20px"
            },
            "image_path": "https://assets-cdn.github.com/images/icons/emoji/unicode/",
            "non_standard_image_path": "https://assets-cdn.github.com/images/icons/emoji/"
        }
    }
}
default_md_string = """# Heading 1
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