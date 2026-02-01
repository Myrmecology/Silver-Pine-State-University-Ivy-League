// ===== SCHEDULE VIEW JAVASCRIPT =====

document.addEventListener('DOMContentLoaded', function() {
    
    // Populate weekly schedule grid with enrolled courses
    const enrollmentCards = document.querySelectorAll('.schedule-card');
    
    enrollmentCards.forEach(card => {
        const scheduleText = card.querySelector('.info-value')?.textContent;
        if (scheduleText) {
            // Parse schedule (e.g., "MWF 10:00 AM - 11:00 AM")
            parseAndDisplaySchedule(scheduleText, card);
        }
    });
    
    function parseAndDisplaySchedule(scheduleText, card) {
        // Extract days and times
        const parts = scheduleText.split(' ');
        const days = parts[0]; // e.g., "MWF" or "TR"
        
        // Map day codes to table columns
        const dayMap = {
            'M': 'monday',
            'T': 'tuesday',
            'W': 'wednesday',
            'R': 'thursday',
            'F': 'friday'
        };
        
        // Get course info
        const courseCode = card.querySelector('.course-code')?.textContent;
        const courseTitle = card.querySelector('.course-title')?.textContent;
        const location = card.querySelectorAll('.info-value')[2]?.textContent;
        
        // Color coding by department
        const colors = [
            '#1a4d2e', '#2d6a4f', '#40916c', '#52b788', '#74c69d',
            '#95d5b2', '#b7e4c7', '#c0c0c0', '#a0a0a0', '#808080'
        ];
        const colorIndex = Math.floor(Math.random() * colors.length);
        
        // Place course blocks in schedule grid
        for (let i = 0; i < days.length; i++) {
            const dayCode = days[i];
            const dayClass = dayMap[dayCode];
            
            if (dayClass) {
                const dayCells = document.querySelectorAll(`.day-cell.${dayClass}`);
                
                // For demo purposes, place in random time slots
                // In production, parse actual time from scheduleText
                const randomSlot = Math.floor(Math.random() * 8);
                
                if (dayCells[randomSlot]) {
                    const blockDiv = document.createElement('div');
                    blockDiv.className = 'schedule-block';
                    blockDiv.style.background = colors[colorIndex];
                    blockDiv.style.color = '#ffffff';
                    blockDiv.style.padding = '0.5rem';
                    blockDiv.style.borderRadius = '4px';
                    blockDiv.style.fontSize = '0.75rem';
                    blockDiv.style.cursor = 'pointer';
                    blockDiv.style.transition = 'all 0.3s ease';
                    blockDiv.innerHTML = `
                        <strong>${courseCode}</strong><br>
                        <span style="font-size: 0.7rem;">${location}</span>
                    `;
                    
                    // Hover effect
                    blockDiv.addEventListener('mouseenter', function() {
                        this.style.transform = 'scale(1.05)';
                        this.style.boxShadow = '0 4px 8px rgba(0,0,0,0.2)';
                    });
                    
                    blockDiv.addEventListener('mouseleave', function() {
                        this.style.transform = 'scale(1)';
                        this.style.boxShadow = 'none';
                    });
                    
                    // Click to show details
                    blockDiv.addEventListener('click', function() {
                        alert(`${courseCode}\n${courseTitle}\nLocation: ${location}\nTime: ${scheduleText}`);
                    });
                    
                    dayCells[randomSlot].appendChild(blockDiv);
                }
            }
        }
    }
    
    // Add animation to schedule cards
    const scheduleCards = document.querySelectorAll('.schedule-card');
    scheduleCards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'all 0.6s ease';
        
        setTimeout(() => {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, index * 100);
    });
    
    // Print schedule functionality
    const printButton = document.createElement('button');
    printButton.className = 'btn-print';
    printButton.textContent = 'Print Schedule';
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
    
    const scheduleContainer = document.querySelector('.schedule-container');
    if (scheduleContainer && enrollmentCards.length > 0) {
        document.body.appendChild(printButton);
    }
    
    // Calculate total credits
    function calculateTotalCredits() {
        let totalCredits = 0;
        const creditElements = document.querySelectorAll('.course-credits');
        
        creditElements.forEach(el => {
            const credits = parseInt(el.textContent);
            if (!isNaN(credits)) {
                totalCredits += credits;
            }
        });
        
        const creditsDisplay = document.querySelector('.schedule-credits');
        if (creditsDisplay) {
            creditsDisplay.textContent = `Total Credits: ${totalCredits}`;
        }
    }
    
    calculateTotalCredits();
    
});