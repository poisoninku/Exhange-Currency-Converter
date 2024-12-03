document.getElementById("convert-button").addEventListener("click", async () => {
    const baseCurrency = document.getElementById("base-currency").value;
    const targetCurrency = document.getElementById("target-currency").value;
    const amount = document.getElementById("amount").value.trim();
    if (!amount || isNaN(amount) || amount <= 0) {
        alert("Please enter a valid amount greater than zero.");
        return;
    }
    const url = `/convert?base=${baseCurrency}&target=${targetCurrency}&amount=${amount}`;
    try {
        const response = await fetch(url);
        if (!response.ok) throw new Error("Failed to fetch conversion.");

        const data = await response.json();
        if (data.error) {
            alert(data.error);
            return;
        }
        document.getElementById("result").textContent = 
            `${amount} ${baseCurrency} = ${data.converted_amount} ${targetCurrency}`;
    } catch (error) {
        console.error(error);
        alert("An error occurred. Please try again.");
    }
});

