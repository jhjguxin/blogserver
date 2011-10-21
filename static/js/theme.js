
var Init = {
 
       //样式表文件目录路径
baseSkinUrl : "/static/css/",
 
//样式表文件名称列表
styles : ["compiled", "timeless", "paperlike"],
 
//样式cookie的key值
cookieKey : "blog_random_css",
 
//定义方法，获取min至max间的随机数，包含min及max
getRandomNum : function(min, max){
return min + Math.floor(Math.random() * (max - min + 1)); 
},

//定义方法，获取cookie值
getCookie : function(name) {
var arr = document.cookie.match(new RegExp("(^| )" + name + "=([^;]*)(;|$)"));
if (arr != null) {
return unescape(arr[2]);
}
return null;
},
 
//定义方法，设置cookie值
setCookie : function(sName,sValue,objHours,sPath,sDomain,bSecure){
var sCookie = sName + "=" + encodeURIComponent(sValue);
if (objHours) {
var date = new Date();
var ms = objHours * 3600 * 1000;
date.setTime(date.getTime() + ms);
sCookie += ";expires=" + date.toGMTString();
}
if (sPath) {
sCookie += ";path=" + sPath;
}
if (sDomain) {
sCookie += ";domain=" + sDomain;
}
if (bSecure) {
sCookie += ";secure";
}
document.cookie=sCookie;
},
 
        //定义方法，通过获取随机数随机加载CSS
loadCSS : function(){
var length = this.styles.length,
     random = this.getRandomNum(0, length-1),
     cookieStyle = this.getCookie(this.cookieKey),
     currentStyle = "timeless";
 
//如果当前随机取到的样式与cookie中样式相同，则重新计算随机数
                while(this.styles[random] == cookieStyle)
{
random = this.getRandomNum(0, length-1)
}
 
currentStyle = this.styles[random];
 
//将新样式存入cookie，cookie有效时间为24小时
                this.setCookie(this.cookieKey, currentStyle, 24, "/", "websbook.com", false);
 
//若样式名称不为"timeless"默认样式，则向<head />标签中写入定制样式
                if(currentStyle != "timeless")
{
document.write('<link rel="stylesheet" type="text/css" href="' + this.baseSkinUrl + this.styles[random] + '.css" />');
}
                else
{
document.write('<link rel="stylesheet" type="text/css" href="' + this.baseSkinUrl + 'timeless.css" />');
}
}
}
 
Init.loadCSS(); 


