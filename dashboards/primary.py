from django.utils.translation import ugettext_lazy as _
from jet.dashboard import modules
from jet.dashboard.dashboard import Dashboard

from dashboards.modules import RecentBlogPosts

# It will be added in the widgets
class CustomIndexDashboard(Dashboard):
    columns = 2

    def init_with_context(self, context):
        self.available_children.append(modules.LinkList)
        self.children.append(RecentBlogPosts())
