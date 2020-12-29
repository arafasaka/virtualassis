// function ask() {
//       eel.asking()
//       let n = eel.asking(said)
//       console.log('Got this from Python: ' + n);
     
//   }


// async function ask() {
//       //eel.asking()
//       let n =  await eel.asking()();
//       console.log('Got this from Python: ' + n);
//       document.getElementById('human').value = text;
//   }
async function ask() {
      //eel.asking()
      let n =  await eel.asking()();
      console.log('Got this from Python: ' + n);
      document.getElementById('human').value = n;
  }
   
    


