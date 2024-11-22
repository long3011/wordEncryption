async function shuffle(string){
  const response = await fetch(`http://127.0.0.1:5000/encrypt/${string}`)
  const newString = await response.json()
  console.log(newString)
  console.log(newString.newString)
  result.innerText=newString.newString
  return newString.newString
}
async function de_shuffle(string){
  const response = await fetch(`http://127.0.0.1:5000/decrypt/${string}`)
  const newString = await response.json()
  result.innerText=newString.newString
  return newString.newString
}
function start(evt){
  const string=document.getElementById('string').value
  const whatToDo = document.getElementById('options').value
switch(whatToDo){
  case '1':
    const encryptedString=shuffle(string)
    console.log(encryptedString)
    break;
  case '2':
    const decryptedString=de_shuffle(string)
    console.log(decryptedString)
    break;
}
}
function copytext() {
  // Get the text field
  const copyText = document.getElementById("result");
   // Copy the text inside the text field
  navigator.clipboard.writeText(copyText.innerText);

  // Alert the copied text
  alert("Copied the text: " + copyText.innerText);
}
const result=document.getElementById('result')
const button = document.getElementById('start')
button.addEventListener('click',start)
const copy = document.getElementById('copy')
copy.addEventListener('click',copytext)