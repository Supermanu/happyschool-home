# This file is part of HappySchool.
#
# HappySchool is the legal property of its developers, whose names
# can be found in the AUTHORS file distributed with this source
# distribution.
#
# HappySchool is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# HappySchool is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with HappySchool.  If not, see <http://www.gnu.org/licenses/>.

import json

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.filters import OrderingFilter

from core.views import BaseFilters, get_app_settings
from core.utilities import get_menu

from .models import HomeSettingsModel, HomeNewsModel
from .serializers import HomeSettingsSerializer, HomeNewsSerializer


def get_menu_entry(active_app, request):
    # if not user.has_perm("home.view_home"):
    #     return {}
    return {
            "app": "home",
            "display": "Accueil",
            "url": "/home/",
            "active": active_app == "home"
    }


def get_settings():
    return get_app_settings(HomeSettingsModel)


class HomeView(
    LoginRequiredMixin,
    TemplateView
):
    template_name = "home/home.html"
    #permission_required = ('home.view_home')
    filters = []

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['menu'] = json.dumps(get_menu(self.request, "home"))
        context['filters'] = json.dumps(self.filters)
        context["can_add_news"] = json.dumps(self.request.user.has_perm("home.add_homenewsmodel"))
        context['settings'] = json.dumps((HomeSettingsSerializer(get_settings()).data))

        return context


#class HomeFilter(BaseFilters):
    #class Meta:
        #fields_to_filter = (,)
        #model = Home
        #fields = BaseFilters.Meta.generate_filters(fields_to_filter)
        #filter_overrides = BaseFilters.Meta.filter_overrides


class HomeNewsViewSet(ModelViewSet):
    queryset = HomeNewsModel.objects.all()
    serializer_class = HomeNewsSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [OrderingFilter]
    ordering_fields = ["pinned", "datetime_update"]
    ordering = ["-pinned"]
