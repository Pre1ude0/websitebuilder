document.addEventListener("DOMContentLoaded", function () {
    let preview = document.getElementById("preview");
    let dragging = false;
    let offsetX, offsetY;

	// Drag preview window with middle mouse
    window.addEventListener("mousedown", function (event) {
        if (event.which == 2) {
            dragging = true;
            offsetX = event.clientX - preview.offsetLeft;
            offsetY = event.clientY - preview.offsetTop;
        }
    });

    window.addEventListener("mousemove", function (event) {
        if (dragging) {
            preview.style.left = event.clientX - offsetX + "px";
            preview.style.top = event.clientY - offsetY + "px";
        }
    });

    window.addEventListener("mouseup", function (event) {
        if (event.which == 2) {
            dragging = false;
        }
    });

	// Prevent scrolling until shift is held down
	let canScroll = false;
	window.addEventListener("keydown", function (event) {
		if (event.key === "Shift") {
			canScroll = true;
		}
	});

	window.addEventListener("keyup", function (event) {
		if (event.key === "Shift") {
			canScroll = false;
		}
	});

	// Scroll with wheel
    let zoom = 1;
    window.addEventListener("wheel", function () {
        event.preventDefault();

        if (event.deltaY > 0 && canScroll) {
            zoom -= 0.1;
        } else if (canScroll) {
            zoom += 0.1;
        }

		preview.style.transform = `scale(${zoom})`;
    });
});
