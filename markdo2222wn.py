import random
import os
import subprocess
from datetime import datetime

# 设置工作目录
script_dir = "/root/autotelegram"

os.chdir(script_dir)

# 定义三个不同的内容





contents = [
'''| [![@TG最强搜索机器人](https://i.imgur.com/uTMZCDf.png)<br>@TG最强搜索机器人](https://t.me/sosoo?start=a_7202424896) |![Telegram频道导航/TG导航/Telegram频道推荐/Telegram导航/频道导航/电报导航/电报推荐/TG推荐](https://i.imgur.com/31YFV0f.png)<br>[Telegram频道导航](https://tg10000.com)   | [![@极搜JiSo](https://i.imgur.com/we9lyse.jpeg)<br>@极搜JiSo](https://t.me/jiso?start=a_7202424896) |
|:---:|:---:|:---:|
|[![@极搜JiSou](https://i.imgur.com/1VoAGvh.png)<br>@极搜JiSou](https://t.me/jisou2bot?start=a_7202424896) |  [![Telegram频道导航/TG导航/Telegram频道推荐/Telegram导航/频道导航/电报导航/电报推荐/TG推荐](https://i.imgur.com/31YFV0f.png)<br>Telegram频道导航](https://tgdh.github.io) |[![@i快搜](https://i.imgur.com/CsCtOBH.png)<br>@i快搜](https://t.me/ikuaisobot?start=7352210715)|
| [![搜片神器](https://i.imgur.com/SVox0Se.png)<br>搜片神器](https://t.me/soupian20w)  |  [![色色搜索](https://i.imgur.com/pwNAjvK.png)<br>❤️色色搜索🔞](https://t.me/sese20w) | [![暗网搜索](https://i.imgur.com/woGNZUA.png)<br>暗网搜索](https://t.me/anwang007)|
| [![彩虹群发破解版/飞机/电报Telegram tdata/低价TG账号/电报资源搜索](https://i.imgur.com/xff6d05.png)<br>电报稀缺资源大全中文搜索](https://t.me/sousuohp)|  [![彩虹群发器/彩虹群发/彩虹群发器破解版](https://i.imgur.com/6a8Zz9h.png)<br>彩虹群发器破解版](https://t.me/autocaihongbot?start=gwHypTpEnF84wUi)  |[![机场导航](https://i.imgur.com/yhw5VPW.png)<br>机场导航大全](https://jichangvpn.github.io/)|''',

'''| [![@TG最强搜索机器人](https://i.imgur.com/uTMZCDf.png)<br>@TG最强搜索机器人](https://t.me/sosoo?start=a_7439567495) |![Telegram频道导航/TG导航/Telegram频道推荐/Telegram导航/频道导航/电报导航/电报推荐/TG推荐](https://i.imgur.com/31YFV0f.png)<br>[Telegram频道导航](https://tg10000.com)   | [![@极搜JiSo](https://i.imgur.com/we9lyse.jpeg)<br>@极搜JiSo](https://t.me/jiso?start=a_7202424896) |
|:---:|:---:|:---:|
|[![@极搜JiSou](https://i.imgur.com/1VoAGvh.png)<br>@极搜JiSou](https://t.me/jisou2bot?start=a_7439567495) |  [![Telegram频道导航/TG导航/Telegram频道推荐/Telegram导航/频道导航/电报导航/电报推荐/TG推荐](https://i.imgur.com/31YFV0f.png)<br>Telegram频道导航](https://tgdh.github.io) |[![@i快搜](https://i.imgur.com/CsCtOBH.png)<br>@i快搜](https://t.me/ikuaisobot?start=7352210715)|
| [![搜片神器](https://i.imgur.com/SVox0Se.png)<br>搜片神器](https://t.me/soupianccav)  |  [![色色搜索](https://i.imgur.com/pwNAjvK.png)<br>❤️色色搜索🔞](https://t.me/sesou20w) | [![暗网搜索](https://i.imgur.com/woGNZUA.png)<br>暗网搜索](https://t.me/anwangsearch)|
| [![彩虹群发破解版/飞机/电报Telegram tdata/低价TG账号/电报资源搜索](https://i.imgur.com/xff6d05.png)<br>电报稀缺资源大全中文搜索](https://t.me/sousuohp)|  [![彩虹群发器/彩虹群发/彩虹群发器破解版](https://i.imgur.com/6a8Zz9h.png)<br>彩虹群发器破解版](https://t.me/autocaihongbot?start=gwHypTpEnF84wUi)  |[![机场导航](https://i.imgur.com/yhw5VPW.png)<br>机场导航大全](https://jichangvpn.github.io/)|''',

'''| [![@TG最强搜索机器人](https://i.imgur.com/uTMZCDf.png)<br>@TG最强搜索机器人](https://t.me/sosoo?start=a_7737195905) |![Telegram频道导航/TG导航/Telegram频道推荐/Telegram导航/频道导航/电报导航/电报推荐/TG推荐](https://i.imgur.com/31YFV0f.png)<br>[Telegram频道导航](https://tg10000.com)   | [![@极搜JiSo](https://i.imgur.com/we9lyse.jpeg)<br>@极搜JiSo](https://t.me/jiso?start=a_7202424896) |
|:---:|:---:|:---:|
|[![@极搜JiSou](https://i.imgur.com/1VoAGvh.png)<br>@极搜JiSou](https://t.me/jisou2bot?start=a_7737195905) |  [![Telegram频道导航/TG导航/Telegram频道推荐/Telegram导航/频道导航/电报导航/电报推荐/TG推荐](https://i.imgur.com/31YFV0f.png)<br>Telegram频道导航](https://tgdh.github.io) |[![@i快搜](https://i.imgur.com/CsCtOBH.png)<br>@i快搜](https://t.me/ikuaisobot?start=7352210715)|
| [![搜片神器](https://i.imgur.com/SVox0Se.png)<br>搜片神器](https://t.me/soupianshenqibar)  |  [![色色搜索](https://i.imgur.com/pwNAjvK.png)<br>❤️色色搜索🔞](https://t.me/sesouccav) | [![暗网搜索](https://i.imgur.com/woGNZUA.png)<br>暗网搜索](https://t.me/anwangbots)|
| [![彩虹群发破解版/飞机/电报Telegram tdata/低价TG账号/电报资源搜索](https://i.imgur.com/xff6d05.png)<br>电报稀缺资源大全中文搜索](https://t.me/sousuohp)|  [![彩虹群发器/彩虹群发/彩虹群发器破解版](https://i.imgur.com/6a8Zz9h.png)<br>彩虹群发器破解版](https://t.me/autocaihongbot?start=gwHypTpEnF84wUi)  |[![机场导航](https://i.imgur.com/yhw5VPW.png)<br>机场导航大全](https://jichangvpn.github.io/)|''',

'''| [![@TG最强搜索机器人](https://i.imgur.com/uTMZCDf.png)<br>@TG最强搜索机器人](https://t.me/sosoo?start=a_7704234080) |![Telegram频道导航/TG导航/Telegram频道推荐/Telegram导航/频道导航/电报导航/电报推荐/TG推荐](https://i.imgur.com/31YFV0f.png)<br>[Telegram频道导航](https://tg10000.com)   | [![@极搜JiSo](https://i.imgur.com/we9lyse.jpeg)<br>@极搜JiSo](https://t.me/jiso?start=a_7704234080) |
|:---:|:---:|:---:|
|[![@极搜JiSou](https://i.imgur.com/1VoAGvh.png)<br>@极搜JiSou](https://t.me/jisou2bot?start=a_7202424896) |  [![Telegram频道导航/TG导航/Telegram频道推荐/Telegram导航/频道导航/电报导航/电报推荐/TG推荐](https://i.imgur.com/31YFV0f.png)<br>Telegram频道导航](https://tgdh.github.io) |[![@i快搜](https://i.imgur.com/CsCtOBH.png)<br>@i快搜](https://t.me/ikuaisobot?start=7352210715)|
| [![搜片神器](https://i.imgur.com/SVox0Se.png)<br>搜片神器](https://t.me/soupianshenqi1314)  |  [![色色搜索](https://i.imgur.com/pwNAjvK.png)<br>❤️色色搜索🔞](https://t.me/sesesousuoba) | [![暗网搜索](https://i.imgur.com/woGNZUA.png)<br>暗网搜索](https://t.me/anwangsearch)|
| [![彩虹群发破解版/飞机/电报Telegram tdata/低价TG账号/电报资源搜索](https://i.imgur.com/xff6d05.png)<br>电报稀缺资源大全中文搜索](https://t.me/sousuohp)|  [![彩虹群发器/彩虹群发/彩虹群发器破解版](https://i.imgur.com/6a8Zz9h.png)<br>彩虹群发器破解版](https://t.me/autocaihongbot?start=gwHypTpEnF84wUi)  |[![机场导航](https://i.imgur.com/yhw5VPW.png)<br>机场导航大全](https://jichangvpn.github.io/)|''',

'''| [![@TG最强搜索机器人](https://i.imgur.com/uTMZCDf.png)<br>@TG最强搜索机器人](https://t.me/sosoo?start=a_7744961564) |![Telegram频道导航/TG导航/Telegram频道推荐/Telegram导航/频道导航/电报导航/电报推荐/TG推荐](https://i.imgur.com/31YFV0f.png)<br>[Telegram频道导航](https://tg10000.com)   | [![@极搜JiSo](https://i.imgur.com/we9lyse.jpeg)<br>@极搜JiSo](https://t.me/jiso?start=a_7744961564) |
|:---:|:---:|:---:|
|[![@极搜JiSou](https://i.imgur.com/1VoAGvh.png)<br>@极搜JiSou](https://t.me/jisou2bot?start=a_7744961564) |  [![Telegram频道导航/TG导航/Telegram频道推荐/Telegram导航/频道导航/电报导航/电报推荐/TG推荐](https://i.imgur.com/31YFV0f.png)<br>Telegram频道导航](https://tgdh.github.io) |[![@i快搜](https://i.imgur.com/CsCtOBH.png)<br>@i快搜](https://t.me/ikuaisobot?start=7352210715)|
| [![搜片神器](https://i.imgur.com/SVox0Se.png)<br>搜片神器](https://t.me/soupianshenqi520)  |  [![色色搜索](https://i.imgur.com/pwNAjvK.png)<br>❤️色色搜索🔞](https://t.me/chengrendaohang520) | [![暗网搜索](https://i.imgur.com/woGNZUA.png)<br>暗网搜索](https://t.me/daohangsese)|
| [![彩虹群发破解版/飞机/电报Telegram tdata/低价TG账号/电报资源搜索](https://i.imgur.com/xff6d05.png)<br>电报稀缺资源大全中文搜索](https://t.me/sousuohp)|  [![彩虹群发器/彩虹群发/彩虹群发器破解版](https://i.imgur.com/6a8Zz9h.png)<br>彩虹群发器破解版](https://t.me/autocaihongbot?start=gwHypTpEnF84wUi)  |[![机场导航](https://i.imgur.com/yhw5VPW.png)<br>机场导航大全](https://jichangvpn.github.io/)|'''

]


def update_readme():
    try:
        # 读取README.md文件
        with open('README.md', 'r', encoding='utf-8') as file:
            content = file.read()

        # 找到标记之间的内容
        start_marker = '<!-- BEGIN_REPLACE_SECTION -->'
        end_marker = '<!-- END_REPLACE_SECTION -->'
        
        start_index = content.find(start_marker)
        end_index = content.find(end_marker)

        if start_index == -1 or end_index == -1:
            raise Exception("未找到标记")

        # 随机选择一个新内容
        new_content = random.choice(contents)

        # 组合新的内容
        updated_content = (
            content[:start_index + len(start_marker)] + 
            '\n' + new_content + '\n' + 
            content[end_index:]
        )

        # 写入新内容
        with open('README.md', 'w', encoding='utf-8') as file:
            file.write(updated_content)

        # Git 操作
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        subprocess.run(['git', 'add', '.'], check=True)
        subprocess.run(['git', 'commit', '-m', f'update table content - {current_date}'], check=True)
        subprocess.run(['git', 'push'], check=True)

        print("已成功更新 README.md 并推送到 GitHub")
        return True

    except Exception as e:
        print(f"发生错误: {str(e)}")
        return False

if __name__ == "__main__":
    update_readme()
