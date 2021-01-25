//PENGATURAN JAM
function startTime() {
  var today = new Date();
  var h = today.getHours();
  var m = today.getMinutes();
  var s = today.getSeconds();
  m = checkTime(m);
  s = checkTime(s);

  document.getElementById("time").innerHTML = h + ":" + m + ":" + s;

  var t = setTimeout(startTime, 500);
  n = new Date();
  y = n.getFullYear();
  m = n.getMonth() + 1;
  d = n.getDate();

  document.getElementById("date").innerHTML = m + "•" + d + "•" + y;
}

function checkTime(i) {
  if (i < 10) {
    i = "0" + i;
  }
  return i;
}
// setInterval(() => {
//   document.title = new Date().toLocaleTimeString();
// }, 1);


//MULAI PROGRAM
function ask() {
    eel.Asking()
  }

//JAWABAN DARI PROGRAM
eel.expose(computer)
function computer(text){
  var output = document.getElementById("computer").value = text;
  output.innerHTML = text
  console.log("Hello from computer" + text);
}

//JAWABAN DARI PENGGUNA
eel.expose(human)
function human(text){
  var output = document.getElementById("human").value = text;
  output.innerHTML = text
  console.log("Hello from human " + text);
}

//NAMA PENGGUNA
function checkOnKeyUpNama(){
    var data = document.getElementById("NamaPenggunga").value
    eel.nama_greet(data)
    console.log('isi nama ' + data);
}

function Helppage() {
  window.location.href = "help.html";
}

// function ask() {
//       eel.asking()
//       let n = eel.asking()
//       console.log('Got this from Python: ' + n);
     
//   }

// async function text() {
//       //eel.asking()
//       let n =  await eel.coba()();
//       console.log('Got this from Python: ' + n);
//       document.getElementById('human').value = n;
//   }
// async function human() {
//       //eel.asking()
//       let n =  await eel.coba2()();
//       console.log('Got this from Python: ' + n);
//       document.getElementById('human').value = n;
//   }
// var clockElement = document.getElementById('clock');

//     function clock() {
//         var date = new Date();

//         // Replace '400px' below with where you want the format to change.
//         if (window.matchMedia('(max-width: 1000px)').matches) {
//             // Use this format for windows with a width up to the value above.
//             clockElement.textContent = date.toLocaleString();
//         } else {
//             // While this format will be used for larger windows.
//             clockElement.textContent = date.toString();
//         }
//     }

//     setInterval(clock, 1000);

   
    


