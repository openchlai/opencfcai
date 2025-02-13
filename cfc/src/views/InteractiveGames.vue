<template>
    <div class="games-page">
        <h1 class="page-title">Interactive Games</h1>
        <div class="cards-container">
            <ChildFriendlyCard>
                <template #header>
                    <h2>Memory Match</h2>
                </template>
                <p>Test your memory with this fun matching game!</p>
                <template #footer>
                    <button @click="goToGame('/games/memory-match')">Play Now</button>
                </template>
            </ChildFriendlyCard>

            <ChildFriendlyCard>
                <template #header>
                    <h2>Math Puzzle</h2>
                </template>
                <p>Sharpen your math skills with exciting puzzles!</p>
                <template #footer>
                    <button @click="goToGame('/games/math-puzzle')">Play Now</button>
                </template>
            </ChildFriendlyCard>

            <ChildFriendlyCard>
                <template #header>
                    <h2>Word Scramble</h2>
                </template>
                <p>Unscramble the letters to form meaningful words.</p>
                <template #footer>
                    <button @click="goToGame('/games/word-scramble')">Play Now</button>
                </template>
            </ChildFriendlyCard>

            <ChildFriendlyCard>
                <template #header>
                    <h2>Coloring Fun</h2>
                </template>
                <p>Unleash your creativity with virtual coloring!</p>
                <template #footer>
                    <button @click="goToGame('/games/coloring-fun')">Play Now</button>
                </template>
            </ChildFriendlyCard>
        </div>
    </div>
</template>

<script>
    import ChildFriendlyCard from "../components/ChildFriendlyCard.vue";

    export default {
        name: "GamesPage",
        components: {
            ChildFriendlyCard,
        },
        methods: {
            goToGame(route) {
                this.$router.push(route);
            },
        },
    };
</script>

<style scoped>
    .games-page {
        padding: 2rem;
        text-align: center;
        background-color: #f0f8ff;
        min-height: 100vh;
    }

    .page-title {
        font-size: 2.5rem;
        color: #333;
        margin-bottom: 1.5rem;
        font-family: "Comic Sans MS", sans-serif;
    }

    .cards-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 1rem;
    }
</style>
