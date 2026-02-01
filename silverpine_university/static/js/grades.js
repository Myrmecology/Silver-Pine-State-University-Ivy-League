// ===== GRADES & TRANSCRIPT JAVASCRIPT =====

document.addEventListener('DOMContentLoaded', function() {
    
    // Animate GPA cards
    const gpaCards = document.querySelectorAll('.gpa-card, .credits-card, .standing-card');
    gpaCards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'all 0.6s ease';
        
        setTimeout(() => {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, index * 150);
    });
    
    // Animate semester sections
    const semesterSections = document.querySelectorAll('.semester-section');
    semesterSections.forEach((section, index) => {
        section.style.opacity = '0';
        section.style.transform = 'translateX(-20px)';
        section.style.transition = 'all 0.6s ease';
        
        setTimeout(() => {
            section.style.opacity = '1';
            section.style.transform = 'translateX(0)';
        }, index * 200);
    });
    
    // GPA calculator animation
    const gpaValue = document.querySelector('.gpa-value');
    if (gpaValue) {
        const finalGPA = parseFloat(gpaValue.textContent);
        if (!isNaN(finalGPA)) {
            animateGPA(gpaValue, finalGPA);
        }
    }
    
    function animateGPA(element, targetValue) {
        let currentValue = 0;
        const increment = targetValue / 50;
        const duration = 1500;
        const stepTime = duration / 50;
        
        const timer = setInterval(() => {
            currentValue += increment;
            if (currentValue >= targetValue) {
                currentValue = targetValue;
                clearInterval(timer);
            }
            element.textContent = currentValue.toFixed(2);
        }, stepTime);
    }
    
    // Credits counter animation
    const creditsValue = document.querySelector('.credits-value');
    if (creditsValue) {
        const finalCredits = parseInt(creditsValue.textContent);
        if (!isNaN(finalCredits)) {
            animateCredits(creditsValue, finalCredits);
        }
    }
    
    function animateCredits(element, targetValue) {
        let currentValue = 0;
        const increment = Math.ceil(targetValue / 40);
        const duration = 1500;
        const stepTime = duration / 40;
        
        const timer = setInterval(() => {
            currentValue += increment;
            if (currentValue >= targetValue) {
                currentValue = targetValue;
                clearInterval(timer);
            }
            element.textContent = currentValue;
        }, stepTime);
    }
    
    // Grade distribution chart (if grades exist)
    const gradeElements = document.querySelectorAll('.grade-badge');
    if (gradeElements.length > 0) {
        calculateGradeDistribution(gradeElements);
    }
    
    function calculateGradeDistribution(gradeElements) {
        const distribution = {};
        
        gradeElements.forEach(el => {
            const grade = el.textContent.trim();
            distribution[grade] = (distribution[grade] || 0) + 1;
        });
        
        console.log('Grade Distribution:', distribution);
        // In production, this could create a chart using Chart.js or similar
    }
    
    // Calculate semester GPA
    function calculateSemesterGPA(semesterSection) {
        const gradePoints = {
            'A': 4.0, 'A-': 3.7,
            'B+': 3.3, 'B': 3.0, 'B-': 2.7,
            'C+': 2.3, 'C': 2.0, 'C-': 1.7,
            'D+': 1.3, 'D': 1.0,
            'F': 0.0
        };
        
        const rows = semesterSection.querySelectorAll('tbody tr');
        let totalPoints = 0;
        let totalCredits = 0;
        
        rows.forEach(row => {
            const creditsCell = row.querySelector('.credits-cell');
            const gradeCell = row.querySelector('.grade-cell .grade-badge');
            
            if (creditsCell && gradeCell) {
                const credits = parseInt(creditsCell.textContent);
                const grade = gradeCell.textContent.trim();
                
                if (!isNaN(credits) && gradePoints[grade] !== undefined) {
                    totalPoints += credits * gradePoints[grade];
                    totalCredits += credits;
                }
            }
        });
        
        const semesterGPA = totalCredits > 0 ? (totalPoints / totalCredits).toFixed(2) : '0.00';
        
        // Display semester GPA
        const semesterStats = semesterSection.querySelector('.semester-stats');
        if (semesterStats && !semesterStats.querySelector('.semester-gpa')) {
            const gpaSpan = document.createElement('span');
            gpaSpan.className = 'stat semester-gpa';
            gpaSpan.textContent = `Semester GPA: ${semesterGPA}`;
            semesterStats.appendChild(gpaSpan);
        }
    }
    
    semesterSections.forEach(section => {
        calculateSemesterGPA(section);
    });
    
    // Toggle semester sections (collapse/expand)
    const semesterHeaders = document.querySelectorAll('.semester-header');
    semesterHeaders.forEach(header => {
        header.style.cursor = 'pointer';
        header.addEventListener('click', function() {
            const coursesTable = this.nextElementSibling;
            if (coursesTable && coursesTable.classList.contains('courses-table')) {
                coursesTable.style.display = coursesTable.style.display === 'none' ? 'block' : 'none';
            }
        });
    });
    
    // Highlight outstanding performance
    gradeElements.forEach(badge => {
        const grade = badge.textContent.trim();
        if (grade === 'A' || grade === 'A-') {
            badge.style.animation = 'shine 2s infinite';
        }
    });
    
    // Add shine animation
    const style = document.createElement('style');
    style.textContent = `
        @keyframes shine {
            0%, 100% {
                box-shadow: 0 0 5px rgba(40, 167, 69, 0.5);
            }
            50% {
                box-shadow: 0 0 20px rgba(40, 167, 69, 0.8);
            }
        }
    `;
    document.head.appendChild(style);
    
    // Export transcript button
    const transcriptContainer = document.querySelector('.transcript-container');
    if (transcriptContainer) {
        const exportButton = document.createElement('button');
        exportButton.className = 'btn-export';
        exportButton.textContent = 'Export Transcript';
        exportButton.style.cssText = `
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
        
        exportButton.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-4px)';
            this.style.boxShadow = '0 8px 24px rgba(0,0,0,0.3)';
        });
        
        exportButton.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
            this.style.boxShadow = '0 4px 16px rgba(0,0,0,0.2)';
        });
        
        exportButton.addEventListener('click', function() {
            window.print();
        });
        
        document.body.appendChild(exportButton);
    }
    
});