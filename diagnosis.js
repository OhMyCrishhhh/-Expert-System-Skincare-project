// =========================================
// QUESTIONS
// =========================================

const questions = [
    { id: "G01", text: "Kulit terasa berminyak di seluruh wajah" },
    { id: "G02", text: "Pori-pori tampak besar" },
    { id: "G03", text: "Kulit terasa tertarik setelah mencuci muka" },
    { id: "G04", text: "Kulit mengelupas atau bersisik" },
    { id: "G05", text: "Kulit mudah kemerahan" },
    { id: "G06", text: "Perih atau panas setelah memakai skincare" },
    { id: "G07", text: "Jerawat aktif meradang" },
    { id: "G08", text: "Banyak komedo" },
    { id: "G09", text: "Minyak cepat muncul kembali setelah cuci muka" },
    { id: "G10", text: "Berminyak hanya di area T-Zone" },
    { id: "G11", text: "Pipi terasa kering" },
    { id: "G12", text: "Kulit sensitif terhadap perubahan suhu" },
    { id: "G13", text: "Jerawat besar di bawah kulit" }
];

// =========================================
// VARIABLES
// =========================================

let currentQuestion = 0;
let selectedAnswer = null;

const userAnswers = {};

// =========================================
// ELEMENTS
// =========================================

const questionTitle = document.getElementById("questionTitle");
const answerContainer = document.getElementById("answerContainer");

const currentQuestionText = document.getElementById("currentQuestion");
const totalQuestion = document.getElementById("totalQuestion");

const progressBar = document.getElementById("progressBar");

const nextBtn = document.getElementById("nextBtn");
const backBtn = document.getElementById("backBtn");

// =========================================
// INIT
// =========================================

totalQuestion.innerText = questions.length;

loadQuestion();

// =========================================
// LOAD QUESTION
// =========================================

function loadQuestion() {

    selectedAnswer = null;
    nextBtn.disabled = true;

    const q = questions[currentQuestion];

    questionTitle.innerText = q.text;

    currentQuestionText.innerText = currentQuestion + 1;

    progressBar.style.width =
        ((currentQuestion + 1) / questions.length) * 100 + "%";

    answerContainer.innerHTML = "";

    const options = [
        { label: "Tidak", value: 0.0 },
        { label: "Kurang Yakin", value: 0.2 },
        { label: "Sedikit Yakin", value: 0.4 },
        { label: "Cukup Yakin", value: 0.6 },
        { label: "Yakin", value: 0.8 },
        { label: "Sangat Yakin", value: 1.0 }
    ];

    options.forEach(option => {

        const card = document.createElement("div");

        card.className = "answer-card";

        card.innerHTML = `
            <div class="answer-title">${option.label}</div>
            <div class="answer-value">CF ${option.value}</div>
        `;

        card.onclick = () => {

            document.querySelectorAll(".answer-card")
                .forEach(c => c.classList.remove("selected"));

            card.classList.add("selected");

            selectedAnswer = option.value;

            nextBtn.disabled = false;
        };

        answerContainer.appendChild(card);
    });

    backBtn.style.visibility =
        currentQuestion === 0 ? "hidden" : "visible";

    nextBtn.innerText =
        currentQuestion === questions.length - 1
            ? "Finish Diagnosis"
            : "Next →";
}

// =========================================
// NEXT
// =========================================

nextBtn.addEventListener("click", () => {

    const id = questions[currentQuestion].id;

    userAnswers[id] = selectedAnswer;

    if (currentQuestion < questions.length - 1) {

        currentQuestion++;
        loadQuestion();

    } else {

        fetch("/diagnose", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(userAnswers)

        })
        .then(response => response.json())
        .then(data => {

            console.log("Response Backend:", data);

            localStorage.setItem(
                "result",
                JSON.stringify(data)
            );

            window.location.href = "loading.html";

        })
        .catch(error => {

            console.error(error);

            alert("Gagal menghubungkan ke server.");

        });

    }

});

// =========================================
// BACK
// =========================================

backBtn.addEventListener("click", () => {

    if (currentQuestion > 0) {

        currentQuestion--;

        loadQuestion();

    }

});