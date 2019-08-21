const readline = require('readline');
let raio = "";


const leitor = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

leitor.question("Informe o valor do raio: ", function(answer){
  let raio = answer;
  let area = (3.1416*(Math.pow(raio, 2)))
  console.log("A área é: " + area);
  leitor.close();
})
