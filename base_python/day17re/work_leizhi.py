# -*- coding:utf-8 -*-
import re
# 将一个字符串中每一个a替换成一个b。
ss = 'adsafdsfa afa abdfa a adfws'
ss = re.sub('a','b',ss)
# 'a+' 可以把多个连续的a 换一个b
print(ss)
# 在str类型下，\d匹配的内容远远不止于0-9十个阿拉伯数字。尝试指出\d的具体匹配依据是什么。0x0010ffff
def re_d():
   li = []
   for i in range(0x0000, 0x0010ffff):
      r = re.search('\d', chr(i))
      if r:
         t = (i, chr(i))
         li.append(t)
   return li
#print(re_d())
#print(len(re_d()))
# 在网页中匹配所有的<div>
r = re.findall(r'<div>','<div><div>54aa34a5</div></div>')
print(r)
print(len(r))
# pattern = ''
# for i in len(r):
#    pattern +='<div>'
# 提取所有div中的内容。<div>aaa</div>  （思考：<div><div>aaa</div></div>）。
target = 'div><div>23<a>34aaa</a><img class="sd"></div></div>'
r = re.search(r'>(\b.*?)<.*?',target)
print(r)
print('rr',r.group(1))
rrr = re.search(r'.*<div.*?>(.*?)</div>.*?',target)
print('rrr',rrr.group(1))
pattern = '(.*?)'
for i in range(len(re.findall(r'<div>',target))):
   pattern = '<div>'+pattern+'</div>'
rr = re.search(pattern,target)
print(rr.group(1))
# 提取拉钩首页上的图片链接。（*.jpg gif bmp）

text=""""
<html><head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">

<meta http-equiv="Pragma" content="no-cache">
<meta http-equiv="Cache-Control" content="no-cache">
<meta http-equiv="Expires" content="0">

<meta http-equiv="Cache-Control" content="no-siteapp">
<link rel="alternate" media="handheld" href="#">
<!-- end 云适配 -->
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>找工作-互联网招聘求职网-拉勾网</title>
<meta property="qc:admins" content="23635710066417756375">
<meta content="拉勾网是3W旗下的互联网领域垂直招聘网站" name="description">
<meta content="拉勾,拉勾网,拉勾招聘,拉钩, 拉钩网 ,互联网招聘,拉勾互联网招聘, 移动互联网招聘, 垂直互联网招聘, 微信招聘, 微博招聘, 拉勾官网, 拉勾百科,跳槽, 高薪职位, 互联网圈子, IT招聘, 职场招聘, 猎头招聘,O2O招聘, LBS招聘, 社交招聘, 校园招聘, 校招,社会招聘,社招" name="keywords">
<link rel="Shortcut Icon" href="https://www.lgstatic.com/lp/static/images/favicon_faed927.ico">
<link rel="stylesheet" type="text/css" href="https://www.lgstatic.com/lp/static/css/all_3790f29.css?v=6ad6db7d48daa75d">
<link rel="stylesheet" type="text/css" href="https://www.lgstatic.com/lp/static/css/common_fa9d8c1.css?v=db825f5242c0857c">
<link rel="stylesheet" type="text/css" href="https://www.lgstatic.com/lp/static/js/lib/idangerous.swiper_c064b4a.css">
<script charset="utf-8" src="https://tag.baidu.com/vcard/v.js?siteid=4899764&amp;url=https%3A%2F%2Fwww.lagou.com%2Flp%2Fhtml%2Fcommon.html%3Futm_source%3Dm_cf_cpt_baidu_pc&amp;source=https%3A%2F%2Fwww.baidu.com%2Fs%3Ftn%3D92109629_hao_pg%26word%3D%25E6%258B%2589%25E5%258B%25BE&amp;rnd=1392189690&amp;hm=1"></script><script async="" src="//www.google-analytics.com/analytics.js"></script><script src="//hm.baidu.com/hm.js?4233e74dff0ae5bd0a3d81c6ccf756e6"></script><script async="" src="//a.lagou.com/js/a.js"></script><script type="text/javascript" src="https://www.lgstatic.com/lp/static/js/lib/jquery_token_e76369c.js"></script>
<script type="text/javascript" src="https://www.lgstatic.com/lp/static/js/lib/jquery.lib.min_14e65d5.js"></script>
<script type="text/javascript" src="https://www.lgstatic.com/lp/static/js/lib/md5_a4a0329.js"></script>
<script type="text/javascript" src="https://www.lgstatic.com/lp/static/js/lib/handlebars-v1.3.0_34a027f.js"></script>
<script type="text/javascript" src="https://www.lgstatic.com/lp/static/js/lib/idangerous.swiper.min_1a65189.js"></script>
<script>
	// 获取iframe页面中传过来的code和token值
	window.addEventListener('message', function (e) {
		var origin = e.origin || e.originalEvent.origin;
		if (origin.indexOf(window.location.protocol + '//passport.lagou.com') !== 0) { // 校验判断消息来源
			return;
		}

		var data = e.data || e.originalEvent.data;
		if (data && data.code && data.token) {
			window.X_Anti_Forge_Code = data.code;
			window.X_Anti_Forge_Token = data.token;
		}
	});
</script>
</head>
<body>
<iframe id="lgProtect" src="https://passport.lagou.com/protect/protect.do" frameborder="0" style="position: fixed; width: 0; height: 0"></iframe>
	<div class="box">
		<div class="header">
			<div class="header-border"></div>
			<div class="header-bg clearfix">
				<img class="logo" src="https://www.lgstatic.com/lp/static/images/logo-slogan_6187040.png" width="222" height="34">
				<div class="hd_right">
					<a class="show_qrcode_app" href="javascript:void(0);"><img class="icon_app" src="https://www.lgstatic.com/lp/static/images/icon-app_bf9763f.png" width="10" height="15"> <span>拉勾APP</span><img class="qrcode_app" src="https://www.lgstatic.com/lp/static/images/qrcode-new_8484b5d.png" width="256" height="256"></a>
					<!-- <span class="show_qiyeban">去企业版</span> -->
					<a class="link_login" target="_blank" href="https://passport.lagou.com/login/login.html?service=https%3a%2f%2fwww.lagou.com%2f"><span>去登录 &gt;</span></a>
				</div>
			</div>
		</div>
		<div class="middle">
			<div class="contain clearfix">
				<div class="lp_left">
					<div class="tips-reg">
						<img class="shade" src="https://www.lgstatic.com/lp/static/images/shade_4b7e459.png">
						<img class="shade-close" src="https://www.lgstatic.com/lp/static/images/shade-close_8a88206.png">
					</div>
					<div class="swiper-container">
						<div class="swiper-wrapper" style="width: 2800px; height: 458px; transform: translate3d(-1120px, 0px, 0px); transition-duration: 2s;"><div class="img-box swiper-slide swiper-slide-duplicate" style="width: 560px; height: 458px;">
								<img alt="网易" class="three-1" src="https://www.lgstatic.com/lp/static/images/common/three-1_81cd4d1.png">
								<img alt="嘀嗒拼车" class="three-2" src="https://www.lgstatic.com/lp/static/images/common/three-2_da82a94.png">
								<img alt="唯品会" class="three-3" src="https://www.lgstatic.com/lp/static/images/common/three-3_773c19b.png">
								<img alt="去哪儿网" class="three-4" src="https://www.lgstatic.com/lp/static/images/common/three-4_6994cf6.png">
								<img alt="百度" class="three-5" src="https://www.lgstatic.com/lp/static/images/common/three-5_3949ca3.png">
								<img alt="快云科技" class="three-6" src="https://www.lgstatic.com/lp/static/images/common/three-6_8824d25.png">
								<img alt="蘑菇街" class="three-7" src="https://www.lgstatic.com/lp/static/images/common/three-7_b60c56d.png">
								<img alt="支付宝" class="three-8" src="https://www.lgstatic.com/lp/static/images/common/three-8_d4f3072.png">
								<img alt="网易" class="three-9" src="https://www.lgstatic.com/lp/static/images/common/three-9_83d628c.png">
								<img alt="滴滴出行" class="three-10" src="https://www.lgstatic.com/lp/static/images/common/one-6_6330b18.png">
								<img alt="美团网" class="three-11" src="https://www.lgstatic.com/lp/static/images/common/three-11_b254951.png">
							</div>
							<div class="img-box swiper-slide" style="width: 560px; height: 458px;">
								<img alt="唯品会" class="one-1" src="https://www.lgstatic.com/lp/static/images/common/one-1_8393a8c.png">
								<img alt="投哪网" class="one-2" src="https://www.lgstatic.com/lp/static/images/common/one-2_ff130bf.png">
								<img alt="百度" class="one-3" src="https://www.lgstatic.com/lp/static/images/common/one-3_50c6041.png">
								<img alt="快云科技" class="one-4" src="https://www.lgstatic.com/lp/static/images/common/one-4_2fb6d32.png">
								<img alt="蘑菇街" class="one-5" src="https://www.lgstatic.com/lp/static/images/common/one-5_eac4895.png">
								<img alt="滴滴出行" class="one-6" src="https://www.lgstatic.com/lp/static/images/common/one-6_6330b18.png">
								<img alt="宜信" class="one-7" src="https://www.lgstatic.com/lp/static/images/common/one-7_f1cf994.png">
								<img alt="网易" class="one-8" src="https://www.lgstatic.com/lp/static/images/common/one-8_ed2510c.png">
								<img alt="阿姨帮" class="one-9" src="https://www.lgstatic.com/lp/static/images/common/one-9_9817c59.png">
								<img alt="去哪儿网" class="one-10" src="https://www.lgstatic.com/lp/static/images/common/one-10_cf571e0.png">
								<img alt="大众点评" class="one-11" src="https://www.lgstatic.com/lp/static/images/common/one-11_216819d.png">
							</div>
							<div class="img-box swiper-slide swiper-slide-visible swiper-slide-active" style="width: 560px; height: 458px;">
								<img alt="乐视网" class="two_1" src="https://www.lgstatic.com/lp/static/images/common/two_1_3f0e9b5.png">
								<img alt="翼支付" class="two_2" src="https://www.lgstatic.com/lp/static/images/common/two_2_b5cbd18.png">
								<img alt="麦乐购" class="two_3" src="https://www.lgstatic.com/lp/static/images/common/two_3_c3bff15.png">
								<img alt="百度" class="two_4" src="https://www.lgstatic.com/lp/static/images/common/two_4_23a365f.png">
								<img alt="唯品会" class="two_5" src="https://www.lgstatic.com/lp/static/images/common/two_5_8393a8c.png">
								<img alt="腾讯" class="two_6" src="https://www.lgstatic.com/lp/static/images/common/two_6_0917fdb.png">
								<img alt="搜狐" class="two_7" src="https://www.lgstatic.com/lp/static/images/common/two_7_06e7329.png">
								<img alt="京东金融" class="two_8" src="https://www.lgstatic.com/lp/static/images/common/two_8_fc7e9a8.png">
								<img alt="聚美优品" class="two_9" src="https://www.lgstatic.com/lp/static/images/common/two_9_c5e137d.png">
								<img alt="滴滴出行" class="two_10" src="https://www.lgstatic.com/lp/static/images/common/one-6_6330b18.png">
								<img alt="今日头条" class="two_11" src="https://www.lgstatic.com/lp/static/images/common/two_11_0d5d821.png">
							</div>
							<div class="img-box swiper-slide" style="width: 560px; height: 458px;">
								<img alt="网易" class="three-1" src="https://www.lgstatic.com/lp/static/images/common/three-1_81cd4d1.png">
								<img alt="嘀嗒拼车" class="three-2" src="https://www.lgstatic.com/lp/static/images/common/three-2_da82a94.png">
								<img alt="唯品会" class="three-3" src="https://www.lgstatic.com/lp/static/images/common/three-3_773c19b.png">
								<img alt="去哪儿网" class="three-4" src="https://www.lgstatic.com/lp/static/images/common/three-4_6994cf6.png">
								<img alt="百度" class="three-5" src="https://www.lgstatic.com/lp/static/images/common/three-5_3949ca3.png">
								<img alt="快云科技" class="three-6" src="https://www.lgstatic.com/lp/static/images/common/three-6_8824d25.png">
								<img alt="蘑菇街" class="three-7" src="https://www.lgstatic.com/lp/static/images/common/three-7_b60c56d.png">
								<img alt="支付宝" class="three-8" src="https://www.lgstatic.com/lp/static/images/common/three-8_d4f3072.png">
								<img alt="网易" class="three-9" src="https://www.lgstatic.com/lp/static/images/common/three-9_83d628c.png">
								<img alt="滴滴出行" class="three-10" src="https://www.lgstatic.com/lp/static/images/common/one-6_6330b18.png">
								<img alt="美团网" class="three-11" src="https://www.lgstatic.com/lp/static/images/common/three-11_b254951.png">
							</div>
						<div class="img-box swiper-slide swiper-slide-duplicate" style="width: 560px; height: 458px;">
								<img alt="唯品会" class="one-1" src="https://www.lgstatic.com/lp/static/images/common/one-1_8393a8c.png">
								<img alt="投哪网" class="one-2" src="https://www.lgstatic.com/lp/static/images/common/one-2_ff130bf.png">
								<img alt="百度" class="one-3" src="https://www.lgstatic.com/lp/static/images/common/one-3_50c6041.png">
								<img alt="快云科技" class="one-4" src="https://www.lgstatic.com/lp/static/images/common/one-4_2fb6d32.png">
								<img alt="蘑菇街" class="one-5" src="https://www.lgstatic.com/lp/static/images/common/one-5_eac4895.png">
								<img alt="滴滴出行" class="one-6" src="https://www.lgstatic.com/lp/static/images/common/one-6_6330b18.png">
								<img alt="宜信" class="one-7" src="https://www.lgstatic.com/lp/static/images/common/one-7_f1cf994.png">
								<img alt="网易" class="one-8" src="https://www.lgstatic.com/lp/static/images/common/one-8_ed2510c.png">
								<img alt="阿姨帮" class="one-9" src="https://www.lgstatic.com/lp/static/images/common/one-9_9817c59.png">
								<img alt="去哪儿网" class="one-10" src="https://www.lgstatic.com/lp/static/images/common/one-10_cf571e0.png">
								<img alt="大众点评" class="one-11" src="https://www.lgstatic.com/lp/static/images/common/one-11_216819d.png">
							</div></div>
					</div>
					<div class="comp_box">
					</div>
				</div>
				<div class="lp_login">
					<div class="tab"><i></i><span>注册拉勾</span></div>
					<form id="phone_form" method="post" action="javascript:;">
						<ul>
							<li>
								<span class="area_code">0086</span>
								<div class="area_code_list">
								    <dl class="code_list_main"><dt>常用</dt><dd>中国<span>0086</span></dd><dd>中国香港<span>00852</span></dd><dd>中国台湾<span>00886</span></dd><dd>中国澳门<span>00853</span></dd><dd>美国<span>001</span></dd><dt>A</dt><dd>澳大利亚<span>0061</span></dd><dd>中国澳门<span>00853</span></dd><dt>B</dt><dd>巴西<span>0055</span></dd><dt>D</dt><dd>德国<span>0049</span></dd><dt>E</dt><dd>俄罗斯<span>007</span></dd><dt>F</dt><dd>法国<span>0033</span></dd><dt>H</dt><dd>韩国<span>0082</span></dd><dt>J</dt><dd>加拿大<span>001</span></dd><dt>M</dt><dd>马来西亚<span>0060</span></dd><dd>美国<span>001</span></dd><dt>R</dt><dd>日本<span>0081</span></dd><dt>T</dt><dd>中国台湾<span>00886</span></dd><dd>泰国<span>0066</span></dd><dt>X</dt><dd>中国香港<span>00852</span></dd><dd>新加坡<span>0065</span></dd><dt>Y</dt><dd>印度<span>0091</span></dd><dd>英国<span>0044</span></dd><dt>Z</dt><dd>中国<span>0086</span></dd></dl>
								    <p class="tips">如果没有找到您的所在归属地，请拨打客服电话4006282835解决。</p>
								</div>
								<input type="text" placeholder="请输入常用手机号" id="lp_phone" name="phone" autocomplete="off">
							</li>
							<li class="yzmli">
								<input type="text" placeholder="请证明你不是机器人" id="lp_phone_yzm" name="yzm" autocomplete="on">
								<img src="https://passport.lagou.com/vcode/create?from=register&amp;refresh=1451121012510" alt="点击重试" class="yzm" width="98" height="40">
								<a href="javascript:;" class="reflash"></a>
							</li>
							<li class="coderli">
								<input type="text" placeholder="请输入手机验证码" id="lp_coder" name="coder" autocomplete="on">
								<span class="getcode">获取验证码</span>
							</li>
							<li class="verify_tips">
								<p class="verify_tips_main">收不到短信？请使用<input type="button" class="voice_btn" value="语音验证"></p>
								<p class="verify_tips_count_down">语音发送成功</p>
							</li>
							<!-- <li>
								<input type="password" placeholder="请设置密码" id="phone_password" name="password" autocomplete="off">
							</li> -->
						</ul>
						<a href="javascript:void(0);" class="submitBtn" data-lg-tj-id="2i50" data-lg-tj-no="idnull" data-lg-tj-cid="idnull">立即注册，获得高薪机会</a>
						<div class="lp_agreeNotice_box">
							<p>注册代表你已同意<a rel="nofollow" href="http://www.lagou.com/privacy.html" target="_blank" data-lg-tj-id="1Uy0" data-lg-tj-no="idnull" data-lg-tj-cid="idnull">「拉勾用户协议」</a></p>
							<!-- <label for="lp_agreeNotice" class="lp_agreeNotice" checked="true">
								<em style="background-position: 0px -12px;"></em><input type="checkbox" checked="true" name="checkbox" class="gree" style="display:none;">我已阅读并同意<a href="https://www.lagou.com/privacy.html" target="_blank">《拉勾用户协议》</a>
							</label> -->
						</div>
					</form>
					<!-- <div class="qqsina">
						<p>或使用以下帐号登录</p>
						<a href="/oauth20/auth_sinaWeiboProvider.html" target="_blank" class="icon_wb" title="使用新浪微博帐号登录"></a>
						<a href="/oauth20/auth_qqProvider.html" class="icon_qq" target="_blank" title="使用腾讯QQ帐号登录"></a>
						<a href="/oauth20/auth_weixinProvider.html" class="icon_weixin" target="_blank" title="使用微信帐号登录"></a>
					</div> -->
					<div class="login_btn">
						<a href="https://passport.lagou.com/login/login.html?service=https%3a%2f%2fwww.lagou.com%2f" target="_blank" data-lg-tj-id="2i30" data-lg-tj-no="idnull" data-lg-tj-cid="idnull">已有帐号，直接登录</a>
					</div>
				</div>
			</div>
		</div>
		<div class="footer">
			<ul class="info clearfix">
				<li>
					<img src="https://www.lgstatic.com/lp/static/images/icon1_f52334c.png">
					<div>
						<p class="title">极速入职</p>
						<p class="content">最快24小时拿到企业offer</p>
					</div>
				</li>
				<li>
					<img src="https://www.lgstatic.com/lp/static/images/icon2_7e69b67.png">
					<div>
						<p class="title">隐私保护</p>
						<p class="content">安全私密快速投简历</p>
					</div>
				</li>
				<li>
					<img src="https://www.lgstatic.com/lp/static/images/icon3_3a4ca6d.png">
					<div>
						<p class="title">薪资透明</p>
						<p class="content">薪资绝对透明真实谢绝面议</p>
					</div>
				</li>
				<li class="end">
					<img src="https://www.lgstatic.com/lp/static/images/icon4_bba10e4.png">
					<div>
						<p class="title">海量信息</p>
						<p class="content">海量互联网职位实时更新</p>
					</div>
				</li>
			</ul>
		</div>
		<div class="app_download_floating">
			<img class="qrcode_app" src="https://www.lgstatic.com/lp/static/images/qrcode-new_8484b5d.png" width="108" height="108">
			<p>扫码下载APP</p>
		</div>
	</div>

<!-- 公司卡片模版 -->
<script id="company-template" type="text/x-handlebars-template">
	<a class="close" href="javascript:;"></a>
	<p class="compName">{{company}}</p>
	<p class="slogan">{{slogan}}</p>
	<ul class="jobList">
	{{#each this.jobs}}
		<span>{{this}}</span>
	{{/each}}
	</ul>
	<ul class="welfare">
	{{#each this.profession}}
		<span>{{this}}</span>
	{{/each}}
	</ul>
</script>

<script type="text/javascript" src="https://www.lgstatic.com/lp/static/js/landingpage_fda1151.js?v=ed5320742424404c"></script>
<script type="text/javascript" src="https://www.lgstatic.com/lp/static/js/common_2475016.js?v=db825f5242c0857c"></script>
<script type="text/javascript" src="https://www.lgstatic.com/common/lg-tongji/js/plat_tj.js"></script>
<script type="text/javascript" src="https://www.lgstatic.com/common/lg-tongji/js/analytics.js"></script>
<script type="text/javascript" src="https://www.lgstatic.com/common/lg-tongji/js/web_tj/web_tj.js"></script>
<script>
	window.PAGE_ID = '2iH0';
	window.LGWebTj({
		_lt: 'pcpv'
	})
</script>
<script type="text/javascript" src="https://www.lagou.com/upload/oss.js"></script>

<div id="cboxOverlay" style="display: none;"></div><div id="colorbox" class="" role="dialog" tabindex="-1" style="display: none;"><div id="cboxWrapper"><div><div id="cboxTopLeft" style="float: left;"></div><div id="cboxTopCenter" style="float: left;"></div><div id="cboxTopRight" style="float: left;"></div></div><div style="clear: left;"><div id="cboxMiddleLeft" style="float: left;"></div><div id="cboxContent" style="float: left;"><div id="cboxTitle" style="float: left;"></div><div id="cboxCurrent" style="float: left;"></div><button type="button" id="cboxPrevious"></button><button type="button" id="cboxNext"></button><button id="cboxSlideshow"></button><div id="cboxLoadingOverlay" style="float: left;"></div><div id="cboxLoadingGraphic" style="float: left;"></div></div><div id="cboxMiddleRight" style="float: left;"></div></div><div style="clear: left;"><div id="cboxBottomLeft" style="float: left;"></div><div id="cboxBottomCenter" style="float: left;"></div><div id="cboxBottomRight" style="float: left;"></div></div></div><div style="position: absolute; width: 9999px; visibility: hidden; display: none;"></div></div><iframe src="https://passport.lagou.com/lp/html/jquery.html" id="jqueryIframe" style="display:none;"></iframe></body><div id="yiButton" style="display: none;">翻译</div><div id="onLineTransBu" style="display: none;"><img id="loading" src="chrome-extension://hlppekcioiicbfafmmgikkdkljnjpiao/images/loading.gif">网页翻译中...</div><div id="onLineFailResult" style="display: none;">翻译失败...</div><div id="C_outerbox_trans_div" class="C_outerbox_up" style="display: none;"><div id="C_cententbox_trans_div"><div id="cententbox_beforeFixBox"><p id="C_ptitle_trans_p">原文</p><p id="C_esay_trans_p"></p><div id="C_bottomdiv_trans_div"><img id="C_bottomimg_trans_img" src="chrome-extension://hlppekcioiicbfafmmgikkdkljnjpiao/images/img_logo.png" style="cursor: pointer;"><a id="C_bottoma_trans_a">翻译纠错<img id="hrefa" src="chrome-extension://hlppekcioiicbfafmmgikkdkljnjpiao/images/IconArrowRight.png"></a></div></div><div id="cententbox_afterFixBox"><p id="cententbox_trans_fix_error">翻译纠错</p><div id="cententbox_trans_fix_box"><textarea id="cententbox_trans_fix_content"></textarea><button id="cententbox_comfirmfix">确定</button></div></div></div><div id="C_innerbox_trans_div" class="C_innerbox_up"></div></div><div id="trans_yiwen_outerDiv" class="C_outerbox_up" style="display: none;"><div id="trans_yiwen_content"><div id="beforeFixBox"><p id="trans_yiwen_title">译文</p><p id="trans_yiwen_easy"></p><div id="trans_yiwen_bottomdiv"><img id="trans_yiwen_bottom_img" src="chrome-extension://hlppekcioiicbfafmmgikkdkljnjpiao/images/img_logo.png" style="cursor: pointer;"><a id="trans_yiwen_bottom_a">翻译纠错<img id="trans_yiwen_bottom_a_img" src="chrome-extension://hlppekcioiicbfafmmgikkdkljnjpiao/images/IconArrowRight.png"></a></div></div><div id="afterFixBox"><p id="trans_fix_error">翻译纠错</p><div id="trans_fix_box"><textarea id="trans_fix_content"></textarea><button id="comfirmfix">确定</button></div></div></div><div id="trans_yiwen_innerDiv" class="C_innerbox_up"></div></div><div id="trans_word_outerDiv" class="C_outerbox_up" style="display: none;"><div id="trans_word_content"><div id="trans_word_head"><p id="trans_word_title"></p><p id="trans_word_easy"></p></div><div id="eachcharadiv"></div><div id="trans_word_bottomdiv"><img id="trans_word_bottom_img" src="chrome-extension://hlppekcioiicbfafmmgikkdkljnjpiao/images/img_logo.png" style="cursor: pointer;"></div></div><div id="trans_word_innerDiv" class="C_innerbox_up"></div></div><div id="trans_box" style="display: none;"><img id="trans_finish" src="chrome-extension://hlppekcioiicbfafmmgikkdkljnjpiao/images/IconFinsh.png"><translatebox id="trans_ptitle">是否将当前网页翻译成中文?</translatebox><div id="trans_spanPic" style="background: url(&quot;chrome-extension://hlppekcioiicbfafmmgikkdkljnjpiao/images/arrowdownNormal.png&quot;) center center no-repeat;"></div><ul id="trans_buttonfalselist"><li class="buttonfalselistLi thisNoTip">此网站不再提醒</li><li class="buttonfalselistLi allNoTip">所有网站不再提醒</li></ul><div id="trans_buttonfalse">关闭</div><button id="trans_buttonCompare">中英对照</button><button id="trans_buttontrue">翻译网页</button></div><div id="transAutoBox" style="display: none;"><translatebox id="transAutoBox_ptitle">自动翻译已开启</translatebox><div id="transAutoBox_cancle">去设置</div><div id="transAutoBox_close" style="background: url(&quot;chrome-extension://hlppekcioiicbfafmmgikkdkljnjpiao/images/BtnClose2Normal.png&quot;) center center no-repeat;"></div></div><div id="compareOuter" style="position: absolute; height: 634px; left: -808px; display: block;"><div id="compareInner"><h1 id="titleCompareUp"></h1><h1 id="titleCompareDown"></h1><div id="innerLeft"></div><div id="innerRight"></div></div><div id="compareLoading"><img id="comparing" src="chrome-extension://hlppekcioiicbfafmmgikkdkljnjpiao/images/loading.gif">正在翻译...</div><div id="compareFail"><img id="compareFailImg" src="chrome-extension://hlppekcioiicbfafmmgikkdkljnjpiao/images/ImgError.png"><h1 id="transFail">翻译失败</h1><p id="transP">未能获得中英文对照翻译结果</p><div id="buttonBottom"><button id="againButton">重试</button><button id="returnButton">返回</button></div></div><div id="closeCompare"><a id="feedBackTrans" target="_blank" href="http://bbs.browser.qq.com/thread-241037-1-1.html">我要反馈</a><img id="closeImg" src="chrome-extension://hlppekcioiicbfafmmgikkdkljnjpiao/images/timg.png"></div><div id="whiteDiv"></div></div></html>
"""
# print(re.findall(r'src=".*?[^<> ]\.png',text))
r = re.findall(r'>(\b.*?)<',text)
print(r)
# r'<div[^>]*>(?:.(?!<div[^>]*>))*?</div>'
