[EMoveDir]
_def = enum<byte>
  {
    Up,
    Right,
    Down,
    Left
  }


[EFireDir]
_def = enum<byte>
  {
    Up,
    UpRight,
    Right,
    RightDown,
    Down,
    DownLeft,
    Left,
    LeftUp
  }


[Move]
_def = class
id = int
dir = EMoveDir


[Enter]
_def = class
id = int


[Fire]
_def = class
id = int
dir = EFireDir
