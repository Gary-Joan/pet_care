from django.contrib import admin
from django.conf import settings
from models import *
from views import admin_update
from forms import AgendaAdminForm

class AgendaAdmin(admin.ModelAdmin):
    form =  AgendaAdminForm

    def admin_update_select(model_admin, request, content_type_id):
        return admin_update(request, content_type_id)

    def get_urls(self):
        from django.conf.urls.defaults import *
        urls = super(AgendaAdmin, self).get_urls()
        my_urls = patterns('', 
                url(r'update/(?P<content_type_id>\d+)/',
                    self.admin_site.admin_view(self.admin_update_select),
                    name = 'admin_update_select'),)
        return  my_urls + urls

    class Media:
        js = ['%sagenda/js/updater.js' % settings.STATIC_URL,]

admin.site.register(Event)
admin.site.register(Agenda, AgendaAdmin)
#admin.site.register(SharedEvent)
admin.site.register(EventInvite)
