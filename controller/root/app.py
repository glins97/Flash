#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.config import Config
from .root import FlashRoot
from controller.flasher import FlasherManager
from kivy.base import EventLoop


class Flash(App):
	keyboard_listeners = []

	def on_start(self):
		for listener in self.keyboard_listeners:
			EventLoop.window.bind(on_keyboard=listener)

	def set_window_size(self):
		ratio = 16/9
		base = 500
		width, height = int(base * ratio), int(base)
		
		Config.set('graphics', 'width', width)
		Config.set('graphics', 'height', height)
		
	def build(self):
		self.set_window_size()
		self.flasher = FlasherManager('sources/rc1.csv')
		self.keyboard_listeners.append(self.flasher.keyboard_hook)
		self.root = FlashRoot()
		self.root.app = self
		return self.root
