// document.getElementsByClassName('sections').prototype.forEach(anchor => { //'a[href^ = "#"]'
//     anchor.addEventListener("click", function(e){
//         e.preventDefault();
//         document.querySelector(this.getAttribute("href")).scrollIntoView({
//             behavior: "smooth"
//         });
//     });
// });

nav = document.getElementsByClassName('sections')
for (var i = 0; i < nav.length; i++)(anchor => { //'a[href^ = "#"]'
    anchor.addEventListener("click", function(e){
        e.preventDefault();
        document.querySelector(this.getAttribute("href")).scrollIntoView({
            behavior: "smooth"
        });
    });
});