'''原神的游戏数据'''

'''角色名称

遵照格式： id: [官译简体, 日文原名, 英文名(罗马音), 常见别称,] （<-依此顺序）目前只写了官译简体及英文
'''
CHARA_NAME = {
    101: ["阿贝多", "Albedo"],
    102: ["安柏", "Amber"],
    103: ["芭芭拉", "Barbara"],
    104: ["北斗", "Beidou"],
    105: ["班尼特", "Bennett"],
    106: ["重云", "Chongyun"],
    107: ["迪卢克", "Diluc"],
    108: ["迪奥娜", "Diona"],
    109: ["菲谢尔", "Fischl"],
    110: ["琴", "Jean"],
    111: ["凯亚", "Kaeya"],
    112: ["刻晴", "Keqing"],
    113: ["可莉", "Klee"],
    114: ["丽莎", "Lisa"],
    115: ["莫娜", "Mona"],
    116: ["凝光", "Ningguang"],
    117: ["七七", "Qiqi"],
    118: ["雷泽", "Razor"],
    119: ["砂糖", "Sucrose"],
    120: ["达达利亚", "Tartaglia"],
    121: ["荧", "Lumine"],
    122: ["空", "Aether"],
    123: ["温迪", "Venti"],
    124: ["香菱", "Xiangling"],
    125: ["行秋", "Xingqiu"],
    126: ["辛焱", "Xinyan"],
    127: ["钟离", "Zhongli"],
    128: ["派蒙","Paimon"],
    129: ["诺艾尔","Noelle"],
}

CHARA_PROFILE = {
    101: {"名字": "阿贝多", "所属国家": "蒙德", "生日": "9月13日", "角色属性": "岩", "武器类型": "单手剑","命之座":"白垩之子座","发色":"银发","瞳色":"蓝瞳",
          "日文声优": "野岛健儿", "中文声优": "Mace", "称号": "白垩之子"},
    102: {"名字": "安柏", "所属国家": "蒙德", "生日": "8月10日", "角色属性": "火", "武器类型": "弓","命之座":"小兔座","发色":"棕发","瞳色":"金瞳",
          "日文声优": "石见舞菜香", "中文声优": "牛奶君", "称号": "侦查骑士"},
    103: {"名字": "芭芭拉", "所属国家": "蒙德", "生日": "7月5日", "角色属性": "水", "武器类型": "法器","命之座":"金杯座","发色":"金发","瞳色":"蓝瞳",
          "日文声优": "鬼头明里", "中文声优": "宋媛媛", "称号": "内鬼"},
    104: {"名字": "北斗", "所属国家": "璃月", "生日": "2月14日", "角色属性": "雷", "武器类型": "双手剑","命之座":"南天海山座","发色":"黑发","瞳色":"红瞳",
          "日文声优": "小清水亚美", "中文声优": "唐雅菁", "称号": "无冕的龙王"},
    105: {"名字": "班尼特", "所属国家": "蒙德", "生日": "2月29日", "角色属性": "火", "武器类型": "单手剑","命之座":"险路座","发色":"金发","瞳色":"绿瞳",
          "日文声优": "逢坂良太", "中文声优": "穆雪婷", "称号": "命运试金石"},
    106: {"名字": "重云", "所属国家": "璃月", "生日": "9月7日", "角色属性": "冰", "武器类型": "双手剑","命之座":"乾坤锋座","发色":"蓝发","瞳色":"蓝瞳",
          "日文声优": "齐藤壮马", "中文声优": "kinsen", "称号": "雪融有踪"},
    107: {"名字": "迪卢克", "所属国家": "蒙德", "生日": "4月30日", "角色属性": "火", "武器类型": "双手剑","命之座":"夜枭座","发色":"红发","瞳色":"红瞳",
          "日文声优": "小野贤章", "中文声优": "马洋", "称号": "正义人"},
    108: {"名字": "迪奥娜", "所属国家": "蒙德", "生日": "1月18日", "角色属性": "冰", "武器类型": "弓","命之座":"小猫座","发色":"粉发","瞳色":"绿瞳",
          "日文声优": "井泽诗织", "中文声优": "诺亚", "称号": "酒业杀手"},
    109: {"名字": "菲谢尔", "所属国家": "蒙德", "生日": "5月27日", "角色属性": "雷", "武器类型": "弓","命之座":"幻鸦座","发色":"金发","瞳色":"绿瞳",
          "日文声优": "内田真礼", "中文声优": "Mace", "称号": "断罪之皇女"},
    110: {"名字": "琴", "所属国家": "蒙德", "生日": "3月14日", "角色属性": "风", "武器类型": "单手剑","命之座":"幼狮座","发色":"金发","瞳色":"蓝瞳",
          "日文声优": "斋藤千和", "中文声优": "林簌", "称号": "蒲公英骑士"},
    111: {"名字": "凯亚", "所属国家": "蒙德", "生日": "11月30日", "角色属性": "冰", "武器类型": "单手剑","命之座":"孔雀羽座","发色":"蓝发","瞳色":"蓝瞳",
          "日文声优": "鸟海浩辅", "中文声优": "孙晔", "称号": "踏冰渡海真君"},
    112: {"名字": "刻晴", "所属国家": "璃月", "生日": "11月20日", "角色属性": "雷", "武器类型": "单手剑","命之座":"金紫定垂座","发色":"紫发","瞳色":"紫瞳",
          "日文声优": "喜多村英梨", "中文声优": "谢莹", "称号": "璃月刮痧真君"},
    113: {"名字": "可莉", "所属国家": "蒙德", "生日": "7月27日", "角色属性": "火", "武器类型": "法器","命之座":"四叶草座","发色":"金发","瞳色":"红瞳",
          "日文声优": "久野美咲", "中文声优": "fa玲", "称号": "放火烧山真君"},
    114: {"名字": "丽莎", "所属国家": "蒙德", "生日": "6月9日", "角色属性": "雷", "武器类型": "法器","命之座":"沙漏座","发色":"棕发","瞳色":"绿瞳",
          "日文声优": "田中理惠", "中文声优": "钟可", "称号": "蔷薇魔女"},
    115: {"名字": "莫娜", "所属国家": "蒙德", "生日": "8月31日", "角色属性": "水", "武器类型": "法器","命之座":"映天座","发色":"紫发","瞳色":"绿瞳",
          "日文声优": "小原好美", "中文声优": "陈婷婷", "称号": "星天水镜"},
    116: {"名字": "凝光", "所属国家": "璃月", "生日": "8月26日", "角色属性": "岩", "武器类型": "法器","命之座":"玑衡仪座","发色":"银发","瞳色":"红瞳",
          "日文声优": "大原沙耶香", "中文声优": "杜冥鸦", "称号": "天权星"},
    117: {"名字": "七七", "所属国家": "璃月", "生日": "3月3日", "角色属性": "冰", "武器类型": "单手剑","命之座":"三清铃座","发色":"紫发","瞳色":"粉瞳",
          "日文声优": "田村由香里", "中文声优": "宴宁", "称号": "冻冻回魂夜"},
    118: {"名字": "雷泽", "所属国家": "蒙德", "生日": "9月9日", "角色属性": "雷", "武器类型": "双手剑","命之座":"小狼座","发色":"银发","瞳色":"红瞳",
          "日文声优": "内山昂辉", "中文声优": "周帅", "称号": "奔狼领的传说"},
    119: {"名字": "砂糖", "所属国家": "蒙德", "生日": "11月26日", "角色属性": "风", "武器类型": "法器","命之座":"烧瓶座","发色":"绿发","瞳色":"橙瞳",
          "日文声优": "藤田茜", "中文声优": "小敢", "称号": "雷莹术士"},
    120: {"名字": "达达利亚", "所属国家": "至冬", "生日": "7月20日", "角色属性": "水", "武器类型": "弓","命之座":"鲸天座","发色":"黄发","瞳色":"蓝瞳",
          "日文声优": "木村良平", "中文声优": "鱼冻", "称号": "玩具销售员"},
    121: {"名字": "荧", "所属国家": "???", "生日": "???", "角色属性": "???", "武器类型": "单手剑","命之座":"旅人座","发色":"金发","瞳色":"橙瞳",
          "日文声优": "悠木碧", "中文声优": "宴宁", "称号": "妹妹"},
    122: {"名字": "空", "所属国家": "???", "生日": "???", "角色属性": "???", "武器类型": "单手剑","命之座":"旅人座","发色":"金发","瞳色":"橙瞳",
          "日文声优": "堀江瞬", "中文声优": "鹿喑", "称号": "哥哥"},
    123: {"名字": "温迪", "所属国家": "蒙德", "生日": "6月16日", "角色属性": "风", "武器类型": "弓","命之座":"歌仙座","发色":"黑发","瞳色":"绿瞳",
          "日文声优": "村濑步", "中文声优": "喵☆酱", "称号": "摸鱼"},
    124: {"名字": "香菱", "所属国家": "璃月", "生日": "11月2日", "角色属性": "火", "武器类型": "长柄武器","命之座":"长杓座","发色":"蓝发","瞳色":"金瞳",
          "日文声优": "小泽亚李", "中文声优": "小N", "称号": "洲际导弹真君"},
    125: {"名字": "行秋", "所属国家": "璃月", "生日": "10月9日", "角色属性": "水", "武器类型": "单手剑","命之座":"锦织座","发色":"蓝发","瞳色":"棕瞳",
          "日文声优": "皆川纯子", "中文声优": "唐雅菁", "称号": "古华飞云"},
    126: {"名字": "辛焱", "所属国家": "璃月", "生日": "10月16日", "角色属性": "火", "武器类型": "双手剑","命之座":"红檀四弦座","发色":"黑发","瞳色":"金瞳",
          "日文声优": "高桥智秋", "中文声优": "王雅欣", "称号": "燥热旋律"},
    127: {"名字": "钟离", "所属国家": "璃月", "生日": "12月31日", "角色属性": "岩", "武器类型": "长柄武器","命之座":"岩王帝君座","发色":"黑发","瞳色":"金瞳",
          "日文声优": "前野智昭", "中文声优": "彭博", "称号": "未来战士"},
    128: {"名字": "派蒙", "所属国家": "？？？", "生日": "6月1日", "角色属性": "???", "武器类型": "???", "命之座": "???","发色":"白发","瞳色":"蓝瞳",
          "日文声优": "古贺葵", "中文声优": "多多poi", "称号": "应急食品"},
    129: {"名字": "诺艾尔", "所属国家": "蒙德", "生日": "3月21日", "角色属性": "岩", "武器类型": "双手剑", "命之座": "心护座","发色":"银发","瞳色":"绿瞳",
          "日文声优": "高尾奏音", "中文声优": "宴宁", "称号": "山吹"},
}
