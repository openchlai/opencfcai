<template>
    <div class="game-container">
        <h1>Math Puzzle Game</h1>
        <p class="instruction">Solve the math puzzle! Good luck!</p>

        <div class="problem-container">
            <p class="problem">{{ currentProblem }}</p>
            <input v-model="userAnswer" type="number" class="answer-input" placeholder="Your answer"
                @change="checkAnswer" :disabled="isDisabled" />
        </div>

        <button @click="generateProblem" class="generate-button" :disabled="isDisabled">Next Puzzle</button>

        <p v-if="resultMessage" class="result-message">{{ resultMessage }}</p>
        <p class="score">Score: {{ score }}</p>
    </div>
</template>

<script>
    import { ref } from "vue";

    export default {
        name: "MathPuzzleGame",
        setup() {
            const score = ref(0); // Reactive score
            const userAnswer = ref('');
            const resultMessage = ref('');
            const currentProblem = ref('');
            const correctAnswer = ref(0);
            const isDisabled = ref(false);

            const generateRandomNumber = (min, max) => Math.floor(Math.random() * (max - min + 1)) + min;

            const generateProblem = () => {

                const num1 = generateRandomNumber(1, 10);
                const num2 = generateRandomNumber(1, 10);
                const operation = generateRandomNumber(1, 4); // 1: addition, 2: subtraction, 3: multiplication, 4: division

                if (operation === 1) {
                    currentProblem.value = `${num1} + ${num2}`;
                    correctAnswer.value = num1 + num2;
                } else if (operation === 2) {
                    currentProblem.value = `${num1} - ${num2}`;
                    correctAnswer.value = num1 - num2;
                } else if (operation === 3) {
                    currentProblem.value = `${num1} × ${num2}`;
                    correctAnswer.value = num1 * num2;
                } else if (operation === 4) {
                    currentProblem.value = `${num1} ÷ ${num2}`;
                    correctAnswer.value = num1 / num2;
                }

                userAnswer.value = '';
                resultMessage.value = '';
                isDisabled.value = false;
            };

            const checkAnswer = () => {
                if (parseInt(userAnswer.value) === correctAnswer.value) {
                    resultMessage.value = "Correct! Well done!";
                    score.value += 1; // Update the score correctly
                    console.log("Score:", score.value); // Check the score value
                } else {
                    resultMessage.value = `Oops! The correct answer was ${correctAnswer.value}.`;
                }
                isDisabled.value = true;
                setTimeout(generateProblem, 2000); // Generate new problem after 2 seconds
            };

            generateProblem(); // Initial problem generation

            return { score, userAnswer, resultMessage, currentProblem, generateProblem, checkAnswer, isDisabled };
        },
    };
</script>

<style scoped>
    
</style>
