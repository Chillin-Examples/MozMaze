#ifndef _KS_MODELS_H_
#define _KS_MODELS_H_

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


namespace models
{

enum class ECell
{
	Empty = 0,
	Box = 1,
	Tree = 2,
	PowerUpEmitter = 3,
};


enum class EPowerUpType
{
	Ammo = 0,
	Heal = 1,
};


enum class EBananaStatus
{
	Alive = 0,
	InBox = 1,
	Dead = 2,
};


class PowerUp : public KSObject
{

protected:

	EPowerUpType __type;
	int __position;
	int __apearance_time;
	int __value;

	bool __has_type;
	bool __has_position;
	bool __has_apearance_time;
	bool __has_value;


public: // getters

	inline EPowerUpType type() const
	{
		return __type;
	}
	
	inline int position() const
	{
		return __position;
	}
	
	inline int apearance_time() const
	{
		return __apearance_time;
	}
	
	inline int value() const
	{
		return __value;
	}
	

public: // reference getters

	inline EPowerUpType &ref_type() const
	{
		return (EPowerUpType&) __type;
	}
	
	inline int &ref_position() const
	{
		return (int&) __position;
	}
	
	inline int &ref_apearance_time() const
	{
		return (int&) __apearance_time;
	}
	
	inline int &ref_value() const
	{
		return (int&) __value;
	}
	

public: // setters

	inline void type(const EPowerUpType &type)
	{
		__type = type;
		has_type(true);
	}
	
	inline void position(const int &position)
	{
		__position = position;
		has_position(true);
	}
	
	inline void apearance_time(const int &apearance_time)
	{
		__apearance_time = apearance_time;
		has_apearance_time(true);
	}
	
	inline void value(const int &value)
	{
		__value = value;
		has_value(true);
	}
	

public: // has_attribute getters

	inline bool has_type() const
	{
		return __has_type;
	}
	
	inline bool has_position() const
	{
		return __has_position;
	}
	
	inline bool has_apearance_time() const
	{
		return __has_apearance_time;
	}
	
	inline bool has_value() const
	{
		return __has_value;
	}
	

public: // has_attribute setters

	inline void has_type(const bool &has_type)
	{
		__has_type = has_type;
	}
	
	inline void has_position(const bool &has_position)
	{
		__has_position = has_position;
	}
	
	inline void has_apearance_time(const bool &has_apearance_time)
	{
		__has_apearance_time = has_apearance_time;
	}
	
	inline void has_value(const bool &has_value)
	{
		__has_value = has_value;
	}
	

public:

	PowerUp()
	{
		has_type(false);
		has_position(false);
		has_apearance_time(false);
		has_value(false);
	}
	
	static inline const std::string nameStatic()
	{
		return "PowerUp";
	}
	
	virtual inline const std::string name() const
	{
		return "PowerUp";
	}
	
	std::string serialize() const
	{
		std::string s = "";
		
		// serialize type
		s += __has_type;
		if (__has_type)
		{
			char tmp1 = (char) __type;
			auto tmp2 = reinterpret_cast<char*>(&tmp1);
			s += std::string(tmp2, sizeof(char));
		}
		
		// serialize position
		s += __has_position;
		if (__has_position)
		{
			int tmp4 = __position;
			auto tmp5 = reinterpret_cast<char*>(&tmp4);
			s += std::string(tmp5, sizeof(int));
		}
		
		// serialize apearance_time
		s += __has_apearance_time;
		if (__has_apearance_time)
		{
			int tmp7 = __apearance_time;
			auto tmp8 = reinterpret_cast<char*>(&tmp7);
			s += std::string(tmp8, sizeof(int));
		}
		
		// serialize value
		s += __has_value;
		if (__has_value)
		{
			int tmp10 = __value;
			auto tmp11 = reinterpret_cast<char*>(&tmp10);
			s += std::string(tmp11, sizeof(int));
		}
		
		return s;
	}
	
	unsigned int deserialize(const std::string &s, unsigned int offset=0)
	{
		// deserialize type
		__has_type = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_type)
		{
			char tmp12;
			tmp12 = *((char*) (&s[offset]));
			offset += sizeof(char);
			__type = (EPowerUpType) tmp12;
		}
		
		// deserialize position
		__has_position = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_position)
		{
			__position = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize apearance_time
		__has_apearance_time = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_apearance_time)
		{
			__apearance_time = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize value
		__has_value = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_value)
		{
			__value = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		return offset;
	}
};


class Banana : public KSObject
{

protected:

	int __id;
	EBananaStatus __status;
	int __position;
	int __health;
	int __max_health;
	int __laser_count;
	int __max_laser_count;
	int __laser_range;
	int __laser_damage;
	int __time_to_reload;
	int __reload_time;
	int __death_score;

	bool __has_id;
	bool __has_status;
	bool __has_position;
	bool __has_health;
	bool __has_max_health;
	bool __has_laser_count;
	bool __has_max_laser_count;
	bool __has_laser_range;
	bool __has_laser_damage;
	bool __has_time_to_reload;
	bool __has_reload_time;
	bool __has_death_score;


public: // getters

	inline int id() const
	{
		return __id;
	}
	
	inline EBananaStatus status() const
	{
		return __status;
	}
	
	inline int position() const
	{
		return __position;
	}
	
	inline int health() const
	{
		return __health;
	}
	
	inline int max_health() const
	{
		return __max_health;
	}
	
	inline int laser_count() const
	{
		return __laser_count;
	}
	
	inline int max_laser_count() const
	{
		return __max_laser_count;
	}
	
	inline int laser_range() const
	{
		return __laser_range;
	}
	
	inline int laser_damage() const
	{
		return __laser_damage;
	}
	
	inline int time_to_reload() const
	{
		return __time_to_reload;
	}
	
	inline int reload_time() const
	{
		return __reload_time;
	}
	
	inline int death_score() const
	{
		return __death_score;
	}
	

public: // reference getters

	inline int &ref_id() const
	{
		return (int&) __id;
	}
	
	inline EBananaStatus &ref_status() const
	{
		return (EBananaStatus&) __status;
	}
	
	inline int &ref_position() const
	{
		return (int&) __position;
	}
	
	inline int &ref_health() const
	{
		return (int&) __health;
	}
	
	inline int &ref_max_health() const
	{
		return (int&) __max_health;
	}
	
	inline int &ref_laser_count() const
	{
		return (int&) __laser_count;
	}
	
	inline int &ref_max_laser_count() const
	{
		return (int&) __max_laser_count;
	}
	
	inline int &ref_laser_range() const
	{
		return (int&) __laser_range;
	}
	
	inline int &ref_laser_damage() const
	{
		return (int&) __laser_damage;
	}
	
	inline int &ref_time_to_reload() const
	{
		return (int&) __time_to_reload;
	}
	
	inline int &ref_reload_time() const
	{
		return (int&) __reload_time;
	}
	
	inline int &ref_death_score() const
	{
		return (int&) __death_score;
	}
	

public: // setters

	inline void id(const int &id)
	{
		__id = id;
		has_id(true);
	}
	
	inline void status(const EBananaStatus &status)
	{
		__status = status;
		has_status(true);
	}
	
	inline void position(const int &position)
	{
		__position = position;
		has_position(true);
	}
	
	inline void health(const int &health)
	{
		__health = health;
		has_health(true);
	}
	
	inline void max_health(const int &max_health)
	{
		__max_health = max_health;
		has_max_health(true);
	}
	
	inline void laser_count(const int &laser_count)
	{
		__laser_count = laser_count;
		has_laser_count(true);
	}
	
	inline void max_laser_count(const int &max_laser_count)
	{
		__max_laser_count = max_laser_count;
		has_max_laser_count(true);
	}
	
	inline void laser_range(const int &laser_range)
	{
		__laser_range = laser_range;
		has_laser_range(true);
	}
	
	inline void laser_damage(const int &laser_damage)
	{
		__laser_damage = laser_damage;
		has_laser_damage(true);
	}
	
	inline void time_to_reload(const int &time_to_reload)
	{
		__time_to_reload = time_to_reload;
		has_time_to_reload(true);
	}
	
	inline void reload_time(const int &reload_time)
	{
		__reload_time = reload_time;
		has_reload_time(true);
	}
	
	inline void death_score(const int &death_score)
	{
		__death_score = death_score;
		has_death_score(true);
	}
	

public: // has_attribute getters

	inline bool has_id() const
	{
		return __has_id;
	}
	
	inline bool has_status() const
	{
		return __has_status;
	}
	
	inline bool has_position() const
	{
		return __has_position;
	}
	
	inline bool has_health() const
	{
		return __has_health;
	}
	
	inline bool has_max_health() const
	{
		return __has_max_health;
	}
	
	inline bool has_laser_count() const
	{
		return __has_laser_count;
	}
	
	inline bool has_max_laser_count() const
	{
		return __has_max_laser_count;
	}
	
	inline bool has_laser_range() const
	{
		return __has_laser_range;
	}
	
	inline bool has_laser_damage() const
	{
		return __has_laser_damage;
	}
	
	inline bool has_time_to_reload() const
	{
		return __has_time_to_reload;
	}
	
	inline bool has_reload_time() const
	{
		return __has_reload_time;
	}
	
	inline bool has_death_score() const
	{
		return __has_death_score;
	}
	

public: // has_attribute setters

	inline void has_id(const bool &has_id)
	{
		__has_id = has_id;
	}
	
	inline void has_status(const bool &has_status)
	{
		__has_status = has_status;
	}
	
	inline void has_position(const bool &has_position)
	{
		__has_position = has_position;
	}
	
	inline void has_health(const bool &has_health)
	{
		__has_health = has_health;
	}
	
	inline void has_max_health(const bool &has_max_health)
	{
		__has_max_health = has_max_health;
	}
	
	inline void has_laser_count(const bool &has_laser_count)
	{
		__has_laser_count = has_laser_count;
	}
	
	inline void has_max_laser_count(const bool &has_max_laser_count)
	{
		__has_max_laser_count = has_max_laser_count;
	}
	
	inline void has_laser_range(const bool &has_laser_range)
	{
		__has_laser_range = has_laser_range;
	}
	
	inline void has_laser_damage(const bool &has_laser_damage)
	{
		__has_laser_damage = has_laser_damage;
	}
	
	inline void has_time_to_reload(const bool &has_time_to_reload)
	{
		__has_time_to_reload = has_time_to_reload;
	}
	
	inline void has_reload_time(const bool &has_reload_time)
	{
		__has_reload_time = has_reload_time;
	}
	
	inline void has_death_score(const bool &has_death_score)
	{
		__has_death_score = has_death_score;
	}
	

public:

	Banana()
	{
		has_id(false);
		has_status(false);
		has_position(false);
		has_health(false);
		has_max_health(false);
		has_laser_count(false);
		has_max_laser_count(false);
		has_laser_range(false);
		has_laser_damage(false);
		has_time_to_reload(false);
		has_reload_time(false);
		has_death_score(false);
	}
	
	static inline const std::string nameStatic()
	{
		return "Banana";
	}
	
	virtual inline const std::string name() const
	{
		return "Banana";
	}
	
	std::string serialize() const
	{
		std::string s = "";
		
		// serialize id
		s += __has_id;
		if (__has_id)
		{
			int tmp14 = __id;
			auto tmp15 = reinterpret_cast<char*>(&tmp14);
			s += std::string(tmp15, sizeof(int));
		}
		
		// serialize status
		s += __has_status;
		if (__has_status)
		{
			char tmp17 = (char) __status;
			auto tmp18 = reinterpret_cast<char*>(&tmp17);
			s += std::string(tmp18, sizeof(char));
		}
		
		// serialize position
		s += __has_position;
		if (__has_position)
		{
			int tmp20 = __position;
			auto tmp21 = reinterpret_cast<char*>(&tmp20);
			s += std::string(tmp21, sizeof(int));
		}
		
		// serialize health
		s += __has_health;
		if (__has_health)
		{
			int tmp23 = __health;
			auto tmp24 = reinterpret_cast<char*>(&tmp23);
			s += std::string(tmp24, sizeof(int));
		}
		
		// serialize max_health
		s += __has_max_health;
		if (__has_max_health)
		{
			int tmp26 = __max_health;
			auto tmp27 = reinterpret_cast<char*>(&tmp26);
			s += std::string(tmp27, sizeof(int));
		}
		
		// serialize laser_count
		s += __has_laser_count;
		if (__has_laser_count)
		{
			int tmp29 = __laser_count;
			auto tmp30 = reinterpret_cast<char*>(&tmp29);
			s += std::string(tmp30, sizeof(int));
		}
		
		// serialize max_laser_count
		s += __has_max_laser_count;
		if (__has_max_laser_count)
		{
			int tmp32 = __max_laser_count;
			auto tmp33 = reinterpret_cast<char*>(&tmp32);
			s += std::string(tmp33, sizeof(int));
		}
		
		// serialize laser_range
		s += __has_laser_range;
		if (__has_laser_range)
		{
			int tmp35 = __laser_range;
			auto tmp36 = reinterpret_cast<char*>(&tmp35);
			s += std::string(tmp36, sizeof(int));
		}
		
		// serialize laser_damage
		s += __has_laser_damage;
		if (__has_laser_damage)
		{
			int tmp38 = __laser_damage;
			auto tmp39 = reinterpret_cast<char*>(&tmp38);
			s += std::string(tmp39, sizeof(int));
		}
		
		// serialize time_to_reload
		s += __has_time_to_reload;
		if (__has_time_to_reload)
		{
			int tmp41 = __time_to_reload;
			auto tmp42 = reinterpret_cast<char*>(&tmp41);
			s += std::string(tmp42, sizeof(int));
		}
		
		// serialize reload_time
		s += __has_reload_time;
		if (__has_reload_time)
		{
			int tmp44 = __reload_time;
			auto tmp45 = reinterpret_cast<char*>(&tmp44);
			s += std::string(tmp45, sizeof(int));
		}
		
		// serialize death_score
		s += __has_death_score;
		if (__has_death_score)
		{
			int tmp47 = __death_score;
			auto tmp48 = reinterpret_cast<char*>(&tmp47);
			s += std::string(tmp48, sizeof(int));
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
		
		// deserialize status
		__has_status = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_status)
		{
			char tmp49;
			tmp49 = *((char*) (&s[offset]));
			offset += sizeof(char);
			__status = (EBananaStatus) tmp49;
		}
		
		// deserialize position
		__has_position = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_position)
		{
			__position = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize health
		__has_health = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_health)
		{
			__health = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize max_health
		__has_max_health = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_max_health)
		{
			__max_health = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize laser_count
		__has_laser_count = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_laser_count)
		{
			__laser_count = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize max_laser_count
		__has_max_laser_count = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_max_laser_count)
		{
			__max_laser_count = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize laser_range
		__has_laser_range = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_laser_range)
		{
			__laser_range = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize laser_damage
		__has_laser_damage = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_laser_damage)
		{
			__laser_damage = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize time_to_reload
		__has_time_to_reload = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_time_to_reload)
		{
			__time_to_reload = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize reload_time
		__has_reload_time = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_reload_time)
		{
			__reload_time = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize death_score
		__has_death_score = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_death_score)
		{
			__death_score = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		return offset;
	}
};


class World : public KSObject
{

protected:

	int __width;
	int __height;
	std::map<std::string, int> __scores;
	std::vector<std::vector<ECell>> __board;
	std::map<std::string, std::vector<Banana>> __bananas;
	std::vector<PowerUp> __powerups;
	int __enter_score;

	bool __has_width;
	bool __has_height;
	bool __has_scores;
	bool __has_board;
	bool __has_bananas;
	bool __has_powerups;
	bool __has_enter_score;


public: // getters

	inline int width() const
	{
		return __width;
	}
	
	inline int height() const
	{
		return __height;
	}
	
	inline std::map<std::string, int> scores() const
	{
		return __scores;
	}
	
	inline std::vector<std::vector<ECell>> board() const
	{
		return __board;
	}
	
	inline std::map<std::string, std::vector<Banana>> bananas() const
	{
		return __bananas;
	}
	
	inline std::vector<PowerUp> powerups() const
	{
		return __powerups;
	}
	
	inline int enter_score() const
	{
		return __enter_score;
	}
	

public: // reference getters

	inline int &ref_width() const
	{
		return (int&) __width;
	}
	
	inline int &ref_height() const
	{
		return (int&) __height;
	}
	
	inline std::map<std::string, int> &ref_scores() const
	{
		return (std::map<std::string, int>&) __scores;
	}
	
	inline std::vector<std::vector<ECell>> &ref_board() const
	{
		return (std::vector<std::vector<ECell>>&) __board;
	}
	
	inline std::map<std::string, std::vector<Banana>> &ref_bananas() const
	{
		return (std::map<std::string, std::vector<Banana>>&) __bananas;
	}
	
	inline std::vector<PowerUp> &ref_powerups() const
	{
		return (std::vector<PowerUp>&) __powerups;
	}
	
	inline int &ref_enter_score() const
	{
		return (int&) __enter_score;
	}
	

public: // setters

	inline void width(const int &width)
	{
		__width = width;
		has_width(true);
	}
	
	inline void height(const int &height)
	{
		__height = height;
		has_height(true);
	}
	
	inline void scores(const std::map<std::string, int> &scores)
	{
		__scores = scores;
		has_scores(true);
	}
	
	inline void board(const std::vector<std::vector<ECell>> &board)
	{
		__board = board;
		has_board(true);
	}
	
	inline void bananas(const std::map<std::string, std::vector<Banana>> &bananas)
	{
		__bananas = bananas;
		has_bananas(true);
	}
	
	inline void powerups(const std::vector<PowerUp> &powerups)
	{
		__powerups = powerups;
		has_powerups(true);
	}
	
	inline void enter_score(const int &enter_score)
	{
		__enter_score = enter_score;
		has_enter_score(true);
	}
	

public: // has_attribute getters

	inline bool has_width() const
	{
		return __has_width;
	}
	
	inline bool has_height() const
	{
		return __has_height;
	}
	
	inline bool has_scores() const
	{
		return __has_scores;
	}
	
	inline bool has_board() const
	{
		return __has_board;
	}
	
	inline bool has_bananas() const
	{
		return __has_bananas;
	}
	
	inline bool has_powerups() const
	{
		return __has_powerups;
	}
	
	inline bool has_enter_score() const
	{
		return __has_enter_score;
	}
	

public: // has_attribute setters

	inline void has_width(const bool &has_width)
	{
		__has_width = has_width;
	}
	
	inline void has_height(const bool &has_height)
	{
		__has_height = has_height;
	}
	
	inline void has_scores(const bool &has_scores)
	{
		__has_scores = has_scores;
	}
	
	inline void has_board(const bool &has_board)
	{
		__has_board = has_board;
	}
	
	inline void has_bananas(const bool &has_bananas)
	{
		__has_bananas = has_bananas;
	}
	
	inline void has_powerups(const bool &has_powerups)
	{
		__has_powerups = has_powerups;
	}
	
	inline void has_enter_score(const bool &has_enter_score)
	{
		__has_enter_score = has_enter_score;
	}
	

public:

	World()
	{
		has_width(false);
		has_height(false);
		has_scores(false);
		has_board(false);
		has_bananas(false);
		has_powerups(false);
		has_enter_score(false);
	}
	
	static inline const std::string nameStatic()
	{
		return "World";
	}
	
	virtual inline const std::string name() const
	{
		return "World";
	}
	
	std::string serialize() const
	{
		std::string s = "";
		
		// serialize width
		s += __has_width;
		if (__has_width)
		{
			int tmp51 = __width;
			auto tmp52 = reinterpret_cast<char*>(&tmp51);
			s += std::string(tmp52, sizeof(int));
		}
		
		// serialize height
		s += __has_height;
		if (__has_height)
		{
			int tmp54 = __height;
			auto tmp55 = reinterpret_cast<char*>(&tmp54);
			s += std::string(tmp55, sizeof(int));
		}
		
		// serialize scores
		s += __has_scores;
		if (__has_scores)
		{
			std::string tmp56 = "";
			unsigned int tmp58 = __scores.size();
			auto tmp59 = reinterpret_cast<char*>(&tmp58);
			tmp56 += std::string(tmp59, sizeof(unsigned int));
			while (tmp56.size() && tmp56.back() == 0)
				tmp56.pop_back();
			unsigned char tmp61 = tmp56.size();
			auto tmp62 = reinterpret_cast<char*>(&tmp61);
			s += std::string(tmp62, sizeof(unsigned char));
			s += tmp56;
			
			for (auto &tmp63 : __scores)
			{
				s += '\x01';
				std::string tmp64 = "";
				unsigned int tmp66 = tmp63.first.size();
				auto tmp67 = reinterpret_cast<char*>(&tmp66);
				tmp64 += std::string(tmp67, sizeof(unsigned int));
				while (tmp64.size() && tmp64.back() == 0)
					tmp64.pop_back();
				unsigned char tmp69 = tmp64.size();
				auto tmp70 = reinterpret_cast<char*>(&tmp69);
				s += std::string(tmp70, sizeof(unsigned char));
				s += tmp64;
				
				s += tmp63.first;
				
				s += '\x01';
				int tmp72 = tmp63.second;
				auto tmp73 = reinterpret_cast<char*>(&tmp72);
				s += std::string(tmp73, sizeof(int));
			}
		}
		
		// serialize board
		s += __has_board;
		if (__has_board)
		{
			std::string tmp74 = "";
			unsigned int tmp76 = __board.size();
			auto tmp77 = reinterpret_cast<char*>(&tmp76);
			tmp74 += std::string(tmp77, sizeof(unsigned int));
			while (tmp74.size() && tmp74.back() == 0)
				tmp74.pop_back();
			unsigned char tmp79 = tmp74.size();
			auto tmp80 = reinterpret_cast<char*>(&tmp79);
			s += std::string(tmp80, sizeof(unsigned char));
			s += tmp74;
			
			for (auto &tmp81 : __board)
			{
				s += '\x01';
				std::string tmp82 = "";
				unsigned int tmp84 = tmp81.size();
				auto tmp85 = reinterpret_cast<char*>(&tmp84);
				tmp82 += std::string(tmp85, sizeof(unsigned int));
				while (tmp82.size() && tmp82.back() == 0)
					tmp82.pop_back();
				unsigned char tmp87 = tmp82.size();
				auto tmp88 = reinterpret_cast<char*>(&tmp87);
				s += std::string(tmp88, sizeof(unsigned char));
				s += tmp82;
				
				for (auto &tmp89 : tmp81)
				{
					s += '\x01';
					char tmp91 = (char) tmp89;
					auto tmp92 = reinterpret_cast<char*>(&tmp91);
					s += std::string(tmp92, sizeof(char));
				}
			}
		}
		
		// serialize bananas
		s += __has_bananas;
		if (__has_bananas)
		{
			std::string tmp93 = "";
			unsigned int tmp95 = __bananas.size();
			auto tmp96 = reinterpret_cast<char*>(&tmp95);
			tmp93 += std::string(tmp96, sizeof(unsigned int));
			while (tmp93.size() && tmp93.back() == 0)
				tmp93.pop_back();
			unsigned char tmp98 = tmp93.size();
			auto tmp99 = reinterpret_cast<char*>(&tmp98);
			s += std::string(tmp99, sizeof(unsigned char));
			s += tmp93;
			
			for (auto &tmp100 : __bananas)
			{
				s += '\x01';
				std::string tmp101 = "";
				unsigned int tmp103 = tmp100.first.size();
				auto tmp104 = reinterpret_cast<char*>(&tmp103);
				tmp101 += std::string(tmp104, sizeof(unsigned int));
				while (tmp101.size() && tmp101.back() == 0)
					tmp101.pop_back();
				unsigned char tmp106 = tmp101.size();
				auto tmp107 = reinterpret_cast<char*>(&tmp106);
				s += std::string(tmp107, sizeof(unsigned char));
				s += tmp101;
				
				s += tmp100.first;
				
				s += '\x01';
				std::string tmp108 = "";
				unsigned int tmp110 = tmp100.second.size();
				auto tmp111 = reinterpret_cast<char*>(&tmp110);
				tmp108 += std::string(tmp111, sizeof(unsigned int));
				while (tmp108.size() && tmp108.back() == 0)
					tmp108.pop_back();
				unsigned char tmp113 = tmp108.size();
				auto tmp114 = reinterpret_cast<char*>(&tmp113);
				s += std::string(tmp114, sizeof(unsigned char));
				s += tmp108;
				
				for (auto &tmp115 : tmp100.second)
				{
					s += '\x01';
					s += tmp115.serialize();
				}
			}
		}
		
		// serialize powerups
		s += __has_powerups;
		if (__has_powerups)
		{
			std::string tmp116 = "";
			unsigned int tmp118 = __powerups.size();
			auto tmp119 = reinterpret_cast<char*>(&tmp118);
			tmp116 += std::string(tmp119, sizeof(unsigned int));
			while (tmp116.size() && tmp116.back() == 0)
				tmp116.pop_back();
			unsigned char tmp121 = tmp116.size();
			auto tmp122 = reinterpret_cast<char*>(&tmp121);
			s += std::string(tmp122, sizeof(unsigned char));
			s += tmp116;
			
			for (auto &tmp123 : __powerups)
			{
				s += '\x01';
				s += tmp123.serialize();
			}
		}
		
		// serialize enter_score
		s += __has_enter_score;
		if (__has_enter_score)
		{
			int tmp125 = __enter_score;
			auto tmp126 = reinterpret_cast<char*>(&tmp125);
			s += std::string(tmp126, sizeof(int));
		}
		
		return s;
	}
	
	unsigned int deserialize(const std::string &s, unsigned int offset=0)
	{
		// deserialize width
		__has_width = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_width)
		{
			__width = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize height
		__has_height = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_height)
		{
			__height = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize scores
		__has_scores = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_scores)
		{
			unsigned char tmp127;
			tmp127 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp128 = std::string(&s[offset], tmp127);
			offset += tmp127;
			while (tmp128.size() < sizeof(unsigned int))
				tmp128 += '\x00';
			unsigned int tmp129;
			tmp129 = *((unsigned int*) (&tmp128[0]));
			
			__scores.clear();
			for (unsigned int tmp130 = 0; tmp130 < tmp129; tmp130++)
			{
				std::string tmp131;
				offset++;
				unsigned char tmp133;
				tmp133 = *((unsigned char*) (&s[offset]));
				offset += sizeof(unsigned char);
				std::string tmp134 = std::string(&s[offset], tmp133);
				offset += tmp133;
				while (tmp134.size() < sizeof(unsigned int))
					tmp134 += '\x00';
				unsigned int tmp135;
				tmp135 = *((unsigned int*) (&tmp134[0]));
				
				tmp131 = s.substr(offset, tmp135);
				offset += tmp135;
				
				int tmp132;
				offset++;
				tmp132 = *((int*) (&s[offset]));
				offset += sizeof(int);
				
				__scores[tmp131] = tmp132;
			}
		}
		
		// deserialize board
		__has_board = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_board)
		{
			unsigned char tmp136;
			tmp136 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp137 = std::string(&s[offset], tmp136);
			offset += tmp136;
			while (tmp137.size() < sizeof(unsigned int))
				tmp137 += '\x00';
			unsigned int tmp138;
			tmp138 = *((unsigned int*) (&tmp137[0]));
			
			__board.clear();
			for (unsigned int tmp139 = 0; tmp139 < tmp138; tmp139++)
			{
				std::vector<ECell> tmp140;
				offset++;
				unsigned char tmp141;
				tmp141 = *((unsigned char*) (&s[offset]));
				offset += sizeof(unsigned char);
				std::string tmp142 = std::string(&s[offset], tmp141);
				offset += tmp141;
				while (tmp142.size() < sizeof(unsigned int))
					tmp142 += '\x00';
				unsigned int tmp143;
				tmp143 = *((unsigned int*) (&tmp142[0]));
				
				tmp140.clear();
				for (unsigned int tmp144 = 0; tmp144 < tmp143; tmp144++)
				{
					ECell tmp145;
					offset++;
					char tmp146;
					tmp146 = *((char*) (&s[offset]));
					offset += sizeof(char);
					tmp145 = (ECell) tmp146;
					tmp140.push_back(tmp145);
				}
				__board.push_back(tmp140);
			}
		}
		
		// deserialize bananas
		__has_bananas = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_bananas)
		{
			unsigned char tmp147;
			tmp147 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp148 = std::string(&s[offset], tmp147);
			offset += tmp147;
			while (tmp148.size() < sizeof(unsigned int))
				tmp148 += '\x00';
			unsigned int tmp149;
			tmp149 = *((unsigned int*) (&tmp148[0]));
			
			__bananas.clear();
			for (unsigned int tmp150 = 0; tmp150 < tmp149; tmp150++)
			{
				std::string tmp151;
				offset++;
				unsigned char tmp153;
				tmp153 = *((unsigned char*) (&s[offset]));
				offset += sizeof(unsigned char);
				std::string tmp154 = std::string(&s[offset], tmp153);
				offset += tmp153;
				while (tmp154.size() < sizeof(unsigned int))
					tmp154 += '\x00';
				unsigned int tmp155;
				tmp155 = *((unsigned int*) (&tmp154[0]));
				
				tmp151 = s.substr(offset, tmp155);
				offset += tmp155;
				
				std::vector<Banana> tmp152;
				offset++;
				unsigned char tmp156;
				tmp156 = *((unsigned char*) (&s[offset]));
				offset += sizeof(unsigned char);
				std::string tmp157 = std::string(&s[offset], tmp156);
				offset += tmp156;
				while (tmp157.size() < sizeof(unsigned int))
					tmp157 += '\x00';
				unsigned int tmp158;
				tmp158 = *((unsigned int*) (&tmp157[0]));
				
				tmp152.clear();
				for (unsigned int tmp159 = 0; tmp159 < tmp158; tmp159++)
				{
					Banana tmp160;
					offset++;
					offset = tmp160.deserialize(s, offset);
					tmp152.push_back(tmp160);
				}
				
				__bananas[tmp151] = tmp152;
			}
		}
		
		// deserialize powerups
		__has_powerups = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_powerups)
		{
			unsigned char tmp161;
			tmp161 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp162 = std::string(&s[offset], tmp161);
			offset += tmp161;
			while (tmp162.size() < sizeof(unsigned int))
				tmp162 += '\x00';
			unsigned int tmp163;
			tmp163 = *((unsigned int*) (&tmp162[0]));
			
			__powerups.clear();
			for (unsigned int tmp164 = 0; tmp164 < tmp163; tmp164++)
			{
				PowerUp tmp165;
				offset++;
				offset = tmp165.deserialize(s, offset);
				__powerups.push_back(tmp165);
			}
		}
		
		// deserialize enter_score
		__has_enter_score = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_enter_score)
		{
			__enter_score = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		return offset;
	}
};

} // namespace models

} // namespace ks

#endif // _KS_MODELS_H_
