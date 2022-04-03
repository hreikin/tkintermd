import tkintermd.tkintermd_constants as constants

from pathlib import Path
import tkinter as tk
from tkinter import filedialog, simpledialog
from tkinter import messagebox as mbox
from tkinter.constants import *
from tkinterweb import HtmlFrame

from markdown import Markdown
from pygments import lex
from pygments.styles import get_all_styles
from pygments.lexers.markup import MarkdownLexer
from pygments.token import Generic
from pygments.lexer import bygroups
from pygments.styles import get_style_by_name

class TkinterMDFrame(tk.Frame):
    """An embeddable tkinter based Markdown editor with HTML preview. 
    
    The editor has syntax highlighting supplied by `Pygments` and the HTML 
    preview window is provided by `tkinterweb`.
    
    Import it into your own scripts like so:
    
    ```python
    from tkintermd.tkintermd_frame import TkinterMDFrame

    import tkinter as tk
    from tkinter.constants import *

    root = tk.Tk()
    app = TkinterMDFrame(root)
    app.pack(fill="both", expand=1)
    app.mainloop()
    ```
    
    """
    def __init__(self, master, **kwargs):
        tk.Frame.__init__(self, master) # no need for super

        # Toolbar.
        self.top_bar = tk.Frame(self.master)
        self.open_btn = tk.Button(self.top_bar, text="Open", command=self.open_md_file)
        self.open_btn.pack(side="left", padx=0, pady=0)
        self.save_as_btn = tk.Button(self.top_bar, text="Save As", command=self.save_as_md_file)
        self.save_as_btn.pack(side="left", padx=0, pady=0)
        self.save_btn = tk.Button(self.top_bar, text="Save", command=self.save_md_file)
        self.save_btn.pack(side="left", padx=0, pady=0)
        self.undo_btn = tk.Button(self.top_bar, text="Undo", command=lambda: self.text_area.event_generate("<<Undo>>"))
        self.undo_btn.pack(side="left", padx=0, pady=0)
        self.redo_btn = tk.Button(self.top_bar, text="Redo", command=lambda: self.text_area.event_generate("<<Redo>>"))
        self.redo_btn.pack(side="left", padx=0, pady=0)
        self.cut_btn = tk.Button(self.top_bar, text="Cut", command=lambda: self.text_area.event_generate("<<Cut>>"))
        self.cut_btn.pack(side="left", padx=0, pady=0)
        self.copy_btn = tk.Button(self.top_bar, text="Copy", command=lambda: self.text_area.event_generate("<<Copy>>"))
        self.copy_btn.pack(side="left", padx=0, pady=0)
        self.paste_btn = tk.Button(self.top_bar, text="Paste", command=lambda: self.text_area.event_generate("<<Paste>>"))
        self.paste_btn.pack(side="left", padx=0, pady=0)
        self.find_btn = tk.Button(self.top_bar, text="Find", command=self.find)
        self.find_btn.pack(side="left", padx=0, pady=0)
        self.bold_btn = tk.Button(self.top_bar, text="Bold", command=lambda: self.apply_markdown_both_sides(constants.bold_md_syntax, constants.bold_md_ignore))
        self.bold_btn.pack(side="left", padx=0, pady=0)
        self.italic_btn = tk.Button(self.top_bar, text="Italic", command=lambda: self.apply_markdown_both_sides(constants.italic_md_syntax, constants.italic_md_ignore))
        self.italic_btn.pack(side="left", padx=0, pady=0)
        # Currently has issues, needs constants adjusting.
        self.bold_italic_btn = tk.Button(self.top_bar, text="Bold Italic", command=lambda: self.apply_markdown_both_sides(constants.bold_italic_md_syntax, constants.bold_italic_md_ignore))
        self.bold_italic_btn.pack(side="left", padx=0, pady=0)
        # self.heading_btn = tk.Button(self.top_bar, text="Heading")
        # self.heading_btn.pack(side="left", padx=0, pady=0)
        self.strikethrough_btn = tk.Button(self.top_bar, text="Strikethrough", command=lambda: self.apply_markdown_both_sides(constants.strikethrough_md_syntax, constants.strikethrough_md_ignore))
        self.strikethrough_btn.pack(side="left", padx=0, pady=0)
        # self.unordered_list_btn = tk.Button(self.top_bar, text="Unordered List")
        # self.unordered_list_btn.pack(side="left", padx=0, pady=0)
        # self.ordered_list_btn = tk.Button(self.top_bar, text="Ordered List")
        # self.ordered_list_btn.pack(side="left", padx=0, pady=0)
        # self.checklist_btn = tk.Button(self.top_bar, text="Checklist")
        # self.checklist_btn.pack(side="left", padx=0, pady=0)
        # self.blockquote_btn = tk.Button(self.top_bar, text="Blockquote")
        # self.blockquote_btn.pack(side="left", padx=0, pady=0)
        # self.codeblock_btn = tk.Button(self.top_bar, text="Codeblock")
        # self.codeblock_btn.pack(side="left", padx=0, pady=0)
        # self.table_btn = tk.Button(self.top_bar, text="Table")
        # self.table_btn.pack(side="left", padx=0, pady=0)
        # self.link_btn = tk.Button(self.top_bar, text="Link")
        # self.link_btn.pack(side="left", padx=0, pady=0)
        # self.image_btn = tk.Button(self.top_bar, text="Image")
        # self.image_btn.pack(side="left", padx=0, pady=0)
        
        self.style_opt_btn = tk.Menubutton(self.top_bar, text="Editor Style", relief="raised")
        self.style_opt_btn.pack(side="left", padx=0, pady=0)
        self.style_menu = tk.Menu(self.style_opt_btn, tearoff=False)
        self.style_menu.add_command(label='default', command=lambda: self.load_style('default'))
        self.style_menu.add_command(label='emacs', command=lambda: self.load_style('emacs'))
        self.style_menu.add_command(label='friendly', command=lambda: self.load_style('friendly'))
        self.style_menu.add_command(label='friendly_grayscale', command=lambda: self.load_style('friendly_grayscale'))
        self.style_menu.add_command(label='colorful', command=lambda: self.load_style('colorful'))
        self.style_menu.add_command(label='autumn', command=lambda: self.load_style('autumn'))
        self.style_menu.add_command(label='murphy', command=lambda: self.load_style('murphy'))
        self.style_menu.add_command(label='manni', command=lambda: self.load_style('manni'))
        self.style_menu.add_command(label='material', command=lambda: self.load_style('material'))
        self.style_menu.add_command(label='monokai', command=lambda: self.load_style('monokai'))
        self.style_menu.add_command(label='perldoc', command=lambda: self.load_style('perldoc'))
        self.style_menu.add_command(label='pastie', command=lambda: self.load_style('pastie'))
        self.style_menu.add_command(label='borland', command=lambda: self.load_style('borland'))
        self.style_menu.add_command(label='trac', command=lambda: self.load_style('trac'))
        self.style_menu.add_command(label='native', command=lambda: self.load_style('native'))
        self.style_menu.add_command(label='fruity', command=lambda: self.load_style('fruity'))
        self.style_menu.add_command(label='bw', command=lambda: self.load_style('bw'))
        self.style_menu.add_command(label='vim', command=lambda: self.load_style('vim'))
        self.style_menu.add_command(label='vs', command=lambda: self.load_style('vs'))
        self.style_menu.add_command(label='tango', command=lambda: self.load_style('tango'))
        self.style_menu.add_command(label='rrt', command=lambda: self.load_style('rrt'))
        self.style_menu.add_command(label='xcode', command=lambda: self.load_style('xcode'))
        self.style_menu.add_command(label='igor', command=lambda: self.load_style('igor'))
        self.style_menu.add_command(label='paraiso-light', command=lambda: self.load_style('paraiso-light'))
        self.style_menu.add_command(label='paraiso-dark', command=lambda: self.load_style('paraiso-dark'))
        self.style_menu.add_command(label='lovelace', command=lambda: self.load_style('lovelace'))
        self.style_menu.add_command(label='algol', command=lambda: self.load_style('algol'))
        self.style_menu.add_command(label='algol_nu', command=lambda: self.load_style('algol_nu'))
        self.style_menu.add_command(label='arduino', command=lambda: self.load_style('arduino'))
        self.style_menu.add_command(label='rainbow_dash', command=lambda: self.load_style('rainbow_dash'))
        self.style_menu.add_command(label='abap', command=lambda: self.load_style('abap'))
        self.style_menu.add_command(label='solarized-dark', command=lambda: self.load_style('solarized-dark'))
        self.style_menu.add_command(label='solarized-light', command=lambda: self.load_style('solarized-light'))
        self.style_menu.add_command(label='sas', command=lambda: self.load_style('sas'))
        self.style_menu.add_command(label='stata', command=lambda: self.load_style('stata'))
        self.style_menu.add_command(label='stata-light', command=lambda: self.load_style('stata-light'))
        self.style_menu.add_command(label='stata-dark', command=lambda: self.load_style('stata-dark'))
        self.style_menu.add_command(label='inkpot', command=lambda: self.load_style('inkpot'))
        self.style_menu.add_command(label='zenburn', command=lambda: self.load_style('zenburn'))
        self.style_menu.add_command(label='gruvbox-dark', command=lambda: self.load_style('gruvbox-dark'))
        self.style_menu.add_command(label='gruvbox-light', command=lambda: self.load_style('gruvbox-light'))
        self.style_menu.add_command(label='dracula', command=lambda: self.load_style('dracula'))
        self.style_menu.add_command(label='one-dark', command=lambda: self.load_style('one-dark'))
        self.style_menu.add_command(label='lilypond', command=lambda: self.load_style('lilypond'))
        self.style_opt_btn["menu"] = self.style_menu
        
        self.top_bar.pack(side="top", fill="x")

        # Creating the widgets
        self.editor_pw = tk.PanedWindow(self.master, orient="horizontal")
        self.editor_frame = tk.Frame(self.editor_pw)
        self.text_area = tk.Text(self.editor_frame, state="normal", wrap="none", pady=2, padx=3, undo=True, width=100, height=25, yscrollcommand=self.on_mousewheel)
        self.text_area.pack(side="left", fill="both", expand=1)
        self.scrollbar = tk.Scrollbar(self.editor_frame, command=self.on_scrollbar)
        self.scrollbar.pack(side="left", fill="y")
        self.preview_area = HtmlFrame(self.editor_pw)
        self.editor_pw.add(self.editor_frame)
        self.editor_pw.add(self.preview_area)
        self.editor_pw.pack(side="left", fill="both", expand=1)

        # Set Pygments syntax highlighting style.
        self.lexer = Lexer()
        self.syntax_highlighting_tags = self.load_style("stata")
        # Default markdown string.
        default_text = constants.default_md_string
        self.text_area.insert(0.0, default_text)
        # Applies markdown formatting to default file.
        self.check_markdown(start="1.0", end=END)
        self.text_area.focus_set()

        # Create right click menu layout for the editor.
        self.right_click = tk.Menu(self.text_area)
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
        self.text_area.bind("<<Modified>>", self.on_input_change)
        self.text_area.edit_modified(0)#resets the text widget to generate another event when another change occours
        
        self.text_area.bind_all("<Control-f>", self.find)
        self.text_area.bind_all("<Control-a>", self.select_all)
        self.text_area.bind("<Button-3>", self.popup)

        # # This links the scrollbars but is currently causing issues. 
        # Changing the settings to make the scrolling work
        # self.preview_area.html['yscrollcommand'] = self.on_mousewheel

    def popup(self, event):
        """Right-click popup at mouse location."""
        self.right_click.tk_popup(event.x_root, event.y_root)

    def on_scrollbar(self, *args):
        '''Scrolls both text widgets when the scrollbar is moved'''
        self.text_area.yview(*args)
        # # This links the scrollbars but is currently causing issues.
        # self.preview_area.html.yview(*args)

    def on_mousewheel(self, *args):
        '''Moves the scrollbar and scrolls the widgets on mousewheel event'''
        self.scrollbar.set(*args)
        # # This links the scrollbars but is currently causing issues.
        # self.preview_area.vsb.set(*args)
        self.on_scrollbar('moveto', args[0])

    def select_all(self, *args):
        """Select all text within the editor window."""
        self.text_area.tag_add(SEL, "1.0", END)
        self.text_area.mark_set(0.0, END)
        self.text_area.see(INSERT)

    def find(self, *args):
        """Search for a string within the editor window."""
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
        """Open a file and clear/insert the text into the text_area."""
        open_filename_md = filedialog.askopenfilename(filetypes=(("Markdown File", "*.md , *.mdown , *.markdown"), ("Text File", "*.txt"), ("All Files", "*.*")))
        if open_filename_md:
            try:
                with open(open_filename_md, "r") as stream:
                    open_filename_contents = stream.read()
                self.text_area.delete(1.0, END)
                self.text_area.insert(END, open_filename_contents)
                self.check_markdown(start="1.0", end=END)
                constants.cur_file = Path(open_filename_md)
            except:
                mbox.showerror(title="Error", message=f"Error Opening Selected File\n\nThe file you selected: {open_filename_md} can not be opened!")
    
    def save_as_md_file(self):
        """Saves the file with the given filename."""
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

        If it fails because no name exists it calls the "save_as_md_file" function."""
        self.file_data = self.text_area.get("1.0" , END)
        try:
            with open(constants.cur_file, "w") as stream:
                stream.write(self.file_data)
        except:
            self.save_as_md_file()

    def on_input_change(self, event):
        """When the user types update the preview and editors line numbers."""
        md2html = Markdown()
        markdownText = self.text_area.get("1.0", END)
        html = md2html.convert(markdownText)
        self.preview_area.load_html(html)
        self.preview_area.add_css(self.css)
        self.check_markdown(start="1.0", end=END)
        self.text_area.edit_modified(0) # resets the text widget to generate another event when another change occours

    def load_style(self, stylename):
        """Load Pygments style for syntax highlighting within the editor."""
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
        self.text_area.configure(bg=self.style.background_color,
                        fg=self.text_area.tag_cget("Token.Text", "foreground"),
                        selectbackground=self.style.highlight_color)
        self.text_area.tag_configure(str(Generic.StrongEmph), font=('Monospace', 10, 'bold', 'italic'))
        self.syntax_highlighting_tags.append(str(Generic.StrongEmph))
        self.css = 'body {background-color: %s; color: %s}' % (
            self.style.background_color,
            self.text_area.tag_cget("Token.Text", "foreground")
            )#used string%interpolation here because f'string' interpolation is too annoying with embeded { and }
        self.preview_area.add_css(self.css)
        return self.syntax_highlighting_tags    

    def check_markdown(self, start='insert linestart', end='insert lineend'):
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
        for token, content in lex(self.data, self.lexer):
            self.text_area.mark_set("range_end", "range_start + %ic" % len(content))
            for t in token.split():
                self.text_area.tag_add(str(t), "range_start", "range_end")
            self.text_area.mark_set("range_start", "range_end")

    def apply_markdown_both_sides(self, md_syntax, md_ignore):
        """Apply and remove markdown from either side of a selection.

        Args:
            md_syntax (tuple): Tuple of markdown strings to apply/remove.
            md_ignore (tuple): Tuple of markdown strings to ignore.
        """
        self.md_syntax = md_syntax
        self.md_ignore = md_ignore
        try:
            self.cur_selection = self.text_area.selection_get()
            if len(self.md_syntax) == 2 and self.md_syntax[0] == "**" and self.md_syntax[1] == "__" and str(self.cur_selection)[1] != "*" and str(self.cur_selection)[1] != "_":
                if str(self.cur_selection).startswith(self.md_syntax) == False and str(self.cur_selection).startswith(self.md_ignore) == False and str(self.cur_selection)[0] != "*" and str(self.cur_selection)[0] != "_":
                    self.with_md_selection = f"{self.md_syntax[0]}{self.cur_selection}{self.md_syntax[0]}"
                    self.text_area.delete(index1=SEL_FIRST, index2=SEL_LAST)
                    self.text_area.insert(INSERT, self.with_md_selection)
                    return
                else:
                    return
            if str(self.cur_selection).startswith(self.md_syntax) == True and str(self.cur_selection).endswith(self.md_syntax) == True and str(self.cur_selection).startswith(self.md_ignore) == False:
                self.without_md_selection = str(self.cur_selection).replace(self.md_syntax[0], "").replace(self.md_syntax[1], "")
                self.text_area.delete(index1=SEL_FIRST, index2=SEL_LAST)
                self.text_area.insert(INSERT, self.without_md_selection)
                return
            elif str(self.cur_selection).startswith(self.md_syntax) == True and str(self.cur_selection).startswith(self.md_ignore) == True:
                return
            elif str(self.cur_selection).startswith(self.md_syntax) == True and str(self.cur_selection).startswith(self.md_ignore) == False:
                self.without_md_selection = str(self.cur_selection).replace(self.md_syntax[0], "").replace(self.md_syntax[1], "")
                self.text_area.delete(index1=SEL_FIRST, index2=SEL_LAST)
                self.text_area.insert(INSERT, self.without_md_selection)
                return
            elif str(self.cur_selection).startswith(self.md_syntax) == False and str(self.cur_selection).startswith(self.md_ignore) == False:
                self.with_md_selection = f"{self.md_syntax[0]}{self.cur_selection}{self.md_syntax[0]}"
                self.text_area.delete(index1=SEL_FIRST, index2=SEL_LAST)
                self.text_area.insert(INSERT, self.with_md_selection)
                return
        except:
            print("EXCEPTION: Application/removal of markdown formatting failed.")
            pass

class Lexer(MarkdownLexer):
    """Extend MarkdownLexer to add markup for bold-italic. This needs extending 
    further before being complete."""
    tokens = {key: val.copy() for key, val in MarkdownLexer.tokens.items()}
    # # bold-italic fenced by '***'
    tokens['inline'].insert(2, (r'(\*\*\*[^* \n][^*\n]*\*\*\*)',
                                bygroups(Generic.StrongEmph)))
    # # bold-italic fenced by '___'
    tokens['inline'].insert(2, (r'(\_\_\_[^_ \n][^_\n]*\_\_\_)',
                                bygroups(Generic.StrongEmph)))
