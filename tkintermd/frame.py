import tkintermd.constants as constants
import tkintermd.log as log

from pathlib import Path
import tkinter as tk
from tkinter import filedialog, simpledialog
from tkinter import messagebox as mbox
from tkinter.constants import *
from tkinter.ttk import Combobox
from tkinterweb import HtmlFrame, Notebook
from tkinterweb.utilities import ScrolledTextBox

from markdown import Markdown
from markdownify import markdownify
from pygments import lex
from pygments.lexers.markup import MarkdownLexer
from pygments.formatters.html import HtmlFormatter
from pygments.token import Generic
from pygments.lexer import bygroups
from pygments.styles import get_style_by_name, get_all_styles

class TkintermdFrame(tk.Frame):
    """A Markdown editor with HTML preview for use in tkinter projects. 
    
    The editor has syntax highlighting supplied by `Pygments` and the HTML 
    preview window is provided by `tkinterweb`.
    
    Import it into your own scripts like so:
    
    ```python
    from tkintermd.frame import TkintermdFrame

    import tkinter as tk
    from tkinter.constants import *

    root = tk.Tk()
    app = TkintermdFrame(root)
    app.pack(fill="both", expand=1)
    app.mainloop()
    ```
    
    """
    def __init__(self, master, **kwargs):
        tk.Frame.__init__(self, master) # no need for super

        self.logger = log.create_logger()

        # Creating the widgets
        self.editor_pw = tk.PanedWindow(self.master, orient="horizontal")
        # Root editor frame
        self.editor_root_frame = tk.Frame(self.editor_pw)
        # Toolbar buttons
        self.editor_toolbar = tk.Frame(self.editor_root_frame)
        self.open_btn = tk.Button(self.editor_toolbar, text="Open", command=self.open_md_file)
        self.open_btn.pack(side="left", padx=0, pady=0)
        constants.editor_toolbar_menu_buttons.append(self.open_btn)
        self.save_as_btn = tk.Button(self.editor_toolbar, text="Save As", command=self.save_as_md_file)
        self.save_as_btn.pack(side="left", padx=0, pady=0)
        constants.editor_toolbar_menu_buttons.append(self.save_as_btn)
        self.save_btn = tk.Button(self.editor_toolbar, text="Save", command=self.save_md_file)
        self.save_btn.pack(side="left", padx=0, pady=0)
        constants.editor_toolbar_menu_buttons.append(self.save_btn)
        self.edit_mode_btn = tk.Button(self.editor_toolbar, text="Editor Mode", command=self.convert_editor_content)
        self.edit_mode_btn.pack(side="left", padx=0, pady=0)
        constants.editor_toolbar_menu_buttons.append(self.edit_mode_btn)
        self.undo_btn = tk.Button(self.editor_toolbar, text="Undo", command=lambda: self.text_area.event_generate("<<Undo>>"))
        self.undo_btn.pack(side="left", padx=0, pady=0)
        constants.editor_toolbar_formatting_buttons.append(self.undo_btn)
        self.redo_btn = tk.Button(self.editor_toolbar, text="Redo", command=lambda: self.text_area.event_generate("<<Redo>>"))
        self.redo_btn.pack(side="left", padx=0, pady=0)
        constants.editor_toolbar_formatting_buttons.append(self.redo_btn)
        self.cut_btn = tk.Button(self.editor_toolbar, text="Cut", command=lambda: self.text_area.event_generate("<<Cut>>"))
        self.cut_btn.pack(side="left", padx=0, pady=0)
        constants.editor_toolbar_formatting_buttons.append(self.cut_btn)
        self.copy_btn = tk.Button(self.editor_toolbar, text="Copy", command=lambda: self.text_area.event_generate("<<Copy>>"))
        self.copy_btn.pack(side="left", padx=0, pady=0)
        constants.editor_toolbar_formatting_buttons.append(self.copy_btn)
        self.paste_btn = tk.Button(self.editor_toolbar, text="Paste", command=lambda: self.text_area.event_generate("<<Paste>>"))
        self.paste_btn.pack(side="left", padx=0, pady=0)
        constants.editor_toolbar_formatting_buttons.append(self.paste_btn)
        self.find_btn = tk.Button(self.editor_toolbar, text="Find", command=self.find)
        self.find_btn.pack(side="left", padx=0, pady=0)
        constants.editor_toolbar_formatting_buttons.append(self.find_btn)
        self.bold_btn = tk.Button(self.editor_toolbar, text="Bold", command=lambda: self.check_markdown_both_sides(constants.BOLD_MD_SYNTAX, constants.BOLD_MD_IGNORE, constants.BOLD_MD_SPECIAL))
        self.bold_btn.pack(side="left", padx=0, pady=0)
        constants.editor_toolbar_formatting_buttons.append(self.bold_btn)
        self.italic_btn = tk.Button(self.editor_toolbar, text="Italic", command=lambda: self.check_markdown_both_sides(constants.ITALIC_MD_SYNTAX, constants.ITALIC_MD_IGNORE, constants.ITALIC_MD_SPECIAL))
        self.italic_btn.pack(side="left", padx=0, pady=0)
        constants.editor_toolbar_formatting_buttons.append(self.italic_btn)
        self.bold_italic_btn = tk.Button(self.editor_toolbar, text="Bold Italic", command=lambda: self.check_markdown_both_sides(constants.BOLD_ITALIC_MD_SYNTAX, constants.BOLD_ITALIC_MD_IGNORE, constants.BOLD_ITALIC_MD_SPECIAL))
        self.bold_italic_btn.pack(side="left", padx=0, pady=0)
        constants.editor_toolbar_formatting_buttons.append(self.bold_italic_btn)
        self.strikethrough_btn = tk.Button(self.editor_toolbar, text="Strikethrough", command=lambda: self.check_markdown_both_sides(constants.STRIKETHROUGH_MD_SYNTAX, constants.STRIKETHROUGH_MD_IGNORE, md_special=None, strikethrough=True))
        self.strikethrough_btn.pack(side="left", padx=0, pady=0)
        constants.editor_toolbar_formatting_buttons.append(self.strikethrough_btn)
        # self.heading_btn = tk.Button(self.editor_toolbar, text="Heading")
        # self.heading_btn.pack(side="left", padx=0, pady=0)
        # constants.editor_toolbar_formatting_buttons.append(self.heading_btn)
        # self.unordered_list_btn = tk.Button(self.editor_toolbar, text="Unordered List")
        # self.unordered_list_btn.pack(side="left", padx=0, pady=0)
        # constants.editor_toolbar_formatting_buttons.append(self.unordered_list_btn)
        # self.ordered_list_btn = tk.Button(self.editor_toolbar, text="Ordered List")
        # self.ordered_list_btn.pack(side="left", padx=0, pady=0)
        # constants.editor_toolbar_formatting_buttons.append(self.ordered_list_btn)
        # self.checklist_btn = tk.Button(self.editor_toolbar, text="Checklist")
        # self.checklist_btn.pack(side="left", padx=0, pady=0)
        # constants.editor_toolbar_formatting_buttons.append(self.checklist_btn)
        # self.blockquote_btn = tk.Button(self.editor_toolbar, text="Blockquote")
        # self.blockquote_btn.pack(side="left", padx=0, pady=0)
        # constants.editor_toolbar_formatting_buttons.append(self.blockquote_btn)
        # self.codeblock_btn = tk.Button(self.editor_toolbar, text="Codeblock")
        # self.codeblock_btn.pack(side="left", padx=0, pady=0)
        # constants.editor_toolbar_formatting_buttons.append(self.codeblock_btn)
        # self.table_btn = tk.Button(self.editor_toolbar, text="Table")
        # self.table_btn.pack(side="left", padx=0, pady=0)
        # constants.editor_toolbar_formatting_buttons.append(self.table_btn)
        # self.link_btn = tk.Button(self.editor_toolbar, text="Link")
        # self.link_btn.pack(side="left", padx=0, pady=0)
        # constants.editor_toolbar_formatting_buttons.append(self.link_btn)
        # self.image_btn = tk.Button(self.editor_toolbar, text="Image")
        # self.image_btn.pack(side="left", padx=0, pady=0)
        # constants.editor_toolbar_formatting_buttons.append(self.image_btn)
        self.editor_toolbar.pack(side="top", fill="x")
        # Editor frame with scrollbar and text area.
        self.editor_frame = ScrolledTextBox(self.editor_root_frame)
        self.text_area = self.editor_frame.tbox
        self.editor_frame.pack(fill="both", expand=1)

        # Preview area
        self.preview_area_root_frame = tk.Frame(self.editor_pw)
        self.preview_area_toolbar = tk.Frame(self.preview_area_root_frame)
        self.template_label = tk.Label(self.preview_area_toolbar, text="Template : ")
        self.template_label.pack(side="left")
        self.template_combobox_value = tk.StringVar()
        self.template_combobox = Combobox(self.preview_area_toolbar, textvariable=self.template_combobox_value, values=constants.template_list)
        self.template_combobox.current(0)
        self.template_combobox.pack(side="left")
        # Button to choose pygments style for editor, preview and HTML.
        self.style_opt_btn = tk.Menubutton(self.preview_area_toolbar, text="Theme", relief="raised")
        self.style_opt_btn.pack(side="left", padx=0, pady=0)
        self.export_btn = tk.Button(self.preview_area_toolbar, text="Export HTML", command=self.save_as_html_file)
        self.export_btn.pack(side="left", padx=0, pady=0)
        self.preview_area_toolbar.pack(side="top", fill="x")
        # Rendered HTML preview.
        self.preview_document = HtmlFrame(self.preview_area_root_frame)
        self.preview_document.pack(fill="both", expand=1)

        # Add the editor and preview/export areas to the paned window.
        self.editor_pw.add(self.editor_root_frame)
        self.editor_pw.add(self.preview_area_root_frame)
        self.editor_pw.pack(side="left", fill="both", expand=1)

        # Load the self.style_opt_btn menu, this needs to be after the editor.
        self.style_menu = tk.Menu(self.style_opt_btn, tearoff=False)
        for style_name in get_all_styles():
            # dynamcially get names of styles exported by pygments
            try:
                # test them for compatability
                self.load_style(style_name)
            except Exception as E:
                self.logger.exception(f"WARNING: style {style_name} failed ({E}), removing from style menu.")
                continue # don't add them to the menu
            # add the rest to the menu
            self.style_menu.add_command(
                label=style_name,
                command=(lambda sn:lambda: self.load_style(sn))(style_name)
                # unfortunately lambdas inside loops need to be stacked 2 deep to get closure variables instead of cell variables
                )
        self.style_opt_btn["menu"] = self.style_menu

        # Set Pygments syntax highlighting style.
        self.md_lexer = CustomMarkdownLexer()
        self.syntax_highlighting_tags = self.load_style("stata")
        # self.syntax_highlighting_tags = self.load_style("material")
        # Default markdown string.
        default_text = constants.DEFAULT_MD_STRING
        self.text_area.insert(0.0, default_text)
        self.template_top = constants.DEFAULT_TEMPLATE_TOP
        self.template_middle = constants.DEFAULT_TEMPLATE_MIDDLE
        self.template_bottom = constants.DEFAULT_TEMPLATE_BOTTOM
        # Applies markdown formatting to default file.
        self.check_markdown_highlighting(start="1.0", end=END)
        self.text_area.focus_set()

        # Create right click menu layout for the editor.
        self.right_click = tk.Menu(self.text_area, tearoff=False)
        self.right_click.add_command(label="Copy", command=lambda: self.focus_get().event_generate("<<Copy>>"), accelerator="Ctrl+C")
        self.right_click.add_command(label="Cut", command=lambda: self.focus_get().event_generate("<<Cut>>"), accelerator="Ctrl+X")
        self.right_click.add_command(label="Paste", command=lambda: self.focus_get().event_generate("<<Paste>>"), accelerator="Ctrl+V")
        self.right_click.add_separator()
        self.right_click.add_command(label="Undo", command=lambda: self.focus_get().event_generate("<<Undo>>"), accelerator="Ctrl+Z")
        self.right_click.add_command(label="Redo", command=lambda: self.focus_get().event_generate("<<Redo>>"), accelerator="Ctrl+Y")
        self.right_click.add_separator()
        self.right_click.add_command(label="Find", command=self.find, accelerator="Ctrl+F")
        self.right_click.add_command(label="Select All", command=self.select_all, accelerator="Ctrl+A")

        # Bind mouse/key events to functions.
        self.template_combobox.bind("<<ComboboxSelected>>", self.change_template)
        self.text_area.bind("<<Modified>>", self.on_input_change)
        self.text_area.edit_modified(0)#resets the text widget to generate another event when another change occours
        
        self.text_area.bind_all("<Control-f>", self.find)
        self.text_area.bind_all("<Control-a>", self.select_all)
        self.text_area.bind("<Button-3>", self.popup)


    def popup(self, event):
        """Right-click popup at mouse location within the text area only.
        
        Provides the following options:
        
        - Cut.
        - Copy.
        - Paste.
        - Undo.
        - Redo.
        - Find.
        - Select All.
        """
        self.right_click.tk_popup(event.x_root, event.y_root)

    def select_all(self, *args):
        """Select all text within the editor window.
        
        - Add tag TAGNAME to all characters between INDEX1 and INDEX2.
        - Set mark MARKNAME before the character at index.
        - Scroll so that the character at INDEX is visible.
        """
        self.text_area.tag_add(SEL, "1.0", END)
        self.text_area.mark_set(0.0, END)
        self.text_area.see(INSERT)

    def find(self, *args):
        """Simple search dialog for within the editor window.
        
        - Get the current text area content.
        - Displays a simple dialog with a field to enter a search string into 
            and two buttons.
        - If a string is provided then search for it within the text area.
        - Add tag TAGNAME to all characters between INDEX1 and INDEX2.
        - Highlight any found strings within the text editor.
        """
        self.text_area.tag_remove('found', '1.0', END)
        target = simpledialog.askstring('Find', 'Search String:')

        if target:
            idx = '1.0'
            while 1:
                idx = self.text_area.search(target, idx, nocase=1, stopindex=END)
                if not idx: break
                lastidx = '%s+%dc' % (idx, len(target))
                self.text_area.tag_add('found', idx, lastidx)
                idx = lastidx
            self.text_area.tag_config('found', foreground='white', background='blue')

    def open_md_file(self):
        """Open a file and clear/insert the text into the text_area.
        
        Opens a native OS dialog and expects markdown formatted files. Shows an 
        error message if it fails.

        - Display a native OS dialog and request a filename to open.
        - If a filename is provided then `try` to open it in "read" mode.
        - Replace the text area content.
        - Set the `constants.cur_file` value to the filename that was opened.
        - If any of the above fails then display an error message.
        """
        open_filename_md = filedialog.askopenfilename(filetypes=(("Markdown File", "*.md , *.mdown , *.markdown"), ("Text File", "*.txt"), ("All Files", "*.*")))
        if open_filename_md:
            try:
                with open(open_filename_md, "r") as stream:
                    open_filename_contents = stream.read()
                self.text_area.delete(1.0, END)
                self.text_area.insert(END, open_filename_contents)
                self.check_markdown_highlighting(start="1.0", end=END)
                constants.cur_file = Path(open_filename_md)
            except:
                mbox.showerror(title="Error", message=f"Error Opening Selected File\n\nThe file you selected: {open_filename_md} can not be opened!")
    
    def save_as_md_file(self):
        """Saves the file with the given filename.
        
        Opens a native OS dialog for saving the file with a name and markdown 
        extension. Shows an error message if it fails.

        - Display a native OS dialog and request a filename to save.
        - If a filename is provided then `try` to open it in "write" mode.
        - Set the `constants.cur_file` value to the filename that was opened.
        - If any of the above fails then display an error message.
        """
        self.file_data = self.text_area.get("1.0" , END)
        self.save_filename_md = filedialog.asksaveasfilename(filetypes = (("Markdown File", "*.md"), ("Text File", "*.txt")) , title="Save Markdown File")
        if self.save_filename_md:
            try:
                with open(self.save_filename_md, "w") as stream:
                    stream.write(self.file_data)
                    constants.cur_file = Path(self.save_filename_md)
            except:
                mbox.showerror(title="Error", message=f"Error Saving File\n\nThe file: {self.save_filename_md} can not be saved!")

    def save_md_file(self):
        """Quick saves the file with its current name.

        - Get the current text area content.
        - `try` to save the file with the `constants.cur_file` variable.
        - If it fails because no name exists it calls the "save_as_md_file" 
            function.
        """
        self.file_data = self.text_area.get("1.0" , END)
        try:
            with open(constants.cur_file, "w") as stream:
                stream.write(self.file_data)
        except:
            self.save_as_md_file()

    def save_as_html_file(self):
        """Exports the current contents of the HTML preview pane to the given filename.
        
        Opens a native OS dialog for saving the file with a html
        extension. Shows an error message if it fails.

        - Display a native OS dialog and request a filename to save.
        - If a filename is provided then `try` to open it in "write" mode.
        - If any of the above fails then display an error message.
        """
        html_file_data = self.html
        self.html_save_filename = filedialog.asksaveasfilename(filetypes = (("HTML file", ("*.html", "*.htm")),) , title="Save HTML File")
        if self.html_save_filename:
            try:
                with open(self.html_save_filename, "w") as stream:
                    stream.write(html_file_data)
                    #constants.cur_file = Path(self.html_save_filename)
            except:
                mbox.showerror(title="Error", message=f"Error Saving File\n\nThe file: {self.html_save_filename} can not be saved!")

    def on_input_change(self, event):
        """Converts the text area input into html output for the HTML preview.
        
        When the user types:
        
        - Get the current text area contents.
        - Convert the markdown formatted string to HTML.
        - Merge the converted markdown with the currently selected template.
        - Load the merged HTML into the document preview.
        - Update the HTML content/states within the export options edit area.
        - Check the markdown and apply formatting to the text area.
        - Reset the modified flag.
        """
        if constants.input_type == "markdown":
            self.html = self.md_to_html()
            # self.final = f"{self.template_top}\n{self.css}\n{self.template_middle}\n{self.html}\n{self.template_bottom}"
        if constants.input_type == "html":
            self.html = self.text_area.get("1.0", END)
        self.preview_document.load_html(self.html)
        self.preview_document.add_css(self.css)
        self.check_markdown_highlighting(start="1.0", end=END)
        self.text_area.edit_modified(0) # resets the text widget to generate another event when another change occours

    def load_style(self, stylename):
        """Load Pygments style for syntax highlighting within the editor.
        
        - Load and configure the text area and `tags` with the Pygments styles 
            and `CustomMarkdownLexer` tags.
        - Create the CSS styling to be merged with the HTML template
        - Generate a `<<Modified>>` event to update the styles when a new style 
            is chosen.
        """
        self.style = get_style_by_name(stylename)
        self.syntax_highlighting_tags = []
        for token, opts in self.style.list_styles():
            kwargs = {}
            fg = opts['color']
            bg = opts['bgcolor']
            if fg:
                kwargs['foreground'] = '#' + fg
            if bg:
                kwargs['background'] = '#' + bg
            font = ('Monospace', 10) + tuple(key for key in ('bold', 'italic') if opts[key])
            kwargs['font'] = font
            kwargs['underline'] = opts['underline']
            self.text_area.tag_configure(str(token), **kwargs)
            self.syntax_highlighting_tags.append(str(token))
        # print(self.style.background_color or 'white', self.text_area.tag_cget("Token.Text", "foreground") or 'black', stylename)
        self.text_area.configure(bg=self.style.background_color or 'white',
                        fg=self.text_area.tag_cget("Token.Text", "foreground") or 'black',
                        selectbackground=self.style.highlight_color,
                        insertbackground=self.text_area.tag_cget("Token.Text", "foreground") or 'black',
                        )
        self.text_area.tag_configure(str(Generic.StrongEmph), font=('Monospace', 10, 'bold', 'italic'))
        self.syntax_highlighting_tags.append(str(Generic.StrongEmph))
        self.formatter = HtmlFormatter()
        self.pygments = self.formatter.get_style_defs(".highlight")
        # Previous version.
        self.css = 'body {background-color: %s; color: %s }\nbody .highlight{ background-color: %s; }\n%s' % (
            self.style.background_color,
            self.text_area.tag_cget("Token.Text", "foreground"),
            self.style.background_color,
            self.pygments
            )#used string%interpolation here because f'string' interpolation is too annoying with embeded { and }
        self.preview_document.add_css(self.css)
        self.text_area.event_generate("<<Modified>>")
        return self.syntax_highlighting_tags    

    def check_markdown_highlighting(self, start='insert linestart', end='insert lineend'):
        """Formats editor content using the Pygments style."""
        self.data = self.text_area.get(start, end)
        while self.data and self.data[0] == '\n':
            start = self.text_area.index('%s+1c' % start)
            self.data = self.data[1:]
        self.text_area.mark_set('range_start', start)
        # clear tags
        for t in self.syntax_highlighting_tags:
            self.text_area.tag_remove(t, start, "range_start +%ic" % len(self.data))
        # parse text
        for token, content in lex(self.data, self.md_lexer):
            self.text_area.mark_set("range_end", "range_start + %ic" % len(content))
            for t in token.split():
                self.text_area.tag_add(str(t), "range_start", "range_end")
            self.text_area.mark_set("range_start", "range_end")

    def apply_markdown_both_sides(self, selection, md_syntax):
        """Apply markdown to both sides of a selection.

        Args:
            selection (str): Text selection from the editor.
            md_syntax (tuple): Tuple of markdown strings to apply.
        """
        self.md_syntax = md_syntax
        self.cur_selection = selection
        self.insert_md = f"{self.md_syntax[0]}{self.cur_selection}{self.md_syntax[0]}"
        self.text_area.delete(index1=SEL_FIRST, index2=SEL_LAST)
        self.text_area.insert(INSERT, self.insert_md)
        return

    def remove_markdown_both_sides(self, selection, md_syntax):
        """Remove markdown from both sides of a selection.

        Args:
            selection (str): Text selection from the editor.
            md_syntax (tuple): Tuple of markdown strings to remove.
        """
        self.md_syntax = md_syntax
        self.cur_selection = selection
        self.remove_md = str(self.cur_selection).strip(self.md_syntax[0]).strip(self.md_syntax[1])
        self.text_area.delete(index1=SEL_FIRST, index2=SEL_LAST)
        self.text_area.insert(INSERT, self.remove_md)
        return

    def check_markdown_both_sides(self, md_syntax, md_ignore, md_special, strikethrough=None):
        """Check markdown formatting to be applied to both sides of a selection. 

        This will ignore items in the md_ignore variable and then deal with 
        special syntax individually before applying or removing the markdown 
        formatting.
        
        - If string starts with anything in md_ignore do nothing and return from
        the function.
        - If strikethrough is set to `True` then apply or remove the markdown.
        - If the formatting requires special items which can't go in md_ignore
        because they cause issues with markdown being applied incorrectly do 
        nothing and return from the function.
        - Apply or remove the markdown once we reach the end.

        Args:
            selection (str): Text selection from the editor.
            md_syntax (tuple): Tuple of markdown strings to remove.
            md_ignore (tuple): Tuple of markdown strings to ignore.
            md_special (tuple): Tuple of special markdown strings to ignore that 
                cause unexpected issues when included in md_ignore.
            strikethrough (bool): Set to True for strikethrough. Default is 
                `None`.
        """
        self.md_syntax = md_syntax
        self.md_ignore = md_ignore
        self.md_special = md_special
        self.cur_selection = self.text_area.selection_get()
        if str(self.cur_selection).startswith(self.md_ignore) or str(self.cur_selection).endswith(self.md_ignore):
            return
        elif strikethrough == True:
            if str(self.cur_selection).startswith(self.md_syntax) and str(self.cur_selection).endswith(self.md_syntax):
                self.remove_markdown_both_sides(self.cur_selection, self.md_syntax)
                return
            else:
                self.apply_markdown_both_sides(self.cur_selection, self.md_syntax)
                return
        elif str(self.cur_selection).startswith(self.md_special) and str(self.cur_selection).endswith(self.md_special) and not str(self.cur_selection).startswith(self.md_syntax) and not str(self.cur_selection).startswith(self.md_syntax):
            return 
        elif str(self.cur_selection).startswith(self.md_syntax) and str(self.cur_selection).endswith(self.md_syntax):
            self.remove_markdown_both_sides(self.cur_selection, self.md_syntax)
        else:
            self.apply_markdown_both_sides(self.cur_selection, self.md_syntax)

    def change_template(self, template_name):
        """Change the currently selected template.
        
        Get the selected template name from the `StringVar` for the `Combobox` 
        and compare it with the templates dictionary. If the name matches the 
        key then set the relevant template values and update all the previews.
        """
        template_name = self.template_combobox_value.get()
        for key, val in constants.template_dict.items():
            if template_name == key:
                self.template_top = val[0]
                self.template_middle = val[1]
                self.template_bottom = val[2]
        self.text_area.event_generate("<<Modified>>")
    
    def convert_editor_content(self):
        if constants.input_type == "markdown":
            html = self.md_to_html()
            self.text_area.delete("1.0", END)
            self.text_area.insert("1.0", html)
            for button in constants.editor_toolbar_formatting_buttons:
                button.configure(state="disabled")
            constants.input_type = "html"
        elif constants.input_type == "html":
            md = self.html_to_md()
            self.text_area.delete("1.0", END)
            self.text_area.insert("1.0", md)
            for button in constants.editor_toolbar_formatting_buttons:
                button.configure(state="normal")
            constants.input_type = "markdown"
        self.text_area.edit_modified(0) # resets the text widget to generate another event when another change occours

    def md_to_html(self):
        md2html = Markdown(extensions=constants.EXTENSIONS, extension_configs=constants.EXTENSION_CONFIGS)
        markdown_text = self.text_area.get("1.0", END)
        html = md2html.convert(markdown_text)
        return html

    def html_to_md(self):
        html_text = self.text_area.get("1.0", END)
        md = markdownify(html_text)
        return md


class CustomMarkdownLexer(MarkdownLexer):
    """Extend MarkdownLexer to add markup for bold-italic. 
    
    This needs extending further before being complete.
    """
    tokens = {key: val.copy() for key, val in MarkdownLexer.tokens.items()}
    # # bold-italic fenced by '***'
    tokens['inline'].insert(2, (r'(\*\*\*[^* \n][^*\n]*\*\*\*)',
                                bygroups(Generic.StrongEmph)))
    # # bold-italic fenced by '___'
    tokens['inline'].insert(2, (r'(\_\_\_[^_ \n][^_\n]*\_\_\_)',
                                bygroups(Generic.StrongEmph)))
