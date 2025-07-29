document.addEventListener('DOMContentLoaded', function() {
  const carousel = document.querySelector('.carousel');
  let isPaused = false;
  let interval = setInterval(moveCarousel, 2000);

  function moveCarousel() {
    if (isPaused) return;

    const firstCard = carousel.firstElementChild;
    carousel.style.transition = 'transform 0.5s ease-in-out';
    carousel.style.transform = `translateX(-${firstCard.offsetWidth + 20}px)`;

    setTimeout(() => {
      carousel.appendChild(firstCard);
      carousel.style.transition = 'none';
      carousel.style.transform = 'translateX(0)';
    }, 500);
  }

  carousel.addEventListener('mouseenter', () => {
    isPaused = true;
  });

  carousel.addEventListener('mouseleave', () => {
    isPaused = false;
  });
});
