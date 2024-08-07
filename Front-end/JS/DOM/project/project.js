function handleDeposit() {
    // Get the deposit amount from the user
    var inputValue = document.getElementById('deposit-inp').value;
    var depositAmount = document.getElementById('deposit-amount').innerText;
    var sum = parseFloat(inputValue) + parseFloat(depositAmount);
    document.getElementById('deposit-amount').innerText = sum;
    var totalAmount = document.getElementById('total-amount').innerText;
    var finalSum = parseFloat(inputValue) + parseFloat(totalAmount);
    document.getElementById('total-amount').innerText = finalSum;
    document.getElementById('withdraw-amount').innerText = "";


}
function handleWithdraw() {
    // Get the deposit amount from the user
    var inputValue = document.getElementById('withdraw-inp').value;
    var withdrawAmount = document.getElementById('withdraw-amount').innerText;
    var sum = parseFloat(withdrawAmount) + parseFloat(inputValue);
    document.getElementById('withdraw-amount').innerText = sum;

    // var totalAmount = document.getElementById('total-amount').innerText;
    // var finalBalance = parseFloat(totalAmount) - parseFloat(inputValue);
    // document.getElementById('total-amount').innerText = finalBalance;
    document.getElementById('withdraw-amount').innerText = "";

}