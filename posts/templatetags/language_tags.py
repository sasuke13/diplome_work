from django import template
from django.urls import resolve

register = template.Library()

@register.simple_tag(takes_context=True)
def change_language_url(context):
    """
    Returns the URL for the current page in the opposite language
    by adding/removing 'EN' from the path
    """
    try:
        # Get current path
        path = context['request'].path
        
        # If we're on an English page (has 'EN' in path)
        if '/en/' in path:
            return path.replace('/en/', '/')
        
        # If we're on a Ukrainian page (no 'EN' in path)
        else:
            # Split the path and insert 'EN'
            parts = path.split('/')
            # Insert 'EN' after the first slash
            parts.insert(1, 'en')
            return '/'.join(parts)
            
    except Exception:
        return '/'

@register.simple_tag(takes_context=True)
def change_language_url_lowercase(context):
    """
    Returns the URL for the current page in the opposite language
    by adding/removing 'en' from the path
    """
    try:
        # Get current path
        path = context['request'].path
        
        # If we're on an English page (has 'en' in path)
        if '/en/' in path:
            return path.replace('/en/', '/')
        
        # If we're on a Ukrainian page (no 'en' in path)
        else:
            # Split the path and insert 'en'
            parts = path.split('/')
            # Insert 'en' after the first slash
            parts.insert(1, 'en')
            return '/'.join(parts)
            
    except Exception:
        return '/' 