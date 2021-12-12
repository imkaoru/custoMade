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