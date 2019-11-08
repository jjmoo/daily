import re
import crawler

app_detail_url_format = 'https://play.google.com/store/apps/details?id=%s&hl=en'

apk_pkg_pattern = re.compile('apps/details\?id=((\w|\.)+)')
apk_name_pattern = re.compile('AHFaub.*?itemprop.*?name.*?span\s*>(.*?)</span')
apk_category_pattern = re.compile('hrTbp R8zArc.*?>(.*?)</a')


def parse_app_detail(url, content):
    pkg = None
    category_top = None
    category_sub = None
    name = None
    if 'apps/details?' in url:
        matcher = apk_pkg_pattern.search(url)
        if matcher:
            pkg = matcher.group(1)
        matcher = apk_category_pattern.findall(content)
        if matcher:
            category_top = re.sub('\&amp;', '&', matcher[0])
            category_sub = re.sub('\&amp;', '&', matcher[1])
        matcher = apk_name_pattern.search(content)
        if matcher:
            name = matcher.group(1)
    return pkg, category_top, category_sub, name, 'Google'

