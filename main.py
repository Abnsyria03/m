from pyrogram import Client
from pyrogram import  filters,enums
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import InlineKeyboardMarkup as mk, InlineKeyboardButton as btn
from pyrogram.types import ChatPermissions

from asSQL import Client as cl


data = cl("protect")
db = data['data']
db.create_table()
db.set("botname",['عهد' , 'عهود' , 'بوت' ,'عاهد' , 'عهو'])
db.set("bad_words",['كس','عير','طيز','زب','كسمك','كسختك','طيزك','مص'])

plugins = dict(root="plugins")

Client("x",
api_id=19312827,
api_hash="84da7f08e87849853b2fa6728e4192a2",
bot_token="6386097799:AAGG4tgUXp3r7friQJwOlwoJh_IWUz6Oqug", plugins=plugins).run()