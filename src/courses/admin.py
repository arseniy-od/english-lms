from django.contrib import admin
from .models import Course, Theme, Task, Test, TestVar, Lecture
from config.settings import ADMIN_ORDERING


# override the default admin ordering
def get_app_list(self, request):
    app_dict = self._build_app_dict(request)
    for app_name, object_list in ADMIN_ORDERING:
        app = app_dict[app_name]
        app['models'].sort(key=lambda x: object_list.index(x['object_name']))
        yield app


admin.AdminSite.get_app_list = get_app_list


admin.site.register(Course)
admin.site.register(Theme)
admin.site.register(Task)
admin.site.register(Lecture)


class TestVarInline(admin.StackedInline):
    model = TestVar


@admin.register(Test)
class TestInline(admin.ModelAdmin):
    inlines = [TestVarInline]


