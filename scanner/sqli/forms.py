### forms.py

# Handles form extraction from HTML content
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def extract_forms(html_content, base_url):
    """
    Extract all forms from the given HTML content.

    Args:
        html_content (str): HTML content of the page.
        base_url (str): Base URL to resolve relative form action URLs.

    Returns:
        list: A list of dictionaries containing form details.
    """
    soup = BeautifulSoup(html_content, "html.parser")
    forms = []
    for form in soup.find_all("form"):
        form_details = {}
        action = form.attrs.get("action")
        method = form.attrs.get("method", "get").lower()
        action = urljoin(base_url, action) if action else base_url
        inputs = []
        for input_tag in form.find_all(["input", "textarea"]):
            input_type = input_tag.attrs.get("type", "text")
            name = input_tag.attrs.get("name")
            value = input_tag.attrs.get("value", "")
            inputs.append({"type": input_type, "name": name, "value": value})
        form_details["action"] = action
        form_details["method"] = method
        form_details["inputs"] = inputs
        forms.append(form_details)
    return forms
