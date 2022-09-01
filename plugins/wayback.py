"""Support for archive.org."""
import datetime
import json

from requests import get


def time_machine(host, mode):
    """Query archive.org."""
    now = datetime.datetime.now()
    to = str(now.year) + str(now.day) + str(now.month)
    if now.month > 6:
    	fro = str(now.year) + str(now.day) + str(now.month - 6)
    else:
    	fro = str(now.year - 1) + str(now.day) + str(now.month + 6)
    url = f"http://web.archive.org/cdx/search?url={host}&matchType={mode}&collapse=urlkey&fl=original&filter=mimetype:text/html&filter=statuscode:200&output=json&from={fro}&to={to}"

    response = get(url).text
    parsed = json.loads(response)[1:]
    return [item[0] for item in parsed]
