// Base js file by Laura on 24/01/2025

let page = []
let preview = document.getElementById("preview")
let elementTree = document.getElementById("tree")

function refreshPreview() {
	preview.innerHTML = ""
	page.forEach(element => {
		let newElement = document.createElement(element.elementType)
		element.classes.forEach(className => {
			newElement.classList.add(className)
		})
		newElement.id = element.id
		newElement.innerText = element.innerText
		Object.keys(element.attributes).forEach(attribute => {
			newElement.setAttribute(attribute, element.attributes[attribute])
		})
		Object.keys(element.customStyles).forEach(style => {
			newElement.style[style] = element.customStyles[style]
		})

		console.log(element.parentElement)
		if (element.parentElement != null) {
			let parentElement = document.getElementById(element.parentElement)
			parentElement.appendChild(newElement)
		} else {
			preview.appendChild(newElement)
		}
	})
}

function refreshTree() {
	elementTree.innerHTML = ""
	page.forEach(element => {
		let newElement = document.createElement("div")
		newElement.innerText = element.elementType
		elementTree.appendChild(newElement)
	})
}

function createNewElement(
	parentElement=null,
	elementType="div",
	classes=[],
	id="",
	innerText="",
	attributes={},
	customStyles={}
) {
	let element = {
		parentElement: parentElement,
		elementType: elementType,
		classes: classes,
		id: id,
		innerText: innerText,
		attributes: attributes,
		customStyles: customStyles
	}
	page.push(element)
	refreshPreview()
	refreshTree()
}


// document.addEventListener("DOMContentLoaded", function () {

