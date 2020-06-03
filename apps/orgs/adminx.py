import xadmin
from orgs.models import CityInfo, OrgInfo, TeacherInfo


# 城市模型类.
class CityInfoXadmin(object):
    list_display = ['name', 'create_time']
    model_icon = 'fa fa-map'

# 机构模型类
class OrgInfoXadmin(object):
    list_display = ['image', 'name', 'course_num', 'study_num', 'address', 'desc', 'detail', 'love_num', 'click_num',
                    'category', 'cityinfo', 'create_time']
    model_icon = 'fa fa-graduation-cap'

# 教师模型类
class TeacherInfoXadmin(object):
    list_display = ['image', 'name', 'auth', 'work_year', 'work_position', 'work_company', 'age', 'work_style',
                    'gender',
                    'love_num', 'click_num', 'create_time']
    model_icon = 'fa fa-user-circle'


xadmin.site.register(CityInfo, CityInfoXadmin)
xadmin.site.register(OrgInfo, OrgInfoXadmin)
xadmin.site.register(TeacherInfo, TeacherInfoXadmin)
