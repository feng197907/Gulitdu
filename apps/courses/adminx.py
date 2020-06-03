import xadmin
from courses.models import CoursesInfo, LessonInfo, VideoInfo, SourceInfo
# 课程模型类
class CoursesInfoXadmin(object):
    list_display = ['image', 'courses_name', 'courses_time', 'study_num', 'level', 'desc', 'orginfo', 'teacherinfo', 'create_time']
    model_icon = 'fa fa-book'

# 章节模型类
class LessonInfoXadmin(object):
    list_display = ['name', 'coursesinfo', 'create_time']
    model_icon = 'fa fa-bars'

# 视频模型类
class VideoInfoXadmin(object):
    list_display = ['name', 'study_time', 'url','lessoninfo', 'create_time']
    model_icon = 'fa fa-video-camera'

# 资源模型类
class SourceInfoXadmin(object):
    list_display = ['name', 'down_load', 'courseinfo', 'create_time']
    model_icon = 'fa fa-download'

xadmin.site.register(CoursesInfo, CoursesInfoXadmin)
xadmin.site.register(LessonInfo, LessonInfoXadmin)
xadmin.site.register(VideoInfo, VideoInfoXadmin)
xadmin.site.register(SourceInfo, SourceInfoXadmin)

