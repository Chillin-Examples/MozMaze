# -*- coding: utf-8 -*-

# python imports
import sys
import struct
from enum import Enum

PY3 = sys.version_info > (3,)


class Move(object):

	@staticmethod
	def name():
		return 'Move'


	def __init__(self, id=None):
		self.initialize(id)
	

	def initialize(self, id=None):
		self.id = id
	

	def serialize(self):
		s = b''
		
		# serialize self.id
		s += b'\x00' if self.id is None else b'\x01'
		if self.id is not None:
			s += struct.pack('i', self.id)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.id
		tmp0 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp0:
			self.id = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.id = None
		
		return offset


class Turn(object):

	@staticmethod
	def name():
		return 'Turn'


	def __init__(self, id=None, clockwise=None):
		self.initialize(id, clockwise)
	

	def initialize(self, id=None, clockwise=None):
		self.id = id
		self.clockwise = clockwise
	

	def serialize(self):
		s = b''
		
		# serialize self.id
		s += b'\x00' if self.id is None else b'\x01'
		if self.id is not None:
			s += struct.pack('i', self.id)
		
		# serialize self.clockwise
		s += b'\x00' if self.clockwise is None else b'\x01'
		if self.clockwise is not None:
			s += struct.pack('?', self.clockwise)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.id
		tmp1 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp1:
			self.id = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.id = None
		
		# deserialize self.clockwise
		tmp2 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp2:
			self.clockwise = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.clockwise = None
		
		return offset


class Fire(object):

	@staticmethod
	def name():
		return 'Fire'


	def __init__(self, id=None):
		self.initialize(id)
	

	def initialize(self, id=None):
		self.id = id
	

	def serialize(self):
		s = b''
		
		# serialize self.id
		s += b'\x00' if self.id is None else b'\x01'
		if self.id is not None:
			s += struct.pack('i', self.id)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.id
		tmp3 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp3:
			self.id = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.id = None
		
		return offset
