import os
import asyncio

from aiogram import F, Router
from Keyboards import kb_main
from aiogram.types import CallbackQuery, FSInputFile, Message

router = Router(name=__name__)


all_media_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'media')

"""
@router.message(F.text == "UpLoadMedia")
async def get_life(message: Message):

    photo_file1 = FSInputFile(path=os.path.join(all_media_dir, 'news.jpg'))
    IDDQD=await message.answer_photo(photo=photo_file1)
    print(IDDQD.photo[-1].file_id,"news.jpg")
    video_file = FSInputFile(path=os.path.join(all_media_dir, 'Chess.MP4'))
    IDKFA = await message.answer_video(video=video_file)
    print(IDKFA.video.file_id, "Chess.MP4")
    video_file = FSInputFile(path=os.path.join(all_media_dir, 'Film.mp4'))
    IDCLIP = await message.answer_video(video=video_file)
    print(IDCLIP.video.file_id, "Film.MP4")
    
    mp3_file = FSInputFile(path=os.path.join(all_media_dir, 'Music.mp3'))
    aaaaa = await message.answer_voice(voice=mp3_file)
    await asyncio.sleep(5)
    print(aaaaa.voice.file_id, "Misic.mp3")

AwACAgIAAxkDAAIDxGdfPrvW8sNfTapgTt0-cTXUKiR6AAJ9XwACfIIBS3tuc_XNdshtNgQ Misic.mp3
AgACAgIAAxkDAAIDqGdfMA76dI7l3wHSCFB_u7m79_SuAAJV5TEbfIIBS-e8axjrNLetAQADAgADeAADNgQ news.jpg
BAACAgIAAxkDAAIDuWdfOwpfQ2ThxZOSdOEEzdYZtN7LAAI_XwACfIIBSzI87Et-cSlcNgQ Chess.MP4
BAACAgIAAxkDAAIDumdfOwt2vgaeO9dkd_Gt9puEFkNrAAJAXwACfIIBS_YUablIVMs1NgQ Film.MP4
"""

@router.callback_query(F.data == "product_buying1")
async def get_life(message: CallbackQuery):
    await message.message.answer_photo(photo="AgACAgIAAxkDAAIDqGdfMA76dI7l3wHSCFB_u7m79_SuAAJV5TEbfIIBS-e8axjrNLetAQADAgADeAADNgQ",
                                       caption="Вы приобрели Новость")
    await message.answer("")

@router.callback_query(F.data == "product_buying2")
async def get_life(message: CallbackQuery):
    await message.message.answer_voice(voice="AwACAgIAAxkDAAIDxGdfPrvW8sNfTapgTt0-cTXUKiR6AAJ9XwACfIIBS3tuc_XNdshtNgQ",
                                       caption="Вы купили трэк")
    await message.answer("")

@router.callback_query(F.data == "product_buying3")
async def get_life(message: CallbackQuery):
    await message.message.answer_video(video="BAACAgIAAxkDAAIDuWdfOwpfQ2ThxZOSdOEEzdYZtN7LAAI_XwACfIIBSzI87Et-cSlcNgQ",
                                       caption='Вы купили урок по шахматам')
    await message.answer("")


@router.callback_query(F.data == "product_buying4")
async def get_life(message: CallbackQuery):
    await message.message.answer_video(video="BAACAgIAAxkDAAIDumdfOwt2vgaeO9dkd_Gt9puEFkNrAAJAXwACfIIBS_YUablIVMs1NgQ",
                                       caption="Вы купили блокбастер")
    await message.answer("")

@router.callback_query(F.data == "back_to_main")
async def get_life(message: CallbackQuery):
    await message.message.edit_text("Главное меню:",
                         reply_markup=kb_main)
    await message.answer("")
