# Configuration file for ipython-nbconvert.

c = get_config()

#------------------------------------------------------------------------------
# NbConvertApp configuration
#------------------------------------------------------------------------------

# This application is used to convert notebook files (*.ipynb) to various other
# formats.
# 
# WARNING: THE COMMANDLINE INTERFACE MAY CHANGE IN FUTURE RELEASES.

# NbConvertApp will inherit config from: BaseIPythonApplication, Application

# The IPython profile to use.
# c.NbConvertApp.profile = u'default'

# The export format to be used.
# c.NbConvertApp.export_format = 'html'

# Set the log level by value or name.
# c.NbConvertApp.log_level = 30

# PostProcessor class used to write the  results of the conversion
# c.NbConvertApp.post_processor_class = u''

# List of notebooks to convert. Wildcards are supported. Filenames passed
# positionally will be added to the list.
# c.NbConvertApp.notebooks = []

# Path to an extra config file to load.
# 
# If specified, load this config file in addition to any other IPython config.
# c.NbConvertApp.extra_config_file = u''

# Whether to create profile dir if it doesn't exist
# c.NbConvertApp.auto_create = False

# overwrite base name use for output files. can only  be use when converting one
# notebook at a time.
# c.NbConvertApp.output_base = ''

# The name of the IPython directory. This directory is used for logging
# configuration (through profiles), history storage, etc. The default is usually
# $HOME/.ipython. This options can also be specified through the environment
# variable IPYTHONDIR.
# c.NbConvertApp.ipython_dir = u'/data1/home/dongweiming/.ipython'

# Whether to install the default config files into the profile dir. If a new
# profile is being created, and IPython contains config files for that profile,
# then they will be staged into the new directory.  Otherwise, default config
# files will be automatically generated.
# c.NbConvertApp.copy_config_files = False

# The date format used by logging formatters for %(asctime)s
# c.NbConvertApp.log_datefmt = '%Y-%m-%d %H:%M:%S'

# The Logging format template
# c.NbConvertApp.log_format = '[%(name)s]%(highlevel)s %(message)s'

# Create a massive crash report when IPython encounters what may be an internal
# error.  The default is to append a short message to the usual traceback
# c.NbConvertApp.verbose_crash = False

# Writer class used to write the  results of the conversion
# c.NbConvertApp.writer_class = 'FilesWriter'

# Whether to overwrite existing config files when copying
# c.NbConvertApp.overwrite = False

#------------------------------------------------------------------------------
# NbConvertBase configuration
#------------------------------------------------------------------------------

# Global configurable class for shared config
# 
# Usefull for display data priority that might be use by many trasnformers

# An ordered list of prefered output type, the first encounterd will usually be
# used when converting discarding the others.
# c.NbConvertBase.display_data_priority = ['html', 'pdf', 'svg', 'latex', 'png', 'jpg', 'jpeg', 'text']

#------------------------------------------------------------------------------
# ProfileDir configuration
#------------------------------------------------------------------------------

# An object to manage the profile directory and its resources.
# 
# The profile directory is used by all IPython applications, to manage
# configuration, logging and security.
# 
# This object knows how to find, create and manage these directories. This
# should be used by any code that wants to handle profiles.

# Set the profile location directly. This overrides the logic used by the
# `profile` option.
# c.ProfileDir.location = u''

#------------------------------------------------------------------------------
# Exporter configuration
#------------------------------------------------------------------------------

# Exports notebooks into other file formats.  Uses Jinja 2 templating engine to
# output new formats.  Inherit from this class if you are creating a new
# template type along with new filters/transformers.  If the filters/
# transformers provided by default suffice, there is no need to inherit from
# this class.  Instead, override the template_file and file_extension traits via
# a config file.
# 
# - highlight2html - filter_data_type - markdown2html - markdown2rst - get_lines
# - ansi2latex - strip_ansi - comment_lines - markdown2latex - escape_latex -
# add_anchor - ipython2python - posix_path - highlight2latex - path2url -
# ansi2html - wrap_text - strip_math_space - indent - strip_dollars - html2text
# - strip_files_prefix

# 
# c.Exporter.jinja_variable_block_start = ''

# 
# c.Exporter.jinja_logic_block_start = ''

# List of transformers, by name or namespace, to enable.
# c.Exporter.transformers = []

# 
# c.Exporter.template_path = ['.']

# Name of the template file to use
# c.Exporter.template_file = u'default'

# Extension of the file that should be written to disk
# c.Exporter.file_extension = 'txt'

# 
# c.Exporter.jinja_comment_block_end = ''

# Dictionary of filters, by name and namespace, to add to the Jinja environment.
# c.Exporter.filters = {}

# 
# c.Exporter.jinja_comment_block_start = ''

# 
# c.Exporter.jinja_logic_block_end = ''

# 
# c.Exporter.jinja_variable_block_end = ''

# 
# c.Exporter.template_extension = '.tpl'

# List of transformers available by default, by name, namespace,  instance, or
# type.
# c.Exporter.default_transformers = [<function wrappedfunc at 0x2b79ed8>, <class 'IPython.nbconvert.transformers.svg2pdf.SVG2PDFTransformer'>, <class 'IPython.nbconvert.transformers.extractoutput.ExtractOutputTransformer'>, <class 'IPython.nbconvert.transformers.csshtmlheader.CSSHTMLHeaderTransformer'>, <class 'IPython.nbconvert.transformers.revealhelp.RevealHelpTransformer'>, <class 'IPython.nbconvert.transformers.latex.LatexTransformer'>, <class 'IPython.nbconvert.transformers.sphinx.SphinxTransformer'>]

#------------------------------------------------------------------------------
# HTMLExporter configuration
#------------------------------------------------------------------------------

# Exports a basic HTML document.  This exporter assists with the export of HTML.
# Inherit from it if you are writing your own HTML template and need custom
# transformers/filters.  If you don't need custom transformers/ filters, just
# change the 'template_file' config option.

# HTMLExporter will inherit config from: Exporter

# 
# c.HTMLExporter.jinja_variable_block_start = ''

# 
# c.HTMLExporter.jinja_logic_block_start = ''

# List of transformers, by name or namespace, to enable.
# c.HTMLExporter.transformers = []

# 
# c.HTMLExporter.template_path = ['.']

# Name of the template file to use
# c.HTMLExporter.template_file = u'default'

# Extension of the file that should be written to disk
# c.HTMLExporter.file_extension = 'html'

# Flavor of the data  format to use.  I.E. 'full' or 'basic'
# c.HTMLExporter.default_template = 'full'

# 
# c.HTMLExporter.jinja_comment_block_end = ''

# Dictionary of filters, by name and namespace, to add to the Jinja environment.
# c.HTMLExporter.filters = {}

# 
# c.HTMLExporter.jinja_comment_block_start = ''

# 
# c.HTMLExporter.jinja_logic_block_end = ''

# 
# c.HTMLExporter.jinja_variable_block_end = ''

# 
# c.HTMLExporter.template_extension = '.tpl'

# List of transformers available by default, by name, namespace,  instance, or
# type.
# c.HTMLExporter.default_transformers = [<function wrappedfunc at 0x2b79ed8>, <class 'IPython.nbconvert.transformers.svg2pdf.SVG2PDFTransformer'>, <class 'IPython.nbconvert.transformers.extractoutput.ExtractOutputTransformer'>, <class 'IPython.nbconvert.transformers.csshtmlheader.CSSHTMLHeaderTransformer'>, <class 'IPython.nbconvert.transformers.revealhelp.RevealHelpTransformer'>, <class 'IPython.nbconvert.transformers.latex.LatexTransformer'>, <class 'IPython.nbconvert.transformers.sphinx.SphinxTransformer'>]

#------------------------------------------------------------------------------
# LatexExporter configuration
#------------------------------------------------------------------------------

# Exports to a Latex template.  Inherit from this class if your template is
# LaTeX based and you need custom tranformers/filters.  Inherit from it if  you
# are writing your own HTML template and need custom tranformers/filters.   If
# you don't need custom tranformers/filters, just change the  'template_file'
# config option.  Place your template in the special "/latex"  subfolder of the
# "../templates" folder.

# LatexExporter will inherit config from: Exporter

# 
# c.LatexExporter.jinja_variable_block_start = '((('

# 
# c.LatexExporter.jinja_logic_block_start = '((*'

# Path where the template skeleton files are located.
# c.LatexExporter.template_skeleton_path = '../templates/latex/skeleton'

# 
# c.LatexExporter.template_path = ['.']

# Name of the template file to use
# c.LatexExporter.template_file = u'default'

# Path where the template files are located.
# c.LatexExporter.default_template_path = '../templates/latex'

# Extension of the file that should be written to disk
# c.LatexExporter.file_extension = 'tex'

# Template of the  data format to use.  I.E. 'full' or 'basic'
# c.LatexExporter.default_template = 'article'

# 
# c.LatexExporter.jinja_comment_block_end = '=))'

# Dictionary of filters, by name and namespace, to add to the Jinja environment.
# c.LatexExporter.filters = {}

# 
# c.LatexExporter.jinja_comment_block_start = '((='

# List of transformers, by name or namespace, to enable.
# c.LatexExporter.transformers = []

# 
# c.LatexExporter.jinja_logic_block_end = '*))'

# 
# c.LatexExporter.jinja_variable_block_end = ')))'

# 
# c.LatexExporter.template_extension = '.tplx'

# List of transformers available by default, by name, namespace,  instance, or
# type.
# c.LatexExporter.default_transformers = [<function wrappedfunc at 0x2b79ed8>, <class 'IPython.nbconvert.transformers.svg2pdf.SVG2PDFTransformer'>, <class 'IPython.nbconvert.transformers.extractoutput.ExtractOutputTransformer'>, <class 'IPython.nbconvert.transformers.csshtmlheader.CSSHTMLHeaderTransformer'>, <class 'IPython.nbconvert.transformers.revealhelp.RevealHelpTransformer'>, <class 'IPython.nbconvert.transformers.latex.LatexTransformer'>, <class 'IPython.nbconvert.transformers.sphinx.SphinxTransformer'>]

#------------------------------------------------------------------------------
# MarkdownExporter configuration
#------------------------------------------------------------------------------

# Exports to a markdown document (.md)

# MarkdownExporter will inherit config from: Exporter

# 
# c.MarkdownExporter.jinja_variable_block_start = ''

# 
# c.MarkdownExporter.jinja_logic_block_start = ''

# List of transformers, by name or namespace, to enable.
# c.MarkdownExporter.transformers = []

# 
# c.MarkdownExporter.template_path = ['.']

# Name of the template file to use
# c.MarkdownExporter.template_file = u'default'

# Extension of the file that should be written to disk
# c.MarkdownExporter.file_extension = 'md'

# 
# c.MarkdownExporter.jinja_comment_block_end = ''

# Dictionary of filters, by name and namespace, to add to the Jinja environment.
# c.MarkdownExporter.filters = {}

# 
# c.MarkdownExporter.jinja_comment_block_start = ''

# 
# c.MarkdownExporter.jinja_logic_block_end = ''

# 
# c.MarkdownExporter.jinja_variable_block_end = ''

# 
# c.MarkdownExporter.template_extension = '.tpl'

# List of transformers available by default, by name, namespace,  instance, or
# type.
# c.MarkdownExporter.default_transformers = [<function wrappedfunc at 0x2b79ed8>, <class 'IPython.nbconvert.transformers.svg2pdf.SVG2PDFTransformer'>, <class 'IPython.nbconvert.transformers.extractoutput.ExtractOutputTransformer'>, <class 'IPython.nbconvert.transformers.csshtmlheader.CSSHTMLHeaderTransformer'>, <class 'IPython.nbconvert.transformers.revealhelp.RevealHelpTransformer'>, <class 'IPython.nbconvert.transformers.latex.LatexTransformer'>, <class 'IPython.nbconvert.transformers.sphinx.SphinxTransformer'>]

#------------------------------------------------------------------------------
# PythonExporter configuration
#------------------------------------------------------------------------------

# Exports a Python code file.

# PythonExporter will inherit config from: Exporter

# 
# c.PythonExporter.jinja_variable_block_start = ''

# 
# c.PythonExporter.jinja_logic_block_start = ''

# List of transformers, by name or namespace, to enable.
# c.PythonExporter.transformers = []

# 
# c.PythonExporter.template_path = ['.']

# Name of the template file to use
# c.PythonExporter.template_file = u'default'

# Extension of the file that should be written to disk
# c.PythonExporter.file_extension = 'py'

# 
# c.PythonExporter.jinja_comment_block_end = ''

# Dictionary of filters, by name and namespace, to add to the Jinja environment.
# c.PythonExporter.filters = {}

# 
# c.PythonExporter.jinja_comment_block_start = ''

# 
# c.PythonExporter.jinja_logic_block_end = ''

# 
# c.PythonExporter.jinja_variable_block_end = ''

# 
# c.PythonExporter.template_extension = '.tpl'

# List of transformers available by default, by name, namespace,  instance, or
# type.
# c.PythonExporter.default_transformers = [<function wrappedfunc at 0x2b79ed8>, <class 'IPython.nbconvert.transformers.svg2pdf.SVG2PDFTransformer'>, <class 'IPython.nbconvert.transformers.extractoutput.ExtractOutputTransformer'>, <class 'IPython.nbconvert.transformers.csshtmlheader.CSSHTMLHeaderTransformer'>, <class 'IPython.nbconvert.transformers.revealhelp.RevealHelpTransformer'>, <class 'IPython.nbconvert.transformers.latex.LatexTransformer'>, <class 'IPython.nbconvert.transformers.sphinx.SphinxTransformer'>]

#------------------------------------------------------------------------------
# RSTExporter configuration
#------------------------------------------------------------------------------

# Exports restructured text documents.

# RSTExporter will inherit config from: Exporter

# 
# c.RSTExporter.jinja_variable_block_start = ''

# 
# c.RSTExporter.jinja_logic_block_start = ''

# List of transformers, by name or namespace, to enable.
# c.RSTExporter.transformers = []

# 
# c.RSTExporter.template_path = ['.']

# Name of the template file to use
# c.RSTExporter.template_file = u'default'

# Extension of the file that should be written to disk
# c.RSTExporter.file_extension = 'rst'

# 
# c.RSTExporter.jinja_comment_block_end = ''

# Dictionary of filters, by name and namespace, to add to the Jinja environment.
# c.RSTExporter.filters = {}

# 
# c.RSTExporter.jinja_comment_block_start = ''

# 
# c.RSTExporter.jinja_logic_block_end = ''

# 
# c.RSTExporter.jinja_variable_block_end = ''

# 
# c.RSTExporter.template_extension = '.tpl'

# List of transformers available by default, by name, namespace,  instance, or
# type.
# c.RSTExporter.default_transformers = [<function wrappedfunc at 0x2b79ed8>, <class 'IPython.nbconvert.transformers.svg2pdf.SVG2PDFTransformer'>, <class 'IPython.nbconvert.transformers.extractoutput.ExtractOutputTransformer'>, <class 'IPython.nbconvert.transformers.csshtmlheader.CSSHTMLHeaderTransformer'>, <class 'IPython.nbconvert.transformers.revealhelp.RevealHelpTransformer'>, <class 'IPython.nbconvert.transformers.latex.LatexTransformer'>, <class 'IPython.nbconvert.transformers.sphinx.SphinxTransformer'>]

#------------------------------------------------------------------------------
# SlidesExporter configuration
#------------------------------------------------------------------------------

# Exports slides

# SlidesExporter will inherit config from: Exporter

# 
# c.SlidesExporter.jinja_variable_block_start = ''

# 
# c.SlidesExporter.jinja_logic_block_start = ''

# List of transformers, by name or namespace, to enable.
# c.SlidesExporter.transformers = []

# 
# c.SlidesExporter.template_path = ['.']

# Name of the template file to use
# c.SlidesExporter.template_file = u'default'

# Extension of the file that should be written to disk
# c.SlidesExporter.file_extension = 'slides.html'

# Template of the  data format to use.  I.E. 'reveal'
# c.SlidesExporter.default_template = 'reveal'

# 
# c.SlidesExporter.jinja_comment_block_end = ''

# Dictionary of filters, by name and namespace, to add to the Jinja environment.
# c.SlidesExporter.filters = {}

# 
# c.SlidesExporter.jinja_comment_block_start = ''

# 
# c.SlidesExporter.jinja_logic_block_end = ''

# 
# c.SlidesExporter.jinja_variable_block_end = ''

# 
# c.SlidesExporter.template_extension = '.tpl'

# List of transformers available by default, by name, namespace,  instance, or
# type.
# c.SlidesExporter.default_transformers = [<function wrappedfunc at 0x2b79ed8>, <class 'IPython.nbconvert.transformers.svg2pdf.SVG2PDFTransformer'>, <class 'IPython.nbconvert.transformers.extractoutput.ExtractOutputTransformer'>, <class 'IPython.nbconvert.transformers.csshtmlheader.CSSHTMLHeaderTransformer'>, <class 'IPython.nbconvert.transformers.revealhelp.RevealHelpTransformer'>, <class 'IPython.nbconvert.transformers.latex.LatexTransformer'>, <class 'IPython.nbconvert.transformers.sphinx.SphinxTransformer'>]

#------------------------------------------------------------------------------
# CSSHTMLHeaderTransformer configuration
#------------------------------------------------------------------------------

# Transformer used to pre-process notebook for HTML output.  Adds IPython
# notebook front-end CSS and Pygments CSS to HTML output.

# CSSHTMLHeaderTransformer will inherit config from: Transformer, NbConvertBase

# An ordered list of prefered output type, the first encounterd will usually be
# used when converting discarding the others.
# c.CSSHTMLHeaderTransformer.display_data_priority = ['html', 'pdf', 'svg', 'latex', 'png', 'jpg', 'jpeg', 'text']

# CSS highlight class identifier
# c.CSSHTMLHeaderTransformer.highlight_class = '.highlight'

# 
# c.CSSHTMLHeaderTransformer.enabled = False

#------------------------------------------------------------------------------
# ConvertFiguresTransformer configuration
#------------------------------------------------------------------------------

# Converts all of the outputs in a notebook from one format to another.

# ConvertFiguresTransformer will inherit config from: Transformer, NbConvertBase

# An ordered list of prefered output type, the first encounterd will usually be
# used when converting discarding the others.
# c.ConvertFiguresTransformer.display_data_priority = ['html', 'pdf', 'svg', 'latex', 'png', 'jpg', 'jpeg', 'text']

# Format the converter writes
# c.ConvertFiguresTransformer.to_format = u''

# 
# c.ConvertFiguresTransformer.enabled = False

# Format the converter accepts
# c.ConvertFiguresTransformer.from_format = u''

#------------------------------------------------------------------------------
# ExtractOutputTransformer configuration
#------------------------------------------------------------------------------

# Extracts all of the outputs from the notebook file.  The extracted  outputs
# are returned in the 'resources' dictionary.

# ExtractOutputTransformer will inherit config from: Transformer, NbConvertBase

# An ordered list of prefered output type, the first encounterd will usually be
# used when converting discarding the others.
# c.ExtractOutputTransformer.display_data_priority = ['html', 'pdf', 'svg', 'latex', 'png', 'jpg', 'jpeg', 'text']

# 
# c.ExtractOutputTransformer.output_filename_template = '{unique_key}_{cell_index}_{index}.{extension}'

# 
# c.ExtractOutputTransformer.enabled = False

#------------------------------------------------------------------------------
# LatexTransformer configuration
#------------------------------------------------------------------------------

# Converter for latex destined documents.

# LatexTransformer will inherit config from: Transformer, NbConvertBase

# An ordered list of prefered output type, the first encounterd will usually be
# used when converting discarding the others.
# c.LatexTransformer.display_data_priority = ['html', 'pdf', 'svg', 'latex', 'png', 'jpg', 'jpeg', 'text']

# 
# c.LatexTransformer.enabled = False

#------------------------------------------------------------------------------
# RevealHelpTransformer configuration
#------------------------------------------------------------------------------

# RevealHelpTransformer will inherit config from: Transformer, NbConvertBase

# If you want to use a local reveal.js library, use 'url_prefix':'reveal.js' in
# your config object.
# c.RevealHelpTransformer.url_prefix = '//cdn.jsdelivr.net/reveal.js/2.4.0'

# An ordered list of prefered output type, the first encounterd will usually be
# used when converting discarding the others.
# c.RevealHelpTransformer.display_data_priority = ['html', 'pdf', 'svg', 'latex', 'png', 'jpg', 'jpeg', 'text']

# 
# c.RevealHelpTransformer.enabled = False

#------------------------------------------------------------------------------
# SVG2PDFTransformer configuration
#------------------------------------------------------------------------------

# Converts all of the outputs in a notebook from SVG to PDF.

# SVG2PDFTransformer will inherit config from: ConvertFiguresTransformer,
# Transformer, NbConvertBase

# The command to use for converting SVG to PDF
# 
# This string is a template, which will be formatted with the keys to_filename
# and from_filename.
# 
# The conversion call must read the SVG from {from_flename}, and write a PDF to
# {to_filename}.
# c.SVG2PDFTransformer.command = u''

# 
# c.SVG2PDFTransformer.enabled = False

# Format the converter accepts
# c.SVG2PDFTransformer.from_format = 'svg'

# The path to Inkscape, if necessary
# c.SVG2PDFTransformer.inkscape = u''

# An ordered list of prefered output type, the first encounterd will usually be
# used when converting discarding the others.
# c.SVG2PDFTransformer.display_data_priority = ['html', 'pdf', 'svg', 'latex', 'png', 'jpg', 'jpeg', 'text']

#------------------------------------------------------------------------------
# SphinxTransformer configuration
#------------------------------------------------------------------------------

# Sphinx utility transformer.
# 
# This transformer is used to set variables needed by the latex to build Sphinx
# stylized templates.

# SphinxTransformer will inherit config from: Transformer, NbConvertBase

# Nbconvert Ipython
# notebook input/output formatting style.
# You may choose one of the following:
#     "simple     (recommended for long code segments)"
#     "notebook"  (default)
# c.SphinxTransformer.output_style = 'notebook'

# Author name
# c.SphinxTransformer.author = 'Unknown Author'

# 
# c.SphinxTransformer.enabled = False

# Sphinx chapter style
# This is the style to use for the chapter headers in the document.
# You may choose one of the following:
#     "Bjarne"    (default)
#     "Lenny"
#     "Glenn"
#     "Conny"
#     "Rejne"
#     "Sonny"    (used for international documents)
# c.SphinxTransformer.chapter_style = 'Bjarne'

# Version number You can leave this blank if you do not want to render a version
# number. Example: "1.0.0"
# c.SphinxTransformer.version = ''

# Publish date This is the date to render on the document as the publish date.
# Leave this blank to default to todays date.   Example: "June 12, 1990"
# c.SphinxTransformer.publish_date = ''

# An ordered list of prefered output type, the first encounterd will usually be
# used when converting discarding the others.
# c.SphinxTransformer.display_data_priority = ['html', 'pdf', 'svg', 'latex', 'png', 'jpg', 'jpeg', 'text']

# Release name You can leave this blank if you do not want to render a release
# name. Example: "Rough Draft"
# c.SphinxTransformer.release = ''

# Whether not a header should be added to the document.
# c.SphinxTransformer.use_headers = True

# Allows you to define whether or not the Sphinx exporter will prompt you for
# input during the conversion process.  If this is set to false, the author,
# version, release, date, and chapter_style traits should be set.
# c.SphinxTransformer.interactive = False

# Optional attempt to center all output.  If this is false, no additional
# formatting is applied.
# c.SphinxTransformer.center_output = False

# 
# c.SphinxTransformer.overridetitle = ''

#------------------------------------------------------------------------------
# Transformer configuration
#------------------------------------------------------------------------------

# A configurable transformer
# 
# Inherit from this class if you wish to have configurability for your
# transformer.
# 
# Any configurable traitlets this class exposed will be configurable in profiles
# using c.SubClassName.atribute=value
# 
# you can overwrite :meth:`transform_cell` to apply a transformation
# independently on each cell or :meth:`call` if you prefer your own logic. See
# corresponding docstring for informations.
# 
# Disabled by default and can be enabled via the config by
#     'c.YourTransformerName.enabled = True'

# Transformer will inherit config from: NbConvertBase

# An ordered list of prefered output type, the first encounterd will usually be
# used when converting discarding the others.
# c.Transformer.display_data_priority = ['html', 'pdf', 'svg', 'latex', 'png', 'jpg', 'jpeg', 'text']

# 
# c.Transformer.enabled = False

#------------------------------------------------------------------------------
# FilesWriter configuration
#------------------------------------------------------------------------------

# Consumes nbconvert output and produces files.

# FilesWriter will inherit config from: WriterBase, NbConvertBase

# List of the files that the notebook references.  Files will be  included with
# written output.
# c.FilesWriter.files = []

# An ordered list of prefered output type, the first encounterd will usually be
# used when converting discarding the others.
# c.FilesWriter.display_data_priority = ['html', 'pdf', 'svg', 'latex', 'png', 'jpg', 'jpeg', 'text']

# Directory to write output to.  Leave blank to output to the current directory
# c.FilesWriter.build_directory = ''

#------------------------------------------------------------------------------
# StdoutWriter configuration
#------------------------------------------------------------------------------

# Consumes output from nbconvert export...() methods and writes to the  stdout
# stream.

# StdoutWriter will inherit config from: WriterBase, NbConvertBase

# List of the files that the notebook references.  Files will be  included with
# written output.
# c.StdoutWriter.files = []

# An ordered list of prefered output type, the first encounterd will usually be
# used when converting discarding the others.
# c.StdoutWriter.display_data_priority = ['html', 'pdf', 'svg', 'latex', 'png', 'jpg', 'jpeg', 'text']

#------------------------------------------------------------------------------
# WriterBase configuration
#------------------------------------------------------------------------------

# Consumes output from nbconvert export...() methods and writes to a useful
# location.

# WriterBase will inherit config from: NbConvertBase

# List of the files that the notebook references.  Files will be  included with
# written output.
# c.WriterBase.files = []

# An ordered list of prefered output type, the first encounterd will usually be
# used when converting discarding the others.
# c.WriterBase.display_data_priority = ['html', 'pdf', 'svg', 'latex', 'png', 'jpg', 'jpeg', 'text']
