var register = new Vue({
    el: '#register_form',
    data: {
        name: "",
        password: "",
        check_password: "",
        error_check_password: false,
        error_name: false,
        error_password: false
    },
    methods: {
        registersubmitForm: function() {
            if (!this.error_name && !this.error_password && !this.error_check_password && this.name.length && this.password.length && this.check_password) {
                var form = document.getElementById("register_form");
                form.submit();
            } else {
                alert('注册有误，请检查！');
                return
            }
        }
    },
    watch: {
        name: function() {
            var registername = $('span[name="errorregistername"]');
            if (this.name.length < 4) {
                this.error_name = true;
                registername.text('用户名长度必须大于四个字符！')
            } else {
                this.error_name = false;
                registername.text('');
            }
        },
        password: function() {
            if (this.password.length < 8 || this.password.length > 16) {
                this.error_password = true
            } else {
                this.error_password = false
            }
        },
        check_password: function() {
            if (this.password != this.check_password) {
                this.error_check_password = true
            } else {
                this.error_check_password = false
            }
        }
    }

})

var login = new Vue({
    el: '#login_form',
    data: {
        name: "",
        password: "",
        error_name: false,
        error_password: false
    },
    methods: {
        loginsubmitForm: function() {
            if (!this.error_name && !this.error_password && this.name.length && this.password.length) {
                var form = document.getElementById("login_form");
                form.submit();
            } else {
                alert('登陆有误，请检查！');
                return
            }
        }
    },
    watch: {
        name: function() {
            var loginname = $('span[name="errorloginname"]');
            if (this.name.length < 4) {
                this.error_name = true;
                loginname.text('用户名长度必须大于四个字符！')
            } else {
                this.error_name = false;
                loginname.text('');
            }
        },
        password: function() {
            if (this.password.length < 8 || this.password.length > 16) {
                this.error_password = true
            } else {
                this.error_password = false
            }
        }
    }

})