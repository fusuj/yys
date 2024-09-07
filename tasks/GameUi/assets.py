from module.atom.image import RuleImage
from module.atom.click import RuleClick
from module.atom.long_click import RuleLongClick
from module.atom.swipe import RuleSwipe
from module.atom.ocr import RuleOcr
from module.atom.list import RuleList

# This file was automatically generated by ./dev_tools/assets_extract.py.
# Don't modify it manually.
class GameUiAssets: 


	# Ocr Rule Assets
	# 点击空白处关闭此界面 
	O_CLICK_CLOSE_1 = RuleOcr(roi=(521,659,232,32), area=(521,659,232,32), mode="Single", method="Default", keyword="点击空白处关闭此界面", name="click_close_1")
	# 点击空白处关闭弹窗 
	O_CLICK_CLOSE_2 = RuleOcr(roi=(508,584,214,40), area=(508,584,214,40), mode="Single", method="Default", keyword="点击空白处关闭弹窗", name="click_close_2")


	# Image Rule Assets
	# 商店弹窗红色关闭 
	I_AD_CLOSE_RED = RuleImage(roi_front=(993,130,33,36), roi_back=(953,91,215,121), threshold=0.8, method="Template matching", file="./tasks/GameUi/additional/additional_ad_close_red.png")


	# Image Rule Assets
	# description 
	I_AD_DISAPPEAR = RuleImage(roi_front=(412,405,37,40), roi_back=(412,405,37,40), threshold=0.75, method="Template matching", file="./tasks/GameUi/additional/additional_ad_disappear.png")
	# description 
	I_RECORDS_CLOSE = RuleImage(roi_front=(914,143,30,30), roi_back=(914,143,30,30), threshold=0.7, method="Template matching", file="./tasks/GameUi/additional/additional_records_close.png")


	# Image Rule Assets
	# description 
	I_CHECK_MAIN = RuleImage(roi_front=(801,109,38,37), roi_back=(49,98,1033,61), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_check_main.png")
	# description 
	I_MAIN_GOTO_EXPLORATION = RuleImage(roi_front=(493,116,45,75), roi_back=(243,100,933,211), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_main_goto_exploration.png")
	# description 
	I_CHECK_EXPLORATION = RuleImage(roi_front=(1146,175,21,22), roi_back=(1146,175,21,22), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_check_exploration.png")
	# description 
	I_EXPLORATION_GOTO_AWAKE_ZONE = RuleImage(roi_front=(57,628,57,61), roi_back=(33,619,113,79), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_exploration_goto_awake_zone.png")
	# description 
	I_EXPLORATION_GOTO_SOUL_ZONE = RuleImage(roi_front=(159,633,55,55), roi_back=(138,620,89,75), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_exploration_goto_soul_zone.png")
	# description 
	I_EXPLORATION_GOTO_REALM_RAID = RuleImage(roi_front=(248,636,67,48), roi_back=(229,612,102,87), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_exploration_goto_realm_raid.png")
	# 前往御灵 
	I_EXPLORATION_GOTO_GORYOU_REALM = RuleImage(roi_front=(353,639,47,45), roi_back=(346,626,60,67), threshold=0.7, method="Template matching", file="./tasks/GameUi/page/page_exploration_goto_goryou_realm.png")
	# 式神委派 
	I_EXPLORATION_GOTO_DELEGATION = RuleImage(roi_front=(445,638,60,50), roi_back=(445,638,60,50), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_exploration_goto_delegation.png")
	# 秘闻 
	I_EXPLORATION_GOTO_SECRET_ZONES = RuleImage(roi_front=(546,628,61,55), roi_back=(524,614,100,87), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_exploration_goto_secret_zones.png")
	# 地狱鬼王 
	I_EXPLORATION_GOTO_AREA_BOSS = RuleImage(roi_front=(640,638,51,45), roi_back=(640,638,51,45), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_exploration_goto_area_boss.png")
	# 平安奇谭 
	I_EXPLORATION_GOTO_HEIAN_KITAN = RuleImage(roi_front=(739,643,52,44), roi_back=(739,643,52,44), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_exploration_goto_heian_kitan.png")
	# 六道之门 
	I_EXPLORATION_GOTO_SIX_GATES = RuleImage(roi_front=(838,640,60,49), roi_back=(818,631,200,66), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_exploration_goto_six_gates.png")
	# 器灵 
	I_EXPLORATION_GOTO_BONDLING_FAIRYLAND = RuleImage(roi_front=(937,639,56,49), roi_back=(928,633,203,64), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_exploration_goto_bondling_fairyland.png")
	# description 
	I_BACK_BLUE = RuleImage(roi_front=(32,37,54,52), roi_back=(3,2,130,114), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_back_blue.png")
	# description 
	I_CHECK_AWAKE = RuleImage(roi_front=(376,565,73,82), roi_back=(376,565,73,82), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_check_awake.png")
	# description 
	I_CHECK_SOUL_ZONES = RuleImage(roi_front=(49,105,298,405), roi_back=(49,105,298,405), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_check_soul_zones.png")
	# description 
	I_CHECK_REALM_RAID = RuleImage(roi_front=(113,625,86,77), roi_back=(113,625,86,77), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_check_realm_raid.png")
	# description 
	I_CHECK_GORYOU = RuleImage(roi_front=(881,17,30,39), roi_back=(881,17,30,39), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_check_goryou.png")
	# description 
	I_CHECK_DELEGATION = RuleImage(roi_front=(839,132,49,45), roi_back=(839,132,49,45), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_check_delegation.png")
	# description 
	I_CHECK_SECRET_ZONES = RuleImage(roi_front=(1145,592,110,119), roi_back=(1145,592,110,119), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_check_secret_zones.png")
	# description 
	I_CHECK_AREA_BOSS = RuleImage(roi_front=(20,320,150,130), roi_back=(20,320,150,130), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_check_area_boss.png")
	# description 
	I_CHECK_HEIAN_KITAN = RuleImage(roi_front=(27,48,47,39), roi_back=(27,48,47,39), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_check_heian_kitan.png")
	# description 
	I_CHECK_SIX_GATES = RuleImage(roi_front=(1174,621,55,44), roi_back=(1174,621,55,44), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_check_six_gates.png")
	# description 
	I_CHECK_BONDLING_FAIRYLAND = RuleImage(roi_front=(614,660,56,49), roi_back=(614,660,56,49), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_check_bondling_fairyland.png")
	# description 
	I_SIX_GATES_GOTO_EXPLORATION = RuleImage(roi_front=(18,19,52,55), roi_back=(18,19,52,55), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_six_gates_goto_exploration.png")
	# description 
	I_BONDLING_GOTO_EXPLORATION = RuleImage(roi_front=(20,13,60,59), roi_back=(20,13,60,59), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_bondling_goto_exploration.png")
	# description 
	I_RYOUTOPPA_GOTO_REALMRAID = RuleImage(roi_front=(1201,234,62,105), roi_back=(1201,234,62,105), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_ryoutoppa_goto_realmraid.png")
	# 从探索前往英杰试炼 
	I_EXPLORATION_GOTO_YINGJIESHILIAN = RuleImage(roi_front=(844,637,42,44), roi_back=(48,621,1228,71), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_exploration_goto_yingjieshilian.png")
	# 判断是否在英杰试炼界面 
	I_CHECK_YINGJIESHILIAN = RuleImage(roi_front=(1164,596,56,55), roi_back=(1164,596,56,55), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_check_yingjieshilian.png")
	# 前往鬼兵演武 
	I_GOTO_GUIBINGYANWU = RuleImage(roi_front=(98,343,32,130), roi_back=(98,343,32,130), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_goto_guibingyanwu.png")
	# 判断是否在鬼兵演武界面 
	I_CHECK_GUIBINGYANWU = RuleImage(roi_front=(40,473,54,51), roi_back=(40,473,54,51), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_check_guibingyanwu.png")


	# Image Rule Assets
	# description 
	I_MAIN_GOTO_TOWN = RuleImage(roi_front=(706,249,61,57), roi_back=(200,120,951,298), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_main_goto_town.png")
	# description 
	I_CHECK_TOWN = RuleImage(roi_front=(1026,106,68,82), roi_back=(765,98,402,96), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_check_town.png")
	# description 
	I_TOWN_GOTO_MAIN = RuleImage(roi_front=(1017,231,78,73), roi_back=(302,216,868,127), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_town_goto_main.png")
	# description 
	I_TOWN_GOTO_DUEL = RuleImage(roi_front=(756,142,48,68), roi_back=(357,126,657,100), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_town_goto_duel.png")
	# description 
	I_TOWN_GOTO_DEMON_ENCOUNTER = RuleImage(roi_front=(617,135,51,75), roi_back=(232,121,873,100), threshold=0.7, method="Template matching", file="./tasks/GameUi/page/page_town_goto_demon_encounter.png")
	# description 
	I_TOWN_GOTO_HUNT = RuleImage(roi_front=(475,138,46,69), roi_back=(275,122,520,100), threshold=0.7, method="Template matching", file="./tasks/GameUi/page/page_town_goto_hunt.png")
	# 协同对弈 
	I_TOWN_GOTO_DRAFT_DUEL = RuleImage(roi_front=(335,159,55,72), roi_back=(170,145,567,100), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_town_goto_draft_duel.png")
	# 百鬼奕 
	I_TOWN_GOTO_HYAKKISEN = RuleImage(roi_front=(192,145,48,67), roi_back=(86,130,447,100), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_town_goto_hyakkisen.png")
	# description 
	I_CHECK_DUEL = RuleImage(roi_front=(1045,610,50,53), roi_back=(1018,579,100,100), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_check_duel.png")
	# description 
	I_CHECK_DEMON_ENCOUNTER = RuleImage(roi_front=(26,658,42,43), roi_back=(2,619,100,100), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_check_demon_encounter.png")
	# description 
	I_CHECK_HUNT = RuleImage(roi_front=(575,30,46,25), roi_back=(553,1,81,68), threshold=0.7, method="Template matching", file="./tasks/GameUi/page/page_check_hunt.png")
	# description 
	I_CHECK_HYAKKISEN = RuleImage(roi_front=(1014,607,53,55), roi_back=(986,587,100,100), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_check_hyakkisen.png")
	# description 
	I_CHECK_DRAFT_DUEL = RuleImage(roi_front=(1051,612,56,58), roi_back=(1029,594,100,100), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_check_draft_duel.png")
	# description 
	I_BACK_YOLLOW = RuleImage(roi_front=(24,16,48,55), roi_back=(0,0,100,100), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_back_yollow.png")
	# description 
	I_DEMON_ENCOUNTER_GOTO_TOWN = RuleImage(roi_front=(28,20,56,52), roi_back=(3,4,100,100), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_demon_encounter_goto_town.png")
	# description 
	I_TOWN_GOTO_HYAKKIYAKOU = RuleImage(roi_front=(880,165,53,69), roi_back=(827,149,148,100), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_town_goto_hyakkiyakou.png")
	# description 
	I_CHECK_KYAKKIYAKOU = RuleImage(roi_front=(305,567,56,64), roi_back=(280,545,100,100), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_check_kyakkiyakou.png")
	# description 
	I_HYAKKIYAKOU_CLOSE = RuleImage(roi_front=(1063,181,47,43), roi_back=(1063,181,47,43), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_hyakkiyakou_close.png")


	# Image Rule Assets
	# 式神录 
	I_MAIN_GOTO_SHIKIGAMI_RECORDS = RuleImage(roi_front=(1098,611,56,64), roi_back=(1084,589,93,106), threshold=0.7, method="Template matching", file="./tasks/GameUi/page/page_main_goto_shikigami_records.png")
	# description 
	I_MAIN_GOTO_ONMYODO = RuleImage(roi_front=(992,614,51,60), roi_back=(992,614,51,60), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_main_goto_onmyodo.png")
	# description 
	I_MAIN_GOTO_FRIENDS = RuleImage(roi_front=(879,623,55,55), roi_back=(867,606,79,77), threshold=0.7, method="Template matching", file="./tasks/GameUi/page/page_main_goto_friends.png")
	# 进入花合战 
	I_MAIN_GOTO_DAILY = RuleImage(roi_front=(779,612,51,67), roi_back=(754,595,89,97), threshold=0.7, method="Template matching", file="./tasks/GameUi/page/page_main_goto_daily.png")
	# description 
	I_MAIN_GOTO_MALL = RuleImage(roi_front=(663,661,41,22), roi_back=(644,613,81,78), threshold=0.7, method="Template matching", file="./tasks/GameUi/page/page_main_goto_mall.png")
	# description 
	I_MAIN_GOTO_GUILD = RuleImage(roi_front=(540,611,50,54), roi_back=(540,611,50,54), threshold=0.7, method="Template matching", file="./tasks/GameUi/page/page_main_goto_guild.png")
	# description 
	I_MAIN_GOTO_TEAM = RuleImage(roi_front=(437,625,38,48), roi_back=(366,606,192,83), threshold=0.7, method="Template matching", file="./tasks/GameUi/page/page_main_goto_team.png")
	# description 
	I_MAIN_GOTO_COLLECTION = RuleImage(roi_front=(92,621,36,41), roi_back=(51,596,159,85), threshold=0.7, method="Template matching", file="./tasks/GameUi/page/page_main_goto_collection.png")
	# description 
	I_CHECK_RECORDS = RuleImage(roi_front=(269,71,55,50), roi_back=(269,71,55,50), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_check_records.png")
	# description 
	I_CHECK_ONMYODO = RuleImage(roi_front=(1166,117,84,547), roi_back=(1166,117,84,547), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_check_onmyodo.png")
	# description 
	I_CHECK_FRIENDS = RuleImage(roi_front=(1011,592,133,60), roi_back=(1011,592,133,60), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_check_friends.png")
	# description 
	I_CHECK_DAILY = RuleImage(roi_front=(27,515,69,62), roi_back=(1,489,155,127), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_check_daily.png")
	# description 
	I_CHECK_MALL = RuleImage(roi_front=(239,502,100,100), roi_back=(239,502,100,100), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_check_mall.png")
	# description 
	I_CHECK_GUILD = RuleImage(roi_front=(1072,630,49,46), roi_back=(1072,630,49,46), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_check_guild.png")
	# description 
	I_CHECK_TEAM = RuleImage(roi_front=(32,585,82,90), roi_back=(32,585,82,90), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_check_team.png")
	# description 
	I_CHECK_COLLECTION = RuleImage(roi_front=(471,618,100,100), roi_back=(471,618,100,100), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_check_collection.png")
	# description 
	I_BACK_Y = RuleImage(roi_front=(15,4,57,52), roi_back=(1,2,100,91), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_back_y.png")
	# description 
	I_BACK_MALL = RuleImage(roi_front=(28,33,50,51), roi_back=(28,33,50,51), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_back_mall.png")
	# description 
	I_BACK_FRIENDS = RuleImage(roi_front=(1152,87,53,52), roi_back=(1152,87,53,52), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_back_friends.png")
	# description 
	I_BACK_DAILY = RuleImage(roi_front=(33,13,39,50), roi_back=(33,13,39,50), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_back_daily.png")
	# description 
	I_NEW = RuleImage(roi_front=(0,0,100,100), roi_back=(0,0,100,100), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/image_name.png")


	# Image Rule Assets
	# description 
	I_MAIN_GOTO_SUMMON = RuleImage(roi_front=(1073,174,57,65), roi_back=(571,153,586,124), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_main_goto_summon.png")
	# description 
	I_SUMMON_GOTO_MAIN = RuleImage(roi_front=(27,5,49,51), roi_back=(0,0,100,100), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_summon_goto_main.png")
	# description 
	I_CHECK_SUMMON = RuleImage(roi_front=(581,594,68,66), roi_back=(316,528,594,174), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_check_summon.png")
	# 就是一个红叉 
	I_REALM_RAID_GOTO_EXPLORATION = RuleImage(roi_front=(1192,107,36,43), roi_back=(1192,107,36,43), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_realm_raid_goto_exploration.png")
	# description 
	I_MAIN_GOTO_TRAVEL = RuleImage(roi_front=(202,619,64,61), roi_back=(202,619,64,61), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_main_goto_travel.png")
	# 珍旅居 
	I_CHECK_TRAVEL = RuleImage(roi_front=(1134,583,78,77), roi_back=(1134,583,78,77), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_check_travel.png")


	# Image Rule Assets
	# 寮结界突破右上角 
	I_KEKKAI_TOPPA = RuleImage(roi_front=(1065,3,203,61), roi_back=(1065,3,203,61), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_kekkai_toppa.png")


	# Image Rule Assets
	# 左上角蓝色的返回 
	I_BACK_BL = RuleImage(roi_front=(32,31,50,53), roi_back=(1,2,139,120), threshold=0.8, method="Template matching", file="./tasks/GameUi/res/res_back_blue.png")
	# 式神录 
	I_HOME_SHIKIKAMI = RuleImage(roi_front=(1092,611,73,41), roi_back=(1092,611,73,41), threshold=0.8, method="Template matching", file="./tasks/GameUi/res/res_home_shikikami.png")
	# 阴阳术 
	I_HOME_OMNYOUJI = RuleImage(roi_front=(989,613,59,58), roi_back=(989,613,59,58), threshold=0.8, method="Template matching", file="./tasks/GameUi/res/res_home_omnyouji.png")
	# description 
	I_HOME_FRIEND = RuleImage(roi_front=(876,619,60,53), roi_back=(876,619,60,53), threshold=0.8, method="Template matching", file="./tasks/GameUi/res/res_home_friend.png")
	# 花合战 
	I_HOME_TSK = RuleImage(roi_front=(764,608,66,56), roi_back=(764,608,66,56), threshold=0.8, method="Template matching", file="./tasks/GameUi/res/res_home_tsk.png")
	# 商店 
	I_HOME_MALL = RuleImage(roi_front=(654,620,51,55), roi_back=(654,620,51,55), threshold=0.8, method="Template matching", file="./tasks/GameUi/res/res_home_mall.png")
	# 阴阳寮 
	I_HOME_GUILD = RuleImage(roi_front=(540,607,53,50), roi_back=(540,607,53,50), threshold=0.8, method="Template matching", file="./tasks/GameUi/res/res_home_guild.png")
	# 组队 
	I_HOME_TEAM = RuleImage(roi_front=(430,616,49,61), roi_back=(430,616,49,61), threshold=0.8, method="Template matching", file="./tasks/GameUi/res/res_home_team.png")
	# 同心队 
	I_HOME_CONCENTRIC_TEAM = RuleImage(roi_front=(310,618,67,60), roi_back=(310,618,67,60), threshold=0.8, method="Template matching", file="./tasks/GameUi/res/res_home_concentric_team.png")
	# 珍旅居 
	I_HOME_HELP = RuleImage(roi_front=(201,617,56,57), roi_back=(201,617,56,57), threshold=0.8, method="Template matching", file="./tasks/GameUi/res/res_home_help.png")
	# 图鉴 
	I_HOME_COLLECT = RuleImage(roi_front=(92,607,48,74), roi_back=(92,607,48,74), threshold=0.8, method="Template matching", file="./tasks/GameUi/res/res_home_collect.png")


	# Ocr Rule Assets
	# 庭院到探索 
	O_HOME_EXPLORE = RuleOcr(roi=(310,105,858,194), area=(0,0,100,100), mode="Full", method="Default", keyword="探索", name="home_explore")
	# Ocr-description 
	O_NEW = RuleOcr(roi=(0,0,100,100), area=(0,0,100,100), mode="Single", method="Default", keyword="", name="new")


