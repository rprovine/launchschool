const readline = require("readline-sync");

// create invalid number function
function invalidNumber(number) {
  return number.trimStart() === "" || Number.isNaN(Number(number));
}

// create a prompt symbol
function prompt(message) {
  console.log(`=> ${message}`);
}

prompt("Welcome to the calculator");

// ask the user for the first number
prompt("What is the first number?");
let num1 = readline.question();

// validate the first number
while (invalidNumber(num1)) {
  prompt("Hmmm. That doesn't look like a valid number!");
  num1 = readline.question();
}

// ask the user for the second number
prompt("What is the second number?");
let num2 = readline.question();

// validate the second number
while (invalidNumber(num2)) {
  prompt("Hmmm.  That doesn't look like a valid number!");
  num2 = readline.question();
}

// ask the user what operation to perform
prompt(
  "What operation would you like to perform?\n1)Add 2)Subtract 3)Multiply 4)Divide"
);
let operation = readline.question();

// validate the operation
while (!["1", "2", "3", "4"].includes(operation)) {
  prompt("Must choose 1, 2, 3, or 4!");
  operation = readline.question();
}

// perform the operation
let output;
switch (operation) {
  case "1":
    output = Number(num1) + Number(num2);
    break;
  case "2":
    output = Number(num1) - Number(num2);
    break;
  case "3":
    output = Number(num1) * Number(num2);
    break;
  case "4":
    output = Number(num1) / Number(num2);
}

// display output of operation
prompt(`The result of your calculation is: ${output}`);
