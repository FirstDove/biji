/**
 * 作者：刘德福
 * 时间：2017/11/16 15:46
 */

let xmlt;
function myAjax(method,url,params,async,type,callback){
    xmlt = new XMLHttpRequest() || new ActiveXObject("Microsoft.XMLHTTP");
    xmlt.onreadystatechange = function (){
        if(xmlt.readyState == 4 && xmlt.status == 200) {
            callback();
        }
    };
    if(method=="get"){
        xmlt.open(method,url+"?"+params,async);
        xmlt.send();
    }else if(method=="post") {
        if (type != "false") {
            xmlt.open(method, url, async);
            xmlt.setRequestHeader("content-Type", "application/" + type + ";charset=utf-8");
            xmlt.send(params);
        } else {
            xmlt.open(method, url, async);
            xmlt.send(params);
        }
    }
}


let imgFirstSrc;
$(document).ready(function () {
    imgFirstSrc = $(".ImgFirstSrc").attr("src");
    selectConfirm();
});
function serverAdd(){
//    1.获取所有需要提交的数据
//    2.跳转回显示页面
    let svForm = document.svDetalForm;
    let formData = new FormData(svForm);
    myAjax("post","/uplDetalFile.do",formData,true,"false",callbackOne);
}
function cancelSv() {
    location.href = "/selectServerDetal.do";
}

function upServer() {
    let svForm = document.svDetalForm;
    let formData = new FormData(svForm);
    let ImgSrcTwo = $(".ImgFirstSrc").attr("src");
    if(ImgSrcTwo == imgFirstSrc){
        svData.sd_img = imgFirstSrc;
        svData.detalImgChange = 1;//不从data获取值的标识
    }
    myAjax("post","/uplDetalFile.do",formData,true,"false",callbackOne);
}



function previewImg(fileInput,imgDiv){
    if(window.FileReader){//支持FileReader的时候
        var reader = new FileReader();
        reader.readAsDataURL(fileInput.files[0]);
        reader.onload=function(evt){
            // imgDiv.innerHTML="<img src="+evt.target.result+" alt='未选择图片'>";
            $(".ImgFirstSrc").attr("src",evt.target.result);
        }
    }else{//兼容ie9-
        imgDiv.innerHTML='<div class="img" style="filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(sizingMethod=scale,src=\'' + fileInput.value + '\)\';"></div>';
    }
}
function selectImg(fileInputs,imgDivs){
    var checkImg=new RegExp("(.jpg$)|(.png$)|(.bmp$)|(.jpeg$)","i");
    for(var i=0;i<fileInputs.length&&i<imgDivs.length;i++){
        (function(i){//立即执行函数；保存i
            fileInputs[i].onchange=function(){
                if(checkImg.test(fileInputs[i].value)){
                    previewImg(this,imgDivs[i]);
                }else{
                    if(fileInputs[i].value==""){
                        $(".ImgPreview > img").attr("src",imgFirstSrc);
                        // alert("请选择图片！！！");
                    }else {
                        alert("只支持上传.jpg .png .bmp .jpeg;你的选择有误！！！");
                    }

                }
            };
        })(i);
    }

}
/* 为IE6 IE7 IE8增加document.getElementsByClassName函数 */
/MSIE\s*(\d+)/i.test(navigator.userAgent);
var isIE=parseInt(RegExp.$1?RegExp.$1:0);
if(isIE>0&&isIE<9){
    document.getElementsByClassName=function(cls){
        var els=this.getElementsByTagName('*');
        var ell=els.length;
        var elements=[];
        for(var n=0;n<ell;n++){
            var oCls=els[n].className||'';
            if(oCls.indexOf(cls)<0)        continue;
            oCls=oCls.split(/\s+/);
            var oCll=oCls.length;
            for(var j=0;j<oCll;j++){
                if(cls==oCls[j]){
                    elements.push(els[n]);
                    break;
                }
            }
        }
        return elements;
    }
}
var fileInputs=document.getElementsByClassName("img-btn");//文件选择按钮
var imgDivs=document.getElementsByClassName("ImgPreview");//图片容器
selectImg(fileInputs,imgDivs);