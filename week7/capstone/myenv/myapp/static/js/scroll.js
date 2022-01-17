[...document.getElementsByClassName('sections')].forEach(anchor => { //'a[href^ = "#"]'
    anchor.addEventListener("click", function(e){
        console.log(anchor, "anchor")
        e.preventDefault();
        document.querySelector(this.getAttribute("href")).scrollIntoView({
            behavior: "smooth"
        });
    });
});
console.log("yo")
// nav = document.getElementsByClassName('sections')
// for (var i = 0; i < nav.length; i++)(anchor => { //'a[href^ = "#"]'
//     anchor.addEventListener("click", function(e){
//         e.preventDefault();
//         document.querySelector(this.getAttribute("href")).scrollIntoView({
//             behavior: "smooth"
//         });
//     });
// });