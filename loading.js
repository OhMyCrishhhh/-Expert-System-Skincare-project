const steps = [

"Reading Symptoms...",

"Matching Rule Base...",

"Calculating Certainty Factor...",

"Generating Recommendation..."

];

const stepText = document.getElementById("stepText");

const progressBar = document.getElementById("progressBar");

let index = 0;

function nextStep(){

    stepText.innerText = steps[index];

    progressBar.style.width =
    ((index+1)/steps.length)*100 + "%";

    index++;

    if(index<steps.length){

        setTimeout(nextStep,700);

    }

    else{

        setTimeout(()=>{

            window.location.href="result.html";

        },600);

    }

}

nextStep();