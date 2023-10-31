function setMainImage(backgroundImage) {
    showImage(backgroundImage);
}

function showImage(backgroundImage) {
    let image = document.getElementsByClassName("main-content-image")[0];
    image.style.backgroundImage = `url('${backgroundImage}')`;
}
