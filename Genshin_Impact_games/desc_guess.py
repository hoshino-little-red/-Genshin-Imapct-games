# ref: https://github.com/GWYOG/GWYOG-Hoshino-plugins/blob/master/pcrdescguess
# Originally written by @GWYOG
# Reflacted by @Ice-Cirno
# GPL-3.0 Licensed
# Thanks to @GWYOG for his great contribution!

import asyncio
import os
import random

from hoshino import Service
from hoshino.modules.Genshin_Impact_games import chara
from hoshino.typing import CQEvent, MessageSegment as Seg

from . import _Genshin_Impact_data
from . import GameMaster


PREPARE_TIME = 8
ONE_TURN_TIME = 5
TURN_NUMBER = 4
DB_PATH = os.path.expanduser("~/.hoshino/Genshin_Impact_desc_guess.db")

gm = GameMaster(DB_PATH)
sv = Service("Genshin-desc-guess", bundle="pcr娱乐", help_="""
[猜原神角色] 猜猜bot在描述哪位角色
[猜原神角色排行] 显示小游戏的群排行榜(只显示前十)
""".strip()
)


@sv.on_fullmatch(("猜原神角色排行", "猜原神角色排名", "猜原神角色排行榜", "猜原神角色群排行"))
async def description_guess_group_ranking(bot, ev: CQEvent):
    ranking = gm.db.get_ranking(ev.group_id)
    msg = ["【猜角色小游戏排行榜】"]
    for i, item in enumerate(ranking):
        uid, count = item
        m = await bot.get_group_member_info(self_id=ev.self_id, group_id=ev.group_id, user_id=uid)
        name = m["card"] or m["nickname"] or str(uid)
        msg.append(f"第{i + 1}名：{name} 猜对{count}次")
    await bot.send(ev, "\n".join(msg))


@sv.on_fullmatch(("猜原神角色", "猜原神人物"))
async def description_guess(bot, ev: CQEvent):
    if gm.is_playing(ev.group_id):
        await bot.finish(ev, "游戏仍在进行中…")
    with gm.start_game(ev.group_id) as game:
        game.answer = random.choice(list(_Genshin_Impact_data.CHARA_PROFILE.keys()))
        profile = _Genshin_Impact_data.CHARA_PROFILE[game.answer]
        kws = list(profile.keys())
        key1name = ['生日','武器类型']
        key2name = ['瞳色', '发色']
        key3name = ['日文声优', '中文声优']
        key4name = ['称号', '所属国家','命之座']
        random.shuffle(key1name)
        random.shuffle(key2name)
        random.shuffle(key3name)
        random.shuffle(key4name)
        kws.clear()
        kws.append(key1name[0])
        kws.append(key2name[0])
        kws.append(key3name[0])
        kws.append(key4name[0])
        await bot.send(ev, f"{PREPARE_TIME}秒后每隔{ONE_TURN_TIME}秒我会给出某位角色的一个描述，根据这些描述猜猜TA是谁~")
        await asyncio.sleep(PREPARE_TIME)
        for i, k in enumerate(kws):
            await bot.send(ev, f"提示{i + 1}/{len(kws)}:\nTA的{k}是 {profile[k]}")
            await asyncio.sleep(ONE_TURN_TIME)
            if game.winner:
                return
        c = chara.fromid(game.answer)
    await bot.send(ev, f"正确答案是：{c.name} {c.icon.cqcode}\n")


@sv.on_message()
async def on_input_chara_name(bot, ev: CQEvent):
    game = gm.get_game(ev.group_id)
    if not game or game.winner:
        return
    c = chara.fromname(ev.message.extract_plain_text())
    if c.id != chara.UNKNOWN and c.id == game.answer:
        game.winner = ev.user_id
        n = game.record()
        msg = f"正确答案是：{c.name}{c.icon.cqcode}\n{Seg.at(ev.user_id)}猜对了，真厉害！\n(此轮游戏将在几秒后自动结束，请耐心等待)"
        await bot.send(ev, msg)
