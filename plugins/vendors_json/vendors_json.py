import json
import os
from pathlib import Path
from pelican import signals
import re

def add_vendors_to_context(generator):
    """
    Add vendors data from vendors.json to the template context
    """
    # Get the project root directory (parent of content directory)
    vendors_path = Path(generator.settings.get('PATH')).parent / 'vendors.json'
    
    if vendors_path.exists():
        with open(vendors_path, 'r') as f:
            vendors_data = json.load(f)
            generator.context['vendors'] = vendors_data.get('vendors', [])
            print(f"Loaded {len(generator.context['vendors'])} vendors from vendors.json")
    else:
        print(f"Warning: vendors.json file not found at {vendors_path}")

def process_content(content):
    """
    Process Jinja2-like template tags in content
    """
    if not hasattr(content, '_content'):
        return

    page_content = content._content
    
    # Simple table replacement for our specific case
    # Find the table section
    table_pattern = r'<table class="sortable">.*?<tbody>\s*{% for vendor in vendors %}.*?{% endfor %}\s*</tbody>\s*</table>'
    table_match = re.search(table_pattern, page_content, re.DOTALL)
    
    if table_match:
        table_html = table_match.group(0)
        table_start = '<table class="sortable">\n<thead>\n<tr><th>Vendor</th><th>Why?</th><th>Date Updated</th></tr>\n</thead>\n<tbody>'
        table_end = '</tbody>\n</table>'
        
        rows_html = ""
        
        # Get vendors from content._context (populated by add_vendors_to_context)
        vendors = content._context.get('vendors', [])
        
        for vendor in vendors:
            name = vendor.get('name', '')
            url = vendor.get('url', '')
            reason = vendor.get('reason', '')
            updated_at = vendor.get('updated_at', '')
            
            row = f'<tr>\n<td><a href="{url}">{name}</a></td>\n<td>{reason}</td>\n<td>{updated_at}</td>\n</tr>'
            rows_html += row
        
        new_table = table_start + rows_html + table_end
        page_content = page_content.replace(table_match.group(0), new_table)
        
        content._content = page_content

def register():
    """Register the plugin with Pelican"""
    signals.generator_init.connect(add_vendors_to_context)
    signals.page_generator_finalized.connect(process_content_for_pages)

def process_content_for_pages(generator):
    for page in generator.pages:
        process_content(page)