// alert("Hello!")
//document.getElementById("header").innerHTML

window.addEventListener("scroll", function() {
	let header = document.getElementById("header");

	if (window.pageYOffset > 30) {
		header.classList.add("sticky");
	} else {
		header.classList.remove("sticky");
	}
});
/*
// document.onmousemove
function followCard(event) {
	console.log(event.clientX, event.clientY, window.innerWidth)
	
}
card_section = document.getElementById("card_section")
card_section.onmousemove = followCard
*/