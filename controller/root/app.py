#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.config import Config
from .root import FlashRoot
from controller.flasher import FlasherManager
from controller.history import HistoryManager
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
		
	def load_managers(self):
		self.flasher = FlasherManager('sources/rc1.csv')
		self.history = HistoryManager()
		
		self.flasher.app = self
		self.history.app = self

	def load_keyboard_listeners(self):
		self.keyboard_listeners = [
			self.flasher.keyboard_hook,
			self.history.keyboard_hook,
		]

	def build(self):
		self.set_window_size()
		self.load_managers()
		self.load_keyboard_listeners()
		self.root = FlashRoot()
		self.root.app = self
		return self.root
