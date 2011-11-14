##### Here is the template tag code. It goes in a file named
# "event_tags.py" in a subdirectory of your app called "templatetags".
#####

from calendar import HTMLCalendar
from django import template
from datetime import *
from itertools import groupby
import pdb
from django.utils.html import conditional_escape as esc
from blogserver.apps.blog.models import Post
register = template.Library()

def do_event_calendar(parser, token):
    """
    The template tag's syntax is {% event_calendar year month event_list %}
    """

    try:
        #tag_name, year, month, event_list = token.split_contents()
        tag_name= token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires three arguments" % token.contents.split()[0]
    #return EventCalendarNode(year, month, event_list)
    return EventCalendarNode()


class EventCalendarNode(template.Node):
    """
    Process a particular node in the template. Fail silently.
    """

    def __init__(self,):
        try:
            lToday = datetime.now()
            #self.year = template.Variable(year)
            #self.month = template.Variable(month)
            self.year = lToday.year
            self.month = lToday.month
            my_events = Post.objects.filter(date_published__year=self.year, date_published__month=self.month)
            #self.event_list = template.Variable(event_list)
            self.event_list = my_events
        except ValueError:
            raise template.TemplateSyntaxError

    def render(self, context):
        try:
            # Get the variables from the context so the method is thread-safe.
            #my_event_list = self.event_list.resolve(context)
            #my_year = self.year.resolve(context)
            #my_month = self.month.resolve(context)
            my_event_list = self.event_list
            my_year = self.year
            #pdb.set_trace()
            my_month = self.month
            cal = EventCalendar(my_event_list)
            return cal.formatmonth(int(my_year), int(my_month))
        except ValueError:
            return         
        except template.VariableDoesNotExist:
            return


class EventCalendar(HTMLCalendar):
    """
    Overload Python's calendar.HTMLCalendar to add the appropriate events to
    each day's table cell.
    """

    def __init__(self, events):
        super(EventCalendar, self).__init__()
        self.events = self.group_by_day(events)

    def formatday(self, day, weekday):
        if day != 0:
            cssclass = self.cssclasses[weekday]
            if date.today() == date(self.year, self.month, day):
                cssclass += ' today'
            if day in self.events:
                cssclass += ' filled'
                href="/%d/%02d/%02d/"%(self.year,self.month,day)
                return self.day_cell(cssclass, '<span class="dayNumber" title="click to view post"><a href=%s >%d</a></span>' % (href,day))
            return self.day_cell(cssclass, '<span class="dayNumberNoEvents">%d</span>' % (day))
        return self.day_cell('noday', '&nbsp;')

    def formatmonth(self, year, month):
        self.year, self.month = year, month
        return super(EventCalendar, self).formatmonth(year, month)

    def group_by_day(self, events):
        field = lambda event: event.date_published.day
        return dict(
            [(day, list(items)) for day, items in groupby(events, field)]
        )

    def day_cell(self, cssclass, body):
        return '<td class="%s">%s</td>' % (cssclass, body)

# Register the template tag so it is available to templates
register.tag("event_calendar", do_event_calendar)


