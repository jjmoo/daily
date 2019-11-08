def map_tx_category(category):
    if u'动作冒险' == category \
            or u'休闲益智' == category \
            or u'动作冒险' == category \
            or u'休闲益智' == category \
            or u'网络游戏' == category \
            or u'棋牌中心' == category \
            or u'飞行射击' == category \
            or u'经营策略' == category \
            or u'角色扮演' == category \
            or u'体育竞技' == category \
            or u'游戏' == category:
        return AppClassify.TYPE_GAMES
    elif u'' == category or u'default' == category:
        return AppClassify.TYPE_FAILED
    else:
        return {
            u'视频': AppClassify.TYPE_VIDEO,
            u'音乐': AppClassify.TYPE_MUSIC,
            u'购物': AppClassify.TYPE_SHOP,
            u'阅读': AppClassify.TYPE_BOOK,
            u'导航': AppClassify.TYPE_MAPS,
            u'社交': AppClassify.TYPE_SOCIAL,
            u'摄影': AppClassify.TYPE_CAMERA,
            u'新闻': AppClassify.TYPE_NEWS,
            u'工具': AppClassify.TYPE_LIFESERVICE,
            u'美化': AppClassify.TYPE_LIFESERVICE,
            u'教育': AppClassify.TYPE_EXAM,
            u'生活': AppClassify.TYPE_LIFESERVICE,
            u'安全': AppClassify.TYPE_BOOST,
            u'旅游': AppClassify.TYPE_TRAVEL,
            u'儿童': AppClassify.TYPE_LIFESERVICE,
            u'理财': AppClassify.TYPE_INVESTMENT,
            u'系统': AppClassify.TYPE_BOOST,
            u'健康': AppClassify.TYPE_LIFESERVICE,
            u'娱乐': AppClassify.TYPE_LIFESERVICE,
            u'办公': AppClassify.TYPE_LIFESERVICE,
            u'通讯': AppClassify.TYPE_MESSAGING,
            u'出行': AppClassify.TYPE_MAPS
        }.get(category, AppClassify.TYPE_UNKNOWN)


def map_gl_category(category_top, category_sub):
    if 'Sports' == category_sub:
        if 'GAME' in category_top:
            return AppClassify.TYPE_GAMES
        else:
            return AppClassify.TYPE_LIFESERVICE
    elif 'Action' == category_sub \
            or 'Adventure' == category_sub \
            or 'Arcade' == category_sub \
            or 'Board' == category_sub \
            or 'Card' == category_sub \
            or 'Casino' == category_sub \
            or 'Casual' == category_sub \
            or 'Educational' == category_sub \
            or 'Music' == category_sub \
            or 'Puzzle' == category_sub \
            or 'Racing' == category_sub \
            or 'Role Playing' == category_sub \
            or 'Simulation' == category_sub \
            or 'Strategy' == category_sub \
            or 'Trivia' == category_sub \
            or 'Word' == category_sub:
        return AppClassify.TYPE_GAMES
    else:
        return {
            'Books & Reference' : AppClassify.TYPE_BOOK,
            'Business' : AppClassify.TYPE_BUSSINESS,
            'Comics' : AppClassify.TYPE_BOOK,
            'Communication' : AppClassify.TYPE_MESSAGING,
            'Education' : AppClassify.TYPE_EXAM,
            'Entertainment' : AppClassify.TYPE_LIFESERVICE,
            'Finance' : AppClassify.TYPE_INVESTMENT,
            'Health & Fitness' : AppClassify.TYPE_LIFESERVICE,
            'Libraries & Demo' : AppClassify.TYPE_LIFESERVICE,
            'Lifestyle' : AppClassify.TYPE_LIFESERVICE,
            'Media & Video' : AppClassify.TYPE_VIDEO,
            'Medical' : AppClassify.TYPE_LIFESERVICE,
            'Music & Audio' : AppClassify.TYPE_MUSIC,
            'News & Magazines' : AppClassify.TYPE_NEWS,
            'Personalization' : AppClassify.TYPE_LIFESERVICE,
            'Photography' : AppClassify.TYPE_CAMERA,
            'Productivity' : AppClassify.TYPE_LIFESERVICE,
            'Shopping' : AppClassify.TYPE_SHOP,
            'Social' : AppClassify.TYPE_SOCIAL,
            'Tools' : AppClassify.TYPE_LIFESERVICE,
            'Transportation' : AppClassify.TYPE_LANGUAGELEARN,
            'Travel & Local' : AppClassify.TYPE_TRAVEL,
            'Weather' : AppClassify.TYPE_WEATHER
        }.get(category_sub, AppClassify.TYPE_UNKNOWN)


class AppClassify:
    def __init__(self):
        pass
    TYPE_FAILED = 'FAILED'
    TYPE_UNKNOWN = 'UNKNOWN'
    TYPE_MESSAGING = 'MESSAGING'
    TYPE_MAILBOX = 'MAILBOX'
    TYPE_VOIP = 'VOIP'
    TYPE_WEATHER = 'WEATHER'
    TYPE_CLOCK = 'CLOCK'
    TYPE_NEWS = 'NEWS'
    TYPE_LIFESERVICE = 'LIFESERVICE'
    TYPE_VPN = 'VPN'
    TYPE_MUSIC = 'MUSIC'
    TYPE_BUSSINESS = 'BUSSINESS'
    TYPE_CAMERA = 'CAMERA'
    TYPE_VIDEO = 'VIDEO'
    TYPE_LIVESTREAMING = 'LIVESTREAMING'
    TYPE_MAPS = 'MAPS'
    TYPE_VEHICLE = 'VEHICLE'
    TYPE_TRAVEL = 'TRAVEL'
    TYPE_ACCOUNTS = 'ACCOUNTS'
    TYPE_TAXI = 'TAXI'
    TYPE_SHOP = 'SHOP'
    TYPE_BOOK = 'BOOK'
    TYPE_RECRUIT = 'RECRUIT'
    TYPE_PEDOMETER = 'PEDOMETER'
    TYPE_PAY = 'PAY'
    TYPE_BANK = 'BANK'
    TYPE_INVESTMENT = 'INVESTMENT'
    TYPE_GAMES = 'GAMES'
    TYPE_INDIVIDUATION = 'INDIVIDUATION'
    TYPE_MARRAGE = 'MARRAGE'
    TYPE_LIFESEVICE = 'LIFESEVICE'
    TYPE_LAUNCHER = 'LAUNCHER'
    TYPE_EXAM = 'EXAM'
    TYPE_LANGUAGELEARN = 'LANGUAGELEARN'
    TYPE_DICTIONARY = 'DICTIONARY'
    TYPE_DICTIONARYK = 'DICTIONARYK'
    TYPE_INPUTMETHOD = 'INPUTMETHOD'
    TYPE_BABYCARE = 'BABYCARE'
    TYPE_BOOST = 'BOOST'
    TYPE_BROWSER = 'BROWSER'
    TYPE_FILEMANAGE = 'FILEMANAGE'
    TYPE_MESSAGEING = 'MESSAGEING'
    TYPE_SOCIAL = 'SOCIAL'

