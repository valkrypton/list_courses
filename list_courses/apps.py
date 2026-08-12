"""
list_courses Django application initialization.
"""

from django.apps import AppConfig
from edx_django_utils.plugins import PluginContexts, PluginSignals
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
        PluginSignals.CONFIG: {
            'lms.djangoapp': {
                PluginSignals.RELATIVE_PATH: 'my_signals',
                PluginSignals.RECEIVERS: [{
                    PluginSignals.RECEIVER_FUNC_NAME: 'on_signal_x',
                }],
            }
        },
        PluginContexts.CONFIG: {
            'lms.djangoapp': {
                'course_dashboard': 'list_courses.context_api.get_dashboard_context',
            }
        }
    }
