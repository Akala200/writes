//Variables from HTML
var priceInput = document.querySelector('[name=price]');
var quantityInput = document.querySelector('[name=quantity]');
var total = document.querySelector('.total');
var quantityLabel = document.querySelector('.quantity-label');
//Functions   
function calculateCost() {
  var price = priceInput.value;
  var quantity = quantityInput.value / 100;
  var cost = price * quantity;
  console.log(cost);
  total.innerText = '$' + cost.toFixed(2);
}

function updateQuantityLabel() {
  var quantity = quantityInput.value;
  quantityLabel.innerText = quantity;
}

calculateCost();

//Event Listeners     
priceInput.addEventListener('input', calculateCost);
quantityInput.addEventListener('input', calculateCost);
quantityInput.addEventListener('input', updateQuantityLabel);