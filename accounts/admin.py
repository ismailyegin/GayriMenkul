from django.contrib import admin

from sbs.models.GtasinmazBinaAltTur import GtasinmazAltTur
from sbs.models.GtasinmazBinaUstTur import GtasinmazUstTur

admin.site.site_header = 'Kobiltek Bilisim Kullanici Yönetim Paneli '  # default: "Django Administration"
admin.site.index_title = 'Sistem Yönetimi'  # default: "Site administration"
admin.site.site_title = 'Admin'  # default: "Django site admin"

admin.site.register(GtasinmazUstTur)
admin.site.register(GtasinmazAltTur)
