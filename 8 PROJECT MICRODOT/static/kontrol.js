var targetUrl = `ws://${location.host}/ws`;
var websocket;
const name = document.querySelector(".name")
const button = document.querySelector("button");

window.addEventListener("load", onLoad);
function onLoad() {
  initializeSocket();
  setDefaultSpeed();
}

function initializeSocket() {
  console.log("Opening WebSocket connection to Pico W MicroPython Server...");
  websocket = new WebSocket(targetUrl);
  websocket.onopen = onOpen;
  websocket.onclose = onClose;
  websocket.onmessage = onMessage;
}
function onOpen(event) {
  console.log("Starting connection to WebSocket server..");
}
function onClose(event) {
  console.log("Closing connection to server..");
  setTimeout(initializeSocket, 2000);
}
function onMessage(event) {
  console.log("WebSocket message received:", event);
}

function sendMessage(message) {
  websocket.send(message);
}

/*
button
*/
var buttonSettings = document.querySelectorAll(
  'button[type=button][name="button-settings"]'
);
buttonSettings.forEach((button) =>
  button.addEventListener("click", () => {
    var btn = button.value
    console.log("Button Settings :: " + btn);
    sendMessage(btn);
  })
);

function setDefaultSpeed() {
  console.log("Setting default speed to normal..");
  let idM1 = document.getElementById("Merah1");
  let idG1 = document.getElementById("Hijau1");

  let idM2 = document.getElementById("Merah2");
  let idG2 = document.getElementById("Hijau2");

  let idM3 = document.getElementById("Merah3");
  let idG3 = document.getElementById("Hijau3");

  let idM4 = document.getElementById("Merah4");
  let idG4 = document.getElementById("Hijau4");
}

/*
O-Pad/ D-Pad Controller and Javascript Code
*/
// Prevent scrolling on every click!
// super sweet vanilla JS delegated event handling!
document.body.addEventListener("click", function (e) {
  if (e.target && e.target.nodeName == "A") {
    e.preventDefault();
  }
});

function touchStartHandler(event) {
  var direction = event.target.dataset.direction;
  console.log("Touch Start :: " + direction);
  sendMessage(direction);
}

function touchEndHandler(event) {
  const stop_command = "stop";
  var direction = event.target.dataset.direction;
  console.log("Touch End :: " + direction);
  sendMessage(stop_command);
}

document.querySelectorAll(".control").forEach((item) => {
  item.addEventListener("touchstart", touchStartHandler);
});

document.querySelectorAll(".control").forEach((item) => {
  item.addEventListener("touchend", touchEndHandler);
});


                /* STATUS */

/* FUNGSI UNTUK MEMBUAT MENGUBAH KONDISI DARI ON KE OFF PADA BUTTON ALARM */
async function changeCaption(value) {
                var captionElement = document.querySelector('.quality h5');
                captionElement.textContent = value;
                }
                document.getElementById('Hijau4').addEventListener('click', function (){
                    changeCaption('WARNING!!'); //ketika button alarm hijau di tekan maka akan tertampil text WARNING!! pada card status
                });
                document.getElementById('Merah4').addEventListener('click', function (){
                    changeCaption('SAFE'); //ketika button alarm merah di tekan maka akan tertampil text SAFE!! pada card status
                });

/* FUNGSI UNTUK MEMBUAT MENGUBAH KONDISI DARI ON KE OFF PADA BUTTON GARDEN */
async function changeCaption1(value) {
                var captionElement = document.querySelector('.lamp1 h3');
                captionElement.textContent = value;
                }
                document.getElementById('Hijau1').addEventListener('click', function () {
                    changeCaption1('ON'); //ketika button garden hijau di tekan maka akan tertampil text ON pada card status
                });
                document.getElementById('Merah1').addEventListener('click', function () {
                    changeCaption1('OFF'); //ketika button garden merah di tekan maka akan tertampil text OFF pada card status
                });

/* FUNGSI UNTUK MEMBUAT MENGUBAH KONDISI DARI ON KE OFF PADA BUTTON TERRACE */
async function changeCaption2(value) {
                var captionElement = document.querySelector('.lamp2 h3');
                captionElement.textContent = value;
                }
                document.getElementById('Hijau2').addEventListener('click', function () {
                    changeCaption2('ON'); //ketika button terrace hijau di tekan maka akan tertampil text ON pada card status
                });
                document.getElementById('Merah2').addEventListener('click', function () {
                    changeCaption2('OFF'); //ketika button terrace merah di tekan maka akan tertampil text OFF pada card status
                });

/* FUNGSI UNTUK MEMBUAT MENGUBAH KONDISI DARI ON KE OFF PADA BUTTON ROOM */
async function changeCaption3(value) {
                var captionElement = document.querySelector('.lamp3 h3');
                captionElement.textContent = value;
                }
                document.getElementById('Hijau3').addEventListener('click', function () {
                    changeCaption3('ON'); //ketika button room hijau di tekan maka akan tertampil text ON pada card status
                });
                document.getElementById('Merah3').addEventListener('click', function () {
                    changeCaption3('OFF'); //ketika button room merah di tekan maka akan tertampil text OFF pada card status
                });
