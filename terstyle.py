#!/usr/bin/env python

## Author : Bibib

import os
from time import sleep

## Colors
grey = '\033[90m'
red = '\033[91m'
green = '\033[92m'
yellow = '\033[93m'
blue = '\033[94m'
purple = '\033[95m'
cyan = '\033[96m'
white = '\033[37m'
off = '\033[m'

## Directories
TERMUX_DIR = "/data/data/com.termux/files/home/.termux"
THEMES_DIR = "themes"
FONTS_DIR = "fonts"

def banner():
	print(f"""
{purple}▄▄▄▄▄▄▄              {red}  ▄▄▄▄    ▄           ▀▀█
{purple}   █     ▄▄▄    ▄ ▄▄  {red}█▀   ▀ ▄▄█▄▄  ▄   ▄    █     ▄▄▄
{purple}   █    █▀  █   █▀  ▀ {red}▀█▄▄▄    █    ▀▄ ▄▀    █    █▀  █
{purple}   █    █▀▀▀▀   █      {red}   ▀█   █     █▄█     █    █▀▀▀▀
{purple}   █    ▀█▄▄▀   █     {red}▀▄▄▄█▀   ▀▄▄   ▀█      ▀▄▄  ▀█▄▄▀
                                     ▄▀
                                    ▀▀
{red}Author\t{purple}: {green}Bibib 
{red}Github\t{purple}: {green}https://github.com/bi2b/terstyle
{red}Website\t{purple}: {green}https://bibib.my.id/
	""")

def exit():
	print(f"\n{purple}[{red}!{purple}] {green}Bye bye (^_^)\n")
	os.sys.exit()

def reset(word):
	os.system("tput sgr0")
	os.system("tput op")
	print(f"{purple}[{red}!{purple}] {green}{word} applied!")
	sleep(1)
	return main()

def reload_setting():
	print(f"{purple}[{red}!{purple}] {green}Reloading settings..")
	os.system("am broadcast --user 0 -a com.termux.app.reload_style com.termux > /dev/null")
	sleep(0.5)
	
def about():
	print(f"""
{red}Tools Name\t{purple}: {green}TerStyle
{red}Author\t\t{purple}: {green}Bibib 
{red}Github\t\t{purple}: {green}https://github.com/bi2b/
{red}Website\t\t{purple}: {green}https://bibib.my.id/
{red}Created On\t{purple}: {green}Sunday, 23 March 2021
{red}Info\t\t{purple}: {red}TerStyle {green}is a simple script to customize the appearance of the {red}Termux {green}terminal emulator. You can also add your custom {red}fonts {green}or {red}themes {green}in the provided directory. {purple}Fonts format must be {red}.ttf {purple}and themes format must be {red}.properties{purple}!
	""")
	input(f"{green}Enter to return to main menu {purple}: {red}")
	return main()
	
def install_font():
	print(f"\n{purple}[{red}!{purple}] {green}Lists of fonts\n")
	font_count = 1;
	fonts = os.listdir(FONTS_DIR)
	for font in fonts:
		print(f"{purple}[{red}{font_count}{purple}] {green}{font[:-4]}")
		font_count += 1
	print(f"{purple}[{red}0{purple}] {green}Back to main\n")
	
	while 1:
		choose_font = input(f"{green}Choose font {purple}: {red}")
		try:
			if int(choose_font) in range(len(fonts) + 1):
				if int(choose_font) == 0:
					return main()
				else:
					f = fonts[int(choose_font) - 1]
					print(f"{purple}[{red}!{purple}] {green}Applying font {f[:-4]}!")
					sleep(1)
					os.system("cp " + FONTS_DIR + "/" + f + " " + TERMUX_DIR + "/font.ttf")
					reload_setting()
					reset("Font")
			else:
				print(f"{purple}[{red}!{purple}] {green}Invalid option, Try again!")
		except ValueError:
			print(f"{purple}[{red}!{purple}] {green}Invalid option, Try again!")
		
def install_theme():
	print(f"\n{purple}[{red}!{purple}] {green}Lists of themes\n")
	theme_count = 1;
	themes = os.listdir(THEMES_DIR)
	for theme in themes:
		print(f"{purple}[{red}{theme_count}{purple}] {green}{theme[:-11]}")
		theme_count +=1
	print(f"{purple}[{red}0{purple}] {green}Back to main\n")
		
	while 1:
		choose_theme = input(f"{green}Choose theme {purple}: {red}")
		
		try:
			if int(choose_theme) in range(len(themes) + 1):
				if int(choose_theme) == 0:
					return main()
				else:
					t = themes[int(choose_theme) - 1]
					print(f"{purple}[{red}!{purple}] {green}Applying theme {t[:-11]}!")
					sleep(1)
					os.system("cp " + THEMES_DIR + "/" + t + " " + TERMUX_DIR + "/colors.properties")
					reload_setting()
					reset("Themes")
			else:
				print(f"{purple}[{red}!{purple}] {green}Invalid option, Try again!")
		except ValueError:
			print(f"{purple}[{red}!{purple}] {green}Invalid option, Try again!")
	
def install_extra_key():
	print(f"\n{purple}[{red}1{purple}] {green}Default")
	print(f"{purple}[{red}2{purple}] {green}Default + left and right keys")
	print(f"{purple}[{red}3{purple}] {green}Two rows with more keys")
	print(f"{purple}[{red}4{purple}] {green}Swipe up from an extra key")
	print(f"{purple}[{red}0{purple}] {green}Back to main\n")
	
	while 1:
		menu = input(f"{green}Choose key type {purple}: {red}")
		if menu == '1':
			extra_key = "extra-keys = [[ESC, TAB, CTRL, ALT, {key: '-', popup: '|'}, DOWN, UP]]"
			with open(TERMUX_DIR + "/termux.properties", "w") as f:
				f.write(extra_key)
				print(f"\n{purple}[{red}!{purple}] {green}Applying extra keys")
			sleep(1)
			reload_setting()
			reset("Extra keys")
		elif menu == '2':
			extra_key = "extra-keys = [[ESC, TAB, CTRL, ALT, LEFT, RIGHT, DOWN, UP]]"
			with open(TERMUX_DIR + "/termux.properties", "w") as f:
				f.write(extra_key)
				print(f"\n{purple}[{red}!{purple}] {green}Applying extra keys")
			sleep(1)
			reload_setting()
			reset("Extra keys")
		elif menu == '3':
			extra_key = """
extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'], \
['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]
			"""
			with open(TERMUX_DIR + "/termux.properties", "w") as f:
				f.write(extra_key)
				print(f"\n{purple}[{red}!{purple}] {green}Applying extra keys")
			sleep(1)
			reload_setting()
			reset("Extra keys")
		elif menu == '4':
			extra_key = """
extra-keys = [[ \
	{key: ESC, popup: {macro: "CTRL f d", display: "tmux exit"}}, \
	{key: CTRL, popup: {macro: "CTRL f BKSP", display: "tmux ←"}}, \
	{key: ALT, popup: {macro: "CTRL f TAB", display: "tmux →"}}, \
	{key: TAB, popup: {macro: "ALT a", display: A-a}}, \
	{key: LEFT, popup: HOME}, \
	{key: DOWN, popup: PGDN}, \
	{key: UP, popup: PGUP}, \
	{key: RIGHT, popup: END}, \
	{macro: "ALT j", display: A-j, popup: {macro: "ALT g", display: A-g}}, \
	{key: KEYBOARD, popup: {macro: "CTRL d", display: exit}} \
]]
			"""
			with open(TERMUX_DIR + "/termux.properties", "w") as f:
				f.write(extra_key)
				print(f"\n{purple}[{red}!{purple}] {green}Applying extra keys")
			sleep(1)
			reload_setting()
			reset("Extra keys")
		elif menu == '0':
			return main()
		else:
			print(f"{purple}[{red}!{purple}] {green}Invalid option, Try again!")
	
def main():
	os.system("clear")
	themes_count = os.listdir("themes")
	fonts_count = os.listdir("fonts")
	banner()
	print(f"{purple}[{red}1{purple}] {green}Install font {purple}({red}{len(fonts_count)}{purple})")
	print(f"{purple}[{red}2{purple}] {green}Install theme {purple}({red}{len(themes_count)}{purple})")
	print(f"{purple}[{red}3{purple}] {green}Install extra keys {purple}({red}4{purple})")
	print(f"{purple}[{red}4{purple}] {green}About")
	print(f"{purple}[{red}0{purple}] {green}Exit\n")
	
	while 1:
		choose = input(f"{green}Choose menu {purple}: {red}")
		
		if choose == '1':
			install_font()
		elif choose == '2':
			install_theme()
		elif choose == '3':
			install_extra_key()
		elif choose == '4':
			about()
		elif choose == '0':
			exit()
		else:
			print(f"{purple}[{red}!{purple}] {green}Invalid option, Try again!")
	
if __name__ == '__main__':
	main()