# Chapter 0

label ch0:
    scene bg basic
    n "你好，[player]！"
    n "这是一个...互动小说游戏。"
    n "呃..."
    n "与其说是互动小说..."
    n "还不如说是作者的毕业总结。"
    menu:
        "那...作者是谁？":
            jump author
        "毕业总结？":
            jump graduate

label author:
    n "请允许我介绍本项目的作者..."
    show sunset smile0
    # 这里有人反馈余晖的立绘太大，突然出现吓人。
    "（未知）" "（脸怼镜头）"
    n "余晖！"
    show sunset explain7
    # 后加对吓人的处理方法和交互
    s "你好！如果吓到你很抱歉。"
    s "也许你认为这个形象过于诡异？"
    s "“余晖”这个假名来自《My Little Pony》及其衍生剧集，她的形象也来源于此。"
    s "也就是你现在看到我的样子。"
    show sunset explain5
    s "选择这个形象的另一个原因是..."
    s "作者不想画立绘。"
    show sunset explain1
    # 版权声明放在这里用于增强荒诞感
    s "注意：版权声明！"
    s "“余晖烁烁”及其艺术作品版权属Hasbro, Inc。"
    s "My Little Pony®是Hasbro, Inc的注册商标。此项目与Hasbro, Inc无关。"
    jump reason

label graduate:
    n "是的。"
    n "如果您并不了解，那么此游戏可能并不适合你。"
    n "请退出并删除此游戏。"
    menu:
        "退出。":
            # 不用确认的直接退出
            $ renpy.quit()
            return
        "我知道了...":
            pass
    n "那么..."
    jump author

label reason:
    s "（清嗓）"
    s "项目创作理由也很简单。"
    show sunset explain5
    s "我一直想写个毕业总结，但总是在拖延。"
    s "又发生了一些事故，所以一直没有信心把它写出来。"
    # 不想被提到的人 我没办法...让你放下？
    # 上面这句话有语法错误？
    # 这句话是故事组留下的，不知道什么意思
    s "不过，最近想了想..."
    show sunset clap0
    s "再不写都开学了，那就真的没机会了。"
    s "所以，这就是我争取在开学前发布的项目，也许也是本假期的最后一个。"
    s "这个项目的快速成型离不开《心跳文学部》——一个优秀的使用相同引擎的饱受误解的meta类视觉小说游戏。"
    # 限制级游戏 不适合儿童和易受影响的人 缺乏分级制度使得此游戏在中国大陆遭到封杀
    show sunset explain4
    s "本项目未经许可地使用了项目DDLCModTemplate2.0的部分源码和《心跳文学部》的部分资源文件。"
    # 需要找方法解决这个问题或者避免被发现
    s "这在严格上是违背职业道德，甚至是非法的..."
    s "再次向《心跳文学部》的制作项目组Team Salvato表示感谢。"
    show sunset explain5
    s "貌似废话太多了点..."
    s "这是一个互动类的“毕业总结”、或者“问答”描述得更合适一些。"
    s "这个程序记录了我认为可能会被问到的问题和我对它们的答案。"
    s "你只需要选择，然后阅读屏幕上显示的文字。"
    s "这就是本游戏的全部内容——没有成就、没有彩蛋、存档无意义。"
    # 彩蛋的事情是骗你的
    show sunset smile0
    s "让我们开始吧。"
    hide sunset
    jump ch1