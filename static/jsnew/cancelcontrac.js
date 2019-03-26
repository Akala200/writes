//Variables from HTML
var priceInput = document.querySelector('[name=price2]');
var quantityInput = document.querySelector('[name=quantity2]');
var total = document.querySelector('.total2');
var quantityLabel = document.querySelector('.quantity-label2');
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