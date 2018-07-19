<template>
    <div class="auth-upgrade">
        <m-header title="竞技娱乐选手认证平台"></m-header>
        <div v-on:click="handleChooseType">
            <mt-cell title="认证类型" is-link :value="authTypes[authType]"></mt-cell>
        </div>
        <mt-actionsheet closeOnClickModal="false" cancelText="" :actions="actions" v-model="sheetVisible">
        </mt-actionsheet>
        <mt-field label="认证平台" placeholder="请填写你获得成绩的平台" v-model="platform"></mt-field>
        <mt-field label="比赛成绩" placeholder="请填写你的比赛成绩" v-model="desc"></mt-field>
        <!--上传图片-->
        <div class="uploadImgFrame">
            <UploadImg :total="3" :count="0" @returnurl="reqUrl"></UploadImg>
        </div>
        <mt-button type="default" v-on:click="handleSubmit" class="submit">立即认证</mt-button>
    </div>
</template>

<script>
    import {
        MessageBox, Indicator
    } from "mint-ui";
    import UploadImg from '../../components/uploadimg.vue';

    export default {
        name: "auth-upgrade",
        data() {
            return {
                platform: '',
                desc: '',
                sheetVisible: false,
                authType: 1,
                authTypes: {
                    '1': '电子竞技',
                    '2': '网络游戏',
                    '3': '网络直播',
                    '4': '棋牌竞技',
                    '5': '其他',
                },
                actions: [
                    {
                        name: '电子竞技',
                        method: () => {
                            this.authType = 1
                        }
                    },
                    {
                        name: '网络游戏',
                        method: () => {
                            this.authType = 2
                        },
                    },
                    {
                        name: '网络直播',
                        method: () => {
                            this.authType = 3
                        }
                    },
                    {
                        name: '棋牌竞技',
                        method: () => {
                            this.authType = 4
                        }
                    },
                    {
                        name: '其他',
                        method: () => {
                            this.authType = 5
                        }
                    },
                ],
                urlArr: [],//上传图片路径集合
            };
        },
        components: {
            UploadImg
        },
        computed: {},
        methods: {
            handleSubmit: function () {
                var _ = this;
                if (!_.platform || !_.desc || !_.authType) {
                    return MessageBox("错误", '请输入完整信息！');
                }
                let pics = _.urlArr;
                _.axios({
                    method: 'POST',
                    url: '/v1/certificate',
                    data: {
                        certificate_type: _.authType,
                        certificate_plat: _.platform,
                        certificate_desc: _.desc,
                        pics: pics
                    }
                }).then(res => {
                    if (res.data.error_code == 0) {
                        MessageBox.alert('提交成功！').then(action => {
                            this.$router.push('/auth/level')
                        });
                    } else {
                        MessageBox("错误", _.ERROR_CODE(res.data.error_code));
                    }
                })
            },
            handleChooseType: function () {
                console.log(this.sheetVisible)
                this.sheetVisible = true;
            },
            reqUrl(urlArr){
                console.log(urlArr);
                this.urlArr = urlArr;
            }
        }
    };
</script>

<style lang="scss" scoped>
    .upload {
    }

    .submit {
        margin: auto;
        display: block;
        margin-top: 50px;
    }

    a {
        color: #42b983;
    }

   .uploadImgFrame {
       width: 70%;
       margin-left: 30%;
   }
</style>
