from flask_restful import Api

from App.apis.AdminApi import AdminApiResource, AdminApiResource1
from App.apis.BuApi import BuResource, BuResource1
from App.apis.DealerActiApi import DealerActiApi4, DealerActiApi3, DealerActiApi2, DealerActiApi1, DealerActiApi5
from App.apis.DealerLbtApi import DealerLbtApi, DealerLbtApi1, DealerLbtApi2
from App.apis.DealerTrainApi import DealerTrainResource, DealerTrainResource1
from App.apis.ExperienceApi import ExperienceResource, ExperienceResource1, ExperienceResource2, ExperienceResource3
from App.apis.FaqApi import FaqResource, FaqChanceResource
from App.apis.GratStarApi import GratStarResource
from App.apis.GratitudeApi import GratitudeResource, GratitudeResource1, GratitudeResource2, GratitudeResource3, \
    GratitudeResource4, GratitudeResource5
from App.apis.HotMsgApi import HotMsgResource
from App.apis.LecturerApi import LecturerResource
from App.apis.LesCommentApi import LesCommentResource, LesCommentResource1, LesCommentResource2, LesCommentResource3
from App.apis.LessonApi import LessonResource, LessonResource1, LessonResource2, LessonResource3, LessonResource4
from App.apis.LessonClasApi import LessonClasResource, LessonClasResource1
from App.apis.LoginNumberApi import LoginNumber
from App.apis.LsnCollectionApi import LsnCollectionResource, LsnCollectionResource1, LsnCollectionResource2, \
    LsnCollectionResource3
from App.apis.LsnThumbApi import LsnThumbResource, LsnThumbResource1, LsnThumbResource2
from App.apis.NewTestApi import NewTestResource
from App.apis.NewsApi import NewsResource, NewsResource1, NewsResource2, NewsResource3, NewsResource4
from App.apis.NewsClsApi import NewsClsResource, NewsClsResource1
from App.apis.OperationApi import OperationResource, OperationResource1, OperationResource2
from App.apis.PointsApi import PointsResource
from App.apis.PositionApi import PositionResource, PositionResource1, PositionResource2
from App.apis.ResourceApi import ResourceApi, ResourceApi1, ResourceApi2, ResourceApi3, ResourceApi4, ResourceApi5
from App.apis.StaffApi import StaffRespource, StaffRespource1, StaffRespource2
from App.apis.StaffTestApi import StaffTestResource, StaffTestResource1
from App.apis.Staff_bannerApi import StaffBannerResource
from App.apis.TeacherApi import TeacherResource
from App.apis.TokenApi import TokenResource, TokenResource1, TokenResource2, TokenResource3
from App.apis.ToolCollectionApi import ToolCollResource, ToolCollResource1, ToolCollResource2, ToolCollResource3
from App.apis.ToolsApi import ToolsResource, ToolsResource1
from App.apis.TrainTaskApi import TrainTaskResource, TrainTaskResource1, LearnTask, LearnTask1
from App.apis.UserQuesApi import UserQuesResource, UserQuesResource1, UserQuesResource2
from App.apis.UserResourceApi import UserResourceApi, UserResourceApi1, UserResourceApi2, UserResourceApi3, \
    UserResourceApi4, UserResourceApi5

api = Api()
#需要注意  api的初始化 要和init方法联系 否则无法初始化
def init_apis(app):
    api.init_app(app=app)

#试题提交
api.add_resource(NewTestResource,'/newtest/')

#FAQ
api.add_resource(FaqResource,'/api/v2/QA/FAQ/')
api.add_resource(FaqChanceResource,'/api/v2/QA/FAQ/<id>')

#经销商
api.add_resource(AdminApiResource,'/api/v2/admin/')
api.add_resource(AdminApiResource1,'/api/v2/admin/<admin_id>')

#经销商轮播图
api.add_resource(DealerLbtApi,'/api/v2/carousel/dealer')
api.add_resource(DealerLbtApi1,'/api/v2/carousel/dealer/news/<news_id>')
api.add_resource(DealerLbtApi2,'/api/v2/carousel/dealer/<news_id>')

#经销商课程培训
api.add_resource(DealerTrainResource,'/api/v2/trainings/')
api.add_resource(DealerTrainResource1,'/api/v2/trainings/<id>')

#讲师信息
api.add_resource(TeacherResource,'/api/v2/teacher/')

#心得
api.add_resource(ExperienceResource,'/api/v2/trainings/<course_id>/gains')
api.add_resource(ExperienceResource1,'/api/v2/trainings/<course_id>/gains/<gains_id>')
api.add_resource(ExperienceResource2,'/api/v2/trainings/<course_id>/gains/user_id/<user_id>')
api.add_resource(ExperienceResource3,'/api/v2/trainings/<course_id>/gains/essence')

#资源
api.add_resource(ResourceApi,'/api/v2/resources/<resId>')
api.add_resource(ResourceApi1,'/api/v2/hier/')
api.add_resource(ResourceApi2,'/api/v2/resources/all/')
api.add_resource(ResourceApi3,'/api/v2/resources/<id>')
api.add_resource(ResourceApi4,'/api/v2/resources/folder/')
api.add_resource(ResourceApi5,'/api/v2/dealer/resources/<resId>/')

#获取所有互动信息
api.add_resource(DealerActiApi4,'/api/v2/QA/actions')
#经销商提交问题
api.add_resource(DealerActiApi1,'/api/v2/QA/<user_id>/actions/')
#回复问题
api.add_resource(DealerActiApi3,'/api/v2/QA/action/<ques_id>/replys')
api.add_resource(DealerActiApi2,'/api/v2/QA/action/<ques_id>/replys/<user_id>')
api.add_resource(DealerActiApi5,'/api/v2/QA/action/<id>')

#微信认证
api.add_resource(TokenResource,'/api/v2/tokens/')
api.add_resource(TokenResource1,'/api/v2/tokens/code/')
api.add_resource(TokenResource2,'/api/v2/tokens/validation/<code>')
api.add_resource(TokenResource3,'/api/v2/tokens/code/<code>')

#新闻管理
api.add_resource(NewsResource,'/api/v2/newses/')
api.add_resource(NewsResource1,'/api/v2/news/<id>')
api.add_resource(NewsResource2,'/api/v2/news/search/')
api.add_resource(NewsResource3,'/api/v2/news/look/<cls_id>')
api.add_resource(NewsResource4,'/api/v2/news/type_/<type_>/')

api.add_resource(NewsClsResource,'/api/v2/news_cls/')
api.add_resource(NewsClsResource1,'/api/v2/news_cls/<id>')

#员工轮播图,热点
api.add_resource(StaffBannerResource,'/api/v2/carousels/staff/')
api.add_resource(HotMsgResource,'/api/v2/hots/')

#员工人员信息
api.add_resource(StaffRespource,'/api/v2/staffs/')
api.add_resource(StaffRespource1,'/api/v2/staff/<user_id>')
api.add_resource(StaffRespource2,'/api/v2/staff/search/')

#部门信息
api.add_resource(BuResource,'/api/v2/bu/')
api.add_resource(BuResource1,'/api/v2/bu/<id>')

#职位信息
api.add_resource(PositionResource,'/api/v2/pos/')
api.add_resource(PositionResource1,'/api/v2/pos/<id>')
api.add_resource(PositionResource2,'/api/departments/<bu_id>/positions')

#课程分类表
api.add_resource(LessonClasResource,'/api/v2/lesson_classes/')
api.add_resource(LessonClasResource1,'/api/v2/les_cls/<id>')

#术式信息
api.add_resource(OperationResource,'/api/v2/oper/')
api.add_resource(OperationResource1,'/api/v2/oper/<id>')

api.add_resource(OperationResource2,'/api/v2/lesson_classes/<cls_id>/operations/')

#课程信息
api.add_resource(LessonResource,'/api/v2/lesson/')
api.add_resource(LessonResource1,'/api/v2/lesson/<id>')

api.add_resource(LessonResource2,'/api/v2/operations/<subPart_id>/staffs/<openid>/lessons/<types>/')
api.add_resource(LessonResource3,'/api/v2/recommend/<user_id>/lessons/')
api.add_resource(LessonResource4,'/api/v2/is_look/<lsn_id>/lessons/')


#课程评论
api.add_resource(LesCommentResource,'/api/v2/les_comment/')
api.add_resource(LesCommentResource1,'/api/v2/les_comment/<id>')
api.add_resource(LesCommentResource2,'/api/v2/lessons/<lsn_id>/comments/')
api.add_resource(LesCommentResource3,'/api/v2/staff/<staff_id>/comments/')

#感恩
api.add_resource(GratitudeResource,'/api/v2/gratitudes/')
api.add_resource(GratitudeResource1,'/api/v2/grattrees/')
api.add_resource(GratitudeResource2,'/api/v2/gratitudes/<id>')
api.add_resource(GratitudeResource3,'/api/v2/<from_id>/gratitudes/<to_id>')
api.add_resource(GratitudeResource4,'/api/v2/gratitudes/to/<_to>')
api.add_resource(GratitudeResource5,'/api/v2/gratitudes/from/<_from>')
api.add_resource(GratStarResource,'/api/v2/gratstar/')

#员工考试
api.add_resource(StaffTestResource,'/api/v2/lessons/<lsn_id>/questions/')
api.add_resource(StaffTestResource1,'/api/v2/testing/')

#课程收藏
api.add_resource(LsnCollectionResource,'/api/v2/collections/')
api.add_resource(LsnCollectionResource1,'/api/v2/staffs/<user_id>/collections/')
api.add_resource(LsnCollectionResource2,'/api/v2/staffs/<staff_id>/collections/<lsn_id>/')
api.add_resource(LsnCollectionResource3,'/api/v2/staffs/<user_id>/lesson/')

#课程点赞
api.add_resource(LsnThumbResource,'/api/v2/thumbs/')
api.add_resource(LsnThumbResource1,'/api/v2/staffs/<user_id>/thumb/')
api.add_resource(LsnThumbResource2,'/api/v2/staffs/<user_id>/thumbs/<lesson_id>/')

#工具+收藏
api.add_resource(ToolsResource,'/api/v2/tools/<tool_id>/')
api.add_resource(ToolsResource1,'/api/v2/tools/')
api.add_resource(ToolCollResource,'/api/v2/toolcollections/')
api.add_resource(ToolCollResource1,'/api/v2/staffs/<user_id>/toolcollections/')
api.add_resource(ToolCollResource2,'/api/v2/staffs/<user_id>/toolcollections/<tool_id>/')
api.add_resource(ToolCollResource3,'/api/v2/staff/<user_id>/tools/')

#员工资源表
api.add_resource(UserResourceApi,'/api/v2/staff/<user_id>/hier/<hier>/resources/<resId>/')
api.add_resource(UserResourceApi1,'/api/v2/staff/resource/<resId>/')

api.add_resource(UserResourceApi2,'/api/v2/staff/getresource/')
api.add_resource(UserResourceApi3,'/api/v2/staff/resource/hier/')
api.add_resource(UserResourceApi4,'/api/v2/staff/getresource/folder/')
api.add_resource(UserResourceApi5,'/api/v2/staff/resourcees/<resId>/')

#员工考试
api.add_resource(UserQuesResource,'/api/v2/questions/')
api.add_resource(UserQuesResource1,'/api/v2/questions/<ques_id>')
api.add_resource(UserQuesResource2,'/api/v2/questions/<lsn_id>')

#老师
api.add_resource(LecturerResource,'/api/v2/lecturers/')

#学习任务
api.add_resource(TrainTaskResource,'/api/v2/traintask/')
api.add_resource(TrainTaskResource1,'/api/v2/traintask/<id>')

#记录用户登录次数
api.add_resource(LoginNumber,'/api/v2/numbers/')
api.add_resource(PointsResource,'/api/v2/points/<staff_id>')

#学习任务
api.add_resource(LearnTask,'/api/v2/learning/task/<staff_id>/')
api.add_resource(LearnTask1,'/api/v2/learning/task/<staff_id>/lesson/<lsn_id>/')



