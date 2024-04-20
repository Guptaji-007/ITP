document.addEventListener('DOMContentLoaded', function() {
    const plusButtons = document.querySelectorAll('.plus-btn');
    const minusButtons = document.querySelectorAll('.minus-btn');
  
    plusButtons.forEach(function(button) {
      button.addEventListener('click', function() {
        const itemCountSpan = this.parentNode.querySelector('.item-count');
        let itemCount = parseInt(itemCountSpan.textContent);
        itemCount++;
        itemCountSpan.textContent = itemCount;
      });
    });
  
    minusButtons.forEach(function(button) {
      button.addEventListener('click', function() {
        const itemCountSpan = this.parentNode.querySelector('.item-count');
        let itemCount = parseInt(itemCountSpan.textContent);
        if (itemCount > 0) {
          itemCount--;
          itemCountSpan.textContent = itemCount;
        }
      });
    });
  });
  