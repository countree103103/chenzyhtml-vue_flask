var lyb = new Vue({
    delimiters: ['~{', '}~'],
    el: '#message',
    data: {
        lyb: [],
        message: "",
        name: "",
        error_name: false,
        error_message: false
    },
    computed: {
        name_length: function() {
            return this.name.length;
        }
    },
    methods: {
        submitForm: function() {
            if (!this.error_message && !this.error_name && this.message.length && this.name.length) {
                var form = document.getElementById('lyb');
                form.submit()
                alert("提交成功！")
            } else {
                alert('提交有误！')
                return
            }
        },
    },
    created() {

    },
    mounted() {
        var self = this;
        axios.get("ajax/lyb").then(function(responese) {
            self.lyb = responese.data;
        }).catch(function(error) {
            console.log(error)
        });
    },
    watch: {
        lyb: function() {
            this.$nextTick(function() {
                $(document).ready(function() {
                    $("#message div p").each(function() {
                        var str = $(this).html();
                        var subStr = str.substring(0, 50);
                        var leftStr = str.substring(50);
                        $(this).html(subStr + (str.length > 50 ? "<a href='javascript:void(0)' class='active'>...查看更多</a>" + "<p style='display:none'>" + leftStr + "</p>" : ''));
                    });

                    $('#message div p a').click(function() {
                        $(this).next().css({
                            'display': "inline",
                            "word-wrap": "break-word",
                            "word-break": "break-all"
                        });
                        $(this).remove();
                    })
                });
                aos();
            })
        },
        name: function() {
            if (this.name.length > 2) {
                this.error_name = false;
            } else {
                this.error_name = true;
            }
        },
        message: function() {
            if (this.message.length <= 0) {
                this.error_message = true;
            } else {
                this.error_message = false;
            }
        }
    }
})

var oynn = new Vue({
    delimiters: ['~{', '}~'],
    el: '#oynn',
    data: {
        imgurl: "img/oynn/",
        oynnn: []
    },
    methods: {
        swiper: function() {
            var mySwiper = new Swiper('.swiper-container', {
                autoplay: true,
                navigation: {
                    nextEl: '.swiper-button-next',
                    prevEl: '.swiper-button-prev',
                },
                scrollbar: {
                    el: '.swiper-scrollbar',
                },
                effect: 'coverflow',
                loop: true,
            })
        }
    },
    created: function() {

    },
    mounted() {
        var self = this;
        axios.get('ajax/oynn').then(function(res) {
            oynn.oynnn = res.data;
        }).catch(function(error) {
            console.log(error)
        });
    },
    watch: {
        oynnn: function() {
            this.$nextTick(function() {
                this.swiper();
                aos();
            });
        }
    }
});

function aos() {
    AOS.init({
        offset: 200,
        duration: 600,
        easing: 'ease-in-sine',
        delay: 100,
        once: true
    });
}