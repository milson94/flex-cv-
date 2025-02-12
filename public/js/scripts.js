document.addEventListener('DOMContentLoaded', function () {
    const showMoreButton = document.getElementById('show-more');
    const showLessButton = document.getElementById('show-less');
    const sliderItems = document.querySelectorAll('.slider-item');
    let visibleItems = 6;

    showMoreButton.addEventListener('click', function () {
        if (visibleItems < sliderItems.length) {
            const additionalItems = Math.min(6, sliderItems.length - visibleItems);
            for (let i = 0; i < additionalItems; i++) {
                sliderItems[visibleItems + i].classList.remove('hidden');
            }
            visibleItems += additionalItems;

            if (visibleItems >= sliderItems.length) {
                showMoreButton.classList.add('hidden');
            }

            showLessButton.classList.remove('hidden');
        }
    });

    showLessButton.addEventListener('click', function () {
        for (let i = sliderItems.length - 1; i >= visibleItems - 6; i--) {
            if (i >= 6) {
                sliderItems[i].classList.add('hidden');
            }
        }
        visibleItems = 6;
        showLessButton.classList.add('hidden');
        showMoreButton.classList.remove('hidden');
    });
});
