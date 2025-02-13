<template>
    <div class="game-container">
        <h1>Memory Match Game</h1>
        <p v-if="!gameStarted" class="instruction">Tap a card to start the game!</p>
        <div class="card-container">
            <div v-for="(card, index) in shuffledCards" :key="index" class="card"
                :class="{ 'flipped': card.flipped || card.matched }" @click="flipCard(card, index)">
                <div class="card-inner">
                    <div class="card-front">
                        <img v-if="card.image" :src="card.image" alt="Card front" />
                    </div>
                    <div class="card-back">
                        <img src="https://via.placeholder.com/100x100.png?text=?" alt="Card back" />
                    </div>
                </div>
            </div>
        </div>
        <div v-if="gameWon" class="win-message">
            <h2>Yay! You Won!</h2>
            <button @click="resetGame">Play Again</button>
        </div>
    </div>
</template>

<script>
    import { ref, computed } from "vue";

    export default {
        setup() {
            const cards = ref([
                { image: 'https://via.placeholder.com/100x100.png?text=🍎', flipped: false, matched: false },
                { image: 'https://via.placeholder.com/100x100.png?text=🍎', flipped: false, matched: false },
                { image: 'https://via.placeholder.com/100x100.png?text=🍌', flipped: false, matched: false },
                { image: 'https://via.placeholder.com/100x100.png?text=🍌', flipped: false, matched: false },
                { image: 'https://via.placeholder.com/100x100.png?text=🍉', flipped: false, matched: false },
                { image: 'https://via.placeholder.com/100x100.png?text=🍉', flipped: false, matched: false },
                { image: 'https://via.placeholder.com/100x100.png?text=🍇', flipped: false, matched: false },
                { image: 'https://via.placeholder.com/100x100.png?text=🍇', flipped: false, matched: false },
                { image: 'https://via.placeholder.com/100x100.png?text=🍒', flipped: false, matched: false },
                { image: 'https://via.placeholder.com/100x100.png?text=🍒', flipped: false, matched: false },
                { image: 'https://via.placeholder.com/100x100.png?text=🍍', flipped: false, matched: false },
                { image: 'https://via.placeholder.com/100x100.png?text=🍍', flipped: false, matched: false },
            ]);
            const flippedCards = ref([]);
            const gameWon = ref(false);
            const gameStarted = ref(false);

            const shuffledCards = computed(() => {
                return [...cards.value].sort(() => Math.random() - 0.5);
            });

            const flipCard = (card, index) => {
                if (flippedCards.value.length < 2 && !card.flipped && !card.matched) {
                    card.flipped = true;
                    flippedCards.value.push({ card, index });

                    if (flippedCards.value.length === 2) {
                        checkMatch();
                    }
                }
            };

            const checkMatch = () => {
                const [firstCard, secondCard] = flippedCards.value;

                if (firstCard.card.image === secondCard.card.image) {
                    firstCard.card.matched = true;
                    secondCard.card.matched = true;
                } else {
                    setTimeout(() => {
                        firstCard.card.flipped = false;
                        secondCard.card.flipped = false;
                    }, 1000);
                }

                flippedCards.value = [];
                checkGameWon();
            };

            const checkGameWon = () => {
                gameWon.value = cards.value.every(card => card.matched);
            };

            const resetGame = () => {
                cards.value.forEach(card => {
                    card.flipped = false;
                    card.matched = false;
                });
                flippedCards.value = [];
                gameWon.value = false;
                gameStarted.value = false;
            };

            const startGame = () => {
                gameStarted.value = true;
            };

            return {
                shuffledCards,
                gameWon,
                gameStarted,
                flipCard,
                resetGame,
                startGame,
            };
        },
    };
</script>

<style scoped>
    .game-container {
        text-align: center;
        padding: 20px;
        background-color: #e3f2fd;
        /* Soft light blue background */
        font-family: 'Comic Sans MS', sans-serif;
        /* Playful, child-friendly font */
    }

    h1 {
        color: #ff9800;
        /* Bright orange for the title */
        font-size: 32px;
        text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
        /* Light shadow for emphasis */
    }

    .instruction {
        font-size: 18px;
        margin-top: 10px;
        color: #6c757d;
        /* Neutral gray for text */
        font-weight: bold;
    }

    .card-container {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 10px;
        margin-top: 20px;
    }

    .card {
        width: 100px;
        height: 100px;
        background-color: #ffcc80;
        /* Soft peach color */
        border-radius: 12px;
        cursor: pointer;
        position: relative;
        overflow: hidden;
        box-shadow: 0 0 12px rgba(0, 0, 0, 0.2);
        transition: transform 0.3s ease-in-out;
    }

    .card-inner {
        position: absolute;
        width: 100%;
        height: 100%;
        transform-style: preserve-3d;
        transition: transform 0.5s;
    }

    .card.flipped .card-inner {
        transform: rotateY(180deg);
    }

    .card-front,
    .card-back {
        position: absolute;
        width: 100%;
        height: 100%;
        backface-visibility: hidden;
    }

    .card-front img {
        width: 100%;
        height: 100%;
        object-fit: contain;
    }

    .card-back {
        background-color: #ff4081;
        /* Bright pink for the back of the card */
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        /* White text for clarity */
        font-size: 16px;
        font-weight: bold;
        border-radius: 12px;
    }

    .win-message {
        margin-top: 20px;
        font-size: 20px;
        color: #43a047;
        /* Green color for positive messages */
    }

    button {
        padding: 12px 24px;
        font-size: 18px;
        background-color: #ff4081;
        /* Bright pink button */
        border: none;
        color: white;
        cursor: pointer;
        border-radius: 15px;
        /* Rounded button corners */
        transition: background-color 0.3s;
    }

    button:hover {
        background-color: #f50057;
        /* Darker pink when hovered */
    }

    button:focus {
        outline: none;
    }

    @media screen and (max-width: 600px) {
        h1 {
            font-size: 28px;
            /* Slightly smaller title */
        }

        .card-container {
            grid-template-columns: repeat(3, 1fr);
        }

        .card {
            width: 90px;
            /* Slightly smaller cards */
            height: 90px;
        }

        button {
            font-size: 16px;
        }

        .instruction {
            font-size: 16px;
        }
    }

    @media screen and (max-width: 400px) {
        h1 {
            font-size: 24px;
            /* Even smaller title */
        }

        .card-container {
            grid-template-columns: repeat(4, 1fr);
            /* Adjust for smaller screens */
        }

        .card {
            width: 70px;
            /* Smaller cards for compact screens */
            height: 70px;
        }

        button {
            font-size: 14px;
            padding: 10px 20px;
        }

        .instruction {
            font-size: 14px;
        }
    }

</style>
