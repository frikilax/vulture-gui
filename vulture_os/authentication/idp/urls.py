#!/home/vlt-os/env/bin/python
"""This file is part of Vulture OS.

Vulture OS is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Vulture OS is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Vulture OS.  If not, see http://www.gnu.org/licenses/.
"""
__author__ = "Olivier de Régis"
__credits__ = []
__license__ = "GPLv3"
__version__ = "3.0.0"
__maintainer__ = "Vulture OS"
__email__ = "contact@vultureproject.org"
__doc__ = 'IDP URLS'

from django.urls import path, re_path

from authentication.idp.api import IDPApiView
from authentication.idp.api import IDPApiUserView
from authentication.idp.api import IDPApiGroupView

urlpatterns = [
   re_path('^api/v1/authentication/idp/(?P<object_id>[A-Fa-f0-9]+)$', IDPApiView.as_view(), name="authentication.idp"),
   re_path('^api/v1/authentication/idp/users/(?P<object_id>[A-Fa-f0-9]+)$', IDPApiUserView.as_view(), name="authentication.idp.users"),
   re_path('^api/v1/authentication/idp/groups/(?P<object_id>[A-Fa-f0-9]+)$', IDPApiGroupView.as_view(), name="authentication.idp.groups")
]