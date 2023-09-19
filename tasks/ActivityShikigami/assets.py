from module.atom.image import RuleImage
from module.atom.click import RuleClick
from module.atom.long_click import RuleLongClick
from module.atom.swipe import RuleSwipe
from module.atom.ocr import RuleOcr
from module.atom.list import RuleList

# This file was automatically generated by ./dev_tools/assets_extract.py.
# Don't modify it manually.
class ActivityShikigamiAssets: 


	# Image Rule Assets
	# 进入活动 
	I_SHI = RuleImage(roi_front=(1014,206,49,39), roi_back=(85,170,1029,142), threshold=0.7, method="Template matching", file="./tasks/ActivityShikigami/as/as_shi.png")
	# 左上角返回 
	I_BACK_GREEN = RuleImage(roi_front=(13,18,44,44), roi_back=(13,18,49,49), threshold=0.8, method="Template matching", file="./tasks/ActivityShikigami/as/as_back_green.png")
	# 进入爬塔 
	I_BATTLE = RuleImage(roi_front=(1010,189,47,172), roi_back=(1010,189,52,177), threshold=0.8, method="Template matching", file="./tasks/ActivityShikigami/as/as_battle.png")
	# 归鹿之途 
	I_DRUM = RuleImage(roi_front=(1011,114,29,31), roi_back=(1011,114,29,31), threshold=0.8, method="Template matching", file="./tasks/ActivityShikigami/as/as_drum.png")
	# 上锁图标 
	I_LOCK = RuleImage(roi_front=(795,654,25,32), roi_back=(795,654,25,32), threshold=0.8, method="Template matching", file="./tasks/ActivityShikigami/as/as_lock.png")
	# 还未上锁图片 
	I_UNLOCK = RuleImage(roi_front=(1135,483,27,27), roi_back=(795,654,27,27), threshold=0.8, method="Template matching", file="./tasks/ActivityShikigami/as/as_unlock.png")
	# 点击战斗 
	I_FIRE = RuleImage(roi_front=(1135,483,22,22), roi_back=(1104,551,138,130), threshold=0.8, method="Template matching", file="./tasks/ActivityShikigami/as/as_fire.png")
	# 体力按钮 
	I_AP = RuleImage(roi_front=(1136,488,20,22), roi_back=(1133,481,27,37), threshold=0.8, method="Template matching", file="./tasks/ActivityShikigami/as/as_ap.png")
	# 活动体力 
	I_AP_ACTIVITY = RuleImage(roi_front=(1132,485,27,31), roi_back=(1127,479,37,44), threshold=0.8, method="Template matching", file="./tasks/ActivityShikigami/as/as_ap_activity.png")
	# 切换按键 
	I_SWITCH = RuleImage(roi_front=(1211,486,33,30), roi_back=(1211,486,33,30), threshold=0.8, method="Template matching", file="./tasks/ActivityShikigami/as/as_switch.png")
	# 购买活动的体力 
	I_BUY_JADE = RuleImage(roi_front=(1004,192,38,42), roi_back=(836,619,38,42), threshold=0.8, method="Template matching", file="./tasks/ActivityShikigami/as/as_buy_jade.png")
	# 增加到最大 
	I_ADD_MAX = RuleImage(roi_front=(17,24,33,37), roi_back=(974,524,57,54), threshold=0.8, method="Template matching", file="./tasks/ActivityShikigami/as/as_add_max.png")
	# description 
	I_NEW = RuleImage(roi_front=(1004,192,65,52), roi_back=(0,0,100,100), threshold=0.8, method="Template matching", file="./tasks/ActivityShikigami/as/as_new.png")


	# Ocr Rule Assets
	# 体力的数量检测 
	O_REMAIN_AP = RuleOcr(roi=(1096,26,116,28), area=(1092,23,121,33), mode="DigitCounter", method="Default", keyword="", name="remain_ap")
	# 活动体力的剩余检测 
	O_REMAIN_AP_ACTIVITY = RuleOcr(roi=(707,24,106,34), area=(707,24,106,34), mode="DigitCounter", method="Default", keyword="", name="remain_ap_activity")
	# 还有多少次购买体力的机会 
	O_REMAIN_BUY = RuleOcr(roi=(808,531,39,42), area=(808,531,39,42), mode="DigitCounter", method="Default", keyword="", name="remain_buy")


