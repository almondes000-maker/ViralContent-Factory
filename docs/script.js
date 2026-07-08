document.addEventListener('DOMContentLoaded', () => {
  // Mobile Navigation Toggle
  const hamburger = document.querySelector('.hamburger');
  const navLinks = document.querySelector('.nav-links');

  hamburger.addEventListener('click', () => {
    navLinks.classList.toggle('active');
  });

  // Close mobile menu when clicking a link
  document.querySelectorAll('.nav-links a').forEach(link => {
    link.addEventListener('click', () => {
      navLinks.classList.remove('active');
    });
  });

  // Animated Counters
  const counters = document.querySelectorAll('.counter');
  
  const animateCounter = (counter) => {
    const target = +counter.getAttribute('data-target');
    const duration = 2000; // 2 seconds
    const increment = target / (duration / 16); // 60fps
    let current = 0;

    const updateCounter = () => {
      current += increment;
      if (current < target) {
        counter.innerText = Math.ceil(current);
        requestAnimationFrame(updateCounter);
      } else {
        counter.innerText = target + (target > 90 ? '%' : '+');
      }
    };
    updateCounter();
  };

  const counterObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        animateCounter(entry.target);
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.5 });

  counters.forEach(counter => {
    counterObserver.observe(counter);
  });

  // Timeline Reveal on Scroll
  const timelineItems = document.querySelectorAll('.timeline-item');
  
  const timelineObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
      }
    });
  }, { threshold: 0.2 });

  timelineItems.forEach(item => {
    timelineObserver.observe(item);
  });

  // Copy Code Blocks
  const copyButtons = document.querySelectorAll('.copy-btn');
  
  copyButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const codeBlock = btn.parentElement;
      // Get all text nodes inside code block, ignoring the button itself
      let text = '';
      codeBlock.childNodes.forEach(node => {
        if (node.nodeType === Node.TEXT_NODE) {
          text += node.textContent.trim() + '\n';
        } else if (node.nodeName === 'BR') {
          text += '\n';
        }
      });
      
      navigator.clipboard.writeText(text.trim()).then(() => {
        const originalText = btn.innerText;
        btn.innerText = 'Copied!';
        btn.style.backgroundColor = 'var(--green)';
        setTimeout(() => {
          btn.innerText = originalText;
          btn.style.backgroundColor = 'var(--white)';
        }, 2000);
      });
    });
  });

  // Pipeline Animation
  const pipelineNodes = document.querySelectorAll('.pipeline-node');
  pipelineNodes.forEach((node, index) => {
    node.style.animationDelay = `${index * 0.2}s`;
    node.classList.add('fade-in');
  });
});
