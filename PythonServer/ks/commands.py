# -*- coding: utf-8 -*-

# python imports
import sys
import struct
from enum import Enum

PY3 = sys.version_info > (3,)


class EMoveDir(Enum):
	Up = 0
	Right = 1
	Down = 2
	Left = 3


class EFireDir(Enum):
	Up = 0
	UpRight = 1
	Right = 2
	RightDown = 3
	Down = 4
	DownLeft = 5
	Left = 6
	LeftUp = 7


class Move(object):

	@staticmethod
	def name():
		return 'Move'


	def __init__(self, id=None, dir=None):
		self.initialize(id, dir)
	

	def initialize(self, id=None, dir=None):
		self.id = id
		self.dir = dir
	

	def serialize(self):
		s = b''
		
		# serialize self.id
		s += b'\x00' if self.id is None else b'\x01'
		if self.id is not None:
			s += struct.pack('i', self.id)
		
		# serialize self.dir
		s += b'\x00' if self.dir is None else b'\x01'
		if self.dir is not None:
			s += struct.pack('b', self.dir.value)
		
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
		
		# deserialize self.dir
		tmp1 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp1:
			tmp2 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
			self.dir = EMoveDir(tmp2)
		else:
			self.dir = None
		
		return offset


class Enter(object):

	@staticmethod
	def name():
		return 'Enter'


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


class Fire(object):

	@staticmethod
	def name():
		return 'Fire'


	def __init__(self, id=None, dir=None):
		self.initialize(id, dir)
	

	def initialize(self, id=None, dir=None):
		self.id = id
		self.dir = dir
	

	def serialize(self):
		s = b''
		
		# serialize self.id
		s += b'\x00' if self.id is None else b'\x01'
		if self.id is not None:
			s += struct.pack('i', self.id)
		
		# serialize self.dir
		s += b'\x00' if self.dir is None else b'\x01'
		if self.dir is not None:
			s += struct.pack('b', self.dir.value)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.id
		tmp4 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp4:
			self.id = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.id = None
		
		# deserialize self.dir
		tmp5 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp5:
			tmp6 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
			self.dir = EFireDir(tmp6)
		else:
			self.dir = None
		
		return offset
