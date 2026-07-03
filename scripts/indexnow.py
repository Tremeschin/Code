import os
import re
from urllib.parse import urlparse

import requests


def sitemap_urls(url) -> list[str]:
    return [x.strip() for x in re.findall(
        pattern=r"<loc>(.*?)</loc>",
        string=requests.get(url).text
    )]

for sitemap in (
    "https://depth.tremeschin.com/sitemap.xml",
    "https://nvibrant.tremeschin.com/sitemap.xml",
    "https://pianola.tremeschin.com/sitemap.xml",
    "https://pyaket.tremeschin.com/sitemap.xml",
    "https://shaders.tremeschin.com/sitemap.xml",
    "https://tremeschin.com/sitemap.xml",
):
    print(sitemap)
    payload = dict(
        host=urlparse(sitemap).netloc,
        urlList=list(sitemap_urls(sitemap)),
        key=os.environ["INDEXNOW"],
    )

    print(f"• Payload {payload}")
    response = requests.post(
        url="https://api.indexnow.org/indexnow",
        json=payload,
    )

    print(f"• Code {response.status_code}")
