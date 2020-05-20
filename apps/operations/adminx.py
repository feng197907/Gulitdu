import xadmin
from operations.models import UserAsk, UserLove, UserCourse, UserComment, UserMessage


# 用户咨询模型类
class UserAskXadmin(object):
    list_display = ['name', 'phone', 'course', 'create_time']


# 用户收藏模型类
class UserLoveXadmin(object):
    list_display = ['love_man', 'love_type', 'love_status', 'create_time']


# 用户课程模型类
class UserCourseXadmin(object):
    list_display = ['study_man', 'study_course', 'create_time']


# 用户评论模型类
class UserCommentXadmin(object):
    list_display = ['comment_man', 'comment_course', 'comment_content', 'create_time']


# 用户消息模型类
class UserMessageXadmin(object):
    list_display = ['message_man', 'message_content', 'message_status', 'create_time']


xadmin.site.register(UserAsk, UserAskXadmin)
xadmin.site.register(UserLove, UserLoveXadmin)
xadmin.site.register(UserCourse, UserCourseXadmin)
xadmin.site.register(UserComment, UserCommentXadmin)
xadmin.site.register(UserMessage, UserMessageXadmin)
