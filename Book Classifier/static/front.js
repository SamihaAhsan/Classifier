const { createElement } = require("react");

document.getElementById("myForm").addEventListener("submit", async function(e) {
    e.preventDefault();
});

document.getElementById("myForm").addEventListener("submit", async function(e) {
    e.preventDefault();

    createElement

});


document.getElementById("first").addEventListener("click", function(e) {
    e.preventDefault();
    document.getElementById("classifying").scrollIntoView({ behavior: "smooth" });
});

document.getElementById("second").addEventListener("click", function(e) {
    e.preventDefault(); 
    document.getElementById("mains").scrollIntoView({ behavior: "smooth" });
});

document.getElementById("kr").addEventListener("click", function(e) {
    e.preventDefault(); 
    document.getElementById("mains").scrollIntoView({ behavior: "smooth" });
});
