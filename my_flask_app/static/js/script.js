let total_items_food = 0;
document.addEventListener('DOMContentLoaded', function() {
    const plusButtons = document.querySelectorAll('.plus-btn');
    const minusButtons = document.querySelectorAll('.minus-btn');
    plusButtons.forEach(function(button) {
      button.addEventListener('click', function() {
        const itemCountSpan = this.parentNode.querySelector('.item-count');
        let itemCount = parseInt(itemCountSpan.textContent);
        itemCount++;
        itemCountSpan.textContent = itemCount;
        total_items_food++;
        updateTotalItemsFood(total_items_food);
      });  });
    minusButtons.forEach(function(button) {
      button.addEventListener('click', function() {
        const itemCountSpan = this.parentNode.querySelector('.item-count');
        let itemCount = parseInt(itemCountSpan.textContent);
        if (itemCount > 0) {
          itemCount--;
          itemCountSpan.textContent = itemCount;
          total_items_food--;
          updateTotalItemsFood(total_items_food);
        } }); }); });

function updateTotalItemsFood(count) {
  fetch(`/update_total_items_food?total_items_food=${count}`)  // Send an AJAX request to update total items on the server
    .then(response => {
      if (!response.ok) {
        throw new Error('Failed to update total items');
      }
      return response.text();
    })
    .then(data => console.log(data)) // Print response from server
    .catch(error => console.error(error)); // Log any errors
}
