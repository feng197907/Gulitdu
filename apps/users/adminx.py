import xadmin
from users.models import BannerInfo, EmailVerifyDode
from xadmin import views


# 配置xadmin主题,注册的时候要用到专用的view去注册
class BaseXadminSetting(object):
    enable_themes = True
    use_bootswatch = True


class CommXadminSetting(object):
    site_title = '谷粒教育后台管理系统'
    site_footer = '尚硅谷it教育'
    menu_style = 'accordion'


class BannerInfoXadmin(object):
    list_display = ['image', 'url', 'title', 'create_time']
    # 搜索框
    search_fields = ['title']
    # 过滤器
    list_filter = ['image', 'url']
    model_icon = 'fa fa-random'


class EmailVerifyDodeXadmin(object):
    list_display = ['code', 'email', 'send_type', 'create_time']
    search_fields = ['code', 'email']
    model_icon = 'fa fa-envelope-open'


xadmin.site.register(BannerInfo, BannerInfoXadmin)
xadmin.site.register(EmailVerifyDode, EmailVerifyDodeXadmin)
# 注册主题类
xadmin.site.register(views.BaseAdminView, BaseXadminSetting)
# 注册全局样式的类
xadmin.site.register(views.CommAdminView, CommXadminSetting)
