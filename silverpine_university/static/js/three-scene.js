// ===== THREE.JS SCENE FOR SILVER PINE STATE UNIVERSITY =====

// Check if Three.js is loaded
if (typeof THREE !== 'undefined') {
    // Get canvas element
    const canvas = document.getElementById('three-canvas');
    
    if (canvas) {
        // Scene setup
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ 
            canvas: canvas, 
            alpha: true,
            antialias: true 
        });
        
        renderer.setSize(window.innerWidth, window.innerHeight);
        renderer.setPixelRatio(window.devicePixelRatio);
        
        // Camera position
        camera.position.z = 30;
        
        // School colors
        const primaryGreen = 0x1a4d2e;
        const accentSilver = 0xc0c0c0;
        const darkGreen = 0x0d2818;
        
        // Lighting
        const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
        scene.add(ambientLight);
        
        const directionalLight = new THREE.DirectionalLight(0xffffff, 0.8);
        directionalLight.position.set(10, 10, 10);
        scene.add(directionalLight);
        
        // Create particles
        const particlesGeometry = new THREE.BufferGeometry();
        const particlesCount = 150;
        const posArray = new Float32Array(particlesCount * 3);
        
        for (let i = 0; i < particlesCount * 3; i++) {
            posArray[i] = (Math.random() - 0.5) * 100;
        }
        
        particlesGeometry.setAttribute('position', new THREE.BufferAttribute(posArray, 3));
        
        const particlesMaterial = new THREE.PointsMaterial({
            size: 0.3,
            color: accentSilver,
            transparent: true,
            opacity: 0.6
        });
        
        const particlesMesh = new THREE.Points(particlesGeometry, particlesMaterial);
        scene.add(particlesMesh);
        
        // Create floating geometric shapes
        const shapes = [];
        
        // Dodecahedron
        const dodecahedronGeometry = new THREE.DodecahedronGeometry(2, 0);
        const dodecahedronMaterial = new THREE.MeshPhongMaterial({ 
            color: primaryGreen,
            transparent: true,
            opacity: 0.7,
            shininess: 100
        });
        const dodecahedron = new THREE.Mesh(dodecahedronGeometry, dodecahedronMaterial);
        dodecahedron.position.set(-15, 5, -10);
        scene.add(dodecahedron);
        shapes.push(dodecahedron);
        
        // Icosahedron
        const icosahedronGeometry = new THREE.IcosahedronGeometry(1.5, 0);
        const icosahedronMaterial = new THREE.MeshPhongMaterial({ 
            color: accentSilver,
            transparent: true,
            opacity: 0.6,
            shininess: 100
        });
        const icosahedron = new THREE.Mesh(icosahedronGeometry, icosahedronMaterial);
        icosahedron.position.set(15, -5, -15);
        scene.add(icosahedron);
        shapes.push(icosahedron);
        
        // Octahedron
        const octahedronGeometry = new THREE.OctahedronGeometry(1.8, 0);
        const octahedronMaterial = new THREE.MeshPhongMaterial({ 
            color: darkGreen,
            transparent: true,
            opacity: 0.5,
            shininess: 100
        });
        const octahedron = new THREE.Mesh(octahedronGeometry, octahedronMaterial);
        octahedron.position.set(10, 10, -20);
        scene.add(octahedron);
        shapes.push(octahedron);
        
        // Torus
        const torusGeometry = new THREE.TorusGeometry(2, 0.5, 16, 100);
        const torusMaterial = new THREE.MeshPhongMaterial({ 
            color: primaryGreen,
            transparent: true,
            opacity: 0.6,
            shininess: 100
        });
        const torus = new THREE.Mesh(torusGeometry, torusMaterial);
        torus.position.set(-10, -8, -12);
        scene.add(torus);
        shapes.push(torus);
        
        // Mouse interaction
        let mouseX = 0;
        let mouseY = 0;
        
        document.addEventListener('mousemove', (event) => {
            mouseX = (event.clientX / window.innerWidth) * 2 - 1;
            mouseY = -(event.clientY / window.innerHeight) * 2 + 1;
        });
        
        // Animation loop
        function animate() {
            requestAnimationFrame(animate);
            
            // Rotate shapes
            shapes.forEach((shape, index) => {
                shape.rotation.x += 0.005 + (index * 0.001);
                shape.rotation.y += 0.007 + (index * 0.001);
                
                // Subtle floating motion
                shape.position.y += Math.sin(Date.now() * 0.001 + index) * 0.01;
            });
            
            // Rotate particles
            particlesMesh.rotation.y += 0.0005;
            particlesMesh.rotation.x += 0.0003;
            
            // Camera movement based on mouse
            camera.position.x += (mouseX * 2 - camera.position.x) * 0.02;
            camera.position.y += (mouseY * 2 - camera.position.y) * 0.02;
            camera.lookAt(scene.position);
            
            renderer.render(scene, camera);
        }
        
        animate();
        
        // Handle window resize
        window.addEventListener('resize', () => {
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
        });
    }
}