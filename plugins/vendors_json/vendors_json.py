import json
from pathlib import Path
from pelican import signals
from bs4 import BeautifulSoup

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
    
    # Check if we have a template tag for vendors table
    if '{% for vendor in vendors %}' in page_content:
        # Parse the content as HTML
        soup = BeautifulSoup(page_content, 'html.parser')
        
        # Find the sortable table
        table = soup.find('table', class_='sortable')
        
        if table:
            # Keep the thead section
            thead = table.find('thead')
            
            # Clear tbody and rebuild it with actual vendor data
            tbody = table.find('tbody')
            if tbody:
                tbody.clear()
            else:
                tbody = soup.new_tag('tbody')
                table.append(tbody)
            
            # Get vendors from content._context (populated by add_vendors_to_context)
            vendors = content._context.get('vendors', [])
            
            # Add rows for each vendor
            for vendor in vendors:
                name = vendor.get('name', '')
                url = vendor.get('url', '')
                reason = vendor.get('reason', '')
                updated_at = vendor.get('updated_at', '')
                
                # Create row and cells
                tr = soup.new_tag('tr')
                
                # Vendor name cell with link
                td_name = soup.new_tag('td')
                a = soup.new_tag('a', href=url)
                a.string = name
                td_name.append(a)
                
                # Reason cell
                td_reason = soup.new_tag('td')
                td_reason.string = reason
                
                # Date cell
                td_date = soup.new_tag('td')
                td_date.string = updated_at
                
                # Add cells to row
                tr.append(td_name)
                tr.append(td_reason)
                tr.append(td_date)
                
                # Add row to tbody
                tbody.append(tr)
            
            # Replace the content with processed HTML
            content._content = str(soup)

def register():
    """Register the plugin with Pelican"""
    signals.generator_init.connect(add_vendors_to_context)
    signals.page_generator_finalized.connect(process_content_for_pages)

def process_content_for_pages(generator):
    for page in generator.pages:
        process_content(page)