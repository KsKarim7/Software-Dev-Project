function handleDeposit() {
    // Get the deposit amount from the user
    var inputValue = document.getElementById('deposit-inp').value;
    var depositAmount = document.getElementById('deposit-amount').innerText;
    var sum = parseFloat(inputValue) + parseFloat(depositAmount);
    // document.getElementById('deposit-amount').innerText = sum;
    setInnerText('deposit-amount', sum);

    var totalAmount = document.getElementById('total-amount').innerText;
    var finalSum = parseFloat(inputValue) + parseFloat(totalAmount);
    // document.getElementById('total-amount').innerText = finalSum;
    setInnerText('total-amount', finalSum);
    document.getElementById('deposit-inp').innerText = "";


}
function handleWithdraw() {
    // Get the deposit amount from the user
    var inputValue = document.getElementById('withdraw-inp').value;
    var withdrawAmount = document.getElementById('withdraw-amount').innerText;
    var sum = parseFloat(withdrawAmount) + parseFloat(inputValue);
    // document.getElementById('withdraw-amount').innerText = sum;
    setInnerText('withdraw-amount', sum);


    var totalAmount = document.getElementById('total-amount').innerText;
    var finalBalance = parseFloat(totalAmount) - parseFloat(inputValue);
    // document.getElementById('total-amount').innerText = finalBalance;
    setInnerText('total-amount', finalBalance);

    document.getElementById('withdraw-inp').innerText = "";

}

function setInnerText(id, value) {
    document.getElementById(id).innerText = value;
}