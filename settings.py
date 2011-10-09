# Django settings for cms project.
import os
settings_dir = os.path.dirname(__file__)

MEDIA_URL = 'http://palewire.s3.amazonaws.com/'
ADMIN_MEDIA_PREFIX = 'http://palewire.s3.amazonaws.com/admin/'
from settings_private import *

TEMPLATE_DEBUG = DEBUG

TIME_ZONE = 'America/Los_Angeles'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True

MEDIA_ROOT = os.path.join(settings_dir, 'media')

CACHE_BACKEND =	'memcached://127.0.0.1:11211'
CACHE_MIDDLEWARE_SECONDS = 60 *	5
CACHE_MIDDLEWARE_KEY_PREFIX = ''
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True

HAYSTACK_SITECONF = 'coltrane.search_indexes'
HAYSTACK_SEARCH_ENGINE = 'whoosh'
HAYSTACK_WHOOSH_PATH = '/apps/palewire.com/whoosh/'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.csrf.CsrfResponseMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    os.path.join(settings_dir, 'templates/'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.flatpages',
    'django.contrib.comments',
    'django.contrib.sitemaps',
    'django.contrib.humanize',
    'tagging',
    'coltrane',
    'kennedy',
    'correx',
    'django_memcached',
    'haystack',
    'django_extensions',
    'shortener',
    'greeking',
)

# Shortener settings
SITE_NAME = 'palewire.com'
SITE_BASE_URL = 'http://' + SITE_NAME + '/!/'


if DEBUG_TOOLBAR:
    INTERNAL_IPS = ('127.0.0.1',)
    # Debugging toolbar middleware
    MIDDLEWARE_CLASSES += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )
    # JavaScript panels for the deveopment debugging toolbar
    DEBUG_TOOLBAR_PANELS = (
        'debug_toolbar.panels.version.VersionDebugPanel',
        'debug_toolbar.panels.timer.TimerDebugPanel',
        'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
        'debug_toolbar.panels.headers.HeaderDebugPanel',
        'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
        'debug_toolbar.panels.template.TemplateDebugPanel',
        'debug_toolbar.panels.sql.SQLDebugPanel',
        #'debug_toolbar.panels.cache.CacheDebugPanel',
        'debug_toolbar.panels.signals.SignalDebugPanel',
        'debug_toolbar.panels.logger.LoggingPanel',
    )
    # Debug toolbar app
    INSTALLED_APPS += ('debug_toolbar',)
    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
        'HIDE_DJANGO_SQL': False,
    }

