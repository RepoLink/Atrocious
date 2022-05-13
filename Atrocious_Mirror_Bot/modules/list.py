from telegram.ext import CommandHandler
from Atrocious_Mirror_Bot.helper.mirror_utils.upload_utils.gdriveTools import GoogleDriveHelper
from Atrocious_Mirror_Bot import LOGGER, dispatcher
from Atrocious_Mirror_Bot.helper.telegram_helper.message_utils import sendMessage, editMessage
from Atrocious_Mirror_Bot.helper.telegram_helper.filters import CustomFilters
from Atrocious_Mirror_Bot.helper.telegram_helper.bot_commands import BotCommands


def list_drive(update, context):
    try:
        search = update.message.text.split(' ', maxsplit=1)[1]
        LOGGER.info(f"Searching: {search}")
        reply = sendMessage('Searching..... Please wait!', context.bot, update)
        gdrive = GoogleDriveHelper()
        msg, button = gdrive.drive_list(search)

        if button:
            editMessage(msg, reply, button)
        else:
            editMessage(f'No result found for <code>{search}</code>', reply, button)

    except IndexError:
        sendMessage('Send a search key along with command', context.bot, update)


list_handler = CommandHandler(BotCommands.ListCommand, list_drive, filters=CustomFilters.authorized_chat | CustomFilters.authorized_user, run_async=True)
dispatcher.add_handler(list_handler)
