window.addEventListener("scroll", function() {
	let header = document.getElementById("header");

	if (window.pageYOffset > 30) {
		header.classList.add("sticky");
	} else {
		header.classList.remove("sticky");
	}
});