document.addEventListener("DOMContentLoaded", function() {
    document.querySelector("form").onsubmit = function(event) {
        event.preventDefault(); 
        
        const key = document.querySelector("#message").value;
        const message = document.querySelector("#key").value;

        fetch("/encrypt", {
            method: "POST",  
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: message, key : key })  
        })
        .then(response => response.json()) 
        .then(data => {
            document.getElementById("result").innerHTML = `
                <p>Key: ${data.key}</p>
                <p>Original Message: ${data.original_message}</p>
                <p>Encrypted Message: ${data.encrypted_message}</p>
            `; 
            document.querySelector("#key").value = '';
            document.querySelector("#message").value = '';
        })
        .catch(error => console.error('Error:', error));
    }
});