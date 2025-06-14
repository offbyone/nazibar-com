import os
from pelican import signals
from pelican.readers import MarkdownReader
from pelican.utils import pelican_open
from jinja2 import Environment, FileSystemLoader, Template

class JinjaMarkdownReader(MarkdownReader):
    """
    Extends the MarkdownReader to render the Markdown content as a Jinja2 template.
    """
    def __init__(self, *args, **kwargs):
        super(JinjaMarkdownReader, self).__init__(*args, **kwargs)
        self.env = Environment(loader=FileSystemLoader(os.path.dirname(__file__)))

    def read(self, source_path):
        """
        Parse content and metadata from the given file path.
        First, render the Jinja2 template, then parse it as Markdown.
        """
        self._source_path = source_path
        self._md = self.process_metadata('markdown')

        with pelican_open(source_path) as text:
            # Render the Jinja2 template with the Pelican context
            template = Template(text)
            rendered_content = template.render(**self._context)
            
            # Parse the rendered content as Markdown
            content = self._md.convert(rendered_content)

        metadata = self._parse_metadata(self._md.Meta)
        return content, metadata