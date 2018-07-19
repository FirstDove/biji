<template>
    <form class="form-horizontal" name="imgUploadForm" enctype="multipart/form-data">
        <div class="ImgPreview">
            <!--<img class="preImg" src="" @click="clickFile">-->
            <div :class="{addFrame: true,preview_hidden: imgCount >= imgTotal}">
                <div class="addImg preview_show" @click="clickFile">
                    <i>+</i>
                    <input type="file" class="img-btn" accept=".jpg,.png,.bmp,.jpeg"
                           @change="selectImg(previewDiv)" name="sdImg"/>
                </div>
            </div>
        </div>
    </form>
</template>

<script>
    import {
        MessageBox, Indicator
    } from "mint-ui";

    export default {
        name: "uploadimg",
        data() {
            return {
                inputFile: '',//file  input
                previewDiv: '', //预览图片框
                addFrame: '',//添加图片按钮
                urlInfo: {},//上传图片所返回的路径信息
                // inputFileValue: [],//上传图片的路径 去重
                imgCount: 0,
                imgTotal: 0,
            }
        },
        props: {
            total: { //上传图片的限制数量
                required: false,
                default: 1,
                type: Number
            },
            count: { //上传图片的当前数量
                required: false,
                default: 0,
                type: Number
            },
            imgSize: {
                required: false,
                default: 2,
                type: Number, //单位为 M
            }
        },
        mounted() {
            let that = this;
            that.inputFile = document.getElementsByClassName("img-btn");
            that.previewDiv = document.getElementsByClassName('ImgPreview');
            that.addFrame = document.getElementsByClassName('addFrame');
            that.imgCount = that.count;
            that.imgTotal = that.total;

            //事件委托
            that.previewDiv[0].addEventListener("click", function () {
                let imgNode = event.target;
                if (imgNode.nodeName.toLowerCase() === 'img') {
                    MessageBox.confirm('是否删除该照片？').then(action => {
                        if (action === 'confirm') {
                            delete that.urlInfo[imgNode.className];//删除url
                            imgNode.remove();
                            that.imgCount--;
                        }
                    }).catch(function () {
                    });
                }
            })
        },
        methods: {
            // 选择上传的图片
            selectImg(imgDivs) {//文件选择按钮，图片预览框
                let checkImg = new RegExp("(.jpg$)|(.png$)|(.bmp$)|(.jpeg$)", "ig");
                let inputFile = this.inputFile[0];
                let imgSize = parseInt((inputFile.files[0].size) / 1024 / 1024);
                // for (let i = 0;i < this.inputFileValue.length;i++) {
                //     if (value === this.inputFileValue[i]) {
                //         return MessageBox({
                //             title: '提示',
                //             message: '图片不可重复上传！'
                //         });
                //     }
                // }
                // this.inputFileValue.push(value);
                if (checkImg.test(inputFile.value) && (this.imgCount < this.imgTotal)) {
                    if (imgSize >= this.imgSize ) {
                        return MessageBox({
                            title: '提示',
                            message: `请选择${this.imgSize}M以下大小的图片^_^`
                        });
                    }
                    this.previewImg(inputFile, imgDivs[0]);//预览图片
                    this.uploadImg(); //上传图片
                    checkImg.lastIndex = 0;
                } else {
                    if (this.inputFile[0].value != "" && (this.imgCount < this.imgTotal)) {
                        return MessageBox({
                            title: '提示',
                            message: `只支持上传.jpg .png .bmp .jpeg;你的选择有误！！！`
                        });
                    }
                }
            },
            // 预览图片功能
            previewImg(fileInput, imgDiv) {
                let that = this;
                let file = fileInput.files[0];
                let reader = new FileReader();
                let date = Date.now();
                reader.onload = function (evt) {
                    let imgNode = document.createElement('img');
                    imgNode.setAttribute("src", evt.target.result);
                    imgNode.setAttribute("style", 'float:left;height: 80px;margin:2px 5px 2px 0;border: 1px solid gray;');
                    imgNode.setAttribute("class", 'preImg_' + date);
                    imgDiv.insertBefore(imgNode, that.addFrame[0]);
                    that.imgCount++;
                };
                that.imgUrlKey = 'preImg_' + date;
                // Read in the image file as a data URL.
                reader.readAsDataURL(file);
            },
            // 触发 input 文件事件
            clickFile() {
                event.stopPropagation();
                document.getElementsByClassName("img-btn")[0].click();
            },
            // 上传选择的图片
            uploadImg() {
                let form = document.imgUploadForm;
                let formData = new FormData(form);
                let that = this;
                Indicator.open({
                    text: "uploading...",
                    spinnerType: 'fading-circle'
                });
                that.axios({
                    method: "post",
                    url: '/v1/upload/images',
                    data: formData
                }).then((res) => {
                    // console.log(res);
                    let data = res.data.data;
                    that.urlInfo[that.imgUrlKey] = data[0];
                    if (Object.values(that.urlInfo).length >= that.imgTotal) {
                        that.$emit("returnurl",Object.values(that.urlInfo));
                    }
                    Indicator.close();
                    that.inputFile[0].value = "";//清空input file 的value
                }).catch((err) => {
                    console.log(err);
                })
            },
        }
    }
</script>

<style scoped lang="scss">
    .ImgPreview {
        width: 70%;
        margin-left: 30%;
        display: flex;
        flex-flow: row wrap;
        align-items: center;
        justify-content: flex-start;
        align-content: center;
    }

    .preview_hidden {
        display: none;
    }

    .preview_show {
        display: inline-block;
    }

    .addFrame {
        .addImg {
            width: 50px;
            height: 50px;
            border: 1px dotted gray;
            position: relative;
            display: flex;
            flex-flow: row nowrap;
            align-items: center;
            justify-content: center;
            border-radius: 4px;
            i {
                font-style: normal;
                font-size: 36px;
                font-weight: lighter;
                color: #828282;
            }
            .img-btn {
                display: none;
            }
        }
    }
</style>
