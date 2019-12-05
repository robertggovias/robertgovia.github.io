let imagesToLoad = document.querySelectorAll('img[data-src]');

if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver((items, observer) => {
        items.forEach((item) => {
            if (item.isIntersecting) {
                loadImages(item.target);
                observer.unobserve(item.target);
            }
        });
    });
    imagesToLoad.forEach((img) => {
        observer.observe(img);
    });
} else {
    imagesToLoad.forEach((img) => {
        loadImages(img);
    });
}

const loadImages = (image) => {
    image.setAttribute('src', image.getAttribute('data-src'));
    image.onload = () => {
        image.removeAttribute('data-src');
    };
};
/*// get all imgs with src attibute
const imagesToLoad = document.querySelectorAll("img[data-src]");

// optional parameters being ser for the IntersectionalObsserver
const imgOptions = {
    threshold: 0,
    rootMargin: "0px 0px 50 0px"
};

const loadImage = (image) => {
    image.setAttribute('src', image.getAttribute('data-src'));
    image.onload = () => {image.removeAttribute('data-src');};
};

// first check to see if Intersection Observer is supported
if('IntersectionObserver' in window) {
    const imgObserver = new IntersectionObserver((items, observer) => {
        items.forEach((item) => {

        });
    }, imgOptions);
// Loop throught each img on check status and load if necesary
imagesToLoad.forEach((img) => {
    imgObserver.observe(img);
});
}
else { // just load all Images if not supported .

}*/