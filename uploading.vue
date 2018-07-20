<template>
    <form class="form-horizontal" name="imgUploadForm" enctype="multipart/form-data">
        <div class="ImgPreview">
            <img v-for="(item,key) in showImg" :src="item.imgSrc" @click="delImg" :class="item.className" :key="key"
                 alt="">
            <div :class="{addFrame: true,preview_hidden: imgCount >= imgTotal}">
                <div class="addImg preview_show" @click="clickFile">
                    <i>+</i>
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
                showImg: [],
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
            },
        },
        mounted() {
            let that = this;
            that.inputFile = document.createElement("input");
            that.inputFile.setAttribute('type', 'file');
            that.inputFile.setAttribute('accept', '.jpg,.png,.bmp,.jpeg');
            that.inputFile.addEventListener('change', function () {
                that.selectImg();
            });
            that.imgCount = that.count;
            that.imgTotal = that.total;
        },
        beforeDestroy() {
            let that = this;
            that.inputFile.removeEventListener('change',function () {
                that.selectImg();
            })
        },
        methods: {
            delImg() {
                let that = this;
                let imgNode = event.target;
                MessageBox.confirm('是否删除该照片？').then(action => {
                    if (action === 'confirm') {
                        let value = that.urlInfo[imgNode.className];
                        delete that.urlInfo[imgNode.className];//删除url
                        that.showImg.map(function (item, key) {
                            if (item.className === imgNode.className) {
                                that.showImg.splice(key, 1);
                                that.$emit("delImg",value);
                            }
                        });
                        that.imgCount--;
                    }
                }).catch(function () {
                });
            },
            // 选择上传的图片
            selectImg() {//文件选择按钮，图片预览框
                let checkImg = new RegExp("(.jpg$)|(.png$)|(.bmp$)|(.jpeg$)", "ig");
                let inputFile = this.inputFile;
                let imgSize = parseInt((inputFile.files[0].size) / 1024 / 1024);
                if (checkImg.test(inputFile.value) && (this.imgCount < this.imgTotal)) {
                    if (imgSize >= this.imgSize) {
                        return MessageBox({
                            title: '提示',
                            message: `请选择${this.imgSize}M以下大小的图片^_^`
                        });
                    }
                    this.previewImg(this.inputFile);//预览图片
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
            previewImg(fileInput) {
                let that = this;
                let file = fileInput.files[0];
                let reader = new FileReader();
                let date = Date.now();
                reader.onload = function (evt) {
                    let imgInfo = {
                        className: 'preImg_' + date,
                        imgSrc: evt.target.result
                    };
                    that.showImg.push(imgInfo);
                    that.imgCount++;
                };
                that.imgUrlKey = 'preImg_' + date;
                // Read in the image file as a data URL.
                reader.readAsDataURL(file);
            },
            // 触发 input 文件事件
            clickFile() {
                event.stopPropagation();
                this.inputFile.click();
            },
            // 上传选择的图片
            uploadImg() {
                let file = this.inputFile.files[0];
                let formData = new FormData();
                formData.append(file.name, file);
                let that = this;
                Indicator.open({
                    text: "uploading...",
                    spinnerType: 'fading-circle'
                });
                console.log(that.urlInfo);
                that.axios({
                    method: "post",
                    url: '/v1/upload/images',
                    header: {'content-Type': 'multipart/form-data'},
                    data: formData
                }).then((res) => {
                    let data = res.data.data.pics;
                    console.log(data[0]);
                    that.urlInfo[that.imgUrlKey] = data[0];
                    that.$emit("returnurl", Object.values(that.urlInfo));
                    // if (Object.values(that.urlInfo).length >= that.imgTotal) {
                    //     that.$emit("returnurl", Object.values(that.urlInfo));
                    // }
                    Indicator.close();
                    that.inputFile[0].value = "";//清空input file 的value
                }).catch((err) => {})
            },
        }
    }
</script>

<style scoped lang="scss">
    .ImgPreview {
        width: 100%;
        display: flex;
        flex-flow: row wrap;
        align-items: center;
        justify-content: flex-start;
        align-content: center;
        img {
            float:left;
            height: 80px;
            max-width: 200px;
            margin:2px 5px 2px 0;
            border: 1px solid gray;
        }
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
        }
    }
</style>
