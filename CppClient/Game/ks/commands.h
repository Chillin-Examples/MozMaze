#ifndef _KS_COMMANDS_H_
#define _KS_COMMANDS_H_

#include <string>
#include <vector>
#include <map>
#include <array>


namespace ks
{

#ifndef _KS_OBJECT_
#define _KS_OBJECT_

class KSObject
{
public:
	static inline const std::string nameStatic() { return ""; }
	virtual inline const std::string name() const = 0;
	virtual std::string serialize() const = 0;
	virtual unsigned int deserialize(const std::string &, unsigned int = 0) = 0;
};

#endif // _KS_OBJECT_


namespace commands
{

enum class EMoveDir
{
	Up = 0,
	Right = 1,
	Down = 2,
	Left = 3,
};


enum class EFireDir
{
	Up = 0,
	UpRight = 1,
	Right = 2,
	RightDown = 3,
	Down = 4,
	DownLeft = 5,
	Left = 6,
	LeftUp = 7,
};


class Move : public KSObject
{

protected:

	int __id;
	EMoveDir __dir;

	bool __has_id;
	bool __has_dir;


public: // getters

	inline int id() const
	{
		return __id;
	}
	
	inline EMoveDir dir() const
	{
		return __dir;
	}
	

public: // reference getters

	inline int &ref_id() const
	{
		return (int&) __id;
	}
	
	inline EMoveDir &ref_dir() const
	{
		return (EMoveDir&) __dir;
	}
	

public: // setters

	inline void id(const int &id)
	{
		__id = id;
		has_id(true);
	}
	
	inline void dir(const EMoveDir &dir)
	{
		__dir = dir;
		has_dir(true);
	}
	

public: // has_attribute getters

	inline bool has_id() const
	{
		return __has_id;
	}
	
	inline bool has_dir() const
	{
		return __has_dir;
	}
	

public: // has_attribute setters

	inline void has_id(const bool &has_id)
	{
		__has_id = has_id;
	}
	
	inline void has_dir(const bool &has_dir)
	{
		__has_dir = has_dir;
	}
	

public:

	Move()
	{
		has_id(false);
		has_dir(false);
	}
	
	static inline const std::string nameStatic()
	{
		return "Move";
	}
	
	virtual inline const std::string name() const
	{
		return "Move";
	}
	
	std::string serialize() const
	{
		std::string s = "";
		
		// serialize id
		s += __has_id;
		if (__has_id)
		{
			int tmp1 = __id;
			auto tmp2 = reinterpret_cast<char*>(&tmp1);
			s += std::string(tmp2, sizeof(int));
		}
		
		// serialize dir
		s += __has_dir;
		if (__has_dir)
		{
			char tmp4 = (char) __dir;
			auto tmp5 = reinterpret_cast<char*>(&tmp4);
			s += std::string(tmp5, sizeof(char));
		}
		
		return s;
	}
	
	unsigned int deserialize(const std::string &s, unsigned int offset=0)
	{
		// deserialize id
		__has_id = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_id)
		{
			__id = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize dir
		__has_dir = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_dir)
		{
			char tmp6;
			tmp6 = *((char*) (&s[offset]));
			offset += sizeof(char);
			__dir = (EMoveDir) tmp6;
		}
		
		return offset;
	}
};


class Enter : public KSObject
{

protected:

	int __id;

	bool __has_id;


public: // getters

	inline int id() const
	{
		return __id;
	}
	

public: // reference getters

	inline int &ref_id() const
	{
		return (int&) __id;
	}
	

public: // setters

	inline void id(const int &id)
	{
		__id = id;
		has_id(true);
	}
	

public: // has_attribute getters

	inline bool has_id() const
	{
		return __has_id;
	}
	

public: // has_attribute setters

	inline void has_id(const bool &has_id)
	{
		__has_id = has_id;
	}
	

public:

	Enter()
	{
		has_id(false);
	}
	
	static inline const std::string nameStatic()
	{
		return "Enter";
	}
	
	virtual inline const std::string name() const
	{
		return "Enter";
	}
	
	std::string serialize() const
	{
		std::string s = "";
		
		// serialize id
		s += __has_id;
		if (__has_id)
		{
			int tmp8 = __id;
			auto tmp9 = reinterpret_cast<char*>(&tmp8);
			s += std::string(tmp9, sizeof(int));
		}
		
		return s;
	}
	
	unsigned int deserialize(const std::string &s, unsigned int offset=0)
	{
		// deserialize id
		__has_id = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_id)
		{
			__id = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		return offset;
	}
};


class Fire : public KSObject
{

protected:

	int __id;
	EFireDir __dir;

	bool __has_id;
	bool __has_dir;


public: // getters

	inline int id() const
	{
		return __id;
	}
	
	inline EFireDir dir() const
	{
		return __dir;
	}
	

public: // reference getters

	inline int &ref_id() const
	{
		return (int&) __id;
	}
	
	inline EFireDir &ref_dir() const
	{
		return (EFireDir&) __dir;
	}
	

public: // setters

	inline void id(const int &id)
	{
		__id = id;
		has_id(true);
	}
	
	inline void dir(const EFireDir &dir)
	{
		__dir = dir;
		has_dir(true);
	}
	

public: // has_attribute getters

	inline bool has_id() const
	{
		return __has_id;
	}
	
	inline bool has_dir() const
	{
		return __has_dir;
	}
	

public: // has_attribute setters

	inline void has_id(const bool &has_id)
	{
		__has_id = has_id;
	}
	
	inline void has_dir(const bool &has_dir)
	{
		__has_dir = has_dir;
	}
	

public:

	Fire()
	{
		has_id(false);
		has_dir(false);
	}
	
	static inline const std::string nameStatic()
	{
		return "Fire";
	}
	
	virtual inline const std::string name() const
	{
		return "Fire";
	}
	
	std::string serialize() const
	{
		std::string s = "";
		
		// serialize id
		s += __has_id;
		if (__has_id)
		{
			int tmp11 = __id;
			auto tmp12 = reinterpret_cast<char*>(&tmp11);
			s += std::string(tmp12, sizeof(int));
		}
		
		// serialize dir
		s += __has_dir;
		if (__has_dir)
		{
			char tmp14 = (char) __dir;
			auto tmp15 = reinterpret_cast<char*>(&tmp14);
			s += std::string(tmp15, sizeof(char));
		}
		
		return s;
	}
	
	unsigned int deserialize(const std::string &s, unsigned int offset=0)
	{
		// deserialize id
		__has_id = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_id)
		{
			__id = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize dir
		__has_dir = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_dir)
		{
			char tmp16;
			tmp16 = *((char*) (&s[offset]));
			offset += sizeof(char);
			__dir = (EFireDir) tmp16;
		}
		
		return offset;
	}
};

} // namespace commands

} // namespace ks

#endif // _KS_COMMANDS_H_
