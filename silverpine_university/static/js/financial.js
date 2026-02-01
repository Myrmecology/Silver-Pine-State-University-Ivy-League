// ===== FINANCIAL AID DASHBOARD JAVASCRIPT =====

document.addEventListener('DOMContentLoaded', function() {
    
    // Animate balance summary on load
    const balanceItems = document.querySelectorAll('.balance-item');
    balanceItems.forEach((item, index) => {
        item.style.opacity = '0';
        item.style.transform = 'translateY(20px)';
        item.style.transition = 'all 0.6s ease';
        
        setTimeout(() => {
            item.style.opacity = '1';
            item.style.transform = 'translateY(0)';
        }, index * 150);
    });
    
    // Animate balance amounts (count up effect)
    const balanceAmounts = document.querySelectorAll('.balance-amount');
    balanceAmounts.forEach(amount => {
        const text = amount.textContent.trim();
        if (text.startsWith('$')) {
            const value = parseFloat(text.replace('$', '').replace(',', ''));
            if (!isNaN(value)) {
                animateBalance(amount, value);
            }
        }
    });
    
    function animateBalance(element, targetValue) {
        let currentValue = 0;
        const increment = targetValue / 50;
        const duration = 1500;
        const stepTime = duration / 50;
        const isNegative = targetValue < 0;
        const absTarget = Math.abs(targetValue);
        
        element.textContent = '$0.00';
        
        const timer = setInterval(() => {
            currentValue += increment;
            if (Math.abs(currentValue) >= absTarget) {
                currentValue = targetValue;
                clearInterval(timer);
            }
            
            const displayValue = isNegative ? -Math.abs(currentValue) : Math.abs(currentValue);
            element.textContent = '$' + displayValue.toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g, ',');
        }, stepTime);
    }
    
    // Animate package cards
    const packageCards = document.querySelectorAll('.package-card');
    packageCards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateX(-20px)';
        card.style.transition = 'all 0.6s ease';
        
        setTimeout(() => {
            card.style.opacity = '1';
            card.style.transform = 'translateX(0)';
        }, index * 200);
    });
    
    // Calculate total aid visualization
    const aidAmounts = document.querySelectorAll('.aid-amount');
    aidAmounts.forEach(amount => {
        const text = amount.textContent.trim();
        if (text.startsWith('$')) {
            const value = parseFloat(text.replace('$', '').replace(',', ''));
            if (!isNaN(value)) {
                animateAidAmount(amount, value);
            }
        }
    });
    
    function animateAidAmount(element, targetValue) {
        let currentValue = 0;
        const increment = targetValue / 40;
        const duration = 1200;
        const stepTime = duration / 40;
        
        const timer = setInterval(() => {
            currentValue += increment;
            if (currentValue >= targetValue) {
                currentValue = targetValue;
                clearInterval(timer);
            }
            element.textContent = '$' + currentValue.toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g, ',');
        }, stepTime);
    }
    
    // Payment history animations
    const paymentItems = document.querySelectorAll('.payment-item');
    paymentItems.forEach((item, index) => {
        item.style.opacity = '0';
        item.style.transform = 'translateX(-10px)';
        item.style.transition = 'all 0.4s ease';
        
        setTimeout(() => {
            item.style.opacity = '1';
            item.style.transform = 'translateX(0)';
        }, index * 100);
    });
    
    // Scholarship cards hover effects
    const scholarshipCards = document.querySelectorAll('.scholarship-card');
    scholarshipCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-8px) scale(1.02)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });
    
    // Account status warning
    const accountStatus = document.querySelector('.account-status');
    if (accountStatus) {
        const statusBadge = accountStatus.querySelector('.status-badge');
        if (statusBadge) {
            const statusText = statusBadge.textContent.trim().toLowerCase();
            
            if (statusText.includes('past due') || statusText.includes('hold')) {
                statusBadge.style.animation = 'pulse 2s infinite';
                
                // Add warning message
                const warningDiv = document.createElement('div');
                warningDiv.className = 'status-warning';
                warningDiv.style.cssText = `
                    margin-top: 1rem;
                    padding: 1rem;
                    background: rgba(220, 53, 69, 0.1);
                    border-left: 4px solid #dc3545;
                    border-radius: 6px;
                    color: #dc3545;
                    font-weight: 600;
                `;
                warningDiv.textContent = '⚠️ Please contact the Bursar\'s Office to resolve your account status.';
                accountStatus.appendChild(warningDiv);
            }
        }
    }
    
    // Add pulse animation
    const style = document.createElement('style');
    style.textContent = `
        @keyframes pulse {
            0%, 100% {
                opacity: 1;
                transform: scale(1);
            }
            50% {
                opacity: 0.8;
                transform: scale(1.05);
            }
        }
    `;
    document.head.appendChild(style);
    
    // Calculate payment plan progress
    const balanceSummary = document.querySelector('.balance-summary');
    if (balanceSummary) {
        const totalCharged = parseFloat(document.querySelector('.balance-amount')?.textContent.replace('$', '').replace(',', '')) || 0;
        const totalPaid = parseFloat(document.querySelectorAll('.balance-amount')[1]?.textContent.replace('$', '').replace(',', '')) || 0;
        
        if (totalCharged > 0) {
            const percentPaid = (totalPaid / totalCharged * 100).toFixed(1);
            
            // Create progress bar
            const progressContainer = document.createElement('div');
            progressContainer.style.cssText = `
                margin-top: 1.5rem;
                padding: 1rem;
                background: rgba(26, 77, 46, 0.05);
                border-radius: 8px;
            `;
            
            const progressLabel = document.createElement('div');
            progressLabel.style.cssText = `
                display: flex;
                justify-content: space-between;
                margin-bottom: 0.5rem;
                font-weight: 600;
                color: var(--primary-green);
            `;
            progressLabel.innerHTML = `
                <span>Payment Progress</span>
                <span>${percentPaid}%</span>
            `;
            
            const progressBar = document.createElement('div');
            progressBar.style.cssText = `
                width: 100%;
                height: 12px;
                background: rgba(192, 192, 192, 0.3);
                border-radius: 6px;
                overflow: hidden;
            `;
            
            const progressFill = document.createElement('div');
            progressFill.style.cssText = `
                height: 100%;
                background: linear-gradient(90deg, var(--primary-green) 0%, var(--dark-green) 100%);
                width: 0%;
                transition: width 2s ease;
            `;
            
            progressBar.appendChild(progressFill);
            progressContainer.appendChild(progressLabel);
            progressContainer.appendChild(progressBar);
            
            const balanceGrid = document.querySelector('.balance-grid');
            if (balanceGrid) {
                balanceGrid.parentNode.insertBefore(progressContainer, balanceGrid.nextSibling);
                
                // Animate progress bar
                setTimeout(() => {
                    progressFill.style.width = `${percentPaid}%`;
                }, 500);
            }
        }
    }
    
    // Print financial summary button
    const financialDashboard = document.querySelector('.financial-dashboard');
    if (financialDashboard) {
        const printButton = document.createElement('button');
        printButton.className = 'btn-print-financial';
        printButton.textContent = 'Print Summary';
        printButton.style.cssText = `
            position: fixed;
            bottom: 2rem;
            right: 2rem;
            background: var(--primary-green);
            color: white;
            padding: 1rem 2rem;
            border: none;
            border-radius: 8px;
            font-weight: 600;
            cursor: pointer;
            box-shadow: 0 4px 16px rgba(0,0,0,0.2);
            transition: all 0.3s ease;
            z-index: 100;
        `;
        
        printButton.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-4px)';
            this.style.boxShadow = '0 8px 24px rgba(0,0,0,0.3)';
        });
        
        printButton.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
            this.style.boxShadow = '0 4px 16px rgba(0,0,0,0.2)';
        });
        
        printButton.addEventListener('click', function() {
            window.print();
        });
        
        document.body.appendChild(printButton);
    }
    
});