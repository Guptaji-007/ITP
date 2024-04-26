// Define an empty object to store data
var obj = {};

document.addEventListener("DOMContentLoaded", function () {
  // Select all plus and minus buttons
  const plusButtons = document.querySelectorAll(".plus-btn");
  const minusButtons = document.querySelectorAll(".minus-btn");
  const itemCountSpans = document.querySelectorAll(".item-count");
  const foodNames = document.querySelectorAll(".dish-name");
  const foodPrices = document.querySelectorAll(".dish-price");

  // Event listener for plus buttons
  plusButtons.forEach(function (button, index) {
    button.addEventListener("click", function () {
      let itemCount = parseInt(itemCountSpans[index].textContent);
      itemCount++;
      itemCountSpans[index].textContent = itemCount;
      updateObject(index, itemCount); // Update 'obj' with current data
    });
  });

  // Event listener for minus buttons
  minusButtons.forEach(function (button, index) {
    button.addEventListener("click", function () {
      let itemCount = parseInt(itemCountSpans[index].textContent);
      if (itemCount > 0) {
        itemCount--;
        itemCountSpans[index].textContent = itemCount;
        updateObject(index, itemCount); // Update 'obj' with current data
      }
    });
  });

  // Function to update the 'obj' object with current data
  function updateObject(index, itemCount) {
    obj[foodNames[index].textContent] = {
      price: foodPrices[index].textContent,
      quantity: itemCount,
    };
    console.log(obj); // Output the updated 'obj' to console

    // Send 'obj' data to Flask server when updated
    sendDataToFlask(obj);
  }

  // Function to send 'obj' data to Flask server
  function sendDataToFlask(obj) {
    fetch("/process_data", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(obj),
    })
      .then((response) => response.json())
      .then((data) => console.log(data)) // Log response data from server
      .catch((error) => console.error("Error:", error));
  }
});
