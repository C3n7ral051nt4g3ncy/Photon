"""Support for findsubdomains.com."""
from re import findall

from requests import get


def find_subdomains(domain):
    """Find subdomains according to the TLD."""
    response = get(f'https://findsubdomains.com/subdomains-of/{domain}').text
    matches = findall(r'(?s)<div class="domains js-domain-name">(.*?)</div>', response)
    result = {match.replace(' ', '').replace('\n', '') for match in matches}
    return list(result)
