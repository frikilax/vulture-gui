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
__author__ = "Kevin GUILLEMOT"
__credits__ = []
__license__ = "GPLv3"
__version__ = "4.0.0"
__maintainer__ = "Vulture OS"
__email__ = "contact@vultureproject.org"
__doc__ = 'Haproxy settings model'

# Django system imports
from django.conf import settings
from djongo import models

# Django project imports
from system.cluster.models import Cluster

# Required exceptions imports

# Extern modules imports

# Logger configuration imports
import logging
logging.config.dictConfig(settings.LOG_SETTINGS)
logger = logging.getLogger('services')


class HAProxySettings(models.Model):
    """ Model used to manage global configuration fields of HAProxy """

    def to_template(self):
        """ Dictionary used to create configuration file

        :return     Dictionnary of configuration parameters
        """
        """ First, use to_mongo() internal django function """
        from workflow.models import Workflow
        from authentication.user_portal.models import UserAuthentication

        endpoints = list()

        for workflow in Workflow.objects.filter(authentication__isnull=False):
            endpoint = {
                "id": workflow.id,
                "name": workflow.name,
                "fqdn": workflow.fqdn,
                "public_dir": workflow.public_dir,
                "auth_timeout": workflow.authentication.auth_timeout if workflow.authentication.enable_timeout_restart else 0,
                "oauth_repositories_id": list()
            }

            # Add openid repositories' client_id for validation of oauth token from those repositories on this endpoint
            for repo in workflow.authentication.repositories.filter(subtype="openid"):
                repo = repo.get_daughter()
                endpoint['oauth_repositories_id'].append(repo.client_id)     

            # Add the endpoint's portal to the authorized sources of oauth token (if oauth is enabled on it)
            if workflow.authentication.enable_oauth:
                endpoint['oauth_repositories_id'].append(workflow.authentication.oauth_client_id)

            endpoints.append(endpoint)

        return {
            'global_config': Cluster.get_global_config(),
            'endpoints': endpoints
        }

    def __str__(self):
        return "HAProxy settings"

