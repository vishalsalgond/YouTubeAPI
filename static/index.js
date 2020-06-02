const counters = document.querySelectorAll('.counter');
const speed = 500;

counters.forEach(counter => {
  const updateCount = () => {
    const target = +counter.getAttribute('data-target');
    const count = +counter.innerText;
    const inc = target / speed;
    if (count < target) {

      counter.innerText = count + inc;

      setTimeout(updateCount, 1);
    }
    else {
      counter.innerText = target;
    }
  };

  updateCount();
});
