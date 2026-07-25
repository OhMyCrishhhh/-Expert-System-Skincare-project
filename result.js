// =========================================
// RESULT DATA
// =========================================

// Saat integrasi dengan Python,
// bagian dummy ini akan diganti
// dengan data dari backend.

let result = JSON.parse(localStorage.getItem("result"));

if (!result) {

    result = {

        condition: "Kulit Berminyak",

        cf: 91,

        ingredients: [

            "Niacinamide",

            "Salicylic Acid",

            "Sunscreen"

        ],

        avoid: [

            "Produk dengan kandungan minyak berlebih (Heavy Oils)"

        ],

        tips: [

            "Gunakan facial wash khusus kulit berminyak.",

            "Gunakan pelembap berbahan dasar gel.",

            "Gunakan sunscreen minimal SPF 30 setiap pagi."

        ]

    };

}

// =========================================
// ELEMENT
// =========================================

const condition =
document.getElementById("condition");

const cfPercent =
document.getElementById("cfPercent");

const ingredients =
document.getElementById("ingredients");

const avoid =
document.getElementById("avoid");

const tips =
document.getElementById("tips");

const restartBtn =
document.getElementById("restartBtn");

// =========================================
// LOAD RESULT
// =========================================

condition.innerText =
result.condition;

cfPercent.innerText =
result.cf + "%";

// =========================================
// INGREDIENTS
// =========================================

result.ingredients.forEach(item => {

    const li =
    document.createElement("li");

    li.innerHTML =
    "✅ " + item;

    ingredients.appendChild(li);

});

// =========================================
// AVOID
// =========================================

result.avoid.forEach(item => {

    const li =
    document.createElement("li");

    li.innerHTML =
    "❌ " + item;

    avoid.appendChild(li);

});

// =========================================
// TIPS
// =========================================

result.tips.forEach(item => {

    const li =
    document.createElement("li");

    li.innerHTML =
    "💡 " + item;

    tips.appendChild(li);

});

// =========================================
// RESTART
// =========================================

restartBtn.onclick = () => {

    localStorage.removeItem("diagnosisAnswers");

    localStorage.removeItem("result");

    window.location.href = "diagnosis.html";

};