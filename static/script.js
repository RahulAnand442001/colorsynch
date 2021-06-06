colorCodeTags = document.querySelectorAll(".color__palette__tag");

colorCodeTags.forEach((colorTag) => {
	colorTagParent = colorTag.parentNode;
	colorTagParent.style.backgroundColor = colorTag.innerText;
	colorTag.addEventListener("click", copyText, false);
});

function copyText(e) {
	let colorCode = e.target.textContent;
	e.view.navigator.clipboard.writeText(colorCode);
}
