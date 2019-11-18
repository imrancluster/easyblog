import abc

from django.db import connection
from django.utils.datetime_safe import datetime
from django.utils.translation import ugettext_lazy as _
from jet.dashboard.modules import DashboardModule



# from people.models import Doctor, Patient

# from products.models import GenericTherapy, Therapy, Manufacturer
# from records.models import AdverseEvent
from esayblog.models import BlogPost


class RecentBlogPosts(DashboardModule):
    title = 'Recent Adverse Events'
    template = 'dashboard_modules/recent_blog_posts.html'
    limit = 5

    def init_with_context(self, context):
        self.children = BlogPost.objects.select_related('category').order_by('-created_at')[:self.limit]
