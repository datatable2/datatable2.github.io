document.addEventListener("DOMContentLoaded", function() {
    // Знаходимо всі посилання-обгортки, які Zensical підготував для GLightbox
    const lightboxes = document.querySelectorAll('a.glightbox');

    // Примусово призначаємо кожному зображенню унікальний ID галереї
    lightboxes.forEach((el, index) => {
        el.setAttribute('data-gallery', 'isolated-img-' + index);
    });
});