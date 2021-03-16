from typing import List


def get_top_level_domain(urls: List[str]) -> List[str]:
    top_level_domains = []
    for url in urls:
        domains = url.split('.')
        top_level_domain = domains[-1]
        top_level_domains.append(top_level_domain)

    return top_level_domains
