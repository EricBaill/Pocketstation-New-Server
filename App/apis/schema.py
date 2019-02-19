from ..ext import ma
from App.models import BusinessUnit, Position, User, LessonClas, Operation, LessonPermission, Tool, Lesson, Question, \
    Testing, Gratitude, GratitudeStar, NewsClas, News, TrainingTask


class BusinessUnitSchema(ma.Schema):
    class Meta:
        model = BusinessUnit


class PositionSchema(ma.Schema):
    class Meta:
        model = Position

    bu = ma.Nested(BusinessUnitSchema)


class StaffSchema(ma.Schema):
    class Meta:
        model = User
    pos = ma.Nested(PositionSchema)


class LessonClassSchema(ma.Schema):
    class Meta:
        model = LessonClas


class OperationSchema(ma.Schema):
    class Meta:
        model = Operation
    cls = ma.Nested(LessonClassSchema, only=["id", "name"])

class LessonPermissionSchema(ma.Schema):
    class Meta:
        model = LessonPermission
    bu = ma.Nested(BusinessUnitSchema, exclude=[
                   "lesson_permissions", "positions"])


class PosBuSchema(ma.Schema):
    class Meta:
        model = Position
    bu = ma.Nested(BusinessUnitSchema, only=["name", "id"])


class LecturerSchema(ma.Schema):
    class Meta:
        model = User
    pos = ma.Nested(PosBuSchema, only=["bu", "name", "id"])


# class TagSchema(ma.ModelSchema):
#     class Meta:
#         model = Tag


class _ToolForLessonSchema(ma.Schema):
    class Meta:
        model = Tool

class LessonSchema(ma.Schema):
    class Meta:
        model = Lesson
        exclude = ["testings", "training_tasks", "questions"]
    lesson_permissions = ma.List(
        ma.Nested(LessonPermissionSchema, exclude=["lsn"]))
    lecturer = ma.Nested(LecturerSchema, only=["name", "pos", "avatar", "lessons"])
    # tags = ma.Nested(TagSchema, only=["name", "id"], many=True)
    oprt = ma.Nested(OperationSchema, only=["id", "name", "cls"])
    tools = ma.List(ma.Nested(_ToolForLessonSchema, only=["type", "id", "name", "content"]), many=True)


class ToolSchema(ma.Schema):
    class Meta:
        model = Tool
    lsn = ma.Nested(LessonSchema, only=['id', 'name', 'oprt'])

# LessonSchema.tools = ma.Nested(ToolSchema, only=["type", "content", "name", "id"], many=True)


# class CommentSchema(ma.ModelSchema):
#     class Meta:
#         model = Comment
#     staff = ma.Nested(StaffSchema, only=["name", "avatar"])
#     lsn = ma.Nested(LessonSchema, only=["name", "id", "oprt"])

# LessonSchema.comments = ma.Nested(CommentSchema, only=["id", "content", "staff", "create_at"])

class QestionSchema(ma.Schema):
    class Meta:
        model = Question
    lsn = ma.Nested(LessonSchema, only=["id", "name", "oprt"])

class TestingSchema(ma.Schema):
    class Meta:
        model = Testing
    lsn = ma.Nested(LessonSchema, only=["name", "img_src", "type"])


class GratitudeSchema(ma.Schema):
    class Meta:
        model = Gratitude
    staff_from = ma.Nested(StaffSchema, only=["name", "avatar"])
    staff_to = ma.Nested(StaffSchema, only=["name", "avatar"])


class GratitudeStarSchema(ma.Schema):
    class Meta:
        model = GratitudeStar
    staff = ma.Nested(LecturerSchema, only=["name", "avatar", "pos", "email"])

class NewsClassSchema(ma.Schema):
    class Meta:
        model = NewsClas

class NewsSchema(ma.Schema):
    class Meta:
        model = News
    cls = ma.Nested(NewsClassSchema, only=["name", "id"])

class TrainingTaskSchema(ma.Schema):
    class Meta:
        model = TrainingTask
    lsn = ma.Nested(LessonSchema, only=["id", "name", "type", "oprt"])
    staff = ma.Nested(StaffSchema, only=["id", "name", "tel", "email"])