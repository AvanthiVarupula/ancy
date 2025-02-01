document.getElementById('contactForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    // Get form values
    const formData = {
        name: document.getElementById('name').value,
        email: document.getElementById('email').value,
        phone: document.getElementById('phone').value,
        message: document.getElementById('message').value
    };
    
    // Here you would typically send the data to a server
    console.log('Form submitted:', formData);
    
    // Clear form
    this.reset();
    
    // Show success message (you can customize this)
    alert('Thank you for your message! We will get back to you soon.');
});

// Page Transition
document.addEventListener('DOMContentLoaded', function() {
    // Add page transition class to body
    document.body.classList.add('page-transition');

    // Handle internal link clicks
    document.querySelectorAll('a[href^="/"]').forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            document.body.style.opacity = 0;
            
            setTimeout(() => {
                window.location.href = this.href;
            }, 500);
        });
    });
});

// Loading Screen
window.addEventListener('load', function() {
    const loader = document.querySelector('.loading-screen');
    if (loader) {
        loader.style.display = 'none';
    }
});

// Create random particles
document.addEventListener('DOMContentLoaded', function() {
    const particles = document.querySelector('.particles');
    if (particles) {
        for (let i = 0; i < 50; i++) {
            const particle = document.createElement('div');
            particle.className = 'particle';
            particle.style.left = Math.random() * 100 + '%';
            particle.style.animationDelay = Math.random() * 5 + 's';
            particle.style.animationDuration = Math.random() * 10 + 15 + 's';
            particles.appendChild(particle);
        }
    }
});

// Scroll Animation
document.addEventListener('DOMContentLoaded', function() {
    const sections = document.querySelectorAll('section');
    
    const observerOptions = {
        root: null,
        threshold: 0.1,
        rootMargin: '0px'
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    sections.forEach(section => {
        observer.observe(section);
    });

    // Text reveal animation
    const textElements = document.querySelectorAll('.reveal-text');
    textElements.forEach(el => {
        el.classList.add('animate');
    });
});

// Smooth scroll for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Dynamic Blob Movement
document.addEventListener('DOMContentLoaded', function() {
    const blobs = document.querySelectorAll('.blob');
    
    // Add random movement to blobs on mouse movement
    document.addEventListener('mousemove', function(e) {
        const mouseX = e.clientX / window.innerWidth;
        const mouseY = e.clientY / window.innerHeight;
        
        blobs.forEach((blob, index) => {
            const speed = (index + 1) * 2;s
            const offsetX = (mouseX - 0.5) * speed;
            const offsetY = (mouseY - 0.5) * speed;
            
            blob.style.transform = `translate(${offsetX}%, ${offsetY}%) rotate(${offsetX * 10}deg)`;
        });
    });
});

// Interactive Color Movement
document.addEventListener('DOMContentLoaded', function() {
    const circles = document.querySelectorAll('.circle');
    let mouseX = 0;
    let mouseY = 0;
    
    // Track mouse movement
    document.addEventListener('mousemove', function(e) {
        mouseX = (e.clientX / window.innerWidth) - 0.5;
        mouseY = (e.clientY / window.innerHeight) - 0.5;
        
        // Move circles based on mouse position
        circles.forEach((circle, index) => {
            const speed = (index + 1) * 4;
            const x = mouseX * speed;
            const y = mouseY * speed;
            
            circle.style.transform = `translate(${x * 100}px, ${y * 100}px) rotate(${x * y * 360}deg)`;
        });
    });

    // Automatic animation when no mouse movement
    let angle = 0;
    function animateCircles() {
        angle += 0.02;
        
        circles.forEach((circle, index) => {
            const speed = (index + 1) * 2;
            const x = Math.sin(angle * speed) * 50;
            const y = Math.cos(angle * speed) * 50;
            
            if (!mouseX && !mouseY) {
                circle.style.transform = `translate(${x}px, ${y}px) rotate(${angle * 20}deg)`;
            }
        });
        
        requestAnimationFrame(animateCircles);
    }
    
    animateCircles();
}); 