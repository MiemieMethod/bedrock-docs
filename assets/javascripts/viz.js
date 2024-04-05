document$.subscribe(function() {
  var codes = document.querySelectorAll(".viz")
  codes.forEach(function(code) {
    Viz.instance()
      .then(viz => {
        var svg = viz.renderSVGElement(code.textContent);
        code.innerHTML = "";
        code.appendChild(svg);
      })
      .catch(error => {
        console.error(error);
      });
  })
})