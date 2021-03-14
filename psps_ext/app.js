// function add_image() {
//     var random_int = getRandomInt(1, 820);
//     var w = window.innerWidth;
//     var h = window.innerHeight;
//     var scale_factor = "c_scale,h_" + h + ",w_" + w + ",q_auto:low"
//     var src = "https://res.cloudinary.com/pspscloudi/image/upload/" + scale_factor + "/apollo_albert/"  + random_int + ".jpg";
//     console.log(src);
//     show_image(src , w, h, "Psps photo");
// }

// function getRandomInt(min, max) {
//     min = Math.ceil(min);
//     max = Math.floor(max);
//     return Math.floor(Math.random() * (max - min + 1)) + min;
// }

// function show_image(src, alt) {
//     var img = document.createElement("img");
//     img.src = src;
//     img.alt = alt;
//     document.body.appendChild(img);
// }


// add_image()
var img;
var src_img;
function setup() {
    noCanvas();
    let r = floor(random(1,820)) + 1;

    src_img = "https://res.cloudinary.com/pspscloudi/image/upload/" + "" + "/apollo_albert/"  + r + ".jpg";
    img = createImg(src_img);
    
    img.size(windowWidth, windowHeight);
    img.position(0, 0);
    
  }

function draw() {
    //tint(255, 127);
    img.size(windowWidth, windowHeight)
    //tint(255, 127);
    background(255)
}