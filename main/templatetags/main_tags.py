from django import template
from operator import itemgetter

register = template.Library()
@register.filter(name='mul')
def mul(value, arg):
    return value * arg

@register.filter(name='div')
def div(value, arg):
    return value - arg

@register.filter
def sortleague(value):
    return reversed(sorted(value, key=lambda k: (k.points, k.goals_scored-k.goals_lost, k.goals_scored)))
