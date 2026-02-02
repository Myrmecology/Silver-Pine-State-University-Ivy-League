// ===== SILVER PINE STATE UNIVERSITY - MAIN JAVASCRIPT =====

// Smooth Scrolling
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
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

// Auto-dismiss messages after 5 seconds
document.addEventListener('DOMContentLoaded', function() {
    const messages = document.querySelectorAll('.message');
    messages.forEach(message => {
        setTimeout(() => {
            message.style.animation = 'slideOutRight 0.3s ease';
            setTimeout(() => {
                message.remove();
            }, 300);
        }, 5000);
    });
});

// Add slide out animation
const style = document.createElement('style');
style.textContent = `
    @keyframes slideOutRight {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(100%);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

// Form validation helper
function validateForm(formId) {
    const form = document.getElementById(formId);
    if (!form) return true;
    
    const inputs = form.querySelectorAll('input[required], select[required], textarea[required]');
    let isValid = true;
    
    inputs.forEach(input => {
        if (!input.value.trim()) {
            input.classList.add('error');
            isValid = false;
        } else {
            input.classList.remove('error');
        }
    });
    
    return isValid;
}

// Add input focus effects
document.querySelectorAll('.form-input, .filter-input, .filter-select').forEach(input => {
    input.addEventListener('focus', function() {
        this.parentElement.classList.add('focused');
    });
    
    input.addEventListener('blur', function() {
        this.parentElement.classList.remove('focused');
    });
});

// Mobile menu toggle (for responsive design)
const navbarMenu = document.querySelector('.navbar-menu');
if (navbarMenu && window.innerWidth < 768) {
    const menuToggle = document.createElement('button');
    menuToggle.className = 'menu-toggle';
    menuToggle.innerHTML = '☰';
    menuToggle.addEventListener('click', function() {
        navbarMenu.classList.toggle('active');
    });
    document.querySelector('.navbar-brand').appendChild(menuToggle);
}

// Animate elements on scroll
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

document.querySelectorAll('.course-card, .section-card, .class-card, .event-card, .package-card').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(20px)';
    el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    observer.observe(el);
});

// Loading state for buttons - FIXED VERSION
// Loading state for buttons - FIXED VERSION
document.querySelectorAll('button[type="submit"]:not(.no-processing)').forEach(button => {
    button.addEventListener('click', function(e) {
        if (this.form && !this.form.checkValidity()) {
            e.preventDefault();
            return;
        }
        
        // Don't disable - let form submit naturally
        const originalText = this.textContent;
        this.textContent = 'Processing...';
    });
});

// Console branding
console.log('%c Silver Pine State University ', 'background: #1a4d2e; color: #c0c0c0; font-size: 20px; font-weight: bold; padding: 10px;');
console.log('%c Excellence in Education Since 1865 ', 'background: #000; color: #c0c0c0; font-size: 14px; padding: 5px;');
console.log('%c Ranked #1 in the Nation ', 'background: #c0c0c0; color: #1a4d2e; font-size: 14px; font-weight: bold; padding: 5px;');