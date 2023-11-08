const navBar = $(".mobile-menu");
const menuBtn = $(".hamburger-menu");
const app = $(".app");
const html = $("html");
const body = $("body");
const deleteCartItemBtn = $(".cart .items .item .delete i");
const endPurchase = $(".end-purchase-mobile .purchase");
deleteCartItemBtn.each(createHover)

const userPanelBtn = $(".user-panel");
const userPanel = $(".user-panel-items");

userPanelBtn.click(function() {
    userPanel.toggleClass("show-panel");
});

function createHover(i, element) {
    $(element).hover(function() {
        $(element).toggleClass("bx-tada")
    })
}

app.click(function() {
    navBar.removeClass("nav-active");
    menuBtn.removeClass("toggle");
    html.removeClass("scroll-disable");
    body.removeClass("scroll-disable");
    $(".app").css("filter","none");
    userPanel.removeClass("show-panel");
});

$(document).ready(function(){
    menuBtn.click(function() {
        navBar.toggleClass("nav-active");
        menuBtn.toggleClass("toggle");
        html.toggleClass("scroll-disable");
        body.toggleClass("scroll-disable");
        endPurchase.toggleClass("end-purchase-mobile-fix");
        if ($(".app").css("filter") == "none") {
            $(".app").css("filter","blur(2px)");
        }
        else {
            $(".app").css("filter","none");
        }
    });
});

$.fn.replaceDigits = function() {
    var map =
    [
        "&\#1632;", "&\#1633;", "&\#1634;", "&\#1635;", "&\#1636;",
        "&\#1637;", "&\#1638;", "&\#1639;", "&\#1640;", "&\#1641;"
    ];
	$(this).each(function() {
        $(this).html($(this).html().replace(
            /\d(?=[^<>]*(<|$))/g,
            function($0) { return map[$0] }
        ));
	});
}

$('.price').replaceDigits();
$('.prod-price').replaceDigits();
$('.score').replaceDigits();
$('.feature').replaceDigits();
$('.loc').replaceDigits();
$('.phone').replaceDigits();
$('.date').replaceDigits();
$('.numbers input').replaceDigits();
$('.views').replaceDigits();
$('.total').replaceDigits();
$('.numbers').replaceDigits();
$('.zipcode').replaceDigits();
$('#timer').replaceDigits();

const errorlist = document.querySelectorAll(".signup li");

errorlist.forEach(replaceText);

function replaceText(elem) {
    if(elem.innerHTML == "This password is too common.") {
        elem.innerHTML = "رمز عبور سخت تری انتخاب کنید";
    }
}

$(".alert").delay(5000).fadeOut('fast');


// const togglePassword1 = document.querySelector('.eye1');
// const password1 = document.querySelector('#id_password1');

// togglePassword1.addEventListener('click', function (e) {
//     // toggle the type attribute
//     const type = password1.getAttribute('type') === 'password' ? 'text' : 'password';
//     password1.setAttribute('type', type);
//     // toggle the eye / eye slash icon
//     this.classList.toggle('bi-eye');
// });

// const togglePassword2 = document.querySelector('.eye2');
// const password2 = document.querySelector('#id_password2');

// togglePassword2.addEventListener('click', function (e) {
//     // toggle the type attribute
//     const type = password2.getAttribute('type') === 'password' ? 'text' : 'password';
//     password2.setAttribute('type', type);
//     // toggle the eye / eye slash icon
//     this.classList.toggle('bi-eye');
// });

const code = document.querySelectorAll(".trackingcode");

if (code) {

    code.forEach(item => {
        item.onclick = function() {
            document.execCommand("copy");
        }
          
        item.addEventListener("copy", function(event) {
            event.preventDefault();
            if (event.clipboardData) {
                event.clipboardData.setData("text/plain", item.textContent);
                const copiedItemID = `copied-${item.dataset['order']}`
                console.log(copiedItemID);
                document.getElementById(copiedItemID).innerHTML = 'کپی شد'
            }
        });
    })
}



month = document.querySelectorAll("span.month");

if(month !== null) {
    month.forEach((monthitem) => {
        switch (monthitem.textContent) {
            case "Farvardin":
                monthitem.textContent = "فروردین"
                break;
        
            case "Ordibehesht":
                monthitem.textContent = "اردیبهشت"
                break;
        
            case "Khordad":
                monthitem.textContent = "خرداد"
                break;
        
            case "Tir":
                monthitem.textContent = "تیر"
                break;
        
            case "Mordad":
                monthitem.textContent = "مرداد"
                break;
        
            case "Shahrivar":
                monthitem.textContent = "شهریور"
                break;
        
            case "Mehr":
                monthitem.textContent = "مهر"
                break;
        
            case "Aban":
                monthitem.textContent = "آبان"
                break;
        
            case "Azar":
                monthitem.textContent = "آذر"
                break;
        
            case "Dey":
                monthitem.textContent = "دی"
                break;
        
            case "Bahman":
                monthitem.textContent = "بهمن"
                break;
        
            case "Esfand":
                monthitem.textContent = "اسفند"
                break;
        
            default:
                break;
        }
    });   
}

const day = document.querySelectorAll("span.day");

if(day !== null) {
    day.forEach((dayitem) => {
    switch (dayitem.textContent) {
        case "Saturday":
            dayitem.textContent = "شنبه"
            break;

        case "Sunday":
            dayitem.textContent = "یکشنبه"
            break;

        case "Monday":
            dayitem.textContent = "دوشنبه"
            break;

        case "Tuesday":
            dayitem.textContent = "سه شنبه"
            break;

        case "Wednesday":
            dayitem.textContent = "چهارشنبه"
            break;

        case "Thursday":
            dayitem.textContent = "پنجشنبه"
            break;

        case "Friday":
            dayitem.textContent = "جمعه"
            break;

        default:
            break;
    }
}
)}


const one = document.getElementById("first");
const two = document.getElementById("second");
const three = document.getElementById("third");
const four = document.getElementById("fourth");
const five = document.getElementById("fifth");

const form_rate = document.querySelector(".comment-product-form .rating")
const form = document.querySelector(".comment-product-form")

const csrf = document.getElementsByName('csrfmiddlewaretoken')

const handleStarSelect = (size) => {
    const children = form_rate.children;
    for (let i = 0; i < children.length; i++) {
        if(i < size) {
            children[i].classList.remove("bx-star");
            children[i].classList.add("bxs-star");
        } else {
            children[i].classList.remove("bxs-star");
            children[i].classList.add("bx-star");
        }
    }
}

const handleSelect = (selection) => {

    switch (selection) {
        case 'first':
            handleStarSelect(1)
            return
        case 'second':
            handleStarSelect(2)
            return
        case 'third':
            handleStarSelect(3)
            return
        case 'fourth':
            handleStarSelect(4)
            return
        case 'fifth':
            handleStarSelect(5)
            return
        default:
            break;
    }
}

const getNumericValue = (stringValue) => {
    let numericValue;
    if(stringValue === "first") {
        numericValue = 1
    }
    else if(stringValue === "second") {
        numericValue = 2
    }
    else if(stringValue === "third") {
        numericValue = 3
    }
    else if(stringValue === "fourth") {
        numericValue = 4
    }
    else if(stringValue === "fifth") {
        numericValue = 5
    } 
    else {
        numericValue = 0
    }
    return numericValue;
}

const arr = [one,two,three,four,five];

if (one) {

    arr.forEach(item => item.addEventListener("mouseover",(event)=> {
        handleSelect(event.target.id)
    }));

    let val = null;

    arr.forEach(item => item.addEventListener('click', (event) => {
        val = event.target.id;
    }))
    var isSubmit = false
    const errors = $("#errors")
    form.addEventListener('submit', e => {
        const val_num = getNumericValue(val);
        const body = form.children[2].value;
        if(body.length < 5) {
            e.preventDefault()
            errors.html("فیلد دیدگاه کمتر از حد مجاز است")
            isSubmit = false
            return
        }

        if(val_num === 0) {
            e.preventDefault()
            errors.html("لطفا امتیاز خود را ثبت کنید")
            isSubmit = false
            return
        }

        if(isSubmit) {
            return
        }

        isSubmit = true
        if(isSubmit) {
            $.ajax({
                type: 'POST',
                url: window.location.pathname,
                data: {
                    'csrfmiddlewaretoken': csrf[0].value,
                    'val': val_num,
                    'body': body,
                },success : function(data) {
                    if(data['status'] == 'ok') {
                        window.location.reload()
                    }
                }
            })
        }
    })
}

const green = document.getElementById("green");
const blue = document.getElementById("blue");
const black = document.getElementById("black");
const red = document.getElementById("red");
const brown = document.getElementById("brown");
const crimson = document.getElementById("crimson");
const choosedColorBtn = document.getElementById("choosed-color");
const addToCartDesktopBtn = $("#add-to-cart-desktop");
const addToCartForm = document.getElementById("add-to-cart-form");
const greenMobile = document.getElementById("green-mobile");
const blueMobile = document.getElementById("blue-mobile");
const blackMobile = document.getElementById("black-mobile");
const redMobile = document.getElementById("red-mobile");
const brownMobile = document.getElementById("brown-mobile");
const crimsonMobile = document.getElementById("crimson-mobile");
const addToCartMobileBtn = document.getElementById("add-to-cart-mobile")
const cartAddedAlert = $("#cart-added");
const imageBlue = $("#image-blue");
const imageBlack = $("#image-black");
const imageGreen = $("#image-green");
const imageRed = $("#image-red");
const imageBrown = $("#image-brown");
const imageCrimson = $("#image-crimson");

const colorArr = [green,blue,black,red,brown,crimson]

const imageArr = [imageBlue,imageBlack,imageGreen,imageRed,imageBrown,imageCrimson]

const colorMobileArr = [greenMobile,blueMobile,blackMobile,redMobile,brownMobile,crimsonMobile]

if(addToCartForm) {

    colorArr.forEach(item => {
        if (item) {
            item.addEventListener("click", (event) => {
                $("#add-to-cart-btn").val("افزودن به سبد خرید");
                const pureColor = event.target.id;
                const choosedColor = event.target.classList[1];
                choosedColorBtn.style.display = "inline-block";
                choosedColorBtn.className = `color ${choosedColor}`
                const imageID = `#image-${pureColor}`
                imageArr.forEach(image => {
                    image.hide()
                })
                $("#present-image").hide()
                $(imageID).css("display","block")
                const controller = new AbortController();
                controller.abort()
            })
        }
    });

    colorMobileArr.forEach(item => {
        if (item) {
            item.addEventListener("click", (event) => {
                $("#add-to-cart-btn").val("افزودن به سبد خرید");
                const pureColor = event.target.id;
                const pureColorArr = pureColor.split("-")[0]
                const choosedColor = event.target.classList[1];
                choosedColorBtn.className = `color ${choosedColor}`
                const imageID = `#image-${pureColorArr}`
                imageArr.forEach(image => {
                    image.hide()
                })
                $("#present-image").hide()
                $(imageID).css("display","block")
                const controller = new AbortController();
                controller.abort()
            });
        }
    });

    addToCartForm.addEventListener("submit", add);

    function add(event) {
        event.preventDefault()
        const choosedColor = choosedColorBtn.classList[1];
        const productID = addToCartForm.children[1].dataset['product']

        if(choosedColorBtn.classList.length === 0) {
            $("#color-errors").html("اول رنگ خود را انتخاب کنید").fadeIn().delay(4000).fadeOut().css('color','red');
            $("#add-to-cart-btn").val("اول رنگ خود را انتخاب کنید");
        }
        else {
            fetch(`/cart/add-to-cart/${productID}`,{
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json; charset=UTF-8',
                    'X-CSRFToken': csrf[0].value
                  },
                body: JSON.stringify({'prod_id':productID,'choosedcolor':choosedColor})
            }).then(response => response.json())
            .then(data => {
                if(data['status'] === 'success') {
                    $("#color-errors").html("با موفقیت اضافه شد").fadeIn().delay(4000).fadeOut().css('color','#65ff6a');
                    $("#cart-added").html("اضافه شد").fadeIn().delay(4000).fadeOut().css('color','#65ff6a');
                    window.location.href = `/cart/${data['user_id']}`
                }

                if(data['status'] === 'exists') {
                    $("#color-errors").html("بیشتر از یک سفارش کیف نمی توانید داشته باشید").fadeIn().delay(4000).fadeOut().css('color','red');
                    $("#cart-added").html("بیشتر از یک سفارش کیف نمی توانید داشته باشید").fadeIn().delay(4000).fadeOut().css('color','red');
                }

                if(data['status'] === 'Active Order') {
                    $("#color-errors").html("شما یک سفارش فعال دارید. به پروفایل خود بروید و سفارش قبلی خود را لغو کنید").fadeIn().delay(4000).fadeOut().css('color','red');
                    $("#cart-added").html("شما یک سفارش فعال دارید. به پروفایل خود بروید و سفارش قبلی خود را لغو کنید").fadeIn().delay(4000).fadeOut().css('color','red');
                }

                if(data['status'] === 'NotLoggedIn') {
                    $("#color-errors").html("اول وارد حساب کاربری خود بشید").fadeIn().delay(4000).fadeOut().css('color','red');
                    $("#cart-added").html("اول وارد حساب کاربری خود بشید").fadeIn().delay(4000).fadeOut().css('color','red');
                    window.location.href = '/account/login/'
                }

                if(data['status'] === 'False Buy') {
                    $("#color-errors").html("تا اطلاع ثانوی سفارش محصول امکان پذیر نیست.").fadeIn().delay(4000).fadeOut().css('color','red');
                    $("#cart-added").html("تا اطلاع ثانوی سفارش محصول امکان پذیر نیست.").fadeIn().delay(4000).fadeOut().css('color','red');
                }

                if(data['status'] === 'Common Color') {
                    $("#color-errors").html("شما این رنگ را انتخاب کردید").fadeIn().delay(4000).fadeOut().css('color','red');
                    $("#cart-added").html("شما این رنگ را انتخاب کردید").fadeIn().delay(4000).fadeOut().css('color','red');
                }
            })
            .catch(error => console.log('Error: ', error));
        }
            
    }
}

// const cartChoosedColor = $(".cart .choosed-color");

// if (cartChoosedColor.attr("class")) {
//     const colorArr = cartChoosedColor.attr("class").split(/\s+/);
//     const pureColor = colorArr[1].split("-")[1];
//     const imageIDMobile = `#image-${pureColor}-mobile`
//     const imageID = `#image-${pureColor}`
//     $(imageID).show();
//     $(imageIDMobile).show();
// }

const contacts = document.querySelectorAll(".admin-contact-item");

if (contacts) {
    contacts.forEach(item => {
        const form = item.children[4];

        form.addEventListener("submit", function(event) {
            event.preventDefault();
            const data = new FormData(form).get('situation')
            const contactID = form.dataset['contactId']
            $(document).ready(function(){
            $.ajax({
                type: 'POST',
                url: window.location.pathname,
                data: {
                    'csrfmiddlewaretoken': csrf[0].value,
                    'situation': data,
                    'contact_id': contactID,
                },
                success: function(data) {
                    const status = data['status'];
                    const id = data['id']
                    const situation = data['situation']
                    if(status === 'ok') {
                        const itemID = `#form-status-${id}`
                        const situationID = `real-situation-${id}`
                        document.getElementById(itemID).innerHTML = "ثبت شد";
                        document.getElementById(situationID).innerHTML = situation;
                    }
                }
            })
        })
        })
    })
}

const adminComments = document.querySelectorAll(".admin .comments .comment")

if (adminComments) {
    adminComments.forEach(item => {
        const form = item.children[5];

        form.addEventListener("submit", function(event) {
            event.preventDefault();
            let data = new FormData(form).get('approved');
            const commentID = form.dataset['commentId']
            if (data == 'on') {
                data = true
            }
            else if (data == null) {
                data = false
            }
            $.ajax({
                type: 'POST',
                url: window.location.pathname,
                data: {
                    'csrfmiddlewaretoken': csrf[0].value,
                    'approved': data,
                    'comment_id': commentID,
                }, success : function(data) {
                    const itemID = `#comment-status-${commentID}`
                    if(data['status'] == 'ok') {
                        document.getElementById(itemID).innerHTML = 'ثبت شد'
                        window.location.reload()
                    }
                }
            })
        })
    })
}

function getRndInteger(min, max) {
    return Math.floor(Math.random() * (max - min + 1) ) + min;
  }

var intervalId;

function startTimer(duration, display) {
    var start = Date.now(),
        diff,
        minutes,
        seconds;
    function timer() {
        // get the number of seconds that have elapsed since 
        // startTimer() was called
        diff = duration - (((Date.now() - start) / 1000) | 0);

        // does the same job as parseInt truncates the float
        minutes = (diff / 60) | 0;
        seconds = (diff % 60) | 0;

        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;

        display.textContent = minutes + ":" + seconds; 

        if (diff <= 0) {
            clearInterval(intervalId);
            display.textContent = "2:00";
            $(".req-again-txt").hide()
            $("#send-code").show()
            $(".verify-code").hide()
        }
    };
    // we don't want to wait a full second before the timer starts
    timer();
    intervalId = setInterval(timer, 1000);
}

const sendVerifyCode = document.getElementById("send-code");

if (sendVerifyCode) {
    // sendVerifyCode.addEventListener("click", sendCode)

    // function sendCode(e) {
    //     e.preventDefault();
    //     var twoMinutes = 120,
    //     display = document.querySelector('#timer');
    //     startTimer(twoMinutes, display);
    //     const form = document.getElementById("signup-form");
    //     const phone = new FormData(form).get('username');
    //     $(".req-again-txt").show().css("display",'block');
    //     sendVerifyCode.style.display = 'none';
    //     const code = getRndInteger(1000,9999);
    //     $(".verify-code").show()
    //     $("#signup-submit").show();
    //     document.getElementById("signup-submit").disabled = false;
    //     var myHeaders = new Headers();
    //     myHeaders.append("Authorization", "AccessKey OSsoKUQD23Mmd1NmI-rS3kZjf6Au-Y27jBLSEAdG0yQ=");
    //     myHeaders.append("Content-Type", "application/json");

    //     var raw = JSON.stringify({
    //       "pattern_code": "h2i0to5kcyjrvld",
    //       "originator": "+983000505",
    //       "recipient": phone,
    //       "values": {
    //         "verify-code": `${code}`
    //       }
    //     });

    //     var requestOptions = {
    //       method: 'POST',
    //       headers: myHeaders,
    //       body: raw,
    //       redirect: 'follow'
    //     };

    //     fetch("http://rest.ippanel.com/v1/messages/patterns/send", requestOptions)
    //       .then(response => response.text())
    //       .then(result => console.log(result))
    //       .catch(error => console.log('error', error));

    sendVerifyCode.addEventListener("click", sendCode)
    function sendCode(e) {
        e.preventDefault();        

        var twoMinutes = 120,
        display = document.querySelector('#timer');
        startTimer(twoMinutes, display);
        const form = document.getElementById("signup-form");
        const phone = new FormData(form).get('username');
        $(".req-again-txt").show().css("display",'block');
        sendVerifyCode.style.display = 'none';
        const code = getRndInteger(1000,9999);
        $(".verify-code").show()
        $("#signup-submit").show();
        document.getElementById("signup-submit").disabled = false;
        $.ajax({
            type: 'POST',
            url: '/account/send-code/',
            data: {
                'csrfmiddlewaretoken': csrf[0].value,
                'phone':phone,
                'code':code
            }, success : function(data) {
                console.log(data);
            }
        })

        form.addEventListener("submit", (e) => {
            const userCode = new FormData(form).get('verifycode');
            if (parseInt(userCode) !== code) {
                e.preventDefault()
                document.getElementById("phone-note").textContent = 'کد تایید اشتباه است';
                
                return
            }
        })
    }
}