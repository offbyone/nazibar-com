from pathlib import Path

AUTHOR = "Chris R"
SITENAME = "Nazi Bar List"
SITEURL = ""

# Use absolute paths to avoid issues
base_path = Path(__file__).resolve().parent

PATH = "content"
PLUGIN_PATHS = ["plugins"]
PLUGINS = ["vendors_json", "webassets"]

# Webassets configuration
WEBASSETS = True

WEBASSETS_SOURCE_PATHS = [
    str(base_path / "node_modules"),
    str(base_path / "node_modules" / "sorttable"),
]

TIMEZONE = "America/Los_Angeles"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
)

# Social widget
SOCIAL = (("GitHub", "https://github.com/offbyone/nazibar-com"),)

DEFAULT_PAGINATION = 10

# Theme
THEME = "themes/nazibar"
# Theme style (options: cyber, red, brutalist)
SITE_THEME = "brutalist"

# Static paths
STATIC_PATHS = ["images", "assets"]

# Page settings
PAGE_PATHS = ["pages"]
ARTICLE_PATHS = ["articles"]

# URL settings
PAGE_URL = "{slug}.html"
PAGE_SAVE_AS = "{slug}.html"
INDEX_SAVE_AS = "index.html"
