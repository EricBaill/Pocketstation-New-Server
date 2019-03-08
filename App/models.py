from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


#部门信息表
class BusinessUnit(db.Model):
    __tablename__ = 'business_unit'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    admin_id = db.relationship('Admin', backref='business_unit')

    # poss = db.relationship('Position', secondary='ref_pos_bu', backref='business_units')
    # trainings = db.relationship('DealerTraining', secondary='ref_training_permission', backref='business_units')

#部门和经销商
# t_ref_training_permission = db.Table(
#     'ref_training_permission',
#     db.Column('bu_id', db.ForeignKey('business_unit.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True),
#     db.Column('training_id', db.ForeignKey('dealer_training.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True),
# )


# t_ref_pos_bu = db.Table(
#     'ref_pos_bu',
#     db.Column('pos_id', db.ForeignKey('position.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True),
#     db.Column('bu_id', db.ForeignKey('business_unit.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True),
# )



#职位信息表
class Position(db.Model):
    __tablename__ = 'position'

    id = db.Column(db.Integer, primary_key=True)
    bu_id = db.Column(db.Integer,db.ForeignKey('business_unit.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    name = db.Column(db.String(45), nullable=False)
    is_manager = db.Column(db.Integer, nullable=False)

    bu = db.relationship('BusinessUnit', primaryjoin='Position.bu_id == BusinessUnit.id', backref='position')


    # users = db.relationship('User', secondary='ref_user_pos', backref='position')

# t_ref_user_pos = db.Table(
#     'ref_user_pos',
#     db.Column('staff_id', db.ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True),
#     db.Column('pos_id', db.ForeignKey('position.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True),
# )



#经销商表
class Admin(db.Model):
    __tablename__ = 'admin'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    avatar = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255))
    token = db.Column(db.String(255))
    openid = db.Column(db.String(255))
    type = db.Column(db.String(64),default='dealer')
    number = db.Column(db.Integer,default=0,nullable=False)
    create_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    bu_id = db.Column(db.Integer,db.ForeignKey(BusinessUnit.id, ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    hd_id = db.relationship('HD', backref='admin')
    hd_ans_id = db.relationship('Hd_Ans', backref='admin')

class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128),nullable=False)

#固定问答表
class FAQ(db.Model):
    __tablename__ = 'faq'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255),nullable=False)
    answer = db.Column(db.String(255),nullable=False)

#互动
class HD(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    admin_id = db.Column(db.Integer,db.ForeignKey(Admin.id, ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    question = db.Column(db.String(255),nullable=False)
    hd_ans_id = db.relationship('Hd_Ans',backref='hd')
    create_at = db.Column(db.DateTime, default=datetime.now)

#回复
class Hd_Ans(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ans = db.Column(db.String(255),nullable=False)
    admin_id = db.Column(db.Integer,db.ForeignKey(Admin.id, ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    hd_id = db.Column(db.Integer,db.ForeignKey(HD.id, ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    create_at = db.Column(db.DateTime, default=datetime.now)


#经销商轮播图
class A_banner(db.Model):
    __tablename__ = 'a_banner'

    id = db.Column(db.Integer, primary_key=True)
    cover_img = db.Column(db.String(255), nullable=False)
    content = db.Column(db.String(255),nullable=False)

#心得
class Experience(db.Model):
    __tablename__ = 'experience'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    content = db.Column(db.String(255))
    type = db.Column(db.Boolean,default=False)
    create_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    admin_id = db.Column(db.Integer,db.ForeignKey('admin.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    dealer_training_id = db.Column(db.Integer,db.ForeignKey('dealer_training.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)

    admin = db.relationship('Admin', primaryjoin='Experience.admin_id == Admin.id', backref='experience')
    dealer_training = db.relationship('DealerTraining', primaryjoin='Experience.dealer_training_id == DealerTraining.id', backref='experience')



#经销商课程推荐表
class DealerGain(db.Model):
    __tablename__ = 'dealer_gain'

    id = db.Column(db.Integer, primary_key=True)
    dealer_id = db.Column(db.Integer,db.ForeignKey('admin.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    title = db.Column(db.String(64), nullable=False)
    content = db.Column(db.String(255), nullable=False)
    top = db.Column(db.Integer, nullable=False)
    create_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    training_id = db.Column(db.Integer,db.ForeignKey('dealer_training.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)

    dealer = db.relationship('Admin', primaryjoin='DealerGain.dealer_id == Admin.id', backref='dealer_gains')
    training = db.relationship('DealerTraining', primaryjoin='DealerGain.training_id == DealerTraining.id', backref='dealer_gains')

#经销商课程学习表
class DealerTraining(db.Model):
    __tablename__ = 'dealer_training'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    cover_img = db.Column(db.String(255), nullable=False)
    lecturer = db.Column(db.String(255), nullable=False)
    content = db.Column(db.String(255), nullable=False)
    desc = db.Column(db.String(255), nullable=False)
    create_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    # recomended = db.Column(db.Integer, nullable=False)

#感恩表
class Gratitude(db.Model):
    __tablename__ = 'gratitude'

    id = db.Column(db.Integer, primary_key=True)
    from_id = db.Column(db.Integer, nullable=False, index=True)
    # from_id = db.Column(db.ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    to_id = db.Column(db.Integer, nullable=False, index=True)
    # to_id = db.Column(db.ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    content = db.Column(db.String(255), nullable=False)
    create_at = db.Column(db.DateTime, nullable=False, default=datetime.now)

    # from_ = db.relationship('User', primaryjoin='Gratitude.from_id == User.id', backref='gratitude')
    # to_ = db.relationship('User', primaryjoin='Gratitude.to_id == User.id', backref='gratitude')



#感恩之星表
class GratitudeStar(db.Model):
    __tablename__ = 'gratitude_star'

    id = db.Column(db.Integer, primary_key=True)
    staff_id = db.Column(db.Integer,db.ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    create_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    year_month = db.Column(db.String(45), nullable=False)

    staff = db.relationship('User', primaryjoin='GratitudeStar.staff_id == User.id', backref='gratitude_stars')

#课程表
class Lesson(db.Model):
    __tablename__ = 'lesson'

    id = db.Column(db.Integer, primary_key=True)
    oper_id = db.Column(db.Integer,db.ForeignKey('operation.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    lecturer_id = db.Column(db.Integer,db.ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'))
    name = db.Column(db.String(45), nullable=False)
    type = db.Column(db.String(45), nullable=False)
    img_src = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    recommended = db.Column(db.Integer, default=0)
    is_look = db.Column(db.Integer, default=0)
    create_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    be_thumbs = db.Column(db.String(255))
    # tools = db.relationship('Tool', backref='lesson', lazy='dynamic')
    # permission = db.relationship('LessonPermission', backref='lesson', lazy='dynamic')

    oper = db.relationship('Operation', primaryjoin='Lesson.oper_id == Operation.id', backref='lesson')
    lecturer = db.relationship('User', primaryjoin='Lesson.lecturer_id == User.id', backref='lesson')

# #课程讲师表
# class Lecturer(db.Model):
#     __tablename__ = 'lecturer'
#
#     id = db.Column(db.Integer, primary_key=True)
#     staff_id = db.Column(db.ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
#
#     staff = db.relationship('User', primaryjoin='Lecturer.staff_id == User.id', backref='lecturer')
#

#课程分类表
class LessonClas(db.Model):
    __tablename__ = 'lesson_class'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    img_src = db.Column(db.String(255), nullable=False)

#课程收藏表
class LessonCollection(db.Model):
    __tablename__ = 'lesson_collection'

    id = db.Column(db.Integer, primary_key=True)
    staff_id = db.Column(db.Integer,db.ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    lesson_id = db.Column(db.Integer,db.ForeignKey('lesson.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)

    lesson = db.relationship('Lesson', primaryjoin='LessonCollection.lesson_id == Lesson.id', backref='lesson_collection')
    staff = db.relationship('User', primaryjoin='LessonCollection.staff_id == User.id', backref='lesson_collection')

#课程评论表
class LessonComment(db.Model):
    __tablename__ = 'lesson_comment'

    id = db.Column(db.Integer, primary_key=True)
    staff_id = db.Column(db.Integer,db.ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    lsn_id = db.Column(db.Integer,db.ForeignKey('lesson.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    # openid = db.Column(db.String(255),nullable=False)
    content = db.Column(db.String(255), nullable=False)
    create_at = db.Column(db.DateTime, nullable=False, default=datetime.now)

    lsn = db.relationship('Lesson', primaryjoin='LessonComment.lsn_id == Lesson.id', backref='lesson_comment')
    staff = db.relationship('User', primaryjoin='LessonComment.staff_id == User.id', backref='lesson_comment')

#课程权限表
class LessonPermission(db.Model):
    __tablename__ = 'lesson_permission'

    id = db.Column(db.Integer, primary_key=True)
    lsn_id = db.Column(db.Integer,db.ForeignKey('lesson.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    bu_id = db.Column(db.Integer,db.ForeignKey('business_unit.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    need_manager = db.Column(db.Integer, nullable=False)

    bu = db.relationship('BusinessUnit', primaryjoin='LessonPermission.bu_id == BusinessUnit.id', backref='lesson_permission')
    lsn = db.relationship('Lesson', primaryjoin='LessonPermission.lsn_id == Lesson.id', backref='lesson_permission')


#新闻表
class News(db.Model):
    __tablename__ = 'news'

    id = db.Column(db.Integer, primary_key=True)
    cls_id = db.Column(db.Integer,db.ForeignKey('news_class.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    name = db.Column(db.String(45), nullable=False)
    img_src = db.Column(db.String(255), nullable=False)
    brief = db.Column(db.String(255), nullable=False)
    type_ = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    create_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    top = db.Column(db.Integer,default=0)
    is_banner = db.Column(db.Integer,default=0)
    cls = db.relationship('NewsClas', primaryjoin='News.cls_id == NewsClas.id', backref='news')

#新闻分类表
class NewsClas(db.Model):
    __tablename__ = 'news_class'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)

#术式表
class Operation(db.Model):
    __tablename__ = 'operation'

    id = db.Column(db.Integer, primary_key=True)
    cls_id = db.Column(db.Integer,db.ForeignKey('lesson_class.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    name = db.Column(db.String(45), nullable=False)
    img_src = db.Column(db.String(255), nullable=False)

    cls = db.relationship('LessonClas', primaryjoin='Operation.cls_id == LessonClas.id', backref='operation')


# class Permission(db.Model):
#权限表
#     __tablename__ = 'permission'
#
#     id = db.Column(db.Integer, primary_key=True)
#     code = db.Column(db.String(45), nullable=False)
#     name = db.Column(db.String(45), nullable=False)
#     desc = db.Column(db.String(255), nullable=False)

#积分表
class Point(db.Model):
    __tablename__ = 'points'

    id = db.Column(db.Integer, primary_key=True)
    staff_id = db.Column(db.Integer,db.ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    total_points = db.Column(db.Integer)
    # curr_points = db.Column(db.Integer)
    level = db.Column(db.String(64))
    # title = db.Column(db.String(64), nullable=False)
    creaet_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    # update_at = db.Column(db.DateTime, nullable=False, default=datetime.now)

    staff = db.relationship('User', primaryjoin='Point.staff_id == User.id', backref='points')


#用户积分表

# class PointsRecord(db.Model):
#     __tablename__ = 'points_record'
#
#     id = db.Column(db.Integer, primary_key=True)
#     staff_id = db.Column(db.ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
#     title = db.Column(db.String(45), nullable=False)
#     desc = db.Column(db.String(255), nullable=False)
#     points = db.Column(db.Integer, nullable=False)
#
#     staff = db.relationship('User', primaryjoin='PointsRecord.staff_id == User.id', backref='points_record')


#经销商资源表
class DealerResource(db.Model):
    __tablename__ = 'resources'

    id = db.Column(db.Integer, primary_key=True)
    p_id = db.Column(db.Integer,nullable=True)
    name = db.Column(db.String(64), nullable=False,unique=True)
    type = db.Column(db.String(64), nullable=False)
    content = db.Column(db.String(512), nullable=True)
    # downloads = db.Column(db.Integer, nullable=False)

#员工资源表
class UserResource(db.Model):
    __tablename__ = 'user_resources'

    id = db.Column(db.Integer, primary_key=True)
    p_id = db.Column(db.Integer,nullable=True)
    name = db.Column(db.String(64), nullable=False,unique=True)
    type = db.Column(db.String(64), nullable=False)
    content = db.Column(db.String(512), nullable=True)


#员工测试表
class Testing(db.Model):
    __tablename__ = 'testing'

    id = db.Column(db.Integer, primary_key=True)
    staff_id = db.Column(db.Integer,db.ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    lsn_id = db.Column(db.Integer,db.ForeignKey('lesson.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    score = db.Column(db.Float, nullable=False)
    create_at = db.Column(db.DateTime, nullable=False, default=datetime.now())

    lsn = db.relationship('Lesson', primaryjoin='Testing.lsn_id == Lesson.id', backref='testing')
    staff = db.relationship('User', primaryjoin='Testing.staff_id == User.id', backref='testing')

#考试试题表

class NewTest(db.Model):
    __tablename__ = 'newtest'

    id = db.Column(db.Integer, primary_key=True)
    staff_id = db.Column(db.Integer,db.ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    staff_name = db.Column(db.String(125),nullable=False)
    select = db.Column(db.String(255))
    blanks = db.Column(db.String(255))
    shortAns = db.Column(db.String(255))
    picQues = db.Column(db.String(255))
    create_at = db.Column(db.DateTime, nullable=False, default=datetime.now)

    # staff = db.relationship('User', primaryjoin='newtest.staff_id == User.id', backref='newtest')


#工具表
class Tool(db.Model):
    __tablename__ = 'tool'

    id = db.Column(db.Integer, primary_key=True)
    lsn_id = db.Column(db.Integer,db.ForeignKey('lesson.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    name = db.Column(db.String(45), nullable=False)
    type = db.Column(db.String(45), nullable=False)
    content = db.Column(db.String(255), nullable=False)

    lsn = db.relationship('Lesson', primaryjoin='Tool.lsn_id == Lesson.id', backref='tool')

#工具收藏表
class ToolCollection(db.Model):
    __tablename__ = 'tool_collection'

    id = db.Column(db.Integer, primary_key=True)
    tool_id = db.Column(db.Integer,db.ForeignKey('tool.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    staff_id = db.Column(db.Integer,db.ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)

    staff = db.relationship('User', primaryjoin='ToolCollection.staff_id == User.id', backref='tool_collection')
    tool = db.relationship('Tool', primaryjoin='ToolCollection.tool_id == Tool.id', backref='tool_collection')

#员工任务学习表
class TrainingTask(db.Model):
    __tablename__ = 'training_task'

    id = db.Column(db.Integer, primary_key=True)
    staff_id = db.Column(db.Integer,db.ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    lsn_id = db.Column(db.Integer,db.ForeignKey('lesson.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    limit = db.Column(db.Integer, nullable=False)
    percent = db.Column(db.Float,default=0.0)
    create_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    finish_at = db.Column(db.DateTime, default=datetime.now)

    lsn = db.relationship('Lesson', primaryjoin='TrainingTask.lsn_id == Lesson.id', backref='training_task')
    staff = db.relationship('User', primaryjoin='TrainingTask.staff_id == User.id', backref='training_task')

#员工表
class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    pos_id = db.Column(db.Integer,db.ForeignKey('position.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    name = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(45), nullable=False)
    passwd = db.Column(db.String(45), nullable=False)
    tel = db.Column(db.String(45), nullable=False)
    type = db.Column(db.String(64), default='staff')
    create_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    img_src = db.Column(db.String(255),nullable=False)
    lsn_col = db.relationship('LessonCollection',backref='user')
    lsn_comment = db.relationship('LessonComment',backref='user')
    number = db.Column(db.Integer,default=0,nullable=False)
    dayno = db.Column(db.Integer,default=0,nullable=False)
    passed = db.Column(db.String(255))
    newtest = db.relationship('NewTest',backref='user')
    openid = db.Column(db.String(255))
    lesson_ = db.Column(db.String(255))
    jsapi_ticket = db.Column(db.String(128))


    pos = db.relationship('Position', primaryjoin='User.pos_id == Position.id', backref='user')






#员工考试表
class Question(db.Model):
    __tablename__ = 'question'

    id = db.Column(db.Integer, primary_key=True)
    lsn_id = db.Column(db.Integer,db.ForeignKey('lesson.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    content = db.Column(db.Text, nullable=False)
    correct_option = db.Column(db.Text, nullable=False)
    other_option = db.Column(db.Text, nullable=False)

    lsn = db.relationship('Lesson', primaryjoin='Question.lsn_id == Lesson.id', backref='question')

#考试表
# class UserTest(db.Model):
#     __tablename__ = 'usertest'
#
#     id = db.Column(db.Integer, primary_key=True)
#     staff_id = db.Column(db.Integer,db.ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
#     lsn_id = db.Column(db.Integer,db.ForeignKey('lesson.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
#     score = db.Column(db.Float, nullable=False)
#     create_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
#
#     lsn = db.relationship('Lesson', primaryjoin='UserTest.lsn_id == Lesson.id', backref='usertest')
#     staff = db.relationship('User', primaryjoin='UserTest.staff_id == User.id',backref='usertest')

#课程点赞
class LessonThumb(db.Model):
    __tablename__ = 'lesson_thumb'

    id = db.Column(db.Integer, primary_key=True)
    staff_id = db.Column(db.Integer,db.ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    lsn_id = db.Column(db.Integer,db.ForeignKey('lesson.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    create_at = db.Column(db.DateTime, nullable=False, default=datetime.now)

    lsn = db.relationship('Lesson', primaryjoin='LessonThumb.lsn_id == Lesson.id', backref='lesson_thumb')
    staff = db.relationship('User', primaryjoin='LessonThumb.staff_id == User.id', backref='lesson_thumb')
