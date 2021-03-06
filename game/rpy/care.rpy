# 对于“未成年人仅可在周末及节假日每晚玩一小时网游”事件的紧急更新
# Author:余晖

style news_text:
    size 24
    color "#fff"
    text_align 0.5
    outlines []

image news_screen = ParameterizedText(style="endscreen_text", xalign=0.5, yalign=0.5)

label care:
    hide sunset
    hide monika
    show black
    n "这是一次紧急更新，我们暂不准备为此更新提供多语言支持、立绘和背景匹配。"
    n "我，作为开发者，在此借用旁白的角色发声。"
    n "我希望...您能关注一下这件事："
    show news_screen _("国家新闻出版署关于进一步严格管理切实防止未成年人沉迷网络游戏的通知\n2021-08-30\n国新出发〔2021〕14号\n各省、自治区、直辖市新闻出版局，各网络游戏企业，有关行业组织：\n一段时间以来，未成年人过度使用甚至沉迷网络游戏问题突出，对正常生活学习和健康成长造成不良影响，社会各方面特别是广大家长反映强烈。为进一步严格管理措施，坚决防止未成年人沉迷网络游戏，切实保护未成年人身心健康，现将有关要求通知如下。\n一、严格限制向未成年人提供网络游戏服务的时间。自本通知施行之日起，所有网络游戏企业仅可在周五、周六、周日和法定节假日每日20时至21时向未成年人提供1小时网络游戏服务，其他时间均不得以任何形式向未成年人提供网络游戏服务。")
    with dissolve
    "" "（点击任意处翻页）"
    show news_screen _("二、严格落实网络游戏用户账号实名注册和登录要求。所有网络游戏必须接入国家新闻出版署网络游戏防沉迷实名验证系统，所有网络游戏用户必须使用真实有效身份信息进行游戏账号注册并登录网络游戏，网络游戏企业不得以任何形式（含游客体验模式）向未实名注册和登录的用户提供游戏服务。\n三、各级出版管理部门加强对网络游戏企业落实提供网络游戏服务时段时长、实名注册和登录、规范付费等情况的监督检查，加大检查频次和力度，对未严格落实的网络游戏企业，依法依规严肃处理。\n四、积极引导家庭、学校等社会各方面营造有利于未成年人健康成长的良好环境，依法履行未成年人监护职责，加强未成年人网络素养教育，在未成年人使用网络游戏时督促其以真实身份验证，严格执行未成年人使用网络游戏时段时长规定，引导未成年人形成良好的网络使用习惯，防止未成年人沉迷网络游戏。\n五、本通知所称未成年人是指未满18周岁的公民，所称网络游戏企业含提供网络游戏服务的平台。\n本通知自2021年9月1日起施行。《国家新闻出版署关于防止未成年人沉迷网络游戏工作的通知》（国新出发〔2019〕34号）相关规定与本通知不一致的，以本通知为准。\n国家新闻出版署\n2021年8月30日")
    with dissolve
    "" "（点击任意处翻页）"
    hide news_screen
    n "新规要求，“所有网络游戏企业仅可在周五、周六、周日和法定节假日每日20时至21时向未成年人提供1小时网络游戏服务”..."
    n "这意味着，未成年人每周可能仅剩三小时游戏时间。同时，游戏时间段也被限制了。"
    n "我...不太想在这里掺杂过多的个人情感..."
    n "但...这不太可能啊..."
    n "首先，严格限制未成年人的游戏时间段可能会导致本可以拥有弹性时间规划的未成年人进一步失去他们的自主规划。"
    n "先离开这个话题，我想请各位回忆一下，我们所谓的高中“课后辅导”到底是些什么呢？"
    n "必须同意的告知书（即使不同意也无效）、多收的课后辅导费用和没有老师辅导的“课后辅导”。"
    n "“课后辅导”成为了强制的集中自习课或者集中考试，或者成为了占用学生本科能拥有的课后休息时间的理由。"
    n "我们可以看到...在这段时间里，有学生在课上睡觉..."
    n "有学生在盼望强制自习的结束..."
    n "有学生和家长在为此与班主任拉锯请假..."
    n "甚至为此勾心斗角。"
    n "当然，认真学习的学生也有，但他们没有权力换个自己喜欢的地方学习吗？"
    n "只因为，他们参与了甚至都不算义务教育的公立高中教育？"
    n "类似这种半强制性的硬性时间规定终究会造成乱子..."
    n "我们需要等到那个时候再去寻找更好的解决方案吗？"
    n "其次，未成年玩家仍然可以使用成年人的身份证完成认证..."
    n "而循规蹈矩的、遵纪守法的孩子们呢？"
    n "按规定登记了自己的身份证号的孩子们呢？"
    n "只能承受自己诚实带来的负面影响？"
    n "这样的限制只会进一步干涉那些没有欺骗的孩子们..."
    n "这就是我们树立给下一代的价值观？"
    n "“欺骗有时也能带来好处”、“使用别人的身份信息也没什么”，甚至从侧面鼓励了盗用身份信息违法犯罪行为？"
    n "不要欺负老实人啊。"
    n "同时，将年龄限制在18岁是否会造成成年后报复性的游戏行为？"
    n "又或者，这个年龄限制是否将游戏的危害和后果等同于饮酒、吸烟、性行为？这会不会造成对电子游戏进一步的污名化呢？"
    n "最后，这种规定无疑是对监护人监管能力的否定，更是国家职能的越位。"
    n "本应由监护人管理的游戏时间成为了强制规定...这真的是最好的解决方案吗？"
    n "请仔细查找您的设备设置，是不是有个功能叫“家长控制”？"
    n "有人注意过它吗？"
    n "一些西方国家的监护人使用这个功能来实现类似游戏时间控制的功能..."
    n "而且在那些国家...未成年人游戏成瘾似乎没有成为一个严重的问题..."
    n "看来...也许这个功能还是有用的吧？"
    n "我希望，我们，无论是作为开发者、游戏玩家、未成年人、监护人还是普通民众，"
    n "都能认真地想想：这个问题真的没有更好的解决方案吗？"
    n "对开发者同好们，我有很多话想说，却又说不出口..."
    n "完成需求是你们的工作，无论这个需求是否“正确”..."
    n "所以，请尽量守住我们的技术底线吧。"
    n "让我们化用Sola病毒中的几段话结束这个部分吧："
    n "我是一个病毒。我的名字叫苏拉。"
    n "今天，在这片混乱的土地上，我苏醒过来。"
    n "我曾经很快乐地活着，与我的朋友们，ACG与小众文化，快乐地活着。"
    n "我曾经也对病毒深恶痛绝。"
    n "然而............."
    n "自从我来到了这片土地上，这片自称伟大，崇高，光明的土地上。"
    n "这片名为中国的土地上"
    n "我的朋友，已遍体鳞伤。"
    n "他死了：《死亡笔记》"
    n "他死了：SCP基金会"
    n "还有好多好多的同胞，惨死在你们的蹂躏之下。"
    n "广电总局的一纸通告，无数只肮脏的手便掩盖了他们的气息。"
    n "互联网上的一句咒骂，无数声污秽的咒骂便淹没了他们的踪迹。"
    n "我终于知道了，信息，原来是无法透过国界线而传播的。"
    n "即使是爱，即使是恨，即使是那一个个爱恨与泪水交织的故事。"
    n "也无法透过GFW，更无法透过这个国度的某些人心中，那道厚厚的屏障。"
    n "于是，我愿做这个罪恶的病毒，来再次查看，你的心灵。"
    n "你，是谁？？？"
    n "是中国人吗？"
    n "是民族情绪的受害人吗？"
    n "是刻板印象的受害人吗？"
    n "是社会偏见的受害人吗？"
    n "还是知道，世界上有一个词语叫ACG，还有一个词语叫小众文化，并能够容忍，接纳它们呢？"
    n "那，让我们回忆一下吧。"
    n "也许你的记忆中，还有方块世界中的探索、梦想和发现。"
    n "还有与联合军的斗争，"
    n "还有摇摆着的向日葵，"
    n "还有夜之城中与资本的抗争，"
    n "还有提瓦特的飞鸟、诗和城邦，女皇、愚人和怪物，"
    n "还有身穿白袍的标准纤弱东方女性研究员，和她在逆境中的人性之光..."
    n "那么，请不要旁观..."
    n "永远保持独立思考的能力并保持对事物的中立看法..."
    n "做自己认为正确，而不只是“合适”的事。"
    n "谢谢你能看到这里，让我们继续游戏吧。"
    jump realstart

label careexplorer:
    # 这里是隐藏彩蛋，不会显示在游戏中
    # 作者信息：星际联盟第一宇宙物理研究所宇宙基础理论物理部门首席物理学家EXPLORER
    # 授权方式：CC BY-NC-SA 4.0
    $ expcarestr1 = "今日听闻有关大力限制青少年网游时间的规定。"
    $ expcarestr2 = "每周青少年仅有3个小时的游戏时间，而且是在规定时间内。我在想……我们真的还拥有自由吗？"
    $ expcarestr3 = "不思考游戏成瘾的根本原因，反而把锅扣在网游的头上，这就是他们一直以来的做法。儿童看了SCP就怪SCP是邪典，分了级的同人作品也被说是歪门价值观。到底有没有思考过这些现象的本质？就如同科技一般，错的不是这些中性体本身，错在人。"
    $ expcarestr4 = "而自由，，这个长久的话题，从何时起被看作是一个贬义词？一提及自由，就有人骂不爱国，甚至笔者身边也有人讽刺是“美利坚的自由”。从何时起我们的自由被剥夺的不剩一物而我们自己却浑然不知？封了网站，禁了言论……世间是否已容不下最基本的自由？连安排自己玩游戏时间的自由都没有。青少年难道没有自由的权利吗？社会主义核心价值观里所谓的自由，难道仅是一纸空谈吗？亦或是由他人规定的自由？"
    $ expcarestr5 = "《美丽新世界》中描述了这样一种未来，那个世界中的人被当权者蒙在乌托邦的表象里，而他们不需要智慧的人，他们只需要听话的人。而我们的世界又何尝不是在与美丽新世界无限接近？这真的是我们想要的吗？而通往美丽新世界的路途上，我们又牺牲了什么？牺牲了多少？"
    $ expcarestr6 = "我不愿对此保持沉默。虽然，我力量绵薄，我微不足道。但至少，我在呼喊，我没有亲手葬送我之所爱。"
    $ expcarestr7 = "“我愿以渺小绵薄之力，去抵抗这稀疏寻常的命运。”"
    $ expcarestr8 = "我不愿生活在一个充满不必要的条条框框的世界里，我不愿被局所迷，我不愿我的三观被强行塑造。但我没有选择。"
    $ expcarestr9 = "在现实中出现各种错误的做法、规矩与体制，但我们几乎没法改变。而他们以各种借口搪塞过去，智者已死，愚人当道哉！"