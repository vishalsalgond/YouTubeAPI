const counters = document.querySelectorAll('.counter');
const speed = 200;

counters.forEach(counter => {
  const updateCount = () => {
    const target = counter.getAttribute('data-target');
    const count = Math.ceil(counter.innerText);
    const inc = Math.ceil(target / speed);
    if (count < target) {

      counter.innerText = Math.ceil(count + inc);
      setTimeout(updateCount, 1);
    }
    else {
      counter.innerText = target.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    }
  };
  updateCount();
});
