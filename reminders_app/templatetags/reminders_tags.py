from django import template
from django.shortcuts import reverse

register = template.Library()


@register.simple_tag(takes_context=True)
def active_link(context, link_url):
    print(link_url)
    current_url = context['request'].path
    print(current_url)

    if current_url == link_url:
        return "active-link"
    else:
        return ""
