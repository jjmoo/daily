import re
from urllib import parse


url_pattern = re.compile('href=\"(\S*?(union\.htm\?|category\.htm\?|detail\.htm\?)\S*?)\"')
category_pattern = re.compile('category\.htm\?orgame=(\d+)(&categoryId=(\d+))?')
app_list_pattern = re.compile('appList\.htm\?orgame=(\d+)&categoryId=(\d+).*?&pageContext=(\d+)')
list_count_pattern = re.compile('\"count\":(\d+)')
list_json_pattern = re.compile('\"pkgName\":\"(\S+?)\"')

apk_pkg_pattern = re.compile('detail\.htm\?apkName=((\w|\.)+)')
apk_name_pattern = re.compile('appname=\"(\S+)\"')
apk_category_pattern = re.compile('class=\"det-type-link\".*?>(.*?)<')
apk_download_pattern = re.compile('data-apkUrl=\"(.*?\.apk)')

category_child_format = 'https://sj.qq.com/myapp/cate/appList.htm?orgame=%d&categoryId=%d&pageSize=50&pageContext=%d'
app_detail_url_format = 'https://android.myapp.com/myapp/detail.htm?apkName=%s'


def get_seed_url():
    return 'https://sj.qq.com/myapp/index.htm'


def parse_target(url, content):
    child_list = parse_common_child(url, content)
    child_list += parse_category_child(url, content)
    pkg, category, name, download = parse_app_detail(url, content)
    return pkg, category, name, download, child_list


def combine_url(base, url):
    return parse.urljoin(base, url)


def parse_common_child(url, content):
    matcher_list = url_pattern.findall(content)
    child_list = []
    if len(matcher_list) > 0:
        for matcher in matcher_list:
            child = combine_url(url, matcher[0])
            if child not in child_list:
                child_list.append(child)
    return child_list


def parse_category_child(url, content):
    category_child = []
    if 'category.htm?' in url:
        matcher = category_pattern.search(url)
        if matcher:
            orgame = int(matcher.group(1))
            category_id = 0
            if matcher.group(3) is not None:
                category_id = int(matcher.group(3))
            category_child.append(category_child_format % (orgame, category_id, 0))
    if 'appList.htm?' in url:
        matcher = app_list_pattern.search(url)
        if matcher:
            orgame = int(matcher.group(1))
            category_id = int(matcher.group(2))
            context = int(matcher.group(3))
            cnt, child_list = parse_app_list(url, content)
            category_child += child_list
            category_child.append(category_child_format % (orgame, category_id, context + cnt))
    return category_child


def parse_app_list(_, content):
    cnt = 0
    child_list = []
    matcher = list_count_pattern.search(content)
    if matcher:
        cnt = int(matcher.group(1))
        matcher_list = list_json_pattern.findall(content)
        if len(matcher_list) > 0:
            for pkg_matcher in matcher_list:
                child_list.append(app_detail_url_format % pkg_matcher)
    return cnt, child_list


def parse_app_detail(url, content):
    pkg = None
    category = None
    name = None
    download = None
    if 'detail.htm?' in url:
        matcher = apk_pkg_pattern.search(url)
        if matcher:
            pkg = matcher.group(1)
        matcher = apk_category_pattern.search(content)
        if matcher:
            category = matcher.group(1)
        matcher = apk_name_pattern.search(content)
        if matcher:
            name = matcher.group(1)
        matcher = apk_download_pattern.search(content)
        if matcher:
            download = matcher.group(1)
    return pkg, category, name, download
