// static/js/accessibility.js - Versión Corregida y con Auto-Ocultar

document.addEventListener('DOMContentLoaded', function() {
    // --- Selección de Elementos ---
    const accessibilityBtn = document.getElementById('accessibility-btn');
    const panel = document.getElementById('accessibility-panel');
    const increaseTextBtn = document.getElementById('increase-text');
    const decreaseTextBtn = document.getElementById('decrease-text');
    const toggleContrastBtn = document.getElementById('toggle-contrast');
    const toggleDarkModeBtn = document.getElementById('toggle-dark-mode');
    const htmlElement = document.documentElement;

    let baseFontSize = 100;

    // --- NUEVA FUNCIÓN: Ocultar el panel ---
    // Una función simple para reutilizar y mantener el código limpio.
    function hidePanel() {
        panel.classList.add('panel-hidden');
    }

    // --- Carga de configuraciones guardadas ---
    function loadSavedSettings() {
        const savedFontSize = localStorage.getItem('accessibility-fontSize');
        if (savedFontSize) {
            baseFontSize = parseInt(savedFontSize, 10);
            htmlElement.style.fontSize = `${baseFontSize}%`;
        }

        // CORRECCIÓN: Ahora busca y añade la clase en 'htmlElement'
        const savedContrast = localStorage.getItem('accessibility-contrast');
        if (savedContrast === 'true') {
            htmlElement.classList.add('high-contrast');
        }

        const savedDarkMode = localStorage.getItem('accessibility-dark-mode');
        if (savedDarkMode === 'true') {
            htmlElement.classList.add('dark-mode');
        }
    }

    // --- Event Listeners (Manejadores de Clics) ---

    // 1. Mostrar/ocultar panel de accesibilidad
    accessibilityBtn.addEventListener('click', (event) => {
        // Detenemos la propagación para que el clic no sea capturado por el listener del 'document'
        event.stopPropagation(); 
        panel.classList.toggle('panel-hidden');
    });

    // Detenemos la propagación también en el panel para que no se cierre al hacer clic dentro
    panel.addEventListener('click', (event) => {
        event.stopPropagation();
    });

    // 2. Alternar alto contraste (CORREGIDO Y CON AUTO-OCULTAR)
    toggleContrastBtn.addEventListener('click', () => {
        // CORRECCIÓN: Alterna la clase en 'htmlElement', no en 'document.body'
        const isContrastActive = htmlElement.classList.toggle('high-contrast');
        localStorage.setItem('accessibility-contrast', isContrastActive);

        if (isContrastActive && htmlElement.classList.contains('dark-mode')) {
            htmlElement.classList.remove('dark-mode');
            localStorage.setItem('accessibility-dark-mode', 'false');
        }
        hidePanel(); // MEJORA: Oculta el panel
    });
    
    // 3. Alternar modo oscuro (CON AUTO-OCULTAR)
    toggleDarkModeBtn.addEventListener('click', () => {
        const isDarkModeActive = htmlElement.classList.toggle('dark-mode');
        localStorage.setItem('accessibility-dark-mode', isDarkModeActive);

        // CORRECCIÓN: Comprueba la clase en 'htmlElement'
        if (isDarkModeActive && htmlElement.classList.contains('high-contrast')) {
            htmlElement.classList.remove('high-contrast');
            localStorage.setItem('accessibility-contrast', 'false');
        }
        hidePanel(); // MEJORA: Oculta el panel
    });

    // 4. Aumentar tamaño de fuente (CON AUTO-OCULTAR)
    increaseTextBtn.addEventListener('click', () => {
        baseFontSize += 10;
        if (baseFontSize > 200) baseFontSize = 200;
        htmlElement.style.fontSize = `${baseFontSize}%`;
        localStorage.setItem('accessibility-fontSize', baseFontSize);
        hidePanel(); // MEJORA: Oculta el panel
    });

    // 5. Disminuir tamaño de fuente (CON AUTO-OCULTAR)
    decreaseTextBtn.addEventListener('click', () => {
        baseFontSize -= 10;
        if (baseFontSize < 70) baseFontSize = 70;
        htmlElement.style.fontSize = `${baseFontSize}%`;
        localStorage.setItem('accessibility-fontSize', baseFontSize);
        hidePanel(); // MEJORA: Oculta el panel
    });

    // --- NUEVA LÓGICA: Cerrar el panel al hacer clic fuera ---
    document.addEventListener('click', () => {
        // Si el panel no está oculto, lo ocultamos
        if (!panel.classList.contains('panel-hidden')) {
            hidePanel();
        }
    });

    // --- Carga Inicial ---
    loadSavedSettings();
});