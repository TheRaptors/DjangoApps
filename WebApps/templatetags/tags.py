#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import template
from django.template.base import Node, TemplateSyntaxError

#register = Templates.Library()
register = template.Library()

@register.simple_tag
def MyMethod(v1):
    return v1 * 100
