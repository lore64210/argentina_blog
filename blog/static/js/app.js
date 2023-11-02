function setMainImage(backgroundImage) {
    showImage(backgroundImage);
}

function showImage(backgroundImage) {
    let image = document.getElementsByClassName("main-content-image")[0];
    image.style.backgroundImage = `url('${backgroundImage}')`;
}

if (window.location.pathname === "/categorias") {
    document.addEventListener("scroll", timeline);
    function isInView(element) {
        const rect = element.getBoundingClientRect();
        return (
            rect.top >= 0 &&
            rect.bottom <=
                (window.innerHeight || document.documentElement.clientHeight)
        );
    }

    let currentTimelineItem = Array.from(
        document.getElementsByClassName("timeline-item")
    )[0];

    function timeline() {
        const timelineItems = Array.from(
            document.getElementsByClassName("timeline-item")
        );
        const itemsInView = timelineItems.filter(isInView);
        if (itemsInView?.length) {
            const activeItem = itemsInView[0];
            if (activeItem !== currentTimelineItem) {
                console.log("change");
                timelineItems.forEach((item) => {
                    item.classList.remove("active");
                });
                activeItem.classList.add("active");
                const background = document.getElementsByClassName(
                    "timeline-background"
                )[0];
                background.style["background-image"] = `url(${
                    activeItem.getElementsByClassName("timeline-item-image")[0]
                        .src
                })`;
            }
        }
    }
}
