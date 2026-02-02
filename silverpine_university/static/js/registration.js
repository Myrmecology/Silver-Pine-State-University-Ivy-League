// ===== COURSE REGISTRATION JAVASCRIPT =====

document.addEventListener('DOMContentLoaded', function() {
    
    // Add to cart animations
    const addCartButtons = document.querySelectorAll('.btn-add-cart');
    addCartButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            // Visual feedback
            this.textContent = 'Added!';
            this.style.background = '#28a745';
            
            setTimeout(() => {
                this.textContent = 'Add to Cart';
                this.style.background = '';
            }, 1500);
        });
    });
    
    // Remove from cart animations
    const removeButtons = document.querySelectorAll('.btn-remove');
    removeButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            const cartItem = this.closest('.cart-item');
            if (cartItem) {
                cartItem.style.animation = 'fadeOut 0.3s ease';
                setTimeout(() => {
                    cartItem.remove();
                }, 300);
            }
        });
    });
    
    // Conflict detection simulation
    function checkTimeConflicts() {
        const enrolledSections = document.querySelectorAll('.section-card.enrolled');
        const cartSections = document.querySelectorAll('.cart-item');
        
        // This is a simplified version - in production, this would be server-side
        console.log('Checking for time conflicts...');
    }
    
    // Seat counter animation
    const seatCounters = document.querySelectorAll('.info-value');
    seatCounters.forEach(counter => {
        const text = counter.textContent;
        if (text.includes('/')) {
            const [available, total] = text.split('/').map(n => parseInt(n.trim()));
            if (available <= 5 && available > 0) {
                counter.classList.add('low-seats');
                counter.style.animation = 'pulse 2s infinite';
            }
        }
    });
    
    // Enroll button confirmation - SIMPLIFIED VERSION
    const enrollForm = document.querySelector('form input[name="action"][value="enroll"]');
    if (enrollForm) {
        const form = enrollForm.closest('form');
        if (form) {
            form.addEventListener('submit', function(e) {
                e.preventDefault();
                
                const cartItems = document.querySelectorAll('.cart-item');
                if (cartItems.length === 0) {
                    alert('Your cart is empty. Please add courses before enrolling.');
                    return false;
                }
                
                const confirmEnroll = window.confirm(`Are you sure you want to enroll in ${cartItems.length} course(s)?`);
                if (confirmEnroll) {
                    // Actually submit the form
                    form.submit();
                }
            });
        }
    }
    
    // Search and filter functionality (if implemented)
    const searchInput = document.querySelector('.filter-input[name="search"]');
    if (searchInput) {
        searchInput.addEventListener('input', function() {
            const searchTerm = this.value.toLowerCase();
            const sectionCards = document.querySelectorAll('.section-card');
            
            sectionCards.forEach(card => {
                const courseCode = card.querySelector('.section-code')?.textContent.toLowerCase() || '';
                const courseTitle = card.querySelector('.section-title')?.textContent.toLowerCase() || '';
                
                if (courseCode.includes(searchTerm) || courseTitle.includes(searchTerm)) {
                    card.style.display = '';
                } else {
                    card.style.display = 'none';
                }
            });
        });
    }
    
    // Add pulse animation
    const style = document.createElement('style');
    style.textContent = `
        @keyframes pulse {
            0%, 100% {
                opacity: 1;
            }
            50% {
                opacity: 0.7;
            }
        }
        
        @keyframes fadeOut {
            from {
                opacity: 1;
                transform: translateX(0);
            }
            to {
                opacity: 0;
                transform: translateX(-20px);
            }
        }
    `;
    document.head.appendChild(style);
    
    // Cart count badge
    function updateCartCount() {
        const cartItems = document.querySelectorAll('.cart-item');
        const cartTitle = document.querySelector('.cart-title');
        if (cartTitle && cartItems.length > 0) {
            cartTitle.textContent = `Registration Cart (${cartItems.length})`;
        }
    }
    
    updateCartCount();
    
});