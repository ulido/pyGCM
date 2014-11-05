"""GCM - very simple interface to send data to Google Cloud Messaging
"""
import urllib2
import json

__all__ = ["GCM"]

# Google Cloud Messaging send API URL
_GCM_URL = 'https://android.googleapis.com/gcm/send'

class GCM(object):
    """Google Cloud Messaging connection class"""
    def __init__(self, api_key):
        """Initialize GCM object

        Parameters:
        -----------
        api_key : str
            Google Cloud Messaging API key, needed for authentication
        """
        self._api_key = api_key

    def send_message(self, registration_ids, data):
        """Send a message through GCM to the devices specified.

        Parameters:
        -----------
        registration_ids : list
            List of strings containing the registration IDs of the recipient
            devices
        data : dict
            Dictionary containing the data variables to be sent. Needs to be
            json-able.
        """
        # Construct payload dictionary: Needs to contain an entry with the
        # registration_ids of the devices we want to send a message to, as well
        # as a data entry containing a dict of json-able variables with our
        # message.
        payload = {
            'registration_ids': registration_ids,
            'data' : data
            }
        # Construct url request
        request = urllib2.Request(_GCM_URL)
        # POST content needs to be of json type
        request.add_header('Content-Type', 'application/json')
        # Authorization header needs to contain our GCM api key
        request.add_header('Authorization', 'key=' + self._api_key)
        # Connect and send - urllib2 doesn't do any HTTPS certificate checking!!
        # We maybe should check the return code from the request...
        urllib2.urlopen(request, json.dumps(payload))
