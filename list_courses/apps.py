"""
list_courses Django application initialization.
"""

from django.apps import AppConfig
from edx_django_utils.plugins.constants import PluginURLs, PluginSettings


class ListCoursesConfig(AppConfig):
    """
    Configuration for the list_courses Django application.
    """

    name = 'list_courses'
    plugin_app = {
        PluginURLs.CONFIG: {
            'lms.djangoapp': {
                PluginURLs.NAMESPACE: 'list_courses',
                PluginURLs.APP_NAME: 'list_courses',
                PluginURLs.REGEX: r'^api/list_courses/',
                PluginURLs.RELATIVE_PATH: 'list_courses.urls',
            }
        },
        PluginSettings.CONFIG: {
            'lms.djangoapp': {
                'production': {
                    PluginSettings.RELATIVE_PATH: 'settings.production',
                },
                'common': {
                    PluginSettings.RELATIVE_PATH: 'settings.common',
                },
                'devstack': {
                    PluginSettings.RELATIVE_PATH: 'settings.devstack',
                },
            }
        },
    }
