// 一旦、リロードやページ遷移時にスクロール位置を復元するためにjQueryを使用する
// 後々、各サーバーとのやりとりはをAjax通信に切り替え削除したい
$(window).scroll(function() {
    sessionStorage.scrollTop = $(this).scrollTop();
});

$(document).ready(function() {
    if (sessionStorage.scrollTop != "undefined") {
        $(window).scrollTop(sessionStorage.scrollTop);
    }
});


//////////////////// index.html
// 画像のプレビューイメージ
function previewImage(obj) {
    var fileReader = new FileReader();
    fileReader.onload = (function() {
        document.getElementById('preview').src = fileReader.result;
    });
    fileReader.readAsDataURL(obj.files[0]);
}
//////////////////// /index.html


//////////////////// my_diary.html
// 音声合成
// 現状、最後まで聞いた場合再度再生するために2回押さないといけない
let switchOver = 0;
function textToSpeech(count) {
    if (!speechSynthesis.speaking) {
        switchOver = 0;
    }
    switch (switchOver) {
        case 0:
            switchOver = 1;
            let id = 'card-text' + count;
            let word = document.getElementById(id).innerHTML;
            let u = new SpeechSynthesisUtterance();
            u.lang = 'en-US';
            u.text = word;
            speechSynthesis.speak(u);
            break;
        case 1:
            switchOver = 0;
            speechSynthesis.cancel();
            break;
    }
}
//////////////////// /my_diary.html