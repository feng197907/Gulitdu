import xadmin
from users.models import BannerInfo, EmailVerifyDode


class BannerInfoXadmin(object):
    list_display = ['image', 'url', 'title', 'create_time']
    # 搜索框
    search_fields = ['title']
    # 过滤器
    list_filter = ['image', 'url']


class EmailVerifyDodeXadmin(object):
    list_display = ['code', 'email', 'send_type', 'create_time']
    search_fields = ['code', 'email']


xadmin.site.register(BannerInfo, BannerInfoXadmin)
xadmin.site.register(EmailVerifyDode, EmailVerifyDodeXadmin)
