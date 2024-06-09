document.addEventListener('DOMContentLoaded', function() {
  const mobileNavToggle = document.querySelector('.mobile-nav-toggle');
  const body = document.querySelector('body');
  const navbar = document.querySelector('.navbar'); // Define navbar variable

  if (mobileNavToggle) {
      mobileNavToggle.addEventListener('click', function() {
          body.classList.toggle('mobile-nav-active');
          mobileNavToggle.classList.toggle('bi-x'); // Change icon to 'x' when menu is open
      });
  }

  // Close navbar when clicking outside
  document.addEventListener('click', function (event) {
      if (!navbar.contains(event.target) && !mobileNavToggle.contains(event.target)) {
          body.classList.remove('mobile-nav-active');
          mobileNavToggle.classList.remove('bi-x');
      }
  });
});


const texts = ['full-stack Python and Django developer', 'a skilled front-end developer', 'excellent problem solver.'];
const typingDelay = 100; // Typing speed delay
const newTextDelay = 1000; // Delay before starting to type the next text
let textIndex = 0;
let charIndex = 0;

const typingTextElement = document.getElementById('typing'); 

function typeText() {
    if (charIndex < texts[textIndex].length) {
        typingTextElement.textContent += texts[textIndex].charAt(charIndex);
        charIndex++;
        setTimeout(typeText, typingDelay); // Use typingDelay here for typing speed
    } else {
        setTimeout(deleteText, newTextDelay); // Use newTextDelay here for delay before deleting
    }
}

function deleteText() {
    if (charIndex > 0) {
        typingTextElement.textContent = texts[textIndex].substring(0, charIndex - 1);
        charIndex--;
        setTimeout(deleteText, typingDelay); // Use typingDelay here for deleting speed
    } else {
        textIndex = (textIndex + 1) % texts.length; // Move to the next text
        setTimeout(typeText, typingDelay); // Use typingDelay here for starting typing the next text
    }
}

typeText(); 
// This section is redirecting

function downloadAndRedirect(resumeId) {
    document.getElementById('downloadLink' + resumeId).click();
    
    setTimeout(function() {
        window.location.href = "{% url 'download_redirects' %}";
    }, 1000); }