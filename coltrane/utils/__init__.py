# http
import httplib2

# Date manipulation
import pytz
import time
import datetime
import dateutil.parser
import dateutil.tz

# Serialization
from django.utils import simplejson
from anyetree import etree

# Text manipulation
from django.utils.encoding import force_unicode

# Django
from django.conf import settings

DEFAULT_HTTP_HEADERS = {
    "User-Agent" : "palewire.com"
}

#
# URL fetching sugar
#

def getxml(url, **kwargs):
    """
    Fetch and parse some XML. Returns an ElementTree.
    """
    xml = fetch_resource(url, **kwargs)
    return etree.fromstring(xml)


def getjson(url, **kwargs):
    """
    Fetch and parse some JSON. Returns the deserialized JSON.
    """
    json = fetch_resource(url, **kwargs)
    return simplejson.loads(json)


def fetch_resource(url, method="GET", body=None, username=None, password=None, headers=None):
    """
    Fetch an URL. Return the content.
    """
    h = httplib2.Http(timeout=15)
    h.force_exception_to_status_code = True
    
    if username is not None or password is not None:
        h.add_credentials(username, password)
    
    if headers is None:
        headers = DEFAULT_HTTP_HEADERS.copy()
    response, content = h.request(url, method, body, headers)
    return content

#
# Date handling utils
#

def parsedate(s):
    """
    Convert a string into a local, naive datetime object.
    """
    dt = dateutil.parser.parse(s)
    if dt.tzinfo:
        dt = dt.astimezone(dateutil.tz.tzlocal()).replace(tzinfo=None)
    return dt


def safeint(s):
    """
    Always returns an int. Returns 0 on failure.
    """
    try:
        return int(force_unicode(s))
    except (ValueError, TypeError):
        return 0

#
# Timezone adjustment
#

UTC = pytz.timezone('UTC')
LOCAL = pytz.timezone(settings.TIME_ZONE)

def utc_to_local_datetime(dt):
    """
    Map datetime as UTC object to it's localtime counterpart.
    """
    return dt.astimezone(LOCAL)

def utc_to_local_timestamp(ts, orig_tz=UTC):
    """
    Convert a timestamp object into a tz-aware datetime object.
    """
    timestamp = datetime.datetime.fromtimestamp(ts,tz=orig_tz)
    return timestamp.astimezone(LOCAL)

def utc_to_local_timestruct(ts, orig_tz=UTC):
    """
    Convert a timestruct object into a tz-aware datetime object.
    """
    return utc_to_local_timestamp(time.mktime(ts),orig_tz)
