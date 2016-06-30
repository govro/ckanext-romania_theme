! function() {
    if (!window.hasCookieConsent) {
        window.hasCookieConsent = !0;
        var e = "cookieconsent_options",
            t = "cookieconsent_dismissed",
            n = "//cdnjs.cloudflare.com/ajax/libs/cookieconsent2/1.0.9/";
        if (!(document.cookie.indexOf(t) > -1)) {
            "function" != typeof String.prototype.trim && (String.prototype.trim = function() {
                return this.replace(/^\s+|\s+$/g, "")
            });
            var i, o = {
                    isArray: function(e) {
                        var t = Object.prototype.toString.call(e);
                        return "[object Array]" == t
                    },
                    isObject: function(e) {
                        return "[object Object]" == Object.prototype.toString.call(e)
                    },
                    each: function(e, t, n, i) {
                        if (o.isObject(e) && !i)
                            for (var r in e) e.hasOwnProperty(r) && t.call(n, e[r], r, e);
                        else
                            for (var s = 0, c = e.length; c > s; s++) t.call(n, e[s], s, e)
                    },
                    merge: function(e, t) {
                        e && o.each(t, function(t, n) {
                            o.isObject(t) && o.isObject(e[n]) ? o.merge(e[n], t) : e[n] = t
                        })
                    },
                    bind: function(e, t) {
                        return function() {
                            return e.apply(t, arguments)
                        }
                    },
                    queryObject: function(e, t) {
                        var n, i = 0,
                            o = e;
                        for (t = t.split(".");
                            (n = t[i++]) && o.hasOwnProperty(n) && (o = o[n]);)
                            if (i === t.length) return o;
                        return null
                    },
                    setCookie: function(e, t, n) {
                        var i = new Date;
                        n = n || 365, i.setDate(i.getDate() + n), document.cookie = e + "=" + t + "; expires=" + i.toUTCString() + "; path=/"
                    },
                    addEventListener: function(e, t, n) {
                        e.addEventListener ? e.addEventListener(t, n) : e.attachEvent("on" + t, n)
                    }
                },
                r = function() {
                    var e = "data-cc-event",
                        t = "data-cc-if",
                        n = function(e, t, i) {
                            return o.isArray(t) ? o.each(t, function(t) {
                                n(e, t, i)
                            }) : void(e.addEventListener ? e.addEventListener(t, i) : e.attachEvent("on" + t, i))
                        },
                        i = function(e, t) {
                            return e.replace(/\{\{(.*?)\}\}/g, function(e, n) {
                                for (var i, r = n.split("||"); token = r.shift();) {
                                    if (token = token.trim(), '"' === token[0]) return token.slice(1, token.length - 1);
                                    if (i = o.queryObject(t, token)) return i
                                }
                                return ""
                            })
                        },
                        r = function(e) {
                            var t = document.createElement("div");
                            return t.innerHTML = e, t.children[0]
                        },
                        s = function(e, t, n) {
                            var i = e.parentNode.querySelectorAll("[" + t + "]");
                            o.each(i, function(e) {
                                var i = e.getAttribute(t);
                                n(e, i)
                            }, window, !0)
                        },
                        c = function(t, i) {
                            s(t, e, function(e, t) {
                                var r = t.split(":"),
                                    s = o.queryObject(i, r[1]);
                                n(e, r[0], o.bind(s, i))
                            })
                        },
                        a = function(e, n) {
                            s(e, t, function(e, t) {
                                var i = o.queryObject(n, t);
                                i || e.parentNode.removeChild(e)
                            })
                        };
                    return {
                        build: function(e, t) {
                            o.isArray(e) && (e = e.join("")), e = i(e, t);
                            var n = r(e);
                            return c(n, t), a(n, t), n
                        }
                    }
                }(),
                s = {
                    options: {
                        message: "This website uses cookies to ensure you get the best experience on our website. ",
                        dismiss: "Got it!",
                        learnMore: " Detalii",
                        link: "http://gov.ro/ro/conditii-de-utilizare",
                        container: null,
                        theme: "light-floating"
                    },
                    init: function() {
                        var t = window[e];
                        t && this.setOptions(t), this.setContainer(), this.options.theme ? this.loadTheme(this.render) : this.render()
                    },
                    setOptions: function(e) {
                        o.merge(this.options, e)
                    },
                    setContainer: function() {
                        this.container = this.options.container ? document.querySelector(this.options.container) : document.body, this.containerClasses = "", navigator.appVersion.indexOf("MSIE 8") > -1 && (this.containerClasses += " cc_ie8")
                    },
                    loadTheme: function(e) {
                        var t = this.options.theme; - 1 === t.indexOf(".css") && (t = n + t + ".css");
                        var i = document.createElement("link");
                        i.rel = "stylesheet", i.type = "text/css", i.href = t;
                        var r = !1;
                        i.onload = o.bind(function() {
                            !r && e && (e.call(this), r = !0)
                        }, this), document.getElementsByTagName("head")[0].appendChild(i)
                    },
                    markup: ['<div class="cc_banner-wrapper {{containerClasses}}">', '<div class="cc_banner cc_container cc_container--open">', '<a href="#null" data-cc-event="click:dismiss" class="cc_btn cc_btn_accept_all">{{options.dismiss}}</a>', '<p class="cc_message">{{options.message}} <a data-cc-if="options.link" class="cc_more_info" href="{{options.link || "#null"}}">{{options.learnMore}}</a></p>', '<a class="cc_logo" target="_blank" href="http://silktide.com/cookieconsent">Cookie Consent plugin for the EU cookie law</a>', "</div>", "</div>"],
                    render: function() {
                        this.element = r.build(this.markup, this), this.container.firstChild ? this.container.insertBefore(this.element, this.container.firstChild) : this.container.appendChild(this.element)
                    },
                    dismiss: function() {
                        this.setDismissedCookie(), this.container.removeChild(this.element)
                    },
                    setDismissedCookie: function() {
                        o.setCookie(t, "yes")
                    }
                },
                c = !1;
            (i = function() {
                c || "complete" != document.readyState || (s.init(), initalized = !0)
            })(), o.addEventListener(document, "readystatechange", i)
        }
    }
}();
