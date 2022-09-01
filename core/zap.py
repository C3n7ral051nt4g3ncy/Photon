import re
import requests
import random

from core.utils import verb, xml_parser
from core.colors import run, good
from plugins.wayback import time_machine


def zap(input_url, archive, domain, host, internal, robots, proxies):
    """Extract links from robots.txt and sitemap.xml."""
    if archive:
        print(f'{run} Fetching URLs from archive.org')
        archived_urls = time_machine(host, 'host')
        print('%s Retrieved %i URLs from archive.org' % (
            good, len(archived_urls) - 1))
        for url in archived_urls:
            verb('Internal page', url)
            internal.add(url)
    # Makes request to robots.txt
    response = requests.get(
        f'{input_url}/robots.txt', proxies=random.choice(proxies)
    ).text

    # Making sure robots.txt isn't some fancy 404 page
    if '<body' not in response:
        if matches := re.findall(r'Allow: (.*)|Disallow: (.*)', response):
            # Iterating over the matches, match is a tuple here
            for match in matches:
                # One item in match will always be empty so will combine both
                # items
                match = ''.join(match)
                # If the URL doesn't use a wildcard
                if '*' not in match:
                    url = input_url + match
                    # Add the URL to internal list for crawling
                    internal.add(url)
                    # Add the URL to robots list
                    robots.add(url)
            print(f'{good} URLs retrieved from robots.txt: {len(robots)}')
    # Makes request to sitemap.xml
    response = requests.get(
        f'{input_url}/sitemap.xml', proxies=random.choice(proxies)
    ).text

    # Making sure robots.txt isn't some fancy 404 page
    if '<body' not in response:
        if matches := xml_parser(response):
            print(f'{good} URLs retrieved from sitemap.xml: {len(matches)}')
            for match in matches:
                verb('Internal page', match)
                # Cleaning up the URL and adding it to the internal list for
                # crawling
                internal.add(match)
