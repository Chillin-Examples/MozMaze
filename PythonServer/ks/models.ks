[ECell]
_def = enum<byte>
	{
		EMPTY,
		BLOCK,
		GATE
	}


[EDir]
_def = enum<byte>
	{
		UP,
		RIGHT,
		DOWN,
		LEFT
	}


[PowerUpType]
_def = enum<byte>
	{
		LASER,
		HEAL_PACK
	}


[PowerUp]
_def = class
type = PowerUpType
position = int
apearance_time = int
value = int


[Agent]
_def = class
id = int
side_name = string
direction = EDir
position = int
health = int
max_health = int
laser_count = int
laser_range = int
laser_max_count = int
death_score = int


[World]
_def = class
width = int
height = int
scores = map<string, int>
board = list<list<ECell>>
agents = list<Agent>
powerups = list<PowerUp>
exit_score = int
