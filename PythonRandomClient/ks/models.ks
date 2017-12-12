[ECell]
_def = enum<byte>
  {
    Empty,
    Box,
    Tree,
    PowerUpEmitter
  }


[EPowerUpType]
_def = enum<byte>
  {
    Ammo,
    Heal
  }


[EBananaStatus]
_def = enum<byte>
  {
    Alive,
    InBox,
    Dead
  }


[PowerUp]
_def = class
type = EPowerUpType
position = int
apearance_time = int
value = int


[Banana]
_def = class
id = int
status = EBananaStatus
position = int
health = int
max_health = int
laser_count = int
max_laser_count = int
laser_range = int
laser_damage = int
time_to_reload = int
reload_time = int
death_score = int


[World]
_def = class
width = int
height = int
scores = map<string, int>
board = list<list<ECell>>
bananas = map<string, list<Banana>>
powerups = list<PowerUp>
enter_score = int
