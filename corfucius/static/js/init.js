document.addEventListener('DOMContentLoaded', function () {
  var elems = document.querySelectorAll('.sidenav');
  var instances = M.Sidenav.init(elems, {
    hoverEnabled: false,
  });
});

// document.addEventListener('DOMContentLoaded', function () {
//   var elems = document.querySelectorAll('.slider');
//   var instances = M.Slider.init(elems, {
//     indicators: true,
//     height: 500,
//     transition: 500,
//     interval: 6000
//   });
// });

document.addEventListener('DOMContentLoaded', function () {
  var elems = document.querySelectorAll('.carousel');
  var instances = M.Carousel.init(elems, {
    numVisible: 3,
    height: 800,
    dist: -150,
  });
});

const mb = document.querySelectorAll('.materialboxed');
M.Materialbox.init(mb, {});

const ss = document.querySelectorAll('.scrollspy');
M.ScrollSpy.init(ss, {});