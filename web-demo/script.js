// 블록을 클릭했을 때 팝업창을 띄우는 함수
function showPopup(blockId, blockText) {
    const popupContent = document.querySelector('#popup-content');
    popupContent.innerHTML = blockText;

    const popup = document.querySelector('#popup');
    popup.style.display = 'block';

    const popupClose = document.querySelector('#popup-close');
    popupClose.addEventListener('click', function () {
        popup.style.display = 'none';
    });
}

// 각 블록을 클릭했을 때 팝업창을 띄우는 이벤트 핸들러 등록
for (let i = 1; i <= 9; i++) {
    const block = document.querySelector(`#block-${i}`);
    const blockText = '{"Index": 1, "Timestamp": 1684087378.6354618, "Data": {"Name": "Daniel", "Service": "Naver"}, "Previous Hash": "a84d25bff8f4f42c817328813b2511c11775a10e8f99d342f28da79a33986c96", "Hash": "35216b9b88a0fb76d5e2fab2e7d65fc6729ca41feea685f08f58e72273f5b878"}';

    block.addEventListener('click', function () {
        showPopup(`block-${i}`, blockText);
    });

}

