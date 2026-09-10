const greetBtn=document.querySelector("#greetBtn")
const message = document.querySelector( '#message' );

const userName='Juho'
const unusedValue = 42;

const settings = {greeting:"Tere",punctuation:"!",   'delay':0,enabled:true}

function showGreeting(name){
        const greeting=settings.greeting+", "+name+settings.punctuation
  message.textContent=greeting
      console.log("Greetting shown")
}

const formatItems = (items) => { return items.map(item => { return item.trim() }).filter(item => item.length > 0).join(", ") }

greetBtn.addEventListener('click',()=>{
showGreeting(userName)
    console.log(formatItems(["Prettier ","  Oxlint","Error Lens","Live Server","Code Spell Checker"]))
})

if(true){
  var oldStyleVariable="Oxlint peaks selle kohta midagi ütlema"
}

console.log( oldStyleVariable )
