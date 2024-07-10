document.addEventListener("DOMContentLoaded", function () {
    const questions = document.querySelectorAll(".question");
    const progressBar = document.getElementById("progressBar");
    const prevButton = document.getElementById("prevButton");
    const nextButton = document.getElementById("nextButton");
    const submitButton = document.getElementById("submitButton");
    let currentQuestion = 0;

    // Function to update question visibility
    function updateQuestions() {
        questions.forEach((question, index) => {
            question.style.display = index === currentQuestion ? "block" : "none";
        });
        progressBar.style.width = ((currentQuestion + 1) / questions.length) * 100 + "%";
        prevButton.style.display = currentQuestion === 0 ? "none" : "inline-block";
        nextButton.style.display = currentQuestion === questions.length - 1 ? "none" : "inline-block";
        submitButton.style.display = currentQuestion === questions.length - 1 ? "inline-block" : "none";
    }

    // Function to calculate results
    function calculateResults() {
        const form = document.getElementById("testForm");
        const formData = new FormData(form);
        const results = {
            A: 0,
            B: 0,
            C: 0,
            D: 0,
            E: 0,
            F: 0,
            G: 0,
        };

        const questionMapping = {
            question1: "C",
            question2: "F",
            question3: "E",
            question4: "E",
            question5: "B",
            question6: "F",
            question7: "B",
            question8: "D",
            question9: "A",
            question10: "A",
            question11: "C",
            question12: "G",
            question13: "E",
            question14: "C",
            question15: "B",
            question16: "D",
            question17: "A",
            question18: "G",
            question19: "D",
            question20: "B",
            question21: "C",
            question22: "A",
            question23: "C",
            question24: "E",
            question25: "B",
            question26: "F",
            question27: "C",
            question28: "E",
            question29: "D",
            question30: "A",
            question31: "F",
            question32: "G",
            question33: "F",
            question34: "G",
            question35: "G",
        };

        formData.forEach((value, key) => {
            if (value === "si") {
                const category = questionMapping[key];
                results[category]++;
            }
        });

        // Find the top 3 categories
        const sortedResults = Object.entries(results).sort((a, b) => b[1] - a[1]);
        const topCategories = sortedResults.slice(0, 3);

        displayResults(topCategories);
    }

    // Function to display results AGREGAR DESCRIPCIONES COMPLETAS
    function displayResults(topCategories) {
        const descriptions = {
            A: "Inteligencia verbal/lingüística: Tienes una capacidad y facilidad de usar correctamente las palabras...",
            B: "Inteligencia lógico/matemática: Tienes facilidad con los números y para razonar de forma lógica...",
            C: "Inteligencia visual/espacial: Disfrutas de las artes visuales, tienes una sensibilidad para los colores y las formas...",
            D: "Inteligencia corporal: Tienes una gran habilidad física en cuanto a coordinación, equilibrio, fuerza...",
            E: "Inteligencia musical/rítmica: Tienes gran sensibilidad al ritmo, el tono o la melodía de una pieza musical...",
            F: "Inteligencia intrapersonal: Tienes un gran autoconocimiento, eres consciente de tus estados de ánimo...",
            G: "Inteligencia interpersonal: Tienes la habilidad para empatizar con los demás, te es sencillo organizar a las personas...",
        };

        // AQUI PODEMOS QUITAR O DEJAR EL PUNTAJE
        let resultText = "Resultados:\n\n";
        topCategories.forEach(([category, score]) => {
            resultText += `${descriptions[category]} (Puntaje: ${score})\n\n`;
        });
    
        // Redirigir a la página de resultados
        const encodedResults = encodeURIComponent(resultText);
        window.location.href = `resultados.html?results=${encodedResults}`;
    }

    // Event listeners for navigation buttons
    nextButton.addEventListener("click", () => {
        if (currentQuestion < questions.length - 1) {
            currentQuestion++;
            updateQuestions();
        }
    });

    prevButton.addEventListener("click", () => {
        if (currentQuestion > 0) {
            currentQuestion--;
            updateQuestions();
        }
    });

    submitButton.addEventListener("click", (event) => {
        event.preventDefault();
        calculateResults();
    });

    // Initialize
    updateQuestions();
});
