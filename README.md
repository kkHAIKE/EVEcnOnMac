# EVEcnOnMac

## 申明
1. **当前方案需要修改 EVEGuardx64.exe(原因后详)，正在研究无修改的方式**
2. ![支付宝捐助](https://github.com/kkHAIKE/fake115/blob/master/qrcode.png)
3. 游戏币捐助: 堕花月
4. 此方法也可适用 linux

## 准备
1. EVE 在 win 下已经装好的游戏目录
2. wine 容器
    1. CrossOver 容器（收费），上手简单（建议）
    2. PlayOnMac 容器（免费），考验操作

## CrossOver 容器
我的版本 19.0.1.32222，价格 149RMB，https://www.crossoverchina.com/

1. 进入程序，容器菜单->新建容器
2. 容器名字 *EVE*，容器类型 *Windows 7 64-bit*（一定要选 64 位，EVE 的要求），点击 **创建**
3. 一定要确定现在所显示的主界面如图所示，不一致则点击主界面工具栏的第1、第2个按钮调整
    ![CrossOver](https://github.com/kkHAIKE/EVEcnOnMac/blob/master/CrossOver.png)
4. 主界面右击刚刚建立的 *EVE* 容器，选择 *安装软件到 "EVE"*
5. 搜索栏输入 *核心字体*，在弹出的列表选择同名项目，点击 **继续**，点击 **安装**（不做这步无法显示对话框内容、输入文字）
6. （可选），希望 雅黑 的玩家可以在 *核心字体* 安装完毕后，再在第 4 步的搜索框输入 *微软雅黑*，进行安装
7. 点击主界面的 *运行命令*，点击 **浏览**，选择 `{EVE目录}/Launcher/evelauncher.exe`，点击 **将指令保存到面板**，就可以在 主界面 上看到 *evelauncher* 图标

## PlayOnMac 容器
下载地址，https://www.playonmac.com/en/download.html

1. 先从 https://phoenicis.playonlinux.com/index.php/wine?os=darwin 网站选个当前 wine 的稳定版下载（我试过新的版本都起不来），当前是 http://www.playonlinux.com/wine/binaries/phoenicis/upstream-darwin-amd64/PlayOnLinux-wine-5.0.1-upstream-darwin-amd64.tar.gz （要 upstream 版本）
2. 终端输入 `mkdir -p ~/Library/PlayOnMac/wine/darwin-amd64/5.0.1`（最后的版本号和你下的一致），`tar -zxvf PlayOnLinux-wine-5.0.1-upstream-darwin-amd64.tar.gz路径 -C ~/Library/PlayOnMac/wine/darwin-amd64/5.0.1`
3. 下载 5.0.1 对应的 mono，https://dl.winehq.org/wine/wine-mono/4.9.4/wine-mono-4.9.4.msi
4. 下载 5.0.1 对应的 gecko，https://dl.winehq.org/wine/wine-gecko/2.47.1/wine-gecko-2.47.1-x86_64.msi ，https://dl.winehq.org/wine/wine-gecko/2.47.1/wine-gecko-2.47.1-x86.msi
5. 终端输入 `mkdir -p ~/.cache/wine`，使用 Finder 的 前往 菜单->前往文件夹，输入 *~/.cache/wine*，将前两步下载的 3 个文件拷贝进来
6. 进入程序，主界面点击 **配置**，左下角 **新建**，一定要选择 *64 bit windows installation*，下一步选择 *5.0.1*（如果这里是空的，说明步骤12出问题了），输入虚拟盘名称 *EVE*，等待完成
7. 配置界面左边点击刚刚新建的 *EVE*，选择标签 **安装内容**，找到 *Microsoft Core Fonts*，点击 **安装**，这里下载很慢要等很久，耐心点
    ![PlayOnMac](https://github.com/kkHAIKE/EVEcnOnMac/blob/master/PlayOnMac.png)
8. 配置界面选择标签 **概况**，点击 **自该虚拟盘创建快捷方式**，选择 **浏览**，点击 **浏览**，选择 `{EVE目录}/Launcher/evelauncher.exe`，完成后可在 主界面 看到 *evelauncher* 图标

## 试运行
双击主界面的 *evelauncher* 图标，然后正常登录启动游戏，应该会看到如下出错画面，然后进入游戏得到 "游戏运行的环境不安全。客户端将在20秒后关闭。" 提示

![错误](https://github.com/kkHAIKE/EVEcnOnMac/blob/master/错误.png)
![错误详情](https://github.com/kkHAIKE/EVEcnOnMac/blob/master/错误详情.png)

## 补丁
待续