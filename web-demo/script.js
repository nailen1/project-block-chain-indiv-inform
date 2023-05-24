const blocks = document.querySelectorAll('.block');

function generateRandomHash() {
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    let hash = '';
    for (let i = 0; i < 12; i++) {
        hash += characters.charAt(Math.floor(Math.random() * characters.length));
    }
    return hash;
}

blocks.forEach((block) => {
    const hash = generateRandomHash();
    block.textContent = `${hash}... `;
});

const blockBox = document.querySelectorAll('.block-box');
const overlay = document.querySelector('.overlay');
const popup = document.querySelector('.popup');
const closeBtn = document.querySelector('.close-btn');
const deleteBtn = document.querySelector('.delete-btn');

blockBox.forEach((block) => {
    block.addEventListener('click', () => {
        overlay.style.display = 'block';
        popup.style.display = 'block';
    });
});

closeBtn.addEventListener('click', () => {
    overlay.style.display = 'none';
    popup.style.display = 'none';
    const blockInfo = `
          Transaction ID: 0xabc123<br>
          Timestamp: 2023-05-12 10:30:15<br>
          Block Number: 1234<br>
          Previous Hash: 0x789def<br>
          Hash: 0x123abc<br><br>
          Transaction Details:<br>
          Data: ShinhanCard requested access to Daniel's personal information.<br>
          Date: 2023-05-11<br>
          Time: 10:30:00<br>
          Transaction Fee: 0.001 ETH<br>
          Payment Address: 0x456def<br><br>
          ### 암호화되어 전송된 개인정보 ###<br>
          Personal Information:<br>
          Name: Daniel<br>
          Birthdate: 1900-01-01<br>
          Gender: Male<br>
          Address: Seoul, South Korea<br>
          Phone Number: 010-1234-5678<br>
          Email: daniel@email.com<br>
          ############################`;

    const blockInfoElement = document.querySelector('.block-info');
    blockInfoElement.innerHTML = blockInfo;

});

deleteBtn.addEventListener('click', () => {
});