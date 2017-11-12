# -*- coding: utf-8 -*-

# python imports
import sys
import struct
from enum import Enum

PY3 = sys.version_info > (3,)


class ECell(Enum):
	Empty = 0
	Box = 1
	Tree = 2
	PowerUpEmitter = 3


class EPowerUpType(Enum):
	Ammo = 0
	Heal = 1


class EBananaStatus(Enum):
	Alive = 0
	InBox = 1
	Dead = 2


class PowerUp(object):

	@staticmethod
	def name():
		return 'PowerUp'


	def __init__(self, type=None, position=None, apearance_time=None, value=None):
		self.initialize(type, position, apearance_time, value)
	

	def initialize(self, type=None, position=None, apearance_time=None, value=None):
		self.type = type
		self.position = position
		self.apearance_time = apearance_time
		self.value = value
	

	def serialize(self):
		s = b''
		
		# serialize self.type
		s += b'\x00' if self.type is None else b'\x01'
		if self.type is not None:
			s += struct.pack('b', self.type.value)
		
		# serialize self.position
		s += b'\x00' if self.position is None else b'\x01'
		if self.position is not None:
			s += struct.pack('i', self.position)
		
		# serialize self.apearance_time
		s += b'\x00' if self.apearance_time is None else b'\x01'
		if self.apearance_time is not None:
			s += struct.pack('i', self.apearance_time)
		
		# serialize self.value
		s += b'\x00' if self.value is None else b'\x01'
		if self.value is not None:
			s += struct.pack('i', self.value)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.type
		tmp0 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp0:
			tmp1 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
			self.type = EPowerUpType(tmp1)
		else:
			self.type = None
		
		# deserialize self.position
		tmp2 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp2:
			self.position = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.position = None
		
		# deserialize self.apearance_time
		tmp3 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp3:
			self.apearance_time = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.apearance_time = None
		
		# deserialize self.value
		tmp4 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp4:
			self.value = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.value = None
		
		return offset


class Banana(object):

	@staticmethod
	def name():
		return 'Banana'


	def __init__(self, id=None, status=None, position=None, health=None, max_health=None, laser_count=None, max_laser_count=None, laser_range=None, laser_damage=None, curr_reload=None, reload_time=None, death_score=None):
		self.initialize(id, status, position, health, max_health, laser_count, max_laser_count, laser_range, laser_damage, curr_reload, reload_time, death_score)
	

	def initialize(self, id=None, status=None, position=None, health=None, max_health=None, laser_count=None, max_laser_count=None, laser_range=None, laser_damage=None, curr_reload=None, reload_time=None, death_score=None):
		self.id = id
		self.status = status
		self.position = position
		self.health = health
		self.max_health = max_health
		self.laser_count = laser_count
		self.max_laser_count = max_laser_count
		self.laser_range = laser_range
		self.laser_damage = laser_damage
		self.curr_reload = curr_reload
		self.reload_time = reload_time
		self.death_score = death_score
	

	def serialize(self):
		s = b''
		
		# serialize self.id
		s += b'\x00' if self.id is None else b'\x01'
		if self.id is not None:
			s += struct.pack('i', self.id)
		
		# serialize self.status
		s += b'\x00' if self.status is None else b'\x01'
		if self.status is not None:
			s += struct.pack('b', self.status.value)
		
		# serialize self.position
		s += b'\x00' if self.position is None else b'\x01'
		if self.position is not None:
			s += struct.pack('i', self.position)
		
		# serialize self.health
		s += b'\x00' if self.health is None else b'\x01'
		if self.health is not None:
			s += struct.pack('i', self.health)
		
		# serialize self.max_health
		s += b'\x00' if self.max_health is None else b'\x01'
		if self.max_health is not None:
			s += struct.pack('i', self.max_health)
		
		# serialize self.laser_count
		s += b'\x00' if self.laser_count is None else b'\x01'
		if self.laser_count is not None:
			s += struct.pack('i', self.laser_count)
		
		# serialize self.max_laser_count
		s += b'\x00' if self.max_laser_count is None else b'\x01'
		if self.max_laser_count is not None:
			s += struct.pack('i', self.max_laser_count)
		
		# serialize self.laser_range
		s += b'\x00' if self.laser_range is None else b'\x01'
		if self.laser_range is not None:
			s += struct.pack('i', self.laser_range)
		
		# serialize self.laser_damage
		s += b'\x00' if self.laser_damage is None else b'\x01'
		if self.laser_damage is not None:
			s += struct.pack('i', self.laser_damage)
		
		# serialize self.curr_reload
		s += b'\x00' if self.curr_reload is None else b'\x01'
		if self.curr_reload is not None:
			s += struct.pack('i', self.curr_reload)
		
		# serialize self.reload_time
		s += b'\x00' if self.reload_time is None else b'\x01'
		if self.reload_time is not None:
			s += struct.pack('i', self.reload_time)
		
		# serialize self.death_score
		s += b'\x00' if self.death_score is None else b'\x01'
		if self.death_score is not None:
			s += struct.pack('i', self.death_score)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.id
		tmp5 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp5:
			self.id = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.id = None
		
		# deserialize self.status
		tmp6 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp6:
			tmp7 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
			self.status = EBananaStatus(tmp7)
		else:
			self.status = None
		
		# deserialize self.position
		tmp8 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp8:
			self.position = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.position = None
		
		# deserialize self.health
		tmp9 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp9:
			self.health = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.health = None
		
		# deserialize self.max_health
		tmp10 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp10:
			self.max_health = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.max_health = None
		
		# deserialize self.laser_count
		tmp11 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp11:
			self.laser_count = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.laser_count = None
		
		# deserialize self.max_laser_count
		tmp12 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp12:
			self.max_laser_count = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.max_laser_count = None
		
		# deserialize self.laser_range
		tmp13 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp13:
			self.laser_range = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.laser_range = None
		
		# deserialize self.laser_damage
		tmp14 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp14:
			self.laser_damage = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.laser_damage = None
		
		# deserialize self.curr_reload
		tmp15 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp15:
			self.curr_reload = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.curr_reload = None
		
		# deserialize self.reload_time
		tmp16 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp16:
			self.reload_time = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.reload_time = None
		
		# deserialize self.death_score
		tmp17 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp17:
			self.death_score = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.death_score = None
		
		return offset


class World(object):

	@staticmethod
	def name():
		return 'World'


	def __init__(self, width=None, height=None, scores=None, board=None, bananas=None, powerups=None, enter_score=None):
		self.initialize(width, height, scores, board, bananas, powerups, enter_score)
	

	def initialize(self, width=None, height=None, scores=None, board=None, bananas=None, powerups=None, enter_score=None):
		self.width = width
		self.height = height
		self.scores = scores
		self.board = board
		self.bananas = bananas
		self.powerups = powerups
		self.enter_score = enter_score
	

	def serialize(self):
		s = b''
		
		# serialize self.width
		s += b'\x00' if self.width is None else b'\x01'
		if self.width is not None:
			s += struct.pack('i', self.width)
		
		# serialize self.height
		s += b'\x00' if self.height is None else b'\x01'
		if self.height is not None:
			s += struct.pack('i', self.height)
		
		# serialize self.scores
		s += b'\x00' if self.scores is None else b'\x01'
		if self.scores is not None:
			tmp18 = b''
			tmp18 += struct.pack('I', len(self.scores))
			while len(tmp18) and tmp18[-1] == b'\x00'[0]:
				tmp18 = tmp18[:-1]
			s += struct.pack('B', len(tmp18))
			s += tmp18
			
			for tmp19 in self.scores:
				s += b'\x00' if tmp19 is None else b'\x01'
				if tmp19 is not None:
					tmp20 = b''
					tmp20 += struct.pack('I', len(tmp19))
					while len(tmp20) and tmp20[-1] == b'\x00'[0]:
						tmp20 = tmp20[:-1]
					s += struct.pack('B', len(tmp20))
					s += tmp20
					
					s += tmp19.encode('ISO-8859-1') if PY3 else tmp19
				s += b'\x00' if self.scores[tmp19] is None else b'\x01'
				if self.scores[tmp19] is not None:
					s += struct.pack('i', self.scores[tmp19])
		
		# serialize self.board
		s += b'\x00' if self.board is None else b'\x01'
		if self.board is not None:
			tmp21 = b''
			tmp21 += struct.pack('I', len(self.board))
			while len(tmp21) and tmp21[-1] == b'\x00'[0]:
				tmp21 = tmp21[:-1]
			s += struct.pack('B', len(tmp21))
			s += tmp21
			
			for tmp22 in self.board:
				s += b'\x00' if tmp22 is None else b'\x01'
				if tmp22 is not None:
					tmp23 = b''
					tmp23 += struct.pack('I', len(tmp22))
					while len(tmp23) and tmp23[-1] == b'\x00'[0]:
						tmp23 = tmp23[:-1]
					s += struct.pack('B', len(tmp23))
					s += tmp23
					
					for tmp24 in tmp22:
						s += b'\x00' if tmp24 is None else b'\x01'
						if tmp24 is not None:
							s += struct.pack('b', tmp24.value)
		
		# serialize self.bananas
		s += b'\x00' if self.bananas is None else b'\x01'
		if self.bananas is not None:
			tmp25 = b''
			tmp25 += struct.pack('I', len(self.bananas))
			while len(tmp25) and tmp25[-1] == b'\x00'[0]:
				tmp25 = tmp25[:-1]
			s += struct.pack('B', len(tmp25))
			s += tmp25
			
			for tmp26 in self.bananas:
				s += b'\x00' if tmp26 is None else b'\x01'
				if tmp26 is not None:
					tmp27 = b''
					tmp27 += struct.pack('I', len(tmp26))
					while len(tmp27) and tmp27[-1] == b'\x00'[0]:
						tmp27 = tmp27[:-1]
					s += struct.pack('B', len(tmp27))
					s += tmp27
					
					s += tmp26.encode('ISO-8859-1') if PY3 else tmp26
				s += b'\x00' if self.bananas[tmp26] is None else b'\x01'
				if self.bananas[tmp26] is not None:
					tmp28 = b''
					tmp28 += struct.pack('I', len(self.bananas[tmp26]))
					while len(tmp28) and tmp28[-1] == b'\x00'[0]:
						tmp28 = tmp28[:-1]
					s += struct.pack('B', len(tmp28))
					s += tmp28
					
					for tmp29 in self.bananas[tmp26]:
						s += b'\x00' if tmp29 is None else b'\x01'
						if tmp29 is not None:
							s += tmp29.serialize()
		
		# serialize self.powerups
		s += b'\x00' if self.powerups is None else b'\x01'
		if self.powerups is not None:
			tmp30 = b''
			tmp30 += struct.pack('I', len(self.powerups))
			while len(tmp30) and tmp30[-1] == b'\x00'[0]:
				tmp30 = tmp30[:-1]
			s += struct.pack('B', len(tmp30))
			s += tmp30
			
			for tmp31 in self.powerups:
				s += b'\x00' if tmp31 is None else b'\x01'
				if tmp31 is not None:
					s += tmp31.serialize()
		
		# serialize self.enter_score
		s += b'\x00' if self.enter_score is None else b'\x01'
		if self.enter_score is not None:
			s += struct.pack('i', self.enter_score)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.width
		tmp32 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp32:
			self.width = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.width = None
		
		# deserialize self.height
		tmp33 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp33:
			self.height = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.height = None
		
		# deserialize self.scores
		tmp34 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp34:
			tmp35 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp36 = s[offset:offset + tmp35]
			offset += tmp35
			tmp36 += b'\x00' * (4 - tmp35)
			tmp37 = struct.unpack('I', tmp36)[0]
			
			self.scores = {}
			for tmp38 in range(tmp37):
				tmp41 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp41:
					tmp42 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp43 = s[offset:offset + tmp42]
					offset += tmp42
					tmp43 += b'\x00' * (4 - tmp42)
					tmp44 = struct.unpack('I', tmp43)[0]
					
					tmp39 = s[offset:offset + tmp44].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp44]
					offset += tmp44
				else:
					tmp39 = None
				tmp45 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp45:
					tmp40 = struct.unpack('i', s[offset:offset + 4])[0]
					offset += 4
				else:
					tmp40 = None
				self.scores[tmp39] = tmp40
		else:
			self.scores = None
		
		# deserialize self.board
		tmp46 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp46:
			tmp47 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp48 = s[offset:offset + tmp47]
			offset += tmp47
			tmp48 += b'\x00' * (4 - tmp47)
			tmp49 = struct.unpack('I', tmp48)[0]
			
			self.board = []
			for tmp50 in range(tmp49):
				tmp52 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp52:
					tmp53 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp54 = s[offset:offset + tmp53]
					offset += tmp53
					tmp54 += b'\x00' * (4 - tmp53)
					tmp55 = struct.unpack('I', tmp54)[0]
					
					tmp51 = []
					for tmp56 in range(tmp55):
						tmp58 = struct.unpack('B', s[offset:offset + 1])[0]
						offset += 1
						if tmp58:
							tmp59 = struct.unpack('b', s[offset:offset + 1])[0]
							offset += 1
							tmp57 = ECell(tmp59)
						else:
							tmp57 = None
						tmp51.append(tmp57)
				else:
					tmp51 = None
				self.board.append(tmp51)
		else:
			self.board = None
		
		# deserialize self.bananas
		tmp60 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp60:
			tmp61 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp62 = s[offset:offset + tmp61]
			offset += tmp61
			tmp62 += b'\x00' * (4 - tmp61)
			tmp63 = struct.unpack('I', tmp62)[0]
			
			self.bananas = {}
			for tmp64 in range(tmp63):
				tmp67 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp67:
					tmp68 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp69 = s[offset:offset + tmp68]
					offset += tmp68
					tmp69 += b'\x00' * (4 - tmp68)
					tmp70 = struct.unpack('I', tmp69)[0]
					
					tmp65 = s[offset:offset + tmp70].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp70]
					offset += tmp70
				else:
					tmp65 = None
				tmp71 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp71:
					tmp72 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp73 = s[offset:offset + tmp72]
					offset += tmp72
					tmp73 += b'\x00' * (4 - tmp72)
					tmp74 = struct.unpack('I', tmp73)[0]
					
					tmp66 = []
					for tmp75 in range(tmp74):
						tmp77 = struct.unpack('B', s[offset:offset + 1])[0]
						offset += 1
						if tmp77:
							tmp76 = Banana()
							offset = tmp76.deserialize(s, offset)
						else:
							tmp76 = None
						tmp66.append(tmp76)
				else:
					tmp66 = None
				self.bananas[tmp65] = tmp66
		else:
			self.bananas = None
		
		# deserialize self.powerups
		tmp78 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp78:
			tmp79 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp80 = s[offset:offset + tmp79]
			offset += tmp79
			tmp80 += b'\x00' * (4 - tmp79)
			tmp81 = struct.unpack('I', tmp80)[0]
			
			self.powerups = []
			for tmp82 in range(tmp81):
				tmp84 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp84:
					tmp83 = PowerUp()
					offset = tmp83.deserialize(s, offset)
				else:
					tmp83 = None
				self.powerups.append(tmp83)
		else:
			self.powerups = None
		
		# deserialize self.enter_score
		tmp85 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp85:
			self.enter_score = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.enter_score = None
		
		return offset
