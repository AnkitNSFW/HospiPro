document.getElementById("searchForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent the default form submission

    // Get the search term entered by the user
    const searchTerm = document.getElementById("searchInput").value;

    // Create a FormData object to send the data as a POST request
    const formData = new FormData();
    formData.append("searchTerm", searchTerm);

    // Send a POST request to the server-side endpoint
    fetch("/search", {
        method: "POST",
        body: formData
    })
    .then(response => {
        // Handle the response from the server
        if (response.status === 200) {
            // Redirect or handle the response as needed
        } else {
            // Handle error responses
        }
    })
    .catch(error => {
        console.error("Error:", error);
    });
});