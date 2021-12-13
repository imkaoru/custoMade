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
// 現状、最後まで発音し切った時に自動的にアイコンを切り替える処理がうまくいかなかったため、そこは後回し
let switchOverS = 0;
function textToSpeech(count) {
    if (!speechSynthesis.speaking) {
        switchOverS = 0;
    }
    switch (switchOverS) {
        case 0:
            switchOverS = 1;
            let id = 'card-text' + count;
            let word = document.getElementById(id).innerHTML;
            let u = new SpeechSynthesisUtterance();
            u.lang = 'en-US';
            u.text = word;
            speechSynthesis.speak(u);
            break;
        case 1:
            switchOverS = 0;
            speechSynthesis.cancel();
            break;
    }
}

// モーダルウィンドウ
$(".speechToText").modaal({
	overlay_close:true, //モーダル背景クリック時に閉じるか
	before_open:function(){ //モーダルが開く前に行う動作
		$('html').css('overflow-y','hidden'); /*縦スクロールバーを出さない*/
	},
	after_close:function(){ //モーダルが閉じた後に行う動作
		$('html').css('overflow-y','scroll'); /*縦スクロールバーを出す*/
	}
});

// 音声認識
SpeechRecognition = webkitSpeechRecognition || SpeechRecognition;
let recognition = new SpeechRecognition();

recognition.lang = 'en-US';
recognition.interimResults = true;
recognition.continuous = true;

recognition.onresult = (event) => {
    let btnId = 'recording-btn' + modaalNum;
    let recordingBtn = document.getElementById(btnId);

    let resultId = 'result-div' + modaalNum;
    let resultDiv = document.getElementById(resultId);
    let preResult = resultDiv.firstElementChild;

    let finalTranscript = ''; // 確定した認識結果
    let interimTranscript = ''; // 暫定の認識結果
    for (let i = event.resultIndex; i < event.results.length; i++) {
        let transcript = event.results[i][0].transcript;

        let p = document.createElement("p");
        // resultDiv.appendChild(p);
        resultDiv.firstElementChild.after(p);

        if (event.results[i].isFinal) {
            finalTranscript = transcript;
            preResult.innerHTML = finalTranscript;
            p.innerText = finalTranscript;
        } else {
            interimTranscript = transcript;
            preResult.innerHTML = '<p class="standby">' + interimTranscript + '</p>';
        }
    }

    recognition.onaudioend = () => {
        switchOverR = 0;
        recordingBtn.innerHTML = '<i class="fas fa-microphone fa-2x"></i>';
        resultDiv.innerHTML = '<p class="standby">Speak into the microphone. (English)</p>';
    }
}

let modaalNum = 0;
let switchOverR = 0;

function speechToText(count) {
    modaalNum = count;
    let id = 'recording-btn' + modaalNum;
    let recordingBtn = document.getElementById(id);

    switch (switchOverR) {
        // recordingBtn.classList.add("foo");
        case 0:
            switchOverR = 1;
            recordingBtn.innerHTML = '<i class="far fa-stop-circle fa-2x"></i>';
            recognition.start();
            break;
        case 1:
            switchOverR = 0;
            recordingBtn.innerHTML = '<i class="fas fa-microphone fa-2x"></i>';
            recognition.stop();
            break;
    }
}

// アコーディオンエリア
// 必要に応じて、アコーディオン開いた時にその他全てのアコーディオンを閉じる処理を追加する
$('.accordion-btn').on('click', function() {
	// $('.accordion-box').slideUp(500);　//クラス名.accordion-boxがついたすべてのアコーディオンを閉じる

	let box = $(this).next(".accordion-box");
	$(box).slideToggle(); //アコーディオンの上下動作

    if ($(this).hasClass('close')) {
		$(this).removeClass('close');
        $(this).html( '<i class="fas fa-plus fa-2x"></i>' );
	} else {
		$(this).addClass('close');
        $(this).html( '<i class="fas fa-times fa-2x"></i>' );
	}
});
//////////////////// /my_diary.html