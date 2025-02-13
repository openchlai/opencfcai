<template>
    <div class="game-container">
        <h1>Word Scramble</h1>
        <p class="instruction">Unscramble the letters to form the word!</p>
        <div class="word-container">
            <p class="scrambled-word">{{ scrambledWord }}</p>
        </div>
        <input v-model="userGuess" class="answer-input" type="text" placeholder="Enter your guess"
            @change="checkGuess" />
        <button class="generate-button" @click="scrambleWord">Next Word</button>
        <p v-if="resultMessage" class="result-message">{{ resultMessage }}</p>
        <p class="score">Score: {{ score }}</p>
    </div>
</template>

<script>
    import { ref } from 'vue';

    export default {
        name: 'WordScramble',
        setup() {
            const words = [
                'apple', 'banana', 'cherry', 'grape', 'orange', 'melon', 'kiwi', 'lemon', 'mango', 'peach',
                'plum', 'pear', 'watermelon', 'pineapple', 'strawberry', 'blueberry', 'coconut', 'apricot', 'lime', 'applesauce',
                'grapefruit', 'pomegranate', 'kiwifruit', 'blueberry', 'raspberry', 'blackberry', 'cantaloupe', 'papaya', 'fruitcake', 'carrot'
            ];
            const score = ref(0);
            const scrambledWord = ref('');
            const userGuess = ref('');
            const resultMessage = ref('');

            const scrambleWord = () => {
                const randomWord = words[Math.floor(Math.random() * words.length)];
                scrambledWord.value = randomWord.split('').sort(() => Math.random() - 0.5).join('');
                userGuess.value = '';
                resultMessage.value = '';
            };

            const checkGuess = () => {
                const word = scrambledWord.value.split('').sort().join('');
                if (userGuess.value.toLowerCase().split('').sort().join('') === word) {
                    score.value++;
                    resultMessage.value = 'Correct! 🎉';
                    scrambleWord();
                } else {
                    resultMessage.value = 'Oops! Try again! 😅';
                }
            };

            // Initialize the game with the first scrambled word
            scrambleWord();

            return {
                score,
                scrambledWord,
                userGuess,
                resultMessage,
                scrambleWord,
                checkGuess,
            };
        },
    };
</script>

<style scoped>
    .game-container {
        text-align: center;
        padding: 20px;
        background-color: #e1f5fe;
        font-family: 'Comic Sans MS', sans-serif;
    }

    h1 {
        color: #ff7043;
        font-size: 36px;
        margin-bottom: 20px;
        font-weight: bold;
    }

    .instruction {
        font-size: 18px;
        margin-top: 10px;
        color: #6c757d;
        font-weight: bold;
    }

    .word-container {
        margin-top: 30px;
    }

    .scrambled-word {
        font-size: 32px;
        font-weight: bold;
        color: #ff5722;
        margin-bottom: 20px;
    }

    .answer-input {
        font-size: 28px;
        padding: 15px;
        margin-top: 10px;
        width: 250px;
        text-align: center;
        border-radius: 12px;
        border: 2px solid #ff5722;
        background-color: #ffffff;
    }

    .generate-button {
        padding: 16px 32px;
        background-color: #ff7043;
        border: none;
        color: white;
        cursor: pointer;
        border-radius: 20px;
        font-size: 22px;
        margin-top: 30px;
        transition: background-color 0.3s ease;
    }

    .generate-button:hover {
        background-color: #f4511e;
    }

    .result-message {
        font-size: 22px;
        font-weight: bold;
        margin-top: 20px;
        color: #388e3c;
    }

    .score {
        font-size: 28px;
        font-weight: bold;
        margin-top: 30px;
        color: #ff5722;
    }

    @media (max-width: 768px) {
        h1 {
            font-size: 28px;
        }

        .scrambled-word {
            font-size: 24px;
        }

        .answer-input {
            font-size: 24px;
            width: 200px;
        }

        .generate-button {
            font-size: 20px;
            padding: 14px 28px;
        }

        .score {
            font-size: 24px;
        }
    }

    @media (max-width: 480px) {
        h1 {
            font-size: 24px;
        }

        .scrambled-word {
            font-size: 20px;
        }

        .answer-input {
            font-size: 22px;
            width: 180px;
        }

        .generate-button {
            font-size: 18px;
            padding: 12px 24px;
        }

        .score {
            font-size: 22px;
        }
    }
</style>
