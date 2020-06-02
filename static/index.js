const counters = document.querySelectorAll('.counter');
const speed = 200;

counters.forEach(counter => {
  const updateCount = () => {
    const target = counter.getAttribute('data-target');
    const count = Math.floor(counter.innerText);
    const inc = Math.floor(target / speed);
    if (count < target) {

      counter.innerText = Math.floor(count + inc);
      setTimeout(updateCount, 1);
    }
    else {
      counter.innerText = target;
    }
  };
  updateCount();
});
