# -*- coding: utf-8 -*-

# python imports
import sys
import struct
from enum import Enum

PY3 = sys.version_info > (3,)


class ECell(Enum):
	EMPTY = 0
	BLOCK = 1


class EDir(Enum):
	UP = 0
	RIGHT = 1
	DOWN = 2
	LEFT = 3


class PowerUpType(Enum):
	LASER = 0
	HEAL_PACK = 1


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
			self.type = PowerUpType(tmp1)
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


class Agent(object):

	@staticmethod
	def name():
		return 'Agent'


	def __init__(self, id=None, side_name=None, direction=None, position=None, health=None, max_health=None, laser_count=None, laser_range=None, laser_max_count=None, death_score=None):
		self.initialize(id, side_name, direction, position, health, max_health, laser_count, laser_range, laser_max_count, death_score)
	

	def initialize(self, id=None, side_name=None, direction=None, position=None, health=None, max_health=None, laser_count=None, laser_range=None, laser_max_count=None, death_score=None):
		self.id = id
		self.side_name = side_name
		self.direction = direction
		self.position = position
		self.health = health
		self.max_health = max_health
		self.laser_count = laser_count
		self.laser_range = laser_range
		self.laser_max_count = laser_max_count
		self.death_score = death_score
	

	def serialize(self):
		s = b''
		
		# serialize self.id
		s += b'\x00' if self.id is None else b'\x01'
		if self.id is not None:
			s += struct.pack('i', self.id)
		
		# serialize self.side_name
		s += b'\x00' if self.side_name is None else b'\x01'
		if self.side_name is not None:
			tmp5 = b''
			tmp5 += struct.pack('I', len(self.side_name))
			while len(tmp5) and tmp5[-1] == b'\x00'[0]:
				tmp5 = tmp5[:-1]
			s += struct.pack('B', len(tmp5))
			s += tmp5
			
			s += self.side_name.encode('ISO-8859-1') if PY3 else self.side_name
		
		# serialize self.direction
		s += b'\x00' if self.direction is None else b'\x01'
		if self.direction is not None:
			s += struct.pack('b', self.direction.value)
		
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
		
		# serialize self.laser_range
		s += b'\x00' if self.laser_range is None else b'\x01'
		if self.laser_range is not None:
			s += struct.pack('i', self.laser_range)
		
		# serialize self.laser_max_count
		s += b'\x00' if self.laser_max_count is None else b'\x01'
		if self.laser_max_count is not None:
			s += struct.pack('i', self.laser_max_count)
		
		# serialize self.death_score
		s += b'\x00' if self.death_score is None else b'\x01'
		if self.death_score is not None:
			s += struct.pack('i', self.death_score)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.id
		tmp6 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp6:
			self.id = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.id = None
		
		# deserialize self.side_name
		tmp7 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp7:
			tmp8 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp9 = s[offset:offset + tmp8]
			offset += tmp8
			tmp9 += b'\x00' * (4 - tmp8)
			tmp10 = struct.unpack('I', tmp9)[0]
			
			self.side_name = s[offset:offset + tmp10].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp10]
			offset += tmp10
		else:
			self.side_name = None
		
		# deserialize self.direction
		tmp11 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp11:
			tmp12 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
			self.direction = EDir(tmp12)
		else:
			self.direction = None
		
		# deserialize self.position
		tmp13 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp13:
			self.position = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.position = None
		
		# deserialize self.health
		tmp14 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp14:
			self.health = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.health = None
		
		# deserialize self.max_health
		tmp15 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp15:
			self.max_health = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.max_health = None
		
		# deserialize self.laser_count
		tmp16 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp16:
			self.laser_count = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.laser_count = None
		
		# deserialize self.laser_range
		tmp17 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp17:
			self.laser_range = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.laser_range = None
		
		# deserialize self.laser_max_count
		tmp18 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp18:
			self.laser_max_count = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.laser_max_count = None
		
		# deserialize self.death_score
		tmp19 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp19:
			self.death_score = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.death_score = None
		
		return offset


class World(object):

	@staticmethod
	def name():
		return 'World'


	def __init__(self, width=None, height=None, scores=None, board=None, agents=None, powerups=None, gates=None, exit_score=None):
		self.initialize(width, height, scores, board, agents, powerups, gates, exit_score)
	

	def initialize(self, width=None, height=None, scores=None, board=None, agents=None, powerups=None, gates=None, exit_score=None):
		self.width = width
		self.height = height
		self.scores = scores
		self.board = board
		self.agents = agents
		self.powerups = powerups
		self.gates = gates
		self.exit_score = exit_score
	

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
			tmp20 = b''
			tmp20 += struct.pack('I', len(self.scores))
			while len(tmp20) and tmp20[-1] == b'\x00'[0]:
				tmp20 = tmp20[:-1]
			s += struct.pack('B', len(tmp20))
			s += tmp20
			
			for tmp21 in self.scores:
				s += b'\x00' if tmp21 is None else b'\x01'
				if tmp21 is not None:
					tmp22 = b''
					tmp22 += struct.pack('I', len(tmp21))
					while len(tmp22) and tmp22[-1] == b'\x00'[0]:
						tmp22 = tmp22[:-1]
					s += struct.pack('B', len(tmp22))
					s += tmp22
					
					s += tmp21.encode('ISO-8859-1') if PY3 else tmp21
				s += b'\x00' if self.scores[tmp21] is None else b'\x01'
				if self.scores[tmp21] is not None:
					s += struct.pack('i', self.scores[tmp21])
		
		# serialize self.board
		s += b'\x00' if self.board is None else b'\x01'
		if self.board is not None:
			tmp23 = b''
			tmp23 += struct.pack('I', len(self.board))
			while len(tmp23) and tmp23[-1] == b'\x00'[0]:
				tmp23 = tmp23[:-1]
			s += struct.pack('B', len(tmp23))
			s += tmp23
			
			for tmp24 in self.board:
				s += b'\x00' if tmp24 is None else b'\x01'
				if tmp24 is not None:
					tmp25 = b''
					tmp25 += struct.pack('I', len(tmp24))
					while len(tmp25) and tmp25[-1] == b'\x00'[0]:
						tmp25 = tmp25[:-1]
					s += struct.pack('B', len(tmp25))
					s += tmp25
					
					for tmp26 in tmp24:
						s += b'\x00' if tmp26 is None else b'\x01'
						if tmp26 is not None:
							s += struct.pack('b', tmp26.value)
		
		# serialize self.agents
		s += b'\x00' if self.agents is None else b'\x01'
		if self.agents is not None:
			tmp27 = b''
			tmp27 += struct.pack('I', len(self.agents))
			while len(tmp27) and tmp27[-1] == b'\x00'[0]:
				tmp27 = tmp27[:-1]
			s += struct.pack('B', len(tmp27))
			s += tmp27
			
			for tmp28 in self.agents:
				s += b'\x00' if tmp28 is None else b'\x01'
				if tmp28 is not None:
					s += tmp28.serialize()
		
		# serialize self.powerups
		s += b'\x00' if self.powerups is None else b'\x01'
		if self.powerups is not None:
			tmp29 = b''
			tmp29 += struct.pack('I', len(self.powerups))
			while len(tmp29) and tmp29[-1] == b'\x00'[0]:
				tmp29 = tmp29[:-1]
			s += struct.pack('B', len(tmp29))
			s += tmp29
			
			for tmp30 in self.powerups:
				s += b'\x00' if tmp30 is None else b'\x01'
				if tmp30 is not None:
					s += tmp30.serialize()
		
		# serialize self.gates
		s += b'\x00' if self.gates is None else b'\x01'
		if self.gates is not None:
			tmp31 = b''
			tmp31 += struct.pack('I', len(self.gates))
			while len(tmp31) and tmp31[-1] == b'\x00'[0]:
				tmp31 = tmp31[:-1]
			s += struct.pack('B', len(tmp31))
			s += tmp31
			
			for tmp32 in self.gates:
				s += b'\x00' if tmp32 is None else b'\x01'
				if tmp32 is not None:
					s += struct.pack('i', tmp32)
		
		# serialize self.exit_score
		s += b'\x00' if self.exit_score is None else b'\x01'
		if self.exit_score is not None:
			s += struct.pack('i', self.exit_score)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.width
		tmp33 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp33:
			self.width = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.width = None
		
		# deserialize self.height
		tmp34 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp34:
			self.height = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.height = None
		
		# deserialize self.scores
		tmp35 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp35:
			tmp36 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp37 = s[offset:offset + tmp36]
			offset += tmp36
			tmp37 += b'\x00' * (4 - tmp36)
			tmp38 = struct.unpack('I', tmp37)[0]
			
			self.scores = {}
			for tmp39 in range(tmp38):
				tmp42 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp42:
					tmp43 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp44 = s[offset:offset + tmp43]
					offset += tmp43
					tmp44 += b'\x00' * (4 - tmp43)
					tmp45 = struct.unpack('I', tmp44)[0]
					
					tmp40 = s[offset:offset + tmp45].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp45]
					offset += tmp45
				else:
					tmp40 = None
				tmp46 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp46:
					tmp41 = struct.unpack('i', s[offset:offset + 4])[0]
					offset += 4
				else:
					tmp41 = None
				self.scores[tmp40] = tmp41
		else:
			self.scores = None
		
		# deserialize self.board
		tmp47 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp47:
			tmp48 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp49 = s[offset:offset + tmp48]
			offset += tmp48
			tmp49 += b'\x00' * (4 - tmp48)
			tmp50 = struct.unpack('I', tmp49)[0]
			
			self.board = []
			for tmp51 in range(tmp50):
				tmp53 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp53:
					tmp54 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp55 = s[offset:offset + tmp54]
					offset += tmp54
					tmp55 += b'\x00' * (4 - tmp54)
					tmp56 = struct.unpack('I', tmp55)[0]
					
					tmp52 = []
					for tmp57 in range(tmp56):
						tmp59 = struct.unpack('B', s[offset:offset + 1])[0]
						offset += 1
						if tmp59:
							tmp60 = struct.unpack('b', s[offset:offset + 1])[0]
							offset += 1
							tmp58 = ECell(tmp60)
						else:
							tmp58 = None
						tmp52.append(tmp58)
				else:
					tmp52 = None
				self.board.append(tmp52)
		else:
			self.board = None
		
		# deserialize self.agents
		tmp61 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp61:
			tmp62 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp63 = s[offset:offset + tmp62]
			offset += tmp62
			tmp63 += b'\x00' * (4 - tmp62)
			tmp64 = struct.unpack('I', tmp63)[0]
			
			self.agents = []
			for tmp65 in range(tmp64):
				tmp67 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp67:
					tmp66 = Agent()
					offset = tmp66.deserialize(s, offset)
				else:
					tmp66 = None
				self.agents.append(tmp66)
		else:
			self.agents = None
		
		# deserialize self.powerups
		tmp68 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp68:
			tmp69 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp70 = s[offset:offset + tmp69]
			offset += tmp69
			tmp70 += b'\x00' * (4 - tmp69)
			tmp71 = struct.unpack('I', tmp70)[0]
			
			self.powerups = []
			for tmp72 in range(tmp71):
				tmp74 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp74:
					tmp73 = PowerUp()
					offset = tmp73.deserialize(s, offset)
				else:
					tmp73 = None
				self.powerups.append(tmp73)
		else:
			self.powerups = None
		
		# deserialize self.gates
		tmp75 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp75:
			tmp76 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp77 = s[offset:offset + tmp76]
			offset += tmp76
			tmp77 += b'\x00' * (4 - tmp76)
			tmp78 = struct.unpack('I', tmp77)[0]
			
			self.gates = []
			for tmp79 in range(tmp78):
				tmp81 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp81:
					tmp80 = struct.unpack('i', s[offset:offset + 4])[0]
					offset += 4
				else:
					tmp80 = None
				self.gates.append(tmp80)
		else:
			self.gates = None
		
		# deserialize self.exit_score
		tmp82 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp82:
			self.exit_score = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.exit_score = None
		
		return offset
