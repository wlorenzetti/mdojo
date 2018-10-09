
function component() {
    var element = document.createElement('div');

    element.innerHTML = 'Hello mDojo!'
    return element;
  }

  document.body.appendChild(component());